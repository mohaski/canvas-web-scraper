# Lab: Getting Started with CodeGrade with Jupyter Notebooks

## ![](https://moringa.instructure.com/courses/1406/files/624680/preview) Lab: Getting Started with CodeGrade with Jupyter Notebooks

In this technical lesson, you'll learn the complete workflow for accessing provided lab files, completing labs in Jupyter notebooks, and submitting your work to CodeGrade.

This lesson will walk you through the general process via an example notebook and CodeGrade submission so that you can become familiar with accessing and submitting your lab assignments.

By the end of this lab, you will be able to:

1. Access the provided lab files
2. Work through a simple example problem in a Jupyter notebook using VSCode
3. Submit your completed work to CodeGrade
4. View results of the auto-tests

* [What is CodeGrade?](#dpPanel0Content)
* [CodeGrade Submission Process](#dpPanel1Content)
* [CodeGrade Grading](#dpPanel2Content)

### What is CodeGrade?

CodeGrade is an educational platform designed specifically for computer science courses. It allows you to submit your code assignments in a secure environment and receive/inspect auto-graded assignments through automated testing. CodeGrade has built-in integration with your Canvas course and your submission link will be accessed from within each respective Canvas assignment.

### CodeGrade Submission Process

For every auto-graded lab assignment that has a CodeGrade submission you will follow this general process:

1. Access provided/starter files

* Via Google Drive link
* Via Github link

2. Open files in VSCode

* Explorer window folders

3. Write necessary code

* Select Jupyter kernel
* Replace None's with code answers

4. Final submission checks

* Restart and run all cells
* Check that all answer cells have ‘CodeGrade step#’ tag and code
* Save, save, save

5. Submit completed notebook to CodeGrade

* Access CodeGrade link in Canvas
* Upload notebook file using GUI window
* View autotest and submission

### CodeGrade Grading

Codegrade is an auto-graded  coding tool and is looking for very specific outputs and labeling. An instructor will be reviewing your code in addition to the Codegrade auto-test. Use the rubric in Canvas to guide your ability to meet the objectives of the lab.

**NOTE**

Your facilitator will be reviewing your assignment and giving you feedback, in addition to the CodeGrade auto-test.

### Tools and Resources

* [Getting Started with CodeGrade Technical Lesson Notebook


  Links to an external site.](https://drive.google.com/file/d/1trSI2LuhIr4-3asHadhC0AHR41C-7RBs/view "Link")
* [VSCode walkthrough video on using Jupyter Notebooks


  Links to an external site.](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) - a good general resource page, with shortcut commands.

### Instructions

* [Task 1: Access Starter Files](#dpPanel3Content)
* [Task 2: Opening Files in VSCode](#dpPanel6Content)
* [Task 3: Develop Your Jupyter Notebook](#dpPanel9Content)
* [Task 4: Submit Completed Notebook to CodeGrade](#dpPanel13Content)
* [Task 5: Viewing the Auto-test Results](#dpPanel14Content)

### Task 1: Access Starter Files

In this task you will be learning the steps on how to download the provided notebook file for this technical lesson. You will submit this file to CodeGrade.

In order to complete lab assignments and submit the appropriate files to CodeGrade you will need to access any provided files.

These files are provided in one of two ways, either via a github repository link or via google drive links.

Each CodeGrade lab assignment will at minimum have a starter Jupyter Notebook file (.ipynb). Assignments may also have secondary files such as data that are needed for completion.

**NOTE**

All files will need to be downloaded/accessed but only your completed notebook needs to be submitted at the end.

### [Accessing via **GitHub Link**](#dpPanel4)

To access the provided files via github link:

1. Click into the github repository link.
2. Fork the lab to your personal github account
3. Clone the forked lab to local folder using terminal/gitbash  
   1. Recommended to create a “Flatiron” folder in your existing “Documents” folder to store git repositories from the bootcamp.
4. Open local folder in VSCode

### [Accessing via **Google Drive Link**](#dpPanel5)

To access the provided files via Google Drive link:

1. Click into each respective file link
   1. There may just be one
2. Use the Google Drive interface to download the files locally
   1. By default files will be placed into your downloads folder
   2. DO NOT use google collab to try and edit the provided file
3. Open downloads folder in VSCode

### Task 2: Opening Files in VSCode

In this task you will learn how to connect to your Downloads folder in VSCode and open the downloaded notebook for this technical lesson.

While VSCode has native support for both python files (.py) and jupyter notebook files (.ipynb), we want to extend this functionality by installing two VSCode extensions: Python and Jupyter.

These can be easily installed if not already done so via the Extensions panel in VSCode. You can search for both extensions respectively.

### [Step 1: Connect to Folder with VSCode](#dpPanel7)

We can utilize the Explorer panel within VSCode to connect to a specific folder (where our newly acquired files live) so that they can then be accessed and edited with VSCode itself:

1. Open the VSCode Explorer panel via the left hand toolbar  
   * Click into the “Open Folder” interface
2. If your VSCode is defaulting to an open folder location other then the one you need, you will need to remove it from the workspace by right clicking and selecting the appropriate option “remove from workspace”
3. Navigate to the folder of choice (Downloads or local repo) and select “add”  
   * This will add the selected folder to your current “workspace”
   * Files within the folder should now populate on the Explorer workspace panel
4. Click individual files to open in a new VSCode tab
   * You can have multiple files/tabs open at once
   * For Github repo assignments the notebook will be named “index.ipynb”

### [Step 2: Using File Actions in VSCode](#dpPanel8)

You will be connecting to your Downloads folder in VSCode and open the downloaded notebook for this technical lesson.

The Explorer panel can be utilized to perform a variety of file actions including creating new files and folders, renaming existing files, and opening additional folders.

**The workspace/folder window:**

* Create new file or folder
  + Python file (.py)
  + Jupyter Notebook file (.ipynb)
  + Plain Text file (.txt)

+ File type is determined by the extension you give it (common examples)

* Add/connect to another folder

+ Will open additional folders without removing connection to others

* Remove connection to Explorer panel

+ Will depopulate the folder from view

**Individual files/subfolders in the workspace window:**

* Copy file
* Rename file
* Delete file
* Open with other applications

### Task 3: Develop Your Jupyter Notebook

When working with Jupyter notebooks in VSCode for lab assignments there are several key considerations to take into account in order to set yourself up for success. 

### [Step 1: Select Kernel](#dpPanel10)

The first thing you need to do within each notebook is select the appropriate coding environment/jupyter kernel so that your code can actually run via the python interpreter.

To select your environment kernel:

1. Click into the "Select Kernel" button on the top right side of the notebook toolbar
2. Select "Python Environments" or "Jupyter Kernel..."

* It may prompt you with the last used environment
* If this is the correct environment you can immediately click it to activate

3. From the list of environments (you should not have many) select the bootcamp environment you installed previously with anaconda

* This will populate the kernel button with your selected environment
* You are now ready to begin coding and running cells

*​*

**Key Considerations**

Due to the nature of how CodeGrade auto-tests work, specific variable assignments within specific cells in the notebook need to be met so that your answers can be appropriately checked.

This is why we have provided starter notebook files that you will need to utilize.

### [Step 2: Answering Code Questions](#dpPanel11)

Instructional text here: assign the string “example” to the provided variable.

```
# CodeGrade step1  
example_anwser_variable = None
```

**The CodeGrade step# comment tag:** These comments CANNOT be changed or moved in any way or it will prevent the specific CG auto-tests for the question from running correctly.

* Step0 is for assignment setup and will never require you to enter any code
* All other step numbers indict a cell that requires a code answer from you

**Replace None with your code:** You are expected to replace None with any necessary code whenever it appears in the provided notebook.

Provided variable names CANNOT be changed or renamed doing so will prevent the CG autotests from running correctly.

* Some cells will have more then one variable answer that needs assignment
* You are allowed to create additional intermediary variables if needed to help answer the question and arrive at your working code
* If these variables are utilized in python to arrive at an answer they must also be in the tagged cell for CodeGrade to recognize them
* DO NOT include any print statements in CodeGrade tagged cells unless very explicitly instructed to, doing so will prevent the CG auto-tests from running correctly

**Thoroughly read instructions and cell comments:** Each assignment will consist of a series of steps broken out by the rubric. Each step will require you to provide code answers in the appropriately tagged/commented cells. Assignments will also contain already written code that you are expected to run without changes to help display your code and catch potential errors.

You may add additional cells into your notebook if needed for code trial and exploration, note however, that these additional cells will not be captured or run by CG at all. Variables assigned in these additional cells likewise will also not be captured by CG during the specific auto-tests.

Specific instructions will be provided for each question and should be followed exactly, including parameter setting, and naming conventions. Pay attention to variable types and data structures for your answers.

* If a question is asking for a list your answer variable should be a list
* If a question is asking you to set a specific parameter value like random\_state=42
* If a question is asking for specific naming use copy and paste to avoid spelling errors

**NOTE**

If a tagged code cell is returning an error (does not run), it will automatically fail the associated CG auto-test.

### [Step 3: Final Submission Checks](#dpPanel12)

Once you have completed the lab assignment and you think you have the appropriate code/answers, there are a few final things you can do prior to submitting to ensure you have viable code and have provided answers for the necessary questions.

Before submitting your notebook to CodeGrade you should:

1. Use the "Restart" followed by the "Run All" command buttons on the notebook toolbar  
   * This will run the full notebook (all code cells) in the appropriate sequentially order
   * Will stop/error out on code cells that do not run
   * Ensures that your code runs properly before submitting
2. Walkthrough your notebook to ensure CodeGrade tags and code exists  
   * Make sure you did not remove any necessary CodeGrade comment tags
   * Make sure that you replaced all of the None's with your code answer
3. Save your completed notebook  
   * You can either save normally (overriding the existing file)
   * Or use 'Save as' to save your completed notebook separately  
     + File naming DOES NOT matter for notebooks being submitted to CodeGrade
     + Make sure to submit the completed notebook version
     + Would recommend saving it another folder outside of your Downloads in this case

### Task 4: Submit Completed Notebook to CodeGrade

Now that you are ready to submit your completed notebook, you need to access the specific CodeGrade submission link and page.

This will always be located in the respective Canvas assignment page. From there you will upload your completed and saved notebook file utilizing the CodeGrade file uploader UI. Once uploaded CodeGrade will begin running the autotest against your notebook and answers.

**NOTE**

Remember that only your completed notebook should be submitted. Any other files that are needed to run your code such as data are provided on the backend for CodeGrade to use.

For the following steps outlines the following path: Create submission → Open (file window) → Submit (CodeGrade window)

1. Upload your notebook to CodeGrade,
   1. Select create a new submission- this will prompt you to select ways to attach/upload your notebook file
2. Upload/open the file from your local computer via the file interface
3. Make sure you click through the GUI until you get back to the actual CodeGrade assignment page and can click ‘Submit’
4. Once uploaded and submitted you should be taken directly to the autotest page
5. You can also check the notebook code itself to ensure you provided the correct file via the “Code” tab

### Task 5: Viewing the Auto-test Results

1. By default once you have submitted you will be taken directly to the auto-test tab
2. You can re-access the CodeGrade assignment and your submission in the Canvas assignment page
3. The labs in your courses will primarily use input/output tests to auto-grade your code against expected outputs  
   1. Individual tests for each step can be expanded to understand what the test is checking for
   2. **Input:** The code check or test that CodeGrade is running against your code
   3. **Expected Output:** The output of the test (input) if your answer is correct
   4. **Actual Output:** The output of the test based on your provided answer
4. You can always resubmit your assignment
5. You can leave a comment on the assignment within the Canvas gradebook or in CodeGrade for your instructor.

**NOTE**

Your facilitator will be reviewing your assignment and giving you feedback, in addition to the CodeGrade Auto-test.

If you think your CodeGrade score has an error, please reach out to your facilitator.

### Submission and Grading Criteria

* You will be submitting your completed `.ipynb` file.
* Your submission will be automatically scored in CodeGrade.
* Click +Create Submission to upload your `.ipynb` file to the CodeGrade submission portal.
* You can review your submission in CodeGrade and see your final score in your Canvas gradebook.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243482

Scraped At: 2026-05-14T20:45:26.154922
