# ds2002

Welcome to DS2002 Data Science Systems!

This repository tracks your working environment during this course. Some course material
and tools will be distributed in this way so that we all have a common set of tools, scripts, and datasets.

This requires that you clone and stay current with the **course code repository** and have the appropriate
tools to complete exercises. 

## Updating your fork 

To stay current with new releases into the course repository, change into the repository folder and follow these steps:

### Add an upstream source
```
git remote add upstream https://github.com/ksiller/ds2002-course.git
```

If you receive an error `error: remote upstream already exists.`, run these commands to remove the existing `upstream` and re-add it.

```
git remote remove upstream
git remote add upstream https://github.com/ksiller/ds2002-course.git
```

Confirm the new `upstream` remote:
```
git remote -v
```

Output:
```
origin  URL_OF_YOUR_REPO (fetch)
origin  URL_OF_YOUR_REPO (push)
upstream        https://github.com/ksiller/ds2002-course.git (fetch)
upstream        https://github.com/ksiller/ds2002-course.git (push)
```

You only have to do this once for your local clone! If you start up a new Codespace from your fork, confirm the upstream with the `git remote -v` command. If you don't see the `upstream https://github.com/ksiller/ds2002-course.git`, repeat the above steps.

### Fetch from upstream and merge 

This assumes that you have successfully [added the upstream source](#add-an-upstream-source). 

1. Switch to main branch:
```
git switch main
```

2. Fetch from the upstream branch:
```
git fetch upstream
```

3. Merge the upstream branch into your local branch.
```
git merge upstream/main
```

This can be run in a single block:
```
git switch main
git fetch upstream
git merge upstream/main
```

If you get an error like this...
```
fatal: 'upstream' does not appear to be a git repository
fatal: Could not read from remote repository.
```
...then go back to the section and complete the steps for [Adding an upstream source](#add-an-upstream-source).


### Saving your changes

If you generate code, scripts, data files, etc. that you would like to keep, simply add, commit, and push
the files back to **your** fork of the repository:
```
git add .
git commit -m "Some meaningful message"
git push origin main
```

Remember that changes you commit and push will be saved to YOUR fork of the repository.
