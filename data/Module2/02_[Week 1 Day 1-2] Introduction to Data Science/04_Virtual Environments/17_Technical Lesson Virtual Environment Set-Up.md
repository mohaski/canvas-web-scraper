# Technical Lesson: Virtual Environment Set-Up

# Technical Lesson: Virtual Environment Set-Up

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Virtual Environment Set-Up

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 15-20 minutes

Having discussed the importance of using virtual environments and how the PyPI and venv toolkit can help to manage dependencies and organize your projects, it’s time to set up the next part of your development environment by creating and install packages into a virtual environment for this course.

By the end of this lesson you will have created a virtual environment, installed the necessary packages into it and verified that it is working and can connect to VSCode.

### Instructions for Creating Virtual Environment

Read through the steps before beginning this installation.

* Items “in quotes” refer to the name of particular dialogue boxes and popups.
* > is used to indicate menu choices. For example, Start > Settings > System > About is the same as saying “Click on the Start menu. In the Start menu, scroll to and click on the Settings sub-menu. Click on System. Scroll to and click on About.
* Before starting, make sure you have:
  + Python 3.7 or higher installed on your computer
  + Visual Studio Code with the Python extension

This walkthrough will guide you through setting up a Python virtual environment using our provided script. This approach ensures everyone in the class has an identical Python environment with the same package versions. Follow these instructions carefully.

### [Step 1: Download and Organize Files](#dpPanel0)

1. **Download the provided files**:
   * Save a copy of both [venv\_creator.py


     Links to an external site.](https://drive.google.com/file/d/1x1xUmn7BJvo_rd5yHLhgT7TCYT12vh0G/view?usp=copy) and [requirements.txt


     Links to an external site.](https://drive.google.com/file/d/1kXGktOKKFEJEApTqTkvsyRGmpqAy92tU/view?usp=copy) to your Downloads folder
2. **Create a course folder (if not already done)**:
   * Navigate to an easily accessible location (like Documents)
   * Create a new folder called fs\_essentials\_course (or whatever name makes sense for you)
3. **Move downloaded files into this newly created folder.** Your folder structure should look something like:

```
📁 .../fs_essentials_course/  
  
├── venv_creator.py  
  
└── requirements.txt
```

### [Step 2: Open Terminal in Course Folder](#dpPanel1)

* [Windows Instructions](#dpPanel2Content)
* [Mac Instructions](#dpPanel3Content)
* [Linux Instructions](#dpPanel4Content)

### Windows Instructions

* Hold Shift and right-click within the fs\_essentials\_course folder
* Select "Open Git Bash here"
* Or navigate to your folder via git bash commands

### Mac Instructions

* Right click the actual fs\_essentials\_course folder
* Select “New Terminal at Folder”
* Or navigate to your folder via terminal commands

### Linux Instructions

* Right-click within the folder
* Select "Open Terminal here"
* Or navigate to your folder via terminal commands

### [Step 3: Run the Provided Python Script](#dpPanel5)

Execute the provided python script this command in your terminal: `python venv_creator.py --name essentials_env --requirements requirements.txt`

Breaking down the code

* `python venv_creator.py` - Runs our custom provided script that executes both venv and pip commands
* `--name essentials_env`- Creates an environment called "essentials\_env"
* `--requirements requirements.txt` - Installs all packages listed in the provided requirements file via pip

### [Output](#dpPanel6)

```
Running: python -m venv essentials_env  
  
Running: course_env/bin/pip install --upgrade pip  
  
Running: course_env/bin/pip install -r requirements.txt  
  
- Package installation progress bars  
  
...  
  
==================================================  
  
Virtual environment 'essentials_env' created successfully!  
  
==================================================  
  
To activate the environment:  
  
    source essentials_env/bin/activate  
  
  
To deactivate the environment:  
  
    deactivate  
  
  
To delete this environment, simply remove the directory:  
  
    rm -rf essentials_env  
  
==================================================
```

### [Step 4: Activate Environment](#dpPanel7)

Use the activation command shown in the script's output:

* **Windows (Git Bash):** `source essentials_env/Scripts/activate`
* **Mac/Linux (slight difference in path):** `source essentials_env/bin/activate`

Your terminal prompt should now show (`essentials_env`) at the beginning, indicating the environment is active.

### [Step 5: VSCode and Verification of Install](#dpPanel8)

Check that packages installed correctly with the command `pip list`.

This should print a list of all the packages and dependencies from your requirements.txt file. If nothing is showing up it means the packages were not installed. Make sure the requirements file is in the appropriate location.

1. **Open VSCode** at your course folder:

   ```
   # In terminal/gitbash within folder  
   code .  
     
   # Or open folder using VSCode Explorer panel (see Python lessons)
   ```
2. **Select the Python interpreter**:
   * Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (Mac)
   * Type and then select the "Python: Select Interpreter" command
   * Choose the interpreter that shows `./essentials_env/bin/python` or similar
3. **Create a test notebook**:
   * Create a new notebook file using VSCode: Name is something like **test.ipynb**
   * In the top-right corner of the notebook file, click into the 'Select Kernel' > 'Python Environments' Dropdown
   * Choose and select your essentials\_env environment (should be the recommended one)
4. **Verify imports and versions**: In the test.ipynb notebook create new code cell and enter the following. Run the cell (shift enter or "Run All") and compare output.

```
import sys  
  
print(f"Python path: {sys.executable}")  
  
# Test a package from requirements.txt  
  
import numpy as np  
  
print(f"NumPy version: {np.__version__}")
```

 Your path should end in **essentials\_env/bin/python** and your numpy version should be **2.2.6**

### Troubleshooting and Common Errors

**Don't worry - setup issues are completely normal!** Even experienced developers encounter environment problems, and troubleshooting them is actually a valuable skill you're building.

Virtual environments can be tricky because they involve multiple moving parts: your operating system, Python installation, terminal settings, and VSCode configuration all need to work together.

The good news is that most setup issues fall into a few common categories with straightforward fixes. This troubleshooting guide will walk you through the most frequent problems you might encounter, helping you identify what's going wrong and get back on track quickly.

Remember, getting your environment working properly now will save you headaches throughout the course, so it's worth taking the time to fix any issues properly rather than working around them.

* [Common Package Errors](#dpPanel9Content)
* [Fix Missing Packages](#dpPanel12Content)
* [Finding Correct Package Name](#dpPanel17Content)
* [Check Existing Packages](#dpPanel21Content)
* [Common Issues](#dpPanel25Content)

### Common Package Errors

The most common environment issues are the the common package errors.

### ["ModuleNotFoundError"](#dpPanel10)

The most common issue is the "ModuleNotFoundError". You will see this more often when you try to run code and see an error like this:

`import seaborn as sns`

`ModuleNotFoundError: No module named 'seaborn'`

This means the package isn't installed in your current environment.

### ["ImportError"](#dpPanel11)

"ImportError" is a package partially missing. This error often will look like:

`ImportError: cannot import name 'something' from 'package'`

This often means you have an older version of the package that doesn't include the feature you're trying to use.

### Fix Missing Packages

### [Step 1: Confirm Your Environment is Active](#dpPanel13)

Before installing anything, make sure your virtual environment is activated.

Your terminal should show: `(essentials_env) user@computer:~/ds_essentials_course$`

If you don't see (essentials\_env), activate it first. Make sure you are in the correct folder in terminal/git bash:

* **# Git Bash (Windows):** `source essentials_env/Scripts/activate`
* **# Mac/Linux:** `source essentials_env/bin/activate`

### [Step 2: Install the Missing Package](#dpPanel14)

Most packages can be installed using their import name:

* `pip install seaborn`
* `pip install matplotlib`
* `pip install requests`

### [Step 3: Update Your Requirements File](#dpPanel15)

After installing new packages, update your requirements.txt so others can replicate your environment: `pip freeze > requirements.txt`

### [Step 4: Quick Package Upgrades](#dpPanel16)

You can also attempt to upgrade existing packages with a simple and quick pip command: `pip install --upgrade package_name`.

### Finding Correct Package Name

Sometimes the package name for pip installation differs from the import name. Here's how to find the right one:

### [Method 1: Search PyPI (Python Package Index)](#dpPanel18)

1. Go to [pypi.org


   Links to an external site.](https://pypi.org)
2. Search for the package you need
3. The correct pip install command is shown on the package page

### [Method 2: Common Name Differences](#dpPanel19)

Some packages have different pip and import names:

pip install and import names

| Import Name | Pip Install Command | Notes |
| --- | --- | --- |
| import cv2 | pip install opencv-python | Computer vision |
| from PIL import Image | pip install Pillow | Image processing |
| import sklearn | pip install scikit-learn | Machine learning |
| import yaml | pip install PyYAML | YAML file handling |
| import bs4 | pip install beautifulsoup4 | Web scraping |

### [Method 3: Google Search Strategy](#dpPanel20)

Search for: "pip install" + [error message]

For example: "pip install" "No module named 'seaborn'"

This usually leads to Stack Overflow answers with the correct pip command.

### Check Existing Packages

### [List All Packages](#dpPanel22)

In terminal/git bash: `pip list`

### [Search for Specific Package](#dpPanel23)

`pip list | grep numpy    # Mac/Linux/Git Bash`

`pip list | findstr numpy # Windows Command Prompt`

### [Check Package Version](#dpPanel24)

In terminal/git bash use the command:`pip show numpy`

This shows detailed information including version, dependencies, and location.

### Common Issues

### [Scenario 1: Jupyter Notebook Can't Find Package](#dpPanel26)

**Problem**: Package installs fine but Jupyter can't import it.

**Solution**: Make sure Jupyter is using the correct kernel:

1. In your notebook, click the kernel selector (top-right)
2. Choose your essentials\_env environment
3. Restart the kernel: Kernel → Restart

### [Scenario 2: Package Installs But Import Still Fails](#dpPanel27)

**Problem**: pip install succeeds but import still fails.

**Possible causes and solutions**:

1. **Wrong environment**: Check if you're in the right virtual environment
2. **Name mismatch**: The package name for pip might differ from import name
3. **Restart needed**: Restart your Python interpreter or Jupyter kernel
4. **Case sensitivity**: Some systems are case-sensitive (numpy vs Numpy)

### [Scenario 3: "Permission Denied" Error](#dpPanel28)

**ERROR:** Could not install packages due to an EnvironmentError: [Errno 13] Permission denied

**Solutions**:

* Make sure your virtual environment is activated
* On Mac/Linux, don't use sudo with pip in virtual environments
* On Windows, try running git bash as Administrator

### [Scenario 4: Package Conflicts](#dpPanel29)

**ERROR:** pip's dependency resolver does not currently resolve conflicts.

**Solutions**:

* Try installing one package at a time
  + `pip install package1`
  + `pip install package2`
* Or use --force-reinstall (use carefully)`pip install --force-reinstall package_name`

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243466

Scraped At: 2026-05-14T20:44:09.316435
