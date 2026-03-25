# Lab 09: Amazon EC2

## Case study

A small organization is moving some workloads off local machines and wants a **pilot Linux server in the cloud** before a larger migration. You stand up that prototype: use the AWS CLI and console to inspect EC2, create an SSH key pair, launch an Ubuntu instance in the shared course account, log in, and install a minimal Python toolchain (including `boto3`, consistent with Lab 08).

When you finish, you will have run through the core provision → connect → configure loop for one VM and will submit scripts plus a short screenshot.

## Learning goals

By completing this lab, you will be able to:

- Confirm AWS CLI identity and use `aws ec2 describe-instances` with `jq` to summarize instances.
- Create an EC2 key pair and use a `.pem` private key with `ssh -i`.
- Gather AMI, subnet, and security group details from the console and launch an instance from a bash script.
- SSH into the instance, install packages, and verify the environment (`python3 -c "import boto3"`, `htop`).

---

### 1. Load your environment

For this lab, start an Open OnDemand CodeServer (VSCode) session on the UVA HPC system. In your session, open a new terminal and activate your environment:

```bash
module load miniforge
source activate ds2002
```

### 2. Confirm your AWS CLI configuration

You used the `ds2002-user` user account in AWS for Lab 08. Confirm that your AWS CLI is configured accordingly.

```bash
aws sts get-caller-identity
```

The output should look like this:
```json
{
    "UserId": "AIDAYRXHJIA3N7XIGYSMI",
    "Account": "587821826102",
    "Arn": "arn:aws:iam::587821826102:user/ds2002-user"
}
```

If not, go through the `aws configure` steps of [Lab 08](../08-s3/README.md#setup) again.

### 3. Check existing EC2 instances

```bash
aws ec2 describe-instances
```

Use `jq` to filter the list to only include `ImageId`, `InstanceId`, `InstanceType`, a display name for the instance (`InstanceName` or `Name`), `PublicIpAddress`, and `State`.

**Hint:** Start with `aws ec2 describe-instances | jq '.Reservations[].Instances[]'`. That gives one JSON object per instance; add `jq` filters to pick the fields below. The instance name shown in the console is usually the tag with `"Key": "Name"`—extract that tag’s `"Value"` (not every tag value).

The output should look like this (one JSON object per instance; your `jq` filter may emit several in sequence):

```json
{
  "ImageId": "ami-07ff62358b87c7116",
  "InstanceId": "i-09829fd2c5dc3d692",
  "InstanceType": "t3.nano",
  "InstanceName": "ds2002-demo",
  "PublicIpAddress": "54.234.9.240",
  "State": {
    "Code": 16,
    "Name": "running"
  }
}
...
```

Create a bash script `ec2-info.sh` with your `aws ec2 ... | jq ...` command.

### 4. Create key pair

Before launching a new EC2 instance, create a key pair that will allow you to connect via `ssh` to the running instance post-launch.

Remember, a key pair has a **public** and a **private** component. AWS stores the **public** half of an SSH key pair in your account and associates it with the key pair name you choose. When you create a key pair, AWS returns the **private** key once (in PEM format). **You must save the private key immediately; you cannot download the private key again later.**


```bash
mkdir -p ~/.ssh
```

Create a new key pair and save the private key under your hidden `~/.ssh` directory (replace `key-ec2-<YOUR_COMPUTING_ID>` with your computing ID, e.g. `key-ec2-mst3k`):

```bash
aws ec2 create-key-pair \
  --key-name key-ec2-<YOUR_COMPUTING_ID> \
  --query 'KeyMaterial' \
  --output text > ~/.ssh/key-ec2-<YOUR_COMPUTING_ID>.pem
```

This will create a new file, `key-ec2-<YOUR_COMPUTING_ID>.pem`. The `pem` file is the **private** key. **Keep it secret and never commit it to Git.**

Let's restrict permission on your private key file.
```bash
chmod 400 ~/.ssh/*.pem
ls -la ~/.ssh
```

**`chmod 400`** makes the private key readable only by you; SSH refuses to use a key that is too permissive.

You will use this key in step 7.

### 5. Spin up a new EC2 instance

In order to launch a new EC2 instance, we need to specify:

- AMI image identifier (Amazon Linux, Ubuntu, etc.)

- Instance type (t2.nano, t2.micro, etc.)

- Name of a key pair for SSH access (created in step 4)

- Security group ID (controls inbound/outbound traffic)

- Network subnet ID (internal network setup within your virtual private cloud)

Create a new bash script `launch-ec2.sh` based on this template:

```bash
#!/bin/bash

AMI=NNNN
INSTANCE_TYPE=XXXX
INSTANCE_NAME=XXXX
KEY_NAME=XXXX
SECURITY_GROUP_ID=NNNN
SUBNET_ID=NNNN

# Complete this command with the right flags (e.g. --image-id, --instance-type, --key-name,
# --security-group-ids, --subnet-id) and a Name tag from INSTANCE_NAME.
aws ec2 run-instances
```

Log into the AWS Console as `ds2002-user` using the URL, username, and password provided in `Lab 08` on Canvas. In the AWS Console, gather the following information:

- Search the Amazon Machine Image catalog for an Ubuntu image. Image IDs start with `ami-*`. Assign the value to the `AMI` variable in your bash script.
- Set `INSTANCE_TYPE` to `t2.nano`
- Set `INSTANCE_NAME` to `ds2002-<YOUR_COMPUTING_ID>`, e.g. `ds2002-mst3k` (same `ds2002-<computing id>` prefix as S3 bucket names in [Practice 09](../../practice/09-iam-s3/README.md))
- Set `KEY_NAME` to `key-ec2-<YOUR_COMPUTING_ID>` which you specified in Step 4, e.g. `key-ec2-mst3k`
- In AWS Console, find the EC2 instance `ds2002-demo`. Select the `Security` tab and locate the ID shown under `Security group`. The Security group IDs start with `sg-*`. Copy that value and assign it to `SECURITY_GROUP_ID` in your bash script.
- Go back to the AWS Console, find the EC2 instance `ds2002-demo` (again). Select the `Networking` tab and locate the subnet ID (values start with `subnet-*`). Copy that value and assign it to `SUBNET_ID` in your bash script.

Complete the `aws ec2 run-instances` command using the appropriate options and the environment variables you set at the top of your bash script.

Execute the `launch-ec2.sh` script. If successful, you should see output similar to this:

```json
{
    "ReservationId": "r-0a1b2c3d4e5f67890",
    "OwnerId": "587821826102",
    "Groups": [],
    "Instances": [
        {
            "InstanceId": "i-0f1e2d3c4b5a67890",
            "ImageId": "ami-0123456789abcdef0",
            "State": {
                "Code": 0,
                "Name": "pending"
            },
            "InstanceType": "t2.nano",
            "KeyName": "key-ec2-mst3k",
            "PrivateDnsName": "ip-10-0-1-23.ec2.internal",
            "PublicDnsName": "",
            "PublicIpAddress": null
        }
    ]
}
```

Your IDs, AMI, key name, and networking fields will differ. `State.Name` may move from `pending` to `running` shortly after launch; `PublicIpAddress` is often empty until the instance gets a public IP.

> **Note:** The public half of the key pair is registered on the instance at launch so you can SSH with your matching `.pem` private key.

### 6. Rerun your `ec2-info.sh` script and redirect its output to `ec2-info.txt` to confirm your new EC2 instance is in the list.

For example (from the directory where the script lives, after `chmod +x ec2-info.sh` if needed):

```bash
./ec2-info.sh > ec2-info.txt
```

Take note of the public IP address of your new instance.

### 7. Install software on your EC2 instance

- SSH into your instance using the key from step 4 and the instance’s public IP address (see steps 3 and 6 for how to find it).

```bash
ssh -i ~/.ssh/key-ec2-<YOUR_COMPUTING_ID>.pem ubuntu@<PUBLIC_IP>
```

Replace `<YOUR_COMPUTING_ID>` and `<PUBLIC_IP>` with your info from step 4 and the instance’s public IP from step 6 (or from the `jq` output in step 3), respectively.


Use `ubuntu` for Ubuntu AMIs and `ec2-user` for Amazon Linux if your AMI uses that default user. These accounts are set up by default when you launch an EC2 instance.

- Use the following commands to install packages on the instance (Ubuntu AMIs use `apt`; `python3-pip`, `git`, and `htop` are standard Ubuntu packages):

  ```bash
  sudo apt-get update
  sudo apt-get install -y python3-pip git htop
  python3 -m pip install --user boto3
  ```

  `sudo` runs `apt-get` as root so system packages install cleanly. Avoid `sudo pip install …` on recent Ubuntu releases (PEP 668 “externally managed environment”); installing `boto3` with `python3 -m pip install --user` puts it in your own `~/.local` and matches how you use `boto3` elsewhere in the course. Alternatively you can install the distro package only: `sudo apt-get install -y python3-boto3 git htop` (no `pip` step).

  If you find yourself installing the same packages on every new VM, consider [bootstrapping with user data](../../practice/10-cloud/README.md#user-data--bootstrapping).

- Confirm the environment and that `boto3` imports:

  ```bash
  hostname
  cat /etc/os-release
  python3 -c "import boto3; print('boto3', boto3.__version__)"
  python3 -m pip list --user
  ```

  If you used only `apt install python3-boto3` (no `pip`), skip `pip list --user` and rely on the `import boto3` line above.

  Save the output to `my-ec2-instance.txt`.

- Run `htop`. How many processors do you see? Take a screenshot and save it in your lab submission folder (e.g. `mywork/lab9`).

## Submit your work

By the end of this lab, your repository should contain the following in `mywork/lab9/`:

- `ec2-info.sh`
- `ec2-info.txt` (from step 6)
- `launch-ec2.sh`
- Screenshot of `htop` on your EC2 instance
- `my-ec2-instance.txt`

Add, commit, and push your `mywork/lab9` folder, then submit the GitHub URL to that folder in Canvas for grading.