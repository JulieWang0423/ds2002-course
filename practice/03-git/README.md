# Git & GitHub

The goal of this activity is to familiarize you with version control using Git and GitHub. These tools are essential for tracking changes in your code, collaborating with others, managing project history, and contributing to open-source projects.

If the initial examples feel like a breeze, challenge yourself with activities in the *Advanced Concepts* section and explore the resource links at the end of this post.

* Start with the **In-class Exercises**.
* Continue with the **Additional Practices** section on your own time. 
* Optional: Explore the **Advanced Concepts** if you wish to explore Git and GitHub in more depth.

## In-class exercises

At your table, select one person to set up a new repository on GitHub. Work through these steps:

### Step 1: Repository Setup
   * One person in your group sets up a new repository on GitHub 
   * The creator adds all group members as collaborators to the new repository on GitHub. The repository should have a single `main` branch.

### Step 2: Clone the Repository
   * All group members clone the new repository to their own environment. Make sure you are not inside any other Git repository! To avoid issues, change to your home directory first:
     ```bash
     cd
     git clone https://github.com/CREATOR_USERNAME/REPO_NAME.git
     cd REPO_NAME
     ```
   Replace `CREATOR_USERNAME` and `REPO_NAME` with the actual GitHub username and repository name.
   
   **Important:** Make sure you are **not** inside an existing Git repository when running the `git clone` command. You don't want to create nested Git repositories.

### Step 3: Create Unique Files
   * Each group member should create a new text file in their local repository. Use unique filenames to avoid collisions (e.g., `alice.txt`, `bob.txt`). Each team member should commit and push their files to the GitHub repository:
     ```bash
     echo "Hello from Alice" > alice.txt
     git add alice.txt
     git commit -m "Add alice.txt"
     git push origin main
     ```

### Step 4: Verify on GitHub
   * All: Check the presence of the new files on GitHub by visiting the repository page.

### Step 5: Pull Latest Changes
   * All: Run the following command in your environment to get the latest changes from GitHub:
     ```bash
     git pull origin main --merge
     ```
     (The `--merge` flag is explicit and avoids warnings in newer Git versions.)

**So far, so good. Let's take it to the next level!**

### Step 6: Create Collision File

When collaborating, team members may be working in parallel on local copies of the same file. This leads to divergence and file version conflicts need to be resolved. Let's simulate such scenario.

   * All: Create a new file `collision.txt` in your local repository. The file should contain a single line with your `first name, favorite animal`. Track, commit, and push it to the remote repo on GitHub:
     ```bash
     echo "Alice, cat" > collision.txt
     git add collision.txt
     git commit -m "Add collision.txt"
     git push origin main
     ```

### Step 7: Resolving Merge Conflicts

**The early bird gets the worm:** If you are the first person to push the `collision.txt` file, you're in luck—the push should go through without a hitch. However, the others will encounter an error message like this:

```bash
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/YOUR_USERNAME/REPO_NAME.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**To resolve the conflict:**

Starting with the group member next to the first person who successfully pushed, go clockwise and perform the following steps:

1. Pull with merge to reconcile the differences:
   ```bash
   git pull origin main --merge
   ```
   (The `--merge` flag is explicit and avoids warnings in newer Git versions.)
   
   This will create a merge commit.

2. Git will pause and indicate that there are conflicts. VSCode (or your editor) will highlight the conflicting lines in `collision.txt`.

3. **Resolve the conflict:** You want to **append** (not replace) the content so that everyone's entry is included. The file should contain all group members' entries, one per line:
   ```
   Alice, cat
   Bob, dog
   Carol, bird
   ```

4. After resolving the conflict, stage the resolved file:
   ```bash
   git add collision.txt
   ```

5. Complete the merge/rebase:
   ```bash
   git commit
   ```
   This completes the merge commit.

6. Push your changes:
   ```bash
   git push origin main
   ```

7. The next person in the group should repeat steps 1-6 until everyone has successfully pushed their entry to the consolidated `collision.txt` file on GitHub. 

**Congratulations, you did it!** You are ready for Lab 02.

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

## Advanced Concepts (Optional)

### Working with branches and resolving merge conflicts

For an additional challenge work through the scenario in the [Advanced Git Demo](../../demo/03-git/).

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
