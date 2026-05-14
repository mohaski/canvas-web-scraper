# Technical Lesson: Git and GitHub Basics

# Technical Lesson: Git and GitHub Basics

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Technical Lesson: Git and GitHub Basics

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[15-20 minutes]

In this lesson, we will walk through the process of getting projects remotely hosted on GitHub onto your local machine and into a local Git repository. This lesson will demonstrate how to fork a repository containing a lab on Python strings, clone it, and open a Jupyter notebook that contains the lab. These skills build on the foundational concepts we have covered so far, such as Git commands, repository management, and working with virtual environments in Anaconda.

### Resources

* [GitHub repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-strings)
* Previous setup topics (Git, Anaconda, Github)

### Tools

* Computer with Internet connection
* Data science ecosystem:  
  + Terminal
  + Activated `learn-env`
  + Fully configured Git/GitHub
  + Jupyter Notebook

### Instructions

The first step is to create a folder on your computer that can host the repository that you are about to fork and clone.

### Step 1: Fork the Repository

1. **Go to the [GitHub repository


   Links to an external site.](https://github.com/learn-co-curriculum/dsc-strings).**
2. **Fork the repository**:

* Click the **Fork** button on the top right to create a copy of the repository in your personal GitHub account.

![GitHub screen showing the Fork button location](https://moringa.instructure.com/courses/1406/files/624779/download)

* If you already have a fork, a modal will appear. Scroll to the bottom and click the link to view your existing fork. Otherwise, you will be redirected to your new personal copy of the repository.

1. **Copy the repository URL**:

* Press **cmd + L (Mac)** or **ctrl + L (Windows)** to highlight the URL bar.
* Press **cmd + C (Mac)** or **ctrl + C (Windows)** to copy the URL.

### Step 2: Clone the Repository

1. **Open Terminal**:

* Make sure you are in your course materials folder or a specific subfolder like phase\_1.

1. **Clone the repository**:

* Type `git clone`  and paste the repository URL (use **cmd + V for Mac**; **shift + insert for Windows** in Git Bash).
* Press Enter to execute the command.

1. **Navigate to the repository folder**:

* After cloning, change into the new repository directory:

`cd <name_of_your_repository>`

### Step 3: Start the Jupyter Notebook

1. **Activate your conda virtual environment**:

* Type the following command and press <Enter>: `conda activate learn-env`.

1. **Start Jupyter Notebook**:

* In the terminal, type `jupyter notebook` and press <Enter>.
* This will open the Jupyter Notebook interface in your default web browser, displaying the contents of the current directory.

1. **Open the notebook file**:

* In the browser window, navigate to the `index.ipynb` file within the cloned repository directory and click on it to open.

1. **Stopping the Jupyter Notebook**:

* To stop the Jupyter Notebook, return to the terminal where it is running and press ctrl + C (control key + the letter c).

### Summary

In this lesson, you learned how to:

* Fork a GitHub repository
* Clone the repository to your local machine
* Work with Jupyter Notebooks locally

In the next lab, you’ll put what you learned into practice. This foundational knowledge will help you manage and collaborate on your data science projects effectively.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243478

Scraped At: 2026-05-14T20:45:00.306274
