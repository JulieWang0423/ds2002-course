# Advanced Git Demo

This demo illustrates the collaborative work on two clones (copies) of the same repository. 

To simulate this with your neighbor, invite them as a collaborator to your repo after you have created it on GitHub. See <a href="https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository" target="_blank" rel="noopener noreferrer">GitHub's guide on inviting collaborators</a>. Alternatively, you can simulate this scenario by working in two different directories on your computer or Codespace.

## Setting up on computer 1

This could be in Codespace, or your local computer. Make sure you are not inside another repository! 

### Tracking and committing files 
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

The untracked files section indicates that Git is aware of the new file, but it's not part of the version control yet. Let's `add` the file (for tracking) and commit it. The `commit` creates a reference point of the current version of all tracked files. 
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
The `git diff` command shows us the differences between file versions. By default the difference between the current version in the filesystem and the last version that was committed. In this case `Good morning` was replaced with `Good evening`.

Let's track and commit those last changes
```bash
git add .
git commit -m "evening"
git status
git log
```

### Checking out different file versions

Let's roll back to the earlier commit *before* we changed greetings.txt. We use the unique identifier of the commit that's shown in the `git log` output. In fact we only need the first few characters of the commit hash, e.g. something like "03280fe38" (your hash will look different). 

Now we can `checkout` that earlier file version. **Note:** This puts you in a "detached HEAD" state, which is fine for viewing old versions.
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

### Working on a new branch

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

### Linking to repository on GitHub

Create repo `demo-repo` on GitHub. Then connect our local repo to it. By convention the remote is referred to as `origin`.
```bash
git remote add origin https://github.com/ksiller/demo-repo.git # replace with your url
git branch -a
```

Push all branches to the remote (referred to as origin) on GitHub.
```bash
git push --all origin
```
Go to GitHub and confirm the updated content in `demo-repo`.

---

## On computer 2

Clone the repo from GitHub; if you're in Codespace, cd to home dir first! It is assumed that you don't have `demo-repo` in current directory.
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

## Back to Computer 1

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
Should now include break.txt

---

### Resolving conflict: Working on the same file in parallel

## Computer 2

Create a new file `conflict.txt`. Track, commit, push and merge.

```bash
echo "my version" > conflict.txt
git add .
git commit -m "my version"
git push origin main
```

---

## Back on computer 1

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

**Congratulations! You are a Git Ninja now.**