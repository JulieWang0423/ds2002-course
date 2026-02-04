# Scripting in bash

The goal of this activity is to familiarize you with scripting in bash. Bash scripting is essential for automating tasks, processing data, orchestrating workflows, and building reusable tools that can save time and reduce errors.

> **Note:** Work through the examples below in your terminal (Codespace or local), experimenting with each command and its various options. If you encounter an error message, don't be discouraged—errors are learning opportunities. Reach out to your peers or instructor for help when needed, and help each other when you can. 

If the initial examples feel like a breeze, challenge yourself with activities in the *Advanced Concepts* section and explore the resource links at the end of this post.

* Start with the **In-class Exercises**.
* Continue with the **Additional Practices** section on your own time. 
* Optional: Explore the **Advanced Concepts** if you wish to explore bash scripting in more depth.

## In-class exercises

Scripts should be written in a way that takes into account several factors:

1. Use the shebang / make the script executable
2. Use input parameters
3. Conditional logic
4. Loops
5. Sleep
6. Environment / paths / env variables
7. Storing a commands output in a variable
8. Error out gracefully
9. Logging
10. Use comments

**Begin your work on Script 1 in [Lab 03 - Scripting](../../labs/03-scripting/README.md).** As you work through the lab, use the sections below as reference for principal scripting concepts.

### shebang
A well-formatted `bash` script begins with a "shebang" line:
```
#!/bin/bash
```
that points to the full path of the `bash` shell. This may differ from one environment
to the next.

To make any bit of code executable, use `chmod +x` on it (or `chmod 755`).

### Input parameters

Remember that `$0`, `$1`, `$2`, etc. are reserved parameters `bash` understands as positional
arguments when invoking from the command-line:

- `$0` is the invoking script itself
- `$1` is the first parameter after the script name
- `$2` is the second parameter ...
- . . .

Review `positional-args.sh` (in this folder).
```bash
#!/bin/bash

echo "$0 <-- invoking script"
echo "$1 <-- first parameter"
echo "$2 <-- second parameter"
```

Run it:
```bash
./positional-args.sh bananas blueberries
```

Output:
```
./positional-args.sh <-- invoking script
bananas <-- first parameter
blueberries <-- second parameter
```

### If/Else conditional logic:

Start your `if` with a comparison, end with `fi`.

```bash
if [[ $VAR -gt 10 ]]
then
  echo "That number is greater than 10."
else
  echo "Your number is pretty small!"
  exit 0;
fi
```

### Loops:

Start with `for`, define a `do` loop, end with `done`

```bash
names=("alice" "bob" "carol")
for name in "${names[@]}"; do
    echo "Name: $name"
done
```

### Sleep

If you need a deliberate pause in the middle of a script, simply `sleep 5` for a 5-second
pause, etc. This may be especially useful when waiting for processes to complete or between retry attempts.

### Environment

`env` gives you all environment variables for your session. This may vary
for an unattended script (without you around).

Add environment variables in `bash`:
```bash
export VARIABLE=value-of-variable
```

Use full paths to your binaries to avoid your unattended script being unable
to locate a binary. Just because you can run it by hand does not mean it can
run without you around.

### Storing a command's output in a variable

```bash
# general format
VAR=$(command_to_execute)
```

Example
```bash
TODAY=$(date)
echo $TODAY
```

Executes the `date` command and stores its output in a variable `TODAY`. Then `echo` the content of `$TODAY` to the terminal.

You are not restricted to a single command. You can also insert a pipeline of commands inside `$( )`.

### Graceful Errors

In most `bash` shell scripts you may `set -e` near the head of the script. This flag
tells the script that, upon any error, it should escape/exit the script and stop running.
This is important since to proceed past an error may produce very bad results or
unintended consequences.

Another option is to use conditionals, such that when a specific line of the script
fails to execute, the failed line can `exit` with a non-zero code. You can retrieve the error code of the last executed command with `$?`. This can be useful output for debugging.

### Logging

A simple-yet-valuable step in your scripting is to log. You can log every action
taken by the script, or limit logging to successes or failures.

A common format for logging might be a snippet like this:

```bash
# First establish the datetime:
NOW=$(date +"%m-%d-%Y-%H:%M:%S")
echo $NOW " OK - Successfully processed " $FILENAME >> /var/log/output.log
```
The result would be a single file building with each row as it is logged.
Note the `>>` to append to a file instead of overwriting it!

### Comments

One of the most useful habits you can develop as a programmer is adding comments
to your code. This explains each chunk of code but might also justify why a particular
choice has been made. This will be invaluable to you, when you come back to the code
two years later, or when your code is shared with others.

Here's a simple example demonstrating good commenting practices:

```bash
#!/bin/bash
# This script greets a user by name
# Usage: ./greet.sh <name>

# Exit immediately if any command fails
set -e

# Check if a name was provided as an argument
if [ $# -eq 0 ]; then
    echo "Error: Please provide a name"
    exit 1
fi

# Store the first argument in a variable
NAME=$1

# Display a personalized greeting
echo "Hello, $NAME! Welcome to bash scripting."
```

## Additional Practice

1. Create a script called `file-info.sh` that:
   - Accepts a filename as a command-line argument
   - Checks if the file exists (exit with error if it doesn't)
   - Displays the file size, line count, and word count
   - Uses full paths for all commands (`/usr/bin/wc`, etc.)
   - Includes proper error handling with `set -e`

2. Create a script called `process-logs.sh` that:
   - Reads from a log file (provided as an argument)
   - Filters lines containing "POST" or "GET"
   - Counts occurrences of each type
   - Writes a summary report to a new file
   - Uses pipes to chain commands together
   
   **Hint:** You can use the log file from `retrieve-file.sh` (which downloads `http.log` from S3), or create your own sample log file with POST and GET entries for testing.

Explore the bash scripts in [this folder](.).

## Advanced Concepts (Optional)

1. Write a script called `backup.sh` that:
   - Takes a directory path as an argument
   - Creates a timestamped backup directory (e.g., `backup-2024-01-15-14-30-00`)
   - Copies all files from the source directory to the backup directory
   - Logs each action to a log file with timestamps
   - Uses environment variables for paths

2. Write a script called `system-check.sh` that:
   - Checks if specific commands are available on the system (`python3`, `git`, `curl`)
   - Uses conditional logic to report which commands are found and which are missing
   - Exits with appropriate error codes based on what's missing
   - Logs the results with timestamps
  
   **Hint:** Run `which` on a fictional command, check the failed command's exit code with `$?` to get an idea for the exit codes to check for.

3. Write a script called `batch-rename.sh` that:
   - Takes a directory path and a file extension as arguments
   - Renames all files with that extension by adding a prefix (e.g., `backup-` before the original name)
   - Creates a log file documenting all renames
   - Includes safety checks to prevent overwriting existing files
  
## Resources

- <a href="https://linuxconfig.org/bash-scripting-tutorial" target="_blank" rel="noopener noreferrer">Bash Scripting Tutorial</a>
- <a href="https://ryanstutorials.net/bash-scripting-tutorial/bash-script.php" target="_blank" rel="noopener noreferrer">Ryan's Bash Scripting Tutorial</a>
- <a href="https://www.youtube.com/watch?v=tK9Oc6AEnR4" target="_blank" rel="noopener noreferrer">Watch: Bash Scripting Tutorial</a>

