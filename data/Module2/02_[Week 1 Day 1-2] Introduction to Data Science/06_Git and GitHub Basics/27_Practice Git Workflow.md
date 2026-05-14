# Practice: Git Workflow

# Practice: Git Workflow

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Practice: Git Workflow

Icon Progress Bar (browser only)

4 min read

Now that you’ve seen a little bit of the bash shell and cloned a Git repository from GitHub, it’s time to practice a full workflow cycle in more detail. This lesson builds on the foundational concepts we covered earlier, such as initializing repositories, staging changes, and synchronizing with remote repositories. We’ll start by creating a new Git repository if you are not working from an existing one.

From there, we'll further investigate how the concepts of `git add`, `git commit`, and `git push` work in practice.

### Instructions

### Step 1: Creating a New Git Repository

1. **Go to GitHub to create a new repository**:

* Navigate to [GitHub New Repository


  Links to an external site.](https://github.com/new) or click the “New” button under the repositories tab on your profile page.

1. **Fill out the repository details**:

* **Name**: git\_practice
* **Description**: Leave it blank for now.
* **Public vs. Private**: Select Public. A public repository is visible to anyone on GitHub.
* **Initialize this repository with a README**: Leave this option unchecked.

* **If checked:** you will clone the online repository as we did before. This will ensure that the local repository and remote repository start at the same point – both with the README.md file in it.
* **If unchecked:** then you can git init a new empty repository on your local computer and then connect it to the online repository. Both repositories will start empty at the same point in development and thus can be connected.

![GitHub Create a new repository screen](https://moringa.instructure.com/courses/1406/files/624685/download)

1. **Create the repository**:

* Click the **Create repository** button. You will see the following page:

![GitHub new repo setup screen showing the SSH button and set of terminal commands to initialize a repo](https://moringa.instructure.com/courses/1406/files/624845/download)

1. **Copy the SSH address**:

* Select the SSH address from the page that appears after creating the repository. This is the address you will use to connect your local repository to the remote one.

### Step 2: Create a New Directory for Your Repo

1. **Open Terminal**:

* Open your command line interface (Terminal on Mac, Git Bash on Windows).

1. **Navigate to your desired directory**:

* Example: `cd ~/Documents/Flatiron/C0_Module_2`

1. **Create a new folder for this lesson**: `mkdir git_practice`

### Step 3: Navigate into Your New Folder

**Change directory**: `cd git_practice`

### Step 4: Initialize This Folder as a Git Repository

**Initialize the repository**: `git init`

### Step 5: Create a README

**Create a README file**:

* Simple method: `echo "# git_practice" >> README.md`
* Using a text editor such as nano: `nano README.txt`

* Type "# git\_practice" in the file. Press "Ctrl+X" to quit and press "Y" to save changes.

### Step 6: Check Git Status

**View the status**: `git status`.

* This command shows the current state of your working directory and staging area.

### Step 7: Add Your File

**Add the README file to the staging area**: `git add README.md`

* Alternatively, add all files: `git add --all`

### Step 8: Check Git Status Again

**View the status**: `git status`.

* Note the difference now that your file is staged.

### Step 9: Commit Your Changes

**Commit the changes**: `git commit -m "your message here"`.

### Step 10: Add a Remote Location

**Connect to the remote repository**:

```
git remote add origin git@github.com:<your_user_name>/git_practice.git
```

* Replace <your\_user\_name> with your GitHub username. You can copy and paste the SSH address provided by GitHub.

![GitHub repo address screen highlighting the copy button](https://moringa.instructure.com/courses/1406/files/625175/download)

### Step 11: Pushing Your Changes

**Push the changes to GitHub**: `git push origin main`.

* This command syncs your local changes with the remote repository on GitHub.

### Step 12: Preview Your Changes

**Refresh the GitHub page**:

* After pushing your changes, refresh the GitHub repository page. You should see your README.md file.

![GitHub screen showing successful repo setup](https://moringa.instructure.com/courses/1406/files/625086/download)

### Summary

In this lesson, you practiced your bash skills with the command line and started practicing your version control skills with Git. You created your first Git repository from scratch and practiced adding, committing, and pushing those changes to GitHub. This foundational workflow is essential for managing and collaborating on data science projects.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243479

Scraped At: 2026-05-14T20:45:05.129025
