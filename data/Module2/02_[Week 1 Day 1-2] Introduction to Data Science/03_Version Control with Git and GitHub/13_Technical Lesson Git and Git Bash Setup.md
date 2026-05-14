# Technical Lesson: Git and Git Bash Setup

# Technical Lesson: Git and Git Bash Setup

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Technical Lesson: Git and Git Bash Setup

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 15-20 minutes

Now that you have an understanding of the core concepts and benefits of using Git and GitHub for version control and collaboration, it’s time to set up your development environment by installing Git and Git Bash.

Setting up Git and Git Bash is a crucial step in your development environment. Git enables version control, allowing you to track changes and collaborate effectively, while Git Bash provides a command line interface for interacting with Git on Windows. By the end of this practice, you will be able to install and activate Git and Git Bash on either a Windows or macOS computer. Follow the instructions for your operating system to get started.

### Git and Git Bash Installation Video

The video below will guide you through each step of the installation process. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of installing Git and Git Bash. 

[VIDEO LINK](https://player.vimeo.com/video/989668653?h=09047f488c)

### Installing Git and Git Bash on Windows OS

### [Installation](#dpPanel0)

* [1. **Navigate to Git's Download Page**](#dpPanel1Content)
* [2. **Determine Your System Type**](#dpPanel2Content)
* [3. **Download the Correct Installer**](#dpPanel3Content)
* [4. **Run the Installer**](#dpPanel4Content)
* [5. **Select Installation Options**](#dpPanel5Content)
* [6. **C**omplete Installation](#dpPanel6Content)

#### 1. **Navigate to Git's Download Page**

* Go to [Git for Windows


  Links to an external site.](https://git-scm.com/download/win) and download the installer.

#### 2. **Determine Your System Type**

Check if your system is 32-bit or 64=bit:

* Go to Start > Settings > System > About.
* Under the **Device specifications** header, next to System type, you’ll see if Windows and your processor are 32-bit or 64-bit.

#### 3. **Download the Correct Installer**

* Based on your system type, download the appropriate 32-bit or 64-bit installer from the [Git for Windows


  Links to an external site.](https://gitforwindows.org/) download page.

#### 4. **Run the Installer**

* Open the downloaded `.exe` file.
* If prompted, allow the application to make changes to your device by clicking **Yes**.
* Click **Next** to accept the license agreement.

#### 5. **Select Installation Options**

* **Installation Destination**: Use the default option.
* **Select Components**: Keep the default options. Ensure “Windows Explorer integration” is checked.
* **Start Menu Folder**: Use the default.
* **Default Editor**: Stick with the default (vim) unless you prefer another.
* **Branch Name**: Choose “Override the default branch name for new repositories” and enter “main.”
* **PATH Environment**: Select “Git from the command line and also from 3rd-party software.”
  + Git can be used natively from Git Bash—a terminal program that comes with the Git installation. Your PATH environment selection will also give you the option to use Git in Windows Command Prompt or Windows Powershell.
* **SSH Executable**: Use the bundled OpenSSH.
* **HTTPS Backend**: Select “Use the OpenSSL library.”
* **Line Ending Conversions**: Choose “Checkout Windows-style, commit Unix-style line endings.”
* **Terminal Emulator**: Select MinTTY.
* **Git Pull Behavior**: Keep the default “Fast-forward or merge".
* **Credential Helper**: Select Git Credential Manager.
* **Extra Options**: Ensure "Enable file system caching" is checked.
* **Experimental Options**: Leave all boxes unchecked.

#### 6. **C**omplete Installation

* Click **Install** and wait for the installation to complete.
* Click **Finish** to complete the setup.

### [Confirmation](#dpPanel7)

To confirm you have installed Git successfully:

1. **Open Git Bash**

* Go to Start > Git Bash.
* Locate Git Bash in the menu.
* Right click to pin Git Bash to the Start menu and taskbar to easy access. it should be near the very top.

**Note:** When we ask you to use the terminal, we mean the Git Bash application we just installed through Git.

1. **Verify Installation**

* In Git Bash (the terminal window), type `git --version` and press **Enter**.
* It should return the version of git you are running, something like: git version 2.45.1.windows.1

### Instructions for Installing Git on MacOS

There are two ways to install Git on MacOS:

### [Option 1: Using XCode](#dpPanel8)

* **Install XCode**

Apple ships a version of git with their developer tools package called XCode. Despite the fact that it is a very large download (about 8 gb!), using the App Store download is the easiest way to get it on your machine.

* Download XCode from the [App Store


  Links to an external site.](https://apps.apple.com/us/app/xcode/id497799835?mt=12/).
* Install and run XCode once to ensure additional packages, including Git, have been installed.

### [Option 2: Downloading from Git](#dpPanel9)

1. **Download Git**

* Navigate to [Git's download page for MacOS


  Links to an external site.](https://git-scm.com/download/mac).
* Choose ”installer” under the Binary Installer option and download it.

1. **Run the Installer**

* Open the downloaded `.dmg` file.
* Double-click the `.pkg` file to run it.
* If a security warning appears, navigate to System Preferences > Security & Privacy > General, and click “Open Anyway.”
* Follow the prompts to complete the installation.
* When the installation is complete, click the "Close" button.
* If the installation window asks if you want to move the installer `.pkg` file to trash, you can click “Move to Trash.”

### [Confirmation](#dpPanel10)

1. **Open Terminal**

* Use Command (⌘) + spacebar to search for “Terminal” and open it.
* Pin Terminal to the taskbar for easy access.

1. **Verify Installation**

* In Terminal, type `git --version` and press **Enter**. It should display the installed Git version.

### Next Steps

Now that you have successfully installed Git and Git Bash, you are ready to set up your GitHub account and configure Git for your projects. Proceed to the next section to learn how to create a GitHub account , clone repositories, commit changes, and collaborate with others.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243460

Scraped At: 2026-05-14T20:43:42.086298
