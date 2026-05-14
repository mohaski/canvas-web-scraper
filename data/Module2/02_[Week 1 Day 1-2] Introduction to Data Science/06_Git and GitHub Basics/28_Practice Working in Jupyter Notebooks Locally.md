# Practice: Working in Jupyter Notebooks Locally

# Practice: Working in Jupyter Notebooks Locally

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Practice: Working in Jupyter Notebooks Locally

Icon Progress Bar (browser only)

4 min read

As a data scientist, collaborating with team members and working on shared projects is a crucial skill. This practice lab will guide you through the process of downloading repositories from others and editing their analysis files using Jupyter notebooks. By mastering these skills, you'll be able to seamlessly integrate into data science teams, contribute to ongoing projects, and build upon the work of your colleagues.

This exercise simulates a common scenario in data science teams: you'll act as a junior data analyst on Flatiron School's marketing team, tasked with creating and experimenting with various school mantras for a potential social media campaign. Your manager, a senior data scientist, has provided a blank template for you to work with.

By the end of this practice, you should be comfortable with:

1. Forking and cloning GitHub repositories
2. Opening and editing Jupyter notebooks from cloned projects
3. Making changes to notebook cells and running code

This practice will reinforce your understanding of version control, local development environments, and collaborative data science practices.

### Instructions

### Step 1: Fork and Clone the Repository

1. **Fork the repository:**

* Go to GitHub and fork [the dsc-running-jupyter-locally-lab repository


  Links to an external site.](https://github.com/learn-co-curriculum/dsc-running-jupyter-locally-lab "Link") to create a copy in your GitHub account.

1. **Copy the URL:**

* Copy the URL of your forked repository.

1. **Open Terminal:**

* Open a terminal window (Terminal on Mac, Git Bask on Windows).

1. **Activate your conda virtual environment:**

* Make sure to activate your conda virtual environment so you have the right version of Python and all of the necessary packages:
* On a mac or in Git Bash on Windows, type `conda activate learn-env`.
* If you have to use the conda shell on windows, type `activate learn-env instead`.

1. **Clone the repository:**

* Navigate to your desired directory and clone the repository using `git clone <URL>`. Replace <URL> with the URL of your repo you copied.

1. **Navigate to the cloned directory:**

* Change to the directory you just created by typing `cd <directory_name>`.
* Running the `ls` command will show you the name of the directory you downloaded.

1. **Start Jupyter Notebook:**

* Run the following command to start Jupyter Notebook: `jupyter notebook`
* In the browser window that opens, click on the `index.ipynb` file to open it.

### Step 2: Make Changes in Jupyter Notebooks

1. **Assign a number to a variable:**

* Replace None with 42:

```
number = None  
number
```

1. **Assign a string to a variable:**

* Locate the `flatiron_mantra` variable and replace None with `"Change Things"`. Make sure to include the double quotes.

```
flatiron_mantra = None  
flatiron_mantra
```

1. **Add a new markdown cell:**

* Below the previous code cell, add a new markdown cell and type:

```
### This is a new header
```

1. **Add a new code cell:**

* Add a new code cell below this one and write any code you want.

### Solution

### Select to see the solution for Step 2

1. **Input:**

```
number = 42  
number =
```

**Expected Output:**

```
42
```

1. **Input:**

```
flatiron_mantra = "Change things"  
flatiron_mantra
```

**Expected Output:**

```
Change things
```

1. Add a new markdown cell below this one and type

```
### This is a new header
```

**Expected Output:**

Markdown cell will change to:

**This is a new header**

1. **Input:**

```
flatiron_mantra_repeated = [flatiron_mantra for x in range(3)]  
flatiron_mantra_repeated
```

**Expected Output:**

```
['Change things', 'Change things', 'Change things']
```

### Summary

Great work! You are well on your way to mastering Jupyter Notebooks. In this practice, you reviewed using the command line and `git clone`, running cells, and checking your outputs. This practice helps solidify your skills in setting up and working with Jupyter Notebooks locally, an essential part of the data scientist’s toolkit. You now have the capability to download repositories, open Jupyter Notebooks, and make necessary edits, which is crucial for collaborating on data science projects.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243480

Scraped At: 2026-05-14T20:45:10.517186
