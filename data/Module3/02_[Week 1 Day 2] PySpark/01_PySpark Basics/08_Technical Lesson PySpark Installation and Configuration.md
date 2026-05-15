# Technical Lesson: PySpark Installation and Configuration

# Technical Lesson: PySpark Installation and Configuration

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: PySpark Installation and Configuration

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

PySpark is a powerful tool for processing large datasets, but setting it up can be a challenge, especially in environments with many dependencies and configurations. In a large-scale enterprise, PySpark is typically run on distributed cloud systems or dedicated hardware clusters. However, you can also run it on your local computer as a standalone setup to get familiar with its features and functionality.

In this lesson, we’ll guide you through **installing PySpark locally and demonstrate the utility of Docker in handling package management**. Docker simplifies the setup by packaging all dependencies, allowing you to work in a controlled environment that mirrors larger-scale setups.

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of PySpark installation and configuration.

[VIDEO LINK](https://player.vimeo.com/video/1038328799?h=167a485bd8)

### What is Docker?

**Docker is a container technology that simplifies software packaging and distribution**, eliminating the challenges of environment setup, logging configuration, and other system settings. In essence, Docker removes the common issue of "It doesn't work on my machine."

**A Docker image operates within a container, functioning as a self-contained system that runs consistently across different platforms**—whether on a Windows desktop, a Mac laptop, or an AWS cloud server. This ensures that dependencies and environments are identical, regardless of the underlying operating system.

Similar to a .yml file for creating a conda environment, **Docker containers rely on a configuration file called a Dockerfile**. This file specifies the container’s requirements, including the operating system, shell, permissions, environment variables, and software dependencies. For our PySpark setup, we’ll use a Dockerfile for a pre-configured image maintained by Jupyter called pyspark-notebook.

To create and run this container, you’ll first need to install Docker on your machine. This will enable you to start working with PySpark in a controlled, isolated environment.

#### Key Steps and Challenges

1. **Installing PySpark Locally:** PySpark can be installed directly on your machine using pip install pyspark, which installs PySpark and its dependencies. However, configuring PySpark manually on a local machine can be challenging due to compatibility issues with Java and other dependencies. This is where Docker can make the setup more manageable.
2. **Understanding Docker for Package Management:** Docker allows you to create isolated environments, or containers, that package all necessary software and dependencies. By using a Docker image pre-configured with Spark, you can avoid many compatibility issues that might arise from direct installation. For a beginner, Docker simplifies the installation by bundling everything required to run PySpark, removing the need for manual configuration.
3. **Setting Up PySpark with Docker:** With Docker installed on your machine, you can run a container with Spark by pulling an image that has PySpark configured. This approach emulates a standalone cluster environment on your local computer, making it an excellent option for testing PySpark commands and running small datasets.

### Resources

* [Get Docker


  Links to an external site.](https://docs.docker.com/get-docker/)
* [DockerHub


  Links to an external site.](https://hub.docker.com/r/jupyter/pyspark-notebook)

### Instructions

#### Step 1. Install Docker

Go to the Get Docker page, click on your operating system, and follow the instructions. Note that there is a graphical user interface called "Docker Desktop" available for Mac and Windows users, whereas at the time of this writing there is not an equivalent tool for Linux users. Linux users can install the "server" version. You may be asked to create a Docker account.

#### Step 2. Pull the PySpark Stack from DockerHub

If you were developing your own Dockerfiles, you could just work locally, similarly to how you could write Python code locally without connecting to any remote repositories. But we want to run an image created by someone else, so we want to use the `docker pull` command from DockerHub. This is roughly equivalent to running `git pull` from GitHub, except you're downloading a pre-built computer image.

Specifically, **run this command in the terminal:**

```
docker pull jupyter/pyspark-notebook
```

This will initiate a download that will likely take a while, then finally you should see a message like this:

```
Status: Downloaded newer image for jupyter/pyspark-notebook:latest
```

You have now pulled down the PySpark stack.

#### Step 3. Run Jupyter Notebook with Docker

Now that you have pulled down pyspark-notebook, run this command in the terminal:

```
docker run -p 8888:8888 jupyter/pyspark-notebook
```

* The -p flag is setting the ports on your computer as well as the container to be connected.

This will launch a notebook server that should look fairly similar to when you run a regular jupyter notebook command.

However you will most likely need to copy the URL displayed in the terminal and paste it into a browser window, rather than having it automatically open like jupyter notebook usually does.

**The URL will look something like this:** http://127.0.0.1:8888/lab?token=<token>

Then, once you paste it into the browser address bar, you'll be redirected to just http://127.0.0.1:8888/lab, which is a Jupyter Lab interface:

![Jupyter Lab interface](https://moringa.instructure.com/courses/1426/files/631424/download)

If you want to navigate back to the classic jupyter notebook file window, simply enter http://127.0.0.1:8888/tree in the address bar (replacing lab with tree).

#### Step 4. Check for Successful PySpark Image Installation

From here, you can create a new notebook and run these lines of code, which should not produce an error:

```
import pyspark  
sc = pyspark.SparkContext('local[*]')  
rdd = sc.parallelize(range(1000))  
rdd.takeSample(False, 5)
```

#### Step 5. Connect Docker Container to Your File System

You might have noticed something strange when you were creating that notebook: there was only a directory called work, nothing related to the directory on your computer where you launched docker run.

This is because even though the notebook server looked very similar to one being run directly on your computer, this one only had access to the container's file system.

If you want to be able to use notebooks from the curriculum or files on disk (e.g. CSV files), it's useful to be able to connect your computer's file system to the container.

#### Step 6. Shut Down Previous Docker Container

Shut down the currently-running container by typing control-C in the terminal window where it is currently running.

If you accidentally closed that terminal window, you can:

1. Use a command-line approach:  
   * Run `docker ps` to see a list of all currently-running docker containers.
   * Run `docker stop <container id>` where <container id> is from the docker ps print-out. For example, `docker stop efb990e0e054`.
2. Or, use Docker Desktop:  
   * Open Docker Desktop and locate the currently-running container in the "Containers / Apps" list.
   * Click the square stop button.

#### Step 7. Start Docker Again, Connected to Your File System

The formal language of this is called "mounting a volume", so it uses the -v command-line option. The general structure looks like this:

docker run -p 8888:8888 -v {absolute file path of current directory}:/home/jovyan/work jupyter/pyspark-notebook

We are mapping {absolute file path of current directory} on your computer onto /home/jovyan/work in the container.

* Fun fact: the username jovyan is a [play on the name Jupyter


  Links to an external site.](https://docs.jupyter.org/en/latest/community/content-community.html#what-is-a-jovyan). Jovyan is to [Jovian


  Links to an external site.](https://en.wiktionary.org/wiki/Jovian) as Jupyter is to Jupiter.

For **Mac or Linux**, the actual command looks like this:

```
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/pyspark-notebook
```

For **Windows**, the actual command looks like this (executed in Command Prompt, not Git Bash):

```
docker run -p 8888:8888 -v %cd%:/home/jovyan/work jupyter/pyspark-notebook
```

Now you should be able to navigate to the work directory and find this notebook there.

#### Step 8. A Few More Command Line Options

1. This starts the container in "interactive mode" and allows you to access the Bash shell inside the container:

   ```
   -it
   ```
2. This removes the container from your list of images as soon as you shut it down. Since you are storing your data on your computer's file system, this is a good option to avoid creating a lot of extra unnecessary files.

   ```
   --rm
   ```

Therefore we recommend that you run this complete command:

* **On Mac/Linux**:

```
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work -it --rm jupyter/pyspark-notebook
```

* **On Windows:**

```
docker run -p 8888:8888 -v %cd%:/home/jovyan/work -it --rm jupyter/pyspark-notebook
```

### Challenges and Solutions for Installing and Configuring PySpark with Docker

**Note:** Some of the challenges have what can be better phrases suggestions since the challenges are open-ended, rather than solutions.

1. **Installing Docker**  
   * **Challenge:** Mac and Windows users can install Docker Desktop, which provides a graphical interface, but Linux users need to install the command-line version, which may feel less intuitive.
   * **Solution:** Linux users can follow Docker's official installation guide for Linux to set up Docker from the command line. Additionally, using Docker’s command-line documentation can help troubleshoot issues specific to Linux environments.
2. **Pulling the PySpark Image from DockerHub**  
   * **Challenge:** Docker images can be large, so downloading the PySpark image from DockerHub may take a significant amount of time, especially with limited bandwidth.
   * **Solution:** Check internet connection stability and avoid network-intensive tasks during the download. Alternatively, you could use a minimized Docker image if PySpark features allow.
3. **Decision Point:** Using a pre-built image from DockerHub saves time and configuration efforts but requires a substantial initial download.  
   * **Pros:** Reduces complexity by using a pre-configured environment, which is ideal for beginners.
   * **Cons:** Time-consuming download and disk space requirements for the full PySpark stack.
4. **Running Jupyter Notebook with Docker**  
   * **Challenge:** After starting the container, Jupyter Notebook does not open automatically. Instead, users must manually paste the generated URL from the terminal into a browser.
   * **Solution:** Clearly explain this requirement during setup, so users know to look for the URL and understand where to paste it.
5. **Checking PySpark Functionality**  
   * **Challenge:** Verifying PySpark installation involves running a few lines of PySpark code in Jupyter Notebook. However, if the environment setup isn’t correct, users may encounter errors at this step.
   * **Solution:** If errors arise, guide users to check that the SparkContext starts without issues, and ensure Docker resources (like memory) are appropriately allocated. Clear instructions on how to troubleshoot common Spark errors are beneficial.
6. **Connecting Docker Container to Local File System (Mounting a Volume)**  
   * **Challenge:** By default, Docker containers do not access local files. Learners may need to use files on their computers for analysis, which requires mounting a volume to link local directories with the container.
   * **Solution:** Provide detailed, OS-specific commands to simplify the mounting process. Explain the significance of mounting and how it enables access to local data within the container.
7. **Decision Point:** Mounting volumes allows data sharing between the container and the local system, which is practical but adds complexity to setup.  
   * **Pros:** Facilitates data access, allowing learners to use local datasets in their notebooks.
   * **Cons:** Slightly more complex setup, especially for those unfamiliar with volume mounting.
8. **Shutting Down the Container**  
   * **Challenge:** Docker containers can continue running in the background even after closing the terminal, which may confuse users.
   * **Solution:** Explain how to use commands like docker ps to view running containers and docker stop <container\_id> to stop them. For Docker Desktop users, show how to manage containers through the graphical interface.
9. **Starting Docker Again with Additional Options**  
   * **Challenge:** For an efficient workflow, it’s often beneficial to run Docker in interactive mode and remove the container automatically after use. These additional options can be overwhelming for beginners.
   * **Solution:** Offer clear guidance on command structure, emphasizing practical options such as -it (interactive mode) and --rm (automatic removal). Encourage learners to include these options as part of their standard setup.
10. **Decision Point:** Adding options like -it and --rm improves workflow efficiency but requires a solid understanding of Docker commands.  
    * **Pros:** Allows users to interact directly with the container and manage storage effectively.
    * **Cons:** Can complicate the initial learning curve, especially for those new to command-line tools.

By addressing these challenges with targeted solutions and clear pros and cons, learners can navigate the PySpark and Docker setup process more confidently, ensuring a stable and efficient environment for running PySpark applications.

---

# Attachments

- Get DockerLinks to an external site.: https://docs.docker.com/get-docker/
- DockerHubLinks to an external site.: https://hub.docker.com/r/jupyter/pyspark-notebook


---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248241

Scraped At: 2026-05-15T09:51:43.561050
