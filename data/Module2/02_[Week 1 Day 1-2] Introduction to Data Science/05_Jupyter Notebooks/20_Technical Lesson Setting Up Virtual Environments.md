# Technical Lesson: Setting Up Virtual Environments

# Technical Lesson: Setting Up Virtual Environments

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Technical Lesson: Setting Up Virtual Environments

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[15-20 minutes]

In this section, you will complete the configuration process by setting up virtual environments. This will involve creating a folder on your local file system to store all your project files and repositories, cloning a repository, and setting up both Git and Conda virtual environments. This setup is crucial for managing dependencies and ensuring a consistent development environment.

To complete the last few steps in the configuration process, you will download some files contained within a remote repository hosted by Flatiron School. You will begin by creating a folder on your local file system to store your repositories and files, where you will then clone the repository into the new folder. Let’s do it!

### Introduction to Setting Up Virtual Environments

Virtual environments are essential tools for data scientists and programmers, allowing you to isolate project dependencies, manage specific versions of packages, and ensure reproducibility. By the end of this lesson, you will have a fully configured environment ready for your data science projects.

#### Setting Up Your Git Virtual Environment

### [Step 1: Preparing Your Local File System](#dpPanel0)

1. **Open** a new terminal window. You will be completing this entire lesson from the terminal window.
2. **Navigate** to your home directory by typing `pwd`. This should show your home directory, the most basic path on your computer.
3. **Change** to your Documents folder by typing `cd Documents`.
4. **Create** a new folder for your repositories and files by typing `mkdir Flatiron`.
5. **Move** into the new Flatiron folder by typing `cd Flatiron`.

### [Step 2: Cloning the Repository](#dpPanel1)

1. **Ensure** you are not inside a Git repository by typing `git status`. If you see "fatal: not a git repository (or any of the parent directories): .git", you are good to proceed.
2. **Clone** the repository by typing `git clone git@github.com:learn-co-curriculum/dsc-config-learn-env.git`. This will create a new subdirectory named  "dsc-config-learn-env" containing a copy of all of the files in this repository.
3. **Move** into the cloned directory by typing `cd dsc-config-learn-env`.

### [Step 3: Confirming the Setup](#dpPanel2)

1. **Verify** your current directoryby typing `pwd`.  You should be inside the “dsc-config-learn-env” folder.

#### Setting Up Your Conda Virtual Environment

### [Step 1: Creating the Conda Virtual Environment](#dpPanel3)

1. **Ensure** you are in the correct directory by typing `pwd`. Make sure the name of the current working directory is “dsc-config-learn-env”.
2. **List**the files in the directory by typing `ls`. You should see a few `.yml` files, which are text files that specify how your virtual environment should be built and what packages should be included.
3. **Create** your virtual environment using the appropriate `.yml` file for your OS:

* MacOS: intel type `conda env create -f mac_intel.c0c1.yml` or `conda env create -f mac_m.c0c1.yml`
* Windows: type `conda env create -f win_c0c1.yml`

### [Step 2: Activating the Conda Virtual Environment](#dpPanel4)

1. **Initialize** a permanent shell by typing `conda init bash`.
2. **Activate** the environment by typing `conda activate learn-env`.
3. **Confirm** activation by typing `conda info --envs`. You should see an asterisk (\*) next to the `learn-env` environment.

* Troubleshooting:

* If you see “WARNING: A newer version of Conda exists”, run `conda update -n base conda`. Then, try creating the environment again.
* If you see “file not found”, ensure you are in the correct directory that contains the `.yml` file by running `ls`. If you do not see the `.yml` file, move into the right directory by typing `cd dsc-config-learn-env`.

### [Step 3: Setting Your Default Environment](#dpPanel5)

It’s helpful to set your terminal to activate the environment by default to avoid manually switching each time you open the terminal.

#### Setting Up Your Jupyter Virtual Environment

### [Step 1: Configuring Your Kernel](#dpPanel6)

1. **Ensure** your learn-env is activated by typing `conda activate learn-env`.
2. **Install** the Jupyter kernel by typing:

   ```
   conda install -y ipykernel  
   python -m ipykernel install --user --name learn-env --display-name "Python (learn-env)"
   ```

### [Step 2: Running Jupyter Notebook](#dpPanel7)

1. **Start**Jupyter notebook by typing `jupyter notebook`. This should open a new browser window at an address like “localhost:8888”.
2. **Select** the learn-env kernel:

* Create a new notebook or open an existing one.
* Navigate to "Kernel>Change kernel" in the top menu bar and select "Python (learn-env)".

#### Summary

It is essential to run `conda activate learn-env` every time you start a new terminal window if you do not set your terminal to activate that environment by default. You can always run `conda info --envs` to check which environment is active.

Congratulations! You have successfully set up your computer with some of the primary tools you need to work as a professional data scientist. This setup will allow you to manage dependencies, ensure reproducibility, and organize your projects efficiently.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243470

Scraped At: 2026-05-14T20:44:28.105151
