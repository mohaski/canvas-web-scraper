# Defining Git and GitHub Basics

# Defining Git and GitHub Basics

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Defining Git and GitHub Basics

Icon Progress Bar (browser only)

14 min read

Having set up your data science environment, it’s now time to delve into Git and GitHub basics. These tools are essential for managing your projects and ensuring you have robust version control. Building on the foundational knowledge you gained during the environment setup, this section will provide an in-depth understanding of key terminology and concepts, and explain how everything works together. This will enable you to effectively manage your code and collaborate with others in your data science projects.

### Git and GitHub Basics

To effectively use Git and GitHub, it’s important to understand the following key terms and concepts. The following list provides detailed explanations of each, helping to solidify how they function individually and together in your workflow.

### Cloning

**Cloning** makes a copy of an existing online repository on your local machine. This can be executed by typing the follow command in terminal with the address for the desired remote repository:

`git clone [REMOTE_REPOSITORY_ADDRESS]`

You have already used this command when you created a local copy of the remote repository containing your Conda environment for this course. Once you have cloned a repository, you can use Git to track any changes you make to this local repository. Be cautious, though, as changes to your local clone can be sent up to the original remote repository. If the remote repository is on your GitHub account, this is usually no problem. However, if it belongs to someone else, you could unintentionally alter their project.

### Forking

**Forking** is a critical feature in GitHub that allows you to create a personal copy of someone else’s repository on your GitHub account. This process is essential for contributing to open-source projects or collaborating with others without affecting the original codebase.

The original remote repository that you fork from is referred to as the **upstream repository**. When you fork a repository, GitHub creates a copy of the upstream repository in your `<github-username>` GitHub account. This forked repository maintains the same file/directory structure, commit history, and usually the same name as the original repository. The primary difference is that it resides in your account, isolating the original repository from any changes you make. In this scheme, the forked repository is often referred to as origin.

Here’s how forking functions:

1. **Navigate to the Repository**: For example, if you want to fork the `dsc-prework-intro` repository that exists on the `learn-co-curriculum` GitHub account, you would go to the GitHub page where it is hosted.
2. **Fork the Repository**: Click the “Fork” button (highlighted on the page). Once the forking process is complete, GitHub will create a copy of the repository on your GitHub account.

After forking, you need to clone your fork to work on it locally:

1. **Clone Your Fork:**

```
git clone git@github.com:<your-username>/<repository-name>.git
```

This command creates a local repository with the same structure as your fork (origin) and the upstream repository.

The important point is that the original upstream repository is shielded from any changes you might make. The local cloned repository is only connected to your fork (origin) but not to the upstream repository. This allows you to make changes to the project locally and push them to your fork without affecting the upstream repository.

**Example:** Suppose you want to contribute to a data science project hosted by a collaborator. By forking their repository, you can make and test changes independently.

![GitHub screen showing Fork button](https://moringa.instructure.com/courses/1406/files/624830/download)

Later, if some of the changes you made to the project might be useful to the upstream project, you can flag these changes and request that the owner of the upstream repository review and adopt them. This is known as a pull request. We will discuss pull requests in more depth in a later module when we cover Git collaboration, but it is important to understand this concept to complete the picture.

**The final step is to clone your fork.** After all, you want to be able to work locally on the lab or project you forked. Cloning your fork might look something like this:

![Terminal showing cloning a forked repo](https://moringa.instructure.com/courses/1406/files/625178/download)

The address git@github.com:admveen/dsc-prework-intro is the SSH address of the remote forked repository.

Once this is done, you will have created a local repository that has the same structure as your fork, the origin of your local repository. It will also have the same structure as the upstream repository. The original upstream repository is shielded from any changes that you might make, and the local cloned repository is only connected to your fork (origin). You are free to make changes to the project as you like locally and push it to your fork without affecting someone else’s work.

**Why Forking is Important:**

* Work on projects independently without affecting the original codebase.
* Experiment with new features or fixes in a safe environment.
* Contribute to open-source projects by submitting pull requests with your improvements.
* Collaborate with others by sharing your fork and inviting feedback.

By understanding and utilizing forking, you can effectively manage and contribute to data science projects, ensuring that your work is organized, collaborative, and impactful.

### Repository Initialization

Local repositories do not always have to be created via cloning a remote repository. You can also directly initialize a local git repository from a working directory with: `git init`

When creating a repository from scratch, you usually create an empty directory and then run `git init` from inside that directory. This command initializes a new Git repository in the directory, allowing you to start tracking changes.

The appearance of the cyan “(main)” on the terminal prompt indicates that your working directory is now a Git repository. It shows that you are working on the main branch of your repository, which is the primary default workflow of your project.

An example is shown below:

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/625037/download)

### Checking Status

To see what changes have been made since the last commit, use `git status`.

This command provides information about modified, deleted, or added files, showing their status in relation to the last commit. Regularly using `git status` while working on a project helps you keep track of which files have been modified, added, or deleted and need to be committed. Understanding the git status output is crucial for managing your changes effectively.

**Example Workflow:**

Imagine you have a repository with a README.md file that you have already committed. You then make changes to this file and create a new Jupyter notebook.

1. **Modify the README.md file and create a new Jupyter notebook**:

* Edit README.md and save your changes.
* Create a new file analysis.ipynb for your data analysis.

1. **Check the status**: `git status`
2. **Interpret the output:**

You might see something like this:

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/625205/download)

This output tells you that `README.md` has been modified but not staged, and `first_notebook.ipynb` and `.gitignore` are **untracked files** since they were freshly created but not yet committed.

### The Staging Area

Before committing changes, you must add them to a **staging area** using the `git add` command. The staging area, also known as the **index**, acts as a temporary holding zone that lets you pick and choose which specific changes you want to include in your commit. This intermediate step gives you more control over your project history, allowing you to group related changes together into meaningful commits.

**Adding Changes to the Staging Area:**

You can add or remove files as you need to from the staging area and then when you are ready you can commit all the changes added to the staging area into a single commit. Having this extra step gives you a little more control over what gets grouped together into a single checkpoint in your project history.

To add changes to the staging area, use: `git add [FILE]`. You can also add all changes at once with: `git add .`.

**A Workflow Example:**

To see what has changed, you can check status: `git status`

You might see the following: 

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/624672/download)

* Red represents unstaged files
* Green represents staged files

The `git add` command has put our README.md file into the staging area ready for commit. If desired, additional files could be added to the staging area by using the git add command on those files.

Using the `git add .` command would put the README.md, first\_notebook.ipynb, and .gitignore into the staging area all at once.

**Understanding the Staging Area**

The staging area allows you to:

* **Group Related Changes**: You can group related changes together in a single commit, ensuring that each commit represents a coherent set of modifications.
* **Review Changes**: By staging changes, you have the opportunity to review what will be included in the next commit, reducing the risk of committing unwanted changes.
* **Organize Your Workflow**: The staging area helps you organize your workflow by separating the process of modifying files from the process of committing changes to the project history.

### Committing

Once you have staged all the changes you want to include in a commit, you will issue the commit command. A commit captures a snapshot of the current state of the staged changes, along with a descriptive message explaining what the commit is about. This step is crucial as it adds the changes to your project’s history, allowing you to track progress and revert to previous states if needed.

**Creating a Commit**

To commit staged changes, use the following command:

`git commit -m “[MEANINGFUL MESSAGE]”`

The commit message should be clear, concise, and written in the imperative mood. It should explain the purpose of the changes being committed. Good commit messages help you and your collaborators understand the history of the project.

**Examples of Good Commit Messages:**

* “Add spell check feature”
* “Fix infinite recursion bug in Karatsuba function”
* “Update discussion of Conda environments in README.md”

**Example Workflow**

Imagine you have made changes to your README.md file and created a new Jupyter notebook. You have already staged these changes using git add.

1. **Check the status** to confirm that the changes are staged: `git status`
2. **Commit the staged changes** with a meaningful message:

`git commit -m "write project introduction in README.md"`

Output:

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/625207/download)

After committing, the changes are now part of the official tracked history of your project. You can view this history using the `git log` command.

1. **View the commit history:**git log

Output:

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/625213/download)

The newest commit sits at the top (HEAD) of the commit history. Each commit includes a unique identifier (hash), author information, date, and the commit message.

**Adding Untracked Files and Committing**

Adding untracked files and committing them follows the same process. Let’s say you have created two new files: .gitignore and first\_notebook.ipynb. You need to stage and commit these files.

1. **Stage the new files:** `git add .gitignore first_notebook.ipynb`
2. **Check the status** to confirm the files are staged: `git status`
3. **Commit the new files** with a meaningful message:

`git commit -m "Create Jupyter notebook and .gitignore for .ipynb_checkpoints"`

Output:

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/624705/download)

After this commit, the .gitignore and first\_notebook.ipynb files are now part of the commit history and are tracked files.

### Pushing

Your local repository is usually connected to a remote repository, meaning they share a commit history. This connection is established when you clone a repository from a remote source, such as GitHub. Initially, the local repository (clone) and the remote repository (fork) have the same commit history. However, as you make changes to your local repository and commit them, these changes need to be synchronized with the remote repository.

An illustration of the situation can be seen below:

![Github process diagram](https://moringa.instructure.com/courses/1406/files/625247/download)

**Pushing** adds the new commits made to your local repository onto the corresponding remote repository on GitHub. In simple terms, pushing is when you sync your local work with what is hosted in the cloud on GitHub.

**How to Push Changes**

To push changes, use the following command: `git push [REMOTE LOCATION ALIAS] [BRANCH]`

* **Remote Location Alias**: This is a placeholder name for a remote repository’s address that your local repository is connected to and has a shared history with. When you clone a repository, Git automatically creates a remote location alias called origin within your local repository. This alias points to the GitHub address of the remote repository you cloned.
* **Branch**: This specifies the branch where you made commits. For example, the main branch is typically named "main".

**Example Workflow:**

Imagine you have committed changes to the main branch of your local repository and now want to push these changes to the remote repository on GitHub.

1. **Push the changes**: `git push origin main`

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/624706/download)

1. **Understand the process**:

* The `origin` alias refers to the remote repository on GitHub.
* The `main` branch is the branch you are pushing to.

After running this command, the corresponding remote repository on GitHub will reflect the new commits you made locally.

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/624671/download)

### Pulling

Pulling brings remote changes down to your local repository. It is the reverse of pushing and ensures that your local repository is synchronized with the remote repository. To pull changes, use the following command: `git pull [REMOTE LOCATION ALIAS] [BRANCH]`

* **Remote Location Alias**: This is the alias for the remote repository (usually origin).
* **Branch**: This specifies the branch you want to pull changes from (e.g., main).

**How to Pull Changes**

1. **Check for Remote Changes**: `git pull origin main`
2. **Understand the process**:

* The origin alias refers to the remote repository on GitHub.
* The main branch is the branch you are pulling changes from.

Pulling is useful when you want to ensure that your local repository is up to date with any changes made to the remote repository. This is particularly important before pushing changes, as it helps avoid conflicts and ensures that your work is based on the latest version of the project.

### Summary of Git Functions

Understanding Git functions can be complex, but the following visualization neatly summarizes various Git functions and how they connect the workspace, staging area, and local/remote repositories:

![Uploaded Image](https://moringa.instructure.com/courses/1406/files/624670/download)

**Initialize**:

* git init: Initializes a new Git repository.
* git clone <url>: Clones an existing repository.

**Update**:

* git pull: Pulls changes from the remote repository to the local repository.
* git fetch: Fetches changes from the remote repository without merging them.

**Changes**:

* git add: Adds changes to the staging area.
* git commit: Commits changes from the staging area to the local repository.
* git push: Pushes changes from the local repository to the remote repository.

### Conceptualize Git and GitHub

Understanding the core Git and GitHub commands is essential for managing your data science projects effectively. Below are the key commands, their purposes, and examples to help consolidate your learning.

Git commands with definition and example

| Command/Action | Description | Example |
| --- | --- | --- |
| git init | Initializes a new Git repository in the current directory, allowing you to start tracking changes. | `git init my_project` creates a new repository named "my\_project". |
| git clone <url> | Creates a local copy of an existing remote repository. | `git clone https://github.com/user/my_project.git` clones "my\_project" from GitHub. |
| Forking | Creates a copy of a remote repository on your GitHub account, allowing you to make modifications independently. | Fork "my\_project" on GitHub to create a copy you can edit. |
| `git status` | Shows the status of your working directory, providing information about tracked and untracked files, staged changes, and uncommitted modifications. | `git status` displays the current state of your repository |
| `git add` | Adds a specific file to the staging area, marking it for inclusion in the next commit. | `git add main.py` stages the file "main.py" |
| `git add .` | Adds all tracked files in the current directory to the staging area, staging all modified files that are already tracked by Git. | `git add .` stages all tracked and modified files. |
| `git commit -m "<message>"` | Creates a commit, saving a snapshot of the current state of the staged changes along with a descriptive message. | `git commit -m "Fixed bug in main.py"` creates a commit with a message. |
| `git push <remote> <branch>` | Uploads your local commits to a remote repository, sharing your changes with others. | `git push origin main` pushes changes in your local "main" branch to the "origin" remote. |
| `git fetch <remote>` | Downloads the latest changes from a remote repository without integrating them into your local working directory. | `git fetch origin` downloads changes from the "origin" remote. |
| `git pull <remote> <branch>` | Downloads and merges changes from a remote repository, combining the latest changes from a remote branch into your local branch. | `git pull origin main` downloads and merges changes from the "main" branch of the "origin" remote. |

### Summary

We have covered a lot of terminology and actions in Git, which might seem complex at first. However, practicing these commands will help you understand them better. It’s time for you to walk through the process step by step yourself. Next, you will practice using many of the concepts and commands we discussed in some hands-on labs.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243476

Scraped At: 2026-05-14T20:44:50.383708
