# Git & GitHub

The goal of this activity is to familiarize you with version control using Git and GitHub. These tools are essential for tracking changes in your code, collaborating with others, managing project history, and contributing to open-source projects.

If the *In-class exercises* and *Additional practice* feel like a breeze, challenge yourself with activities in the *Advanced Concepts* section and explore the resource links at the end of this post.

* Start with the **In-class Exercises**.
* Continue with the **Additional Practices** section on your own time. 
* Optional: Explore the **Advanced Concepts** if you wish to explore Git and GitHub in more depth.

## In-class exercises

### Update your forked repository

We talked about the relationship of GitHub repositories, their forks, and local clones. Now it is your turn to pull the latest content from the course repository into your personal fork.

#### Step 1: Update your local clone (or repo in Codespace)

* Open a terminal on your computer or Codespace instance in your forked Git repository.
* Check with `pwd` that you're at the top level of your local repository. Use the `cd` command to change to it if needed.
* In your local repo, execute the commands shown in the [Updating your fork](../../README.md#updating-your-fork) section (part of the repo's README.md file).
* Execute `git status` and `git log` to check the updates.

#### Step 2: Push your local changes to your fork on GitHub

* In your local repo, execute the commands shown in the [Saving your changes](../../README.md#saving-your-changes) section (also part of the repo's README.md file).

**Excellent, your repository is up to date.**

## Collaboration with Git/GitHub

This demo illustrates the collaborative work on two clones (copies) of the same repository. 

>NOTE: You should go through this exercise in groups of two or three. Alternatively, you can simulate this scenario by working in two different directories on your computer or Codespace.

### Setting up on computer 1 - Team member 1

This could be in Codespace, or your local computer. Make sure you are not inside another repository! 

**While team member 1 is walking through these steps, the other team member(s) should observe; all team members should discuss as you step through this exercise so you can deepen your understanding.**

#### Tracking and committing files 
```bash
cd
pwd
ls
mkdir demo-repo
cd demo-repo
git init
ls -la
```
Notice the new `.git` directory. 

```bash
echo "Good morning" > greetings.txt
ls -la
git status
```

Output:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	greetings.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The untracked files section indicates that Git is aware of the new file, but it's not part of the version control yet. Let's `add` the file (for tracking) and commit it. The `commit` creates a reference point of the current version of all tracked files. Think of it as a snapshot. 
```bash
git add .
git commit -m "morning"
git status
```

Output:
```
On branch main
nothing to commit, working tree clean
```
Notice how the status has changed after the commit. 

The log provides details about the commit history. 
```bash
git log
```

Output:
```
commit fbd6cffa05c93452c433b5d6c355797bce5e5cc9 (HEAD -> main)
Author: ksiller <ksiller@gmail.com>
Date:   Wed Jan 21 04:25:30 2026 -0500

    morning
```

Edit `greetings.txt` and save it.

```bash
echo "Good evening!" > greetings.txt

git status
git diff
```

Output:
```
diff --git a/greetings.txt b/greetings.txt
index 9fc8e01..f70861f 100644
--- a/greetings.txt
+++ b/greetings.txt
@@ -1 +1 @@
-Good morning
+Good evening
```
The `git diff` command shows us the differences between file versions. By default, it shows the difference between the current version in the filesystem and the last version that was committed. In this case `Good morning` was replaced with `Good evening`.

Let's track and commit those last changes
```bash
git add .
git commit -m "evening"
git status
git log
```
Confirm the commit in the logs.

#### Checking out different file versions

Let's roll back to the earlier commit *before* we changed `greetings.txt`. We use the unique identifier of the commit that's shown in the `git log` output. In fact we only need the first few characters of the commit hash, e.g. something like "03280fe38" (your hash will look different). 

Now we can `checkout` that earlier file version.

>Note: This puts you in a "detached HEAD" state, which is fine for viewing old versions.

```bash
git checkout 03280fe38 # update this hash with your actual commit hash from git log
cat greetings.txt
```
Notice the content has changed back to the earlier version: greetings.txt contains `Good morning`.

OK, let's switch back to the latest version. We're working on the main branch (default). `git checkout <branch>` gets the latest committed file versions for that branch.
```bash
git checkout main
git status
git branch
```

#### Working on a new branch

Let's create a new branch. Branches allow you to develop code in parallel. This is useful when working on implementing new code features or fixing bugs. It allows working on code modifications without affecting code in the main branch (or other branches).
```bash
git switch -c new_day
git branch
```

Output:
```
Switched to a new branch 'new_day'
  main
* new_day
```
Notice the `*`. It indicates the branch you're on.

Let's update the file, track and commit it, and check the logs
```bash
echo "Yet another day!" > greetings.txt
cat greetings.txt
git add .
git commit -m "another day"
git log
```

Output:
```
commit 4bf7e286703573669bc2c0925486ec29e025050a (HEAD -> new_day)
Author: ksiller <ksiller@gmail.com>
Date:   Wed Jan 21 04:53:38 2026 -0500

    another day
```
Notice the `HEAD` pointing to our new branch `new_day`.

Let's switch back to `main`.
```bash
git switch main
git branch
```

And add another file to main branch

```bash
echo 'Time to practice' > practice.txt
git add .
git commit -m "practice"
git switch new_day # no practice.txt on this branch
ls # no practice.txt on this branch
git switch main  
ls # and practice.txt is back
```

#### Linking to repository on GitHub

Create repo `demo-repo` on GitHub. Then connect your local repo to it. By convention the remote is referred to as `origin`. Take note of the new repository's URL on GitHub.

If you are working on your own computer (or any system other than Codespace), you should be able to use your Personal Access Token for authentication and continue with `Option 1: https protocol`. 

If you are in Codespace or would like to explore the use of ssh keys, continue with `Option 2: ssh protocol`.

**Option 1: https protocol**

```bash
git remote add origin https://github.com/ksiller/demo-repo.git # replace with your url
git remote -v
```
The first command assigns the URL of your repo to the designator `origin`, which is the convention for referencing GitHub repositories. 

To confirm, the `git remote -v` command shows you this association.

Output:
```
origin  https://github.com/YOUR_USERNAME/REPO_NAME.git (fetch)
origin  https://github.com/YOUR_USERNAME/REPO_NAME.git (push)
```
Continue with [Pushing all changes](#pushing-all-changes).

**Option 2: ssh protocol**

If you are using Codespace, you have to use the ssh protocol and keys to link your new GitHub repository. Follow these steps:

**1. Create ssh keys**
```bash
ssh-keygen
```
You will be prompted with three questions:
- Enter file in which to save the key (/home/vscode/.ssh/id_rsa): 
- Enter passphrase (empty for no passphrase): 
- Enter same passphrase again: 
Don't enter anything, just hit enter/return to accept the default for each of them. 

This will create two files in a hidden directory in `~/.ssh`:
- `id_rsa` : This is your private key. **Don't share it with anyone.**
- `id_rsa.pub`: This is your public key. You can place it on other systems to log in there without being prompted for a password.

**2. Print your public key to the screen**
```bash
cat ~/.ssh/id_rsa.pub
```
Copy the entire output to your clipboard. It starts with `ssh-rsa ...`. This is your public key.

**3. Add your public key to your GitHub account**
   
Follow the instructions starting at step 2 [Adding a new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account).

**4. Set the origin URL**

Go back to the Codespace terminal. Run these commands.
```bash
git remote add origin git@github.com:ksiller/demo-repo.git # replace with your url
git remote -v
```
The first command assigns the URL of your repo to the designator `origin`, which is the convention for referencing GitHub repositories. 

To confirm, the `git remote -v` command shows you this association.

Output:
```
origin  git@github.com:YOUR_USERNAME/REPO_NAME.git (fetch)
origin  git@github.com:YOUR_USERNAME/REPO_NAME.git (push)
```
Continue with [Pushing all changes](#pushing-all-changes).

#### Pushing all changes

Push all branches to the remote (referred to as origin) on GitHub.
```bash
git push --all origin
```
Go to GitHub and confirm the updated content in `demo-repo`.

**Add your team member(s) as collaborators to the new GitHub repository.** See the [GitHub instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository) for details.

---

### On computer 2 - Team member 2

**Now team member 2 (and 3) is taking the wheel. Team member 1 should observe; all team members should discuss as they proceed.**

On your local computer, clone from GitHub the repo that your team mate invited you to. If you want to use Codespace, start a new Codespace instance from your team mate's repository; you can skip the `git clone` and `cd` step.
```bash
git clone https://github.com/ksiller/demo-repo.git
cd demo-repo
```
You only have to do this once. 

Continue and create a new file on this machine. Track, commit, and push back to remote repo on GitHub:
```bash
echo "time for a break!" > break.txt
git add .
git commit -m "break"
ls
git log
git status
git push origin main
```

Go to GitHub and confirm that `break.txt` is now in the `demo-repo`.

---

### Back to Computer 1 - team member 1

```bash
git status # make sure all local changes are committed, if not commit them before proceeding!
git log
```
Notice the last commit message and hash. Now let's get the latest from the main branch in the remote GitHub repo.

Let's get the latest from the GitHub repository
```bash
git fetch origin main
git switch main # make sure we're on local main branch
git merge origin/main # merge the remote (origin) main branch into the active local branch 
git log
ls
```
The directory should now include `break.txt`.

---

#### Resolving conflict: Working on the same file in parallel

### Computer 2 - Team member 2

Create a new file `conflict.txt`. Track, commit, and push it.

```bash
echo "my version" > conflict.txt
git add .
git commit -m "my version"
git push origin main
```

---

### Back on computer 1 - Team member 1

At the same time your collaborator is also working on `conflict.txt`.

```bash
echo "another version" > conflict.txt
git add . 
git commit -m "my conflict 1"
git status
git log
```
So far so good. We created a new file not knowing that the remote repo had a recent update with the same file `conflict.txt` but different content.

```bash
git fetch origin main
git switch main
git merge origin/main
```
Boom! Git recognizes that the remote branch we want to merge into main has a different version of `conflict.txt`.

```bash
git log
git status
git diff
```
We resolve it in our code editor, and save it.

```bash
git add .
git commit -m "resolved conflict"
git push origin main
```

**Congratulations! You are a Git Ninja now and ready for [Lab 02](../../labs/02-git/README.md).**

## Additional Practice

### Setting up and Managing Repositories

Read <a href="https://uvads.github.io/git-basics/" target="_blank" rel="noopener noreferrer">git in Data Science</a> for a brief introduction.

Then work through the <a href="https://uvads.github.io/git-basics/docs/creating-repositories/" target="_blank" rel="noopener noreferrer">Creating and Managing Git Repositories Exercises</a>. These exercises will cover:

* Init
* Fork (should be familiar from [Setup Instructions](../../setup/README.md))
* Delete
* Managing Collaborators 

### Working with branches

1. **List all branches:**
   ```bash
   git branch
   ```
   This shows all local branches. The current branch is marked with an asterisk (*).

2. **Create a new branch:**
   ```bash
   git switch -c feature-branch
   ```
   The `-c` flag creates a new branch and switches to it immediately. Alternatively, you can create a branch first with `git branch feature-branch` and then switch to it with `git switch feature-branch`.

3. **Switch to an existing branch:**
   ```bash
   # be safe, make sure you are not losing anything
   git add .
   git commit -m "committing everything before getting files from other branches"
   # now it is safe to switch
   git switch main
   ```
   This switches you to the `main` branch. **Make sure you've committed or stashed any changes before switching branches.**

### Pull requests

Pull requests (PRs) are a way to propose changes to a repository. When you create a pull request, you're asking the repository maintainer to review and merge your changes into the main branch. Pull requests allow for code review, discussion, and collaboration before changes are integrated into the project.

1. Create a new branch for your changes:
   ```bash
   git switch -c my-feature
   ```

2. Make some changes:
   ```bash
   echo "## Features" >> README.md
   echo "- Feature 1" >> README.md
   git add README.md
   git commit -m "Add features section to README"
   ```

3. Push the branch to GitHub:
   ```bash
   git push -u origin my-feature
   ```
   The `-u` flag sets up tracking between your local branch and the remote branch, so future `git push` and `git pull` commands know which remote branch to use.

4. On GitHub:
   - Navigate to your repository
   - You should see a banner suggesting to create a pull request
   - Click "Compare & pull request"
   - Add a description of your changes
   - Click "Create pull request"

5. Review the pull request:
   - Check the "Files changed" tab to see your modifications
   - Add comments if needed
   - Merge the pull request when ready

6. After merging, update your local repository:
   ```bash
   git switch main
   git pull origin main --merge
   git branch -d my-feature
   ```

### Practice With GitHub Skills

1. Go to **[GitHub Skills](https://skills.github.com/)**
2. Find the first lesson, "Introduction to GitHub" and right-click on the link to open it in a new browser tab.
3. Read the page closely, paying attention to what you will do in this lesson.
4. Right-click on the "Start course" button (as instructed) to open it in a new brower tab.
5. Follow the instructions closely to copy their lesson into your own account.
6. Once that is complete, wait about 20 seconds and refresh the page in your copy of the lesson.
7. Follow the instructions to complete the lesson.

## Advanced Concepts (Optional)

### Initializing a new repo and connecting it to GitHub with gh cli

You may already have a project set up in a directory on your computer (or in codespace), but it's not set up as a Git repository yet. The following steps show you how to initialize it and connect it to GitHub.

### Create a new local Git repository

1. Create a new directory for your project:
   ```bash
   cd # go to your home directory, or any other directory that is NOT inside an existing repo
   mkdir my-git-project
   cd my-git-project
   ```

2. Initialize a Git repository:
   ```bash
   git init
   ```

3. Verify the repository was created:
   ```bash
   ls -la .git
   ```

   You should see a `.git` directory containing the repository metadata. 
   > **Note:** This repository only exists in your local environment; it is not on GitHub yet.


4. Create repository from command line (requires GitHub CLI)
   ```bash
   # Install GitHub CLI if not already installed
   # Then create the repository:
   gh repo create my-git-project --public --source=. --remote=origin --push
   ```

   This single command creates the GitHub repository and pushes your code.

### Stashing, rebasing, etc.

If you want to explore additional Git features, review the <a href="https://uvads.github.io/git-basics/docs/advanced/" target="_blank" rel="noopener noreferrer">Advanced git</a> tutorial.

### Creating a Repository from a Template

GitHub allows you to create new repositories from templates, which can include pre-configured files, workflows, and settings. This is useful for starting projects with best practices already in place.

### Using the Secure Repository Template

The course repository includes a template URL for creating repositories with security best practices. Here's how to use it:

**Step 1: Get the template URL**

The template URL is located in `github-new-repo-from-template.txt` in this directory (`practice/03-git/`). The URL format is:

```
https://github.com/new?owner=YOUR_USERNAME&template_name=secure-repository-supply-chain&template_owner=skills&name=YOUR_REPO_NAME&visibility=public
```

**Step 2: Customize the URL**

Replace the placeholders:
- `YOUR_USERNAME` - Your GitHub username or organization name
- `YOUR_REPO_NAME` - The name you want for your new repository
- `visibility=public` - Change to `visibility=private` if you want a private repository

**Step 3: Create the repository**

1. Copy the complete URL with your customizations
2. Paste it into your browser's address bar
3. Press Enter
4. GitHub will open the repository creation page with the template pre-selected
5. Review the settings and click "Create repository"

**Example:**

If your username is `johndoe` and you want to create a repo called `my-secure-project`:

```
https://github.com/new?owner=johndoe&template_name=secure-repository-supply-chain&template_owner=skills&name=my-secure-project&visibility=public
```

**What you get:**

The "secure-repository-supply-chain" template from GitHub Skills includes:
- Security best practices configuration
- Supply chain security settings
- Dependabot setup for dependency updates
- Security policies
- Code scanning workflows
- GitHub Actions for security checks

**Alternative: Using GitHub's Web Interface**

You can also create a repository from a template using GitHub's web interface:

1. Go to the template repository: https://github.com/skills/secure-repository-supply-chain
2. Click the green **"Use this template"** button
3. Select **"Create a new repository"**
4. Choose your owner, repository name, and visibility
5. Click **"Create repository"**

## Resources

- <a href="https://uvads.github.io/git-basics/" target="_blank" rel="noopener noreferrer">git in Data Science</a> - Brief introduction to Git
- <a href="https://skills.github.com/" target="_blank" rel="noopener noreferrer">GitHub Skills</a>
