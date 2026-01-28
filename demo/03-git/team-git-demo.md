### Collaboration with Git/GitHub

In this exercise you will team up. At your table, select one person to set up a new repository on GitHub. Work through these steps:

#### Step 1: Repository Setup
   * One person in your group sets up a new repository on GitHub 
   * The creator adds all group members as collaborators to the new repository on GitHub. The repository should have a single `main` branch.

#### Step 2: Clone the Repository
   * All group members clone the new repository to their own environment. Make sure you are not inside any other Git repository! To avoid issues, change to your home directory first:
     ```bash
     cd
     git clone https://github.com/CREATOR_USERNAME/REPO_NAME.git
     cd REPO_NAME
     ```
   Replace `CREATOR_USERNAME` and `REPO_NAME` with the actual GitHub username and repository name.
   
   **Important:** Make sure you are **not** inside an existing Git repository when running the `git clone` command. You don't want to create nested Git repositories.

#### Step 3: Create Unique Files
   * Each group member should create a new text file in their local repository. Use unique filenames to avoid collisions (e.g., `alice.txt`, `bob.txt`). Each team member should commit and push their files to the GitHub repository:
     ```bash
     echo "Hello from Alice" > alice.txt
     git add alice.txt
     git commit -m "Add alice.txt"
     git push origin main
     ```

#### Step 4: Verify on GitHub
   * All: Check the presence of the new files on GitHub by visiting the repository page.

#### Step 5: Pull Latest Changes
   * All: Run the following command in your environment to get the latest changes from GitHub:
     ```bash
     git pull origin main --merge
     ```
     (The `--merge` flag is explicit and avoids warnings in newer Git versions.)

**So far, so good. Let's take it to the next level!**

#### Step 6: Create Collision File

When collaborating, team members may be working in parallel on local copies of the same file. This leads to divergence and file version conflicts need to be resolved. Let's simulate such scenario.

   * All: Create a new file `collision.txt` in your local repository. The file should contain a single line with your `first name, favorite animal`. Track, commit, and push it to the remote repo on GitHub:
     ```bash
     echo "Alice, cat" > collision.txt
     git add collision.txt
     git commit -m "Add collision.txt"
     git push origin main
     ```

#### Step 7: Resolving Merge Conflicts

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

**Congratulations, you did it!**