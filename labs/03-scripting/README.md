# Lab 03: Scripting

The goal of this activity is to get you comfortable with writing scripts in bash and Python. You will practice working with environment variables, making API requests, and handling user input. Follow the steps below to create scripts that demonstrate these fundamental scripting concepts.

Follow the steps below for practice with writing scripts. You will develop one bash script and one Python script in this lab. Commit both to your `ds2002-scripts` repository and submit the URL to your repo for grading.

## Setup

For the Python scripts in this lab, you will need Python3 installed on your local system, or use Codespace.

Python3 should be available in your path. Use `which python3` to find the path. That path should be something like `/usr/bin/python3`

You will also need to install the `requests` library for Python. To do this, run this command:

```bash
python3 -m pip install requests

# or

pip install requests
```

Depending on your account permissions you may get an error, preventing you from installing packages into the system's python environment. In such case, add the `--user` flag to the install command, which will direct the installation into a personal package library in your home directory `~/.local`.

```bash
python3 -m pip install --user requests

# or

pip install --user requests
```

## Script 1: Write a Bash script to analyze Moby Dick

**The Case:** You've just received an urgent email from a major publishing house. They're preparing a special annotated edition of Herman Melville's classic novel "Moby Dick" and need your help with a critical literary analysis project. 

The editorial team wants to analyze word frequency and usage patterns throughout the 200,000+ word novel, but they're drowning in manual work. They've been searching through the text by hand, and with dozens of words to analyze, this approach is taking weeks. The deadline for the annotated edition is fast approaching, and they need a solution—fast.

**Your Task:** Build an automated text analysis tool that can instantly search through the entire novel, count word occurrences, and generate reports. This script will save the editorial team countless hours and help them meet their deadline. You're not just writing code—you're rescuing a publishing project!

**Let's Build It:**

1. In the fork of your ds2002-course repository, create a new folder `mywork/lab3`.

2. Change to the `mywork/lab3` directory and create a new file `analyze-moby-dick.sh`.

3. The `analyze-moby-dick.sh` bash script should automate the following tasks and meet the following specifications:

   a. The script accepts two command line arguments. The first argument is a string that defines the word to search for; the second argument specifies an output file. Internally, the script stores the value of the first command line argument in a variable named `SEARCH_PATTERN` and second in a variable named `OUTPUT`.

   b. Use the curl command to download the text of the Moby Dick novel and save it as `mobydick.txt` in the current directory. 
   
   **The url is:**
   ```
   https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt 
   ```
   
   **Hint:** Review [practice/02-cli](../../practice/02-cli/README.md) for using curl to downloading data and saving to a file.

   c. Use the `grep` command to search the `mobydick.txt` file for occurrences of the word specified by the first command line argument, now stored in the `SEARCH_PATTERN` variable. **Hint:** Lookup the `grep -o` option.

   d. Use `wc` to count the number of occurrences of the SEARCH_PATTERN returned by grep. **Hint:** Pipes can be of great help here. Store that number in a new variable `OCCURRENCES`.

   e. Write to the file specified by `OUTPUT` the following message: "The search pattern `<S>` was found `<N>` time(s)." Replace `<S>` and `<N>` with the proper variable expressions.

   **🎉 Success!** Your script is working and the publisher is thrilled! They can now analyze any word in the novel in seconds instead of hours. Move on to Script 2, or push your skills further with the additional challenge below.
   
   **⚡ Additional Challenge (Optional):**
   Your script impressed the editorial team so much that they want to expand its capabilities! They're asking for a more robust version that handles edge cases and provides richer analysis:
   
   a. If the second command line argument is missing (i.e. no output file specified), the script should write the output to a default file `results.txt`.

   b. If the specified output file already exists, the script should inform the user that the file already exists and abort processing.

   c. In addition to outputting the total number of occurrences, the script will also list the lines in the text where the searched word was found. **Hint:** check out the `cut` command.

   d. The search should be case-insensitive. **Hint:** Check the documentation for the `grep` command.

With your bash script complete, you've successfully automated the text analysis workflow and saved the publishing team countless hours. The script demonstrates the power of combining command-line tools like `curl`, `grep`, and `wc` with bash scripting to solve real-world data processing challenges. Now, let's move on to exploring how Python can help us interact with remote APIs and work with more complex data structures.

## Script 2: Use Python to fetch remote data

**The Case:** You're working with a software development team that needs to track and analyze developer activity across multiple GitHub repositories. The team lead wants to create a dashboard that shows recent activity, but manually checking each developer's GitHub profile is time-consuming and doesn't scale.

**Your Task:** Build a Python script that automatically fetches and displays recent GitHub activity using the GitHub API. This script will demonstrate how to work with REST APIs, handle JSON data, and use environment variables for configuration—essential skills for any data scientist working with modern web services.

**Let's Build It:**

1. Create a new script called `github-events.py` in your `mywork/lab3` directory, and open it in an editor.

2. Put your Python3 path in a shebang line. Use the command below to find your `PATH` to python:

    ```
    which python3
    ```

    For the shebang, use the absolute path to `python3` or leverage the more flexible `/usr/bin/env` command to identify the python3 interpreters (see lecture slides).

3. For this script you will need to set an environment variable in your `bash` shell. Edit your `~/.bashrc` file and export a new variable named `GITHUB_USER`. Give it the value of your own GitHub username.

    ```
    export GITHUB_USER="ksiller" # replace with your own GitHub username
    ```

    After you add this line, run the command `source ~/.bashrc` to load this new value into your environment.

4. Back to your Python script. In order to work with `env` variables and remote APIs you need three imports:

    ```python
    import os
    import json
    import requests
    ```
    To retrieve the value of an environment variable in Python, use this syntax:

    ```python
    GHUSER = os.getenv('GITHUB_USER')
    ```

    You can test that this works by using Python interactively. Load your imports and execute that line, and you should be able to `print (GHUSER)` to get your username.

5. Next, we will use this variable to fetch the recent activity for this user account (you!) in GitHub. First let's configure the remote endpoint to get that information. The format for that API address is:

    ```
    https://api.github.com/users/USERNAME/events
    ```

    To dynamically insert your GITHUB_USER name into this URL, define a `url` variable like this:

    ```python
    url = f'https://api.github.com/users/{GHUSER}/events'
    ```

    You will know if this is formatted correctly if you `print(url)` within Python and see a well-formed address.

6. Use this address to fetch your recent GitHub activity with the `requests` library. We will load the response back from the API into a variable, and loop through the first five responses:

    ```python
    r = json.loads(requests.get(url).text)

    for x in r[:5]:
      event = x['type'] + ' :: ' + x['repo']['name']
      print(event)
    ```

    Take a moment to `print(r)` and view all the results. You can also do this by opening the fully-formatted URL above in a web browser. Note the variety of data available around your work in GitHub. 

    Much more information on the [**GitHub API is available**](https://docs.github.com/en/rest?apiVersion=2022-11-28). 

7. Use `chmod` to make your script executable, add the path to your script to the PATH environment variable in your ~/.bashrc, source the ~/.bashrc, and run it. Make sure no errors occur.

8. **Additional Challenge (Optional):** To take it a step further, explore the keys contained in the returned json data and output additional information for each event.
    
**🎉 Success!** You've successfully created a script that interacts with a real-world API! Your script can now fetch live data from GitHub, parse JSON responses, and display meaningful information. This demonstrates the power of Python for working with web APIs—a skill that's essential for accessing data from countless services across the internet. Next, let's explore how to work with environment variables and user input to make your scripts more flexible and interactive.

## Submit your work

You created two scripts for this lab (`analyze-moby-dick.sh` and `github-events.py`). They should be in a folder `ds2002-course/mywork/lab3` within your fork of the course repository, added, committed, and pushed. Then submit the URL of `ds2002-course/mywork/lab3` in the text box within Canvas.
