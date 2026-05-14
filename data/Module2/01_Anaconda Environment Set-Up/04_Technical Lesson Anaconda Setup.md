# Technical Lesson: Anaconda Setup

# Technical Lesson: Anaconda Setup

## ![](https://moringa.instructure.com/courses/1406/files/624720/preview) Technical Lesson: Anaconda Setup

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 15-20 minutes

Having discussed the importance of Conda environments and using Conda to manage dependencies and organize your projects, it’s time to set up the next part of your development environment by installing Anaconda. This technical lesson focuses on installing Anaconda, which includes Conda, to ensure you have all the necessary tools for your data science tasks.

By the end of this practice, you will be able to install and verify your Anaconda installation on either a Windows or macOS computer.

### Instructions for Installing Anaconda on Windows

Read through the steps before beginning this installation.

* Items “in quotes” refer to the name of particular dialogue boxes and popups.
* > is used to indicate menu choices. For example, Start > Settings > System > About is the same as saying “Click on the Start menu. In the Start menu, scroll to and click on the Settings sub-menu. Click on System. Scroll to and click on About.”

Watch the videos below for a walkthrough on installing Anaconda on Windows.

#### Part 1

[VIDEO LINK](https://player.vimeo.com/video/960768994?h=a08486f062)

#### Part 2

[VIDEO LINK](https://player.vimeo.com/video/960768490?h=bd33b87e31)

#### Part 3

[VIDEO LINK](https://player.vimeo.com/video/960771981?h=e964cf2352)

#### Part 4

[VIDEO LINK](https://player.vimeo.com/video/960767965?h=edf404800c)

Follow these instructions carefully to install Anaconda on your Windows machine.

### Installation

1. **Navigate to Anaconda’s Download Page**

* Go to [Anaconda’s download page


  Links to an external site.](https://www.anaconda.com/products/individual) and download the installer for Windows.

1. **Determine Your System Type**

* Check if your system is 32-bit or 64-bit.
* On Windows 10/11, head to Start > Settings > System > About.
* Under the “Device specifications” header, next to System type, you’ll see if Windows and your processor are 32-bit or 64-bit.

1. **Download the Correct Installer**

* Based on your system type, download the appropriate installer from Anaconda’s download page.

1. **Run the Installer**

* Open the downloaded .exe file.
* If prompted, allow the application to make changes to your device by clicking “Yes.”
* Click “I Agree” to accept the license agreement.

1. **Installation Options**

* Install for “Just Me” which will only install the Anaconda distribution for the current user account.
* In the Advanced Options, check both options to “Add Anaconda to my PATH environment variable” and “Register Anaconda3 as my default Python 3.x.”
* **Add Anaconda3 to my PATH environment variables**: This option might not be checked by default. Check it to ensure that Anaconda can be used from Anaconda Prompt, Windows Command Prompt, or Windows Powershell.
* **Register Anaconda3 as my default Python 3.x**: This makes sure that the Python installation of Anaconda is used as the default one.

1. **Complete Installation**

* Click “Install” and wait while Anaconda is installed onto your computer.
* Skip installing any add-ons by clicking “Next.”
* Select “Finish” to complete the setup.
* If prompted, update Anaconda. This will close Navigator and start the update process.

### Confirmation

To confirm you have installed Git successfully:

1. **Open Git Bash**

* Start > Git Bash (This is the application you installed in the previous lesson).

1. **Verify Installation**

* In the Git Bash window, type: `conda info`
* It should return a table of details about your conda installation

### Instructions for Installing Anaconda on MacOS

Follow these instructions carefully to install Anaconda on your macOS machine.

### Installation

1. **Navigate to Anaconda’s Download Page**

* Go to [Anaconda’s download page


  Links to an external site.](https://www.anaconda.com/products/individual) and download the installer for macOS.
* If your Mac has an M1 chip, download the Apple Silicon Graphical Installer; otherwise, download the 64-bit macOS Graphical Installer.

1. **Run the Installer**

* Once the installer is downloaded, double-click the .pkg file to run it.
* Click “Continue” when the pop-up security warning asks if you are sure you want to open it.

1. **Handling Security Warnings**

* If you get a security warning that says the file cannot be opened because it is from an unidentified developer:
  + Click on the Apple symbol at the top left of your screen.
  + Select “System Preferences” from the drop-down menu.
  + Select “Security and Privacy.”
  + Select the “General” tab.
  + Click the “Open Anyway” option under “Allow apps downloaded from.” You may need to click the lock to make changes, which will prompt you to enter your password.

1. **Complete Installation**

* When the Installer opens, click “Continue” on each screen, then “Install.” You may need to enter your password when prompted.
* Skip installing any add-ons by clicking “Next.”
* If the installation window asks if you want to move the installer .pkg file to trash, you can click “Move to Trash.”

### Confirmation

1. **Open Terminal**

* Open the “Terminal” app in the “Utilities” folder within your “Applications” folder. Alternatively, use Command (⌘) + spacebar to bring up a search bar, enter “Terminal” in the search bar, and open it.

1. **Verify Installation**

* In the Terminal window, type: `conda info` and click <Enter>.
* It should return a table of details about your Conda installation.

### Next Steps

With Anaconda installed and verified, you are now ready to set up and manage your development environments using Conda. This setup will allow you to efficiently handle various data science projects, ensuring that your work is well-organized and reproducible. In the next section, we will guide you through installing and using Jupyter Notebooks, a powerful tool included with Anaconda for interactive data analysis and visualization.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243442

Scraped At: 2026-05-14T20:42:29.067661
