# Introduction to Virtual Environments

# Introduction to Virtual Environments

## ![](https://bletchley.instructure.com/courses/139/files/735/preview) Introduction to Virtual Environments

Icon Progress Bar (browser only)

7 min read

Having successfully installed and configured Git and GitHub, the next step is to set up our virtual coding environment using both venv and PyPI. This will allow us to access powerful toolkits and packages that are essential for data science.

We will utilize PyPI to install a pre-specified virtual environment that ensures you have all the necessary libraries and tools for data manipulation, analysis, and machine learning in a single environment. This setup will enhance your efficiency and streamline your workflow, allowing you to focus on the actual data science.

### Introduction to Virtual Environments

Imagine you're working on multiple Python projects on your computer. Project A needs version 2.1 of a library called requests, while Project B requires version 1.8 of the same library. If you install packages globally on your system, you can only have one version of requests at a time - creating a conflict that could break one of your projects.

This is where **Python virtual environments** come in. Think of an environment as an isolated workspace for your Python project, complete with its own set of installed packages and specific Python version. Each environment is like having a separate computer for each project, preventing conflicts between different projects' dependencies.

When you install a package like pandas or matplotlib, you'll notice many additional packages being installed that you didn't explicitly request. This isn't an error - it's how Python's package ecosystem works. **Dependencies** are other packages that your requested package needs to function properly.

For example, when you install matplotlib for plotting, it automatically pulls in dependencies like numpy (for numerical operations), pillow (for image handling), cycler (for color cycling), and several others. These underlying libraries handle the mathematical computations, image processing, and formatting that make matplotlib's plotting capabilities possible.

Similarly, pandas depends on numpy for its core data structures, pytz for timezone handling, and python-dateutil for date parsing.

You'll see packages with names like setuptools, wheel, six, or packaging being installed - these are foundational tools that help other packages install and run correctly.

### Interchangeable Terms

You'll hear Python developers use "package" and "library" interchangeably when talking about installable code:

* "Install the numpy **package**"
* "Import the pandas **library**"
* "The matplotlib **package/library** is great for plotting"

In practice, they mean the same thing when discussing code you install with pip install. Whether someone says "pandas package" or "pandas library," they're referring to the same thing you install and import.

### Technical Difference

Technically, a **package** is a folder containing Python files, while a **library** is a broader collection of related functionality (multiple packages). But this distinction rarely matters in day-to-day work.

Don't worry about the terminology. When someone mentions a Python "package" or "library," they're talking about code you can install with pip and import into your projects. Both terms are correct and widely used.

#### Why Virtual Environments are Important

### The Challenge/Problem

One of the biggest challenges in coding is the "it works on my machine" problem. You write code that runs perfectly on your computer, but when a colleague tries to run it, they get errors. Often, this happens because:

* You have different versions of Python installed
* You have different versions of required packages (dependencies)
* You have packages installed that your colleague doesn't have
* Your operating system handles certain operations differently

### Environmental Consistency

Critical in data science, where slight differences in package versions can lead to different analytical results, model predictions, or visualizations. This is crucial for:

* Collaboration: Team members can easily work on the same project
* Deployment: Your code will work the same way in production as it does locally
* Future maintenance: You can return to your project months later and still run it
* Scientific computing: Research results must be reproducible to be valid

### Reproducibility

Reproducibility is the cornerstone of reliable data science. When you share a project, collaborate with teammates, or return to your own work months later, you need confidence that the code will produce identical results. Without proper environment management, you're likely to encounter the dreaded "it works on my machine" problem - where code that runs perfectly on your computer fails elsewhere due to different package versions, missing dependencies, or incompatible software configurations.

Virtual environments solve this by creating isolated, documented setups that can be shared and replicated elsewhere by anyone.

### How do PyPI and venv work?

PyPI offers access to a comprehensive suite of tools and features specifically designed to streamline and enhance the workflow of data scientists. By integrating powerful pre-built packages and libraries with advanced capabilities, PyPI ensures that you have everything you need to focus on your data analysis, modeling, and visualization tasks.

Here’s a closer look at how PyPI and venv work to significantly benefit your process as a data scientist:

### Access to Packages

PyPI, commonly referred to as pip, installs packages from the Python Package Index, the official repository containing hundreds of thousands of Python packages.

It communicates directly with Python's built-in virtual environment tools and focuses specifically on Python packages.

Pip is prepackaged as a part of most newer Python versions and you should already have access to it.

### Basic pip Usage

Utilizing specific pip commands in your terminal, you can install pre-built packages from the Python Package index. These are just example commands, we will walk through the actual install on the next page.

`pip install requests          # Install the latest version`

`pip install requests==2.1.0   # Install a specific version`

`pip list                      # Show installed packages`

`pip uninstall requests        # Remove a package`

### Isolated Environments

venv, Python's native virtual environment tool, allows us to create a unique environment folder within our computer for different projects, where we can install specific packages and versions via pip.

A virtual environment creates an isolated Python installation for your project. When you create and activate a virtual environment:

* Python looks for packages in the specific environment's folder, not globally
* Any packages you install with pip go into this environment only
* You can have different versions of packages in different environments
* Each environment can even use a different version of Python if necessary

This allows for different projects to coexist without interfering with each other, promoting better code organization, reproducibility, and ease of collaboration.

### Basic venv Usage

We again can utilize specific terminal commands to create and activate our virtual environments. These are just example commands, we will walk through the actual install on the next page.

* Create a new virtual environment. Need to provide a name, i.e. 'example\_env'. This creates a folder for the environment in your current working directory. `python3 -m venv example_env`

* Activate the virtual environment. Need to ensure that you activate the specific environment you want to be working and installing packages in before doing so.
  + On Windows: `example_env\Scripts\activate`
  + On macOS/Linux: `source example_env/bin/activate`

* Your terminal prompt should now show the environment name (might look slightly different depending on OS)`(example_env) $`

### Environment Blueprint

So far we have discussed how PyPI and venv work locally for an individual. The real power lies in the reproducibly of an environment however.

To accomplish this, venv utilizes what is known as a requirements file. This file is general named **'requirements.txt'** accordingly and is a simple text file that specifies the packages and desired versions that should be installed.

This file can then be attached to any project, perhaps via a Github repository, and shared out so that anyone else can reproduce the same environment on their machine.

* Install packages specified in file `pip install -r requirements.txt`

* Create requirements file from existing environment `pip freeze > requirements.txt`

By leveraging these features, PyPI and venv enable data scientists to work more efficiently and effectively, ensuring that you can tackle complex data challenges with confidence while ensuring reproducibility.

### Next Steps

With an understanding of virtual environments and their benefits, it’s time to install and setup the environment needed for this course on your system. This will set up your development environment and prepare you for data science tasks. Follow the instructions in the next section to create a virtual environment and install the necessary packages in order to get started with your Data Science environment.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243464

Scraped At: 2026-05-14T20:43:54.034492
