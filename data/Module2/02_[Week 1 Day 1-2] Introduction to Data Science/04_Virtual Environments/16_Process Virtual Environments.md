# Process: Virtual Environments

# Process: Virtual Environments

## // Process: Virtual Environments

Icon Progress Bar (browser only)

1 min read

Before diving into data science tasks, it’s essential to have a well-organized development environment. The toolkit introduced above helps you create isolated environments for different projects, manage packages and dependencies, and ensure reproducibility. This process will guide you through creating and managing virtual environments environments, installing necessary packages, and maintaining your setup, making it easier to handle various data science projects seamlessly.

The following process aligns well with the CRISP-DM framework, supporting all phases from data understanding to deployment by ensuring tools and dependencies are consistently managed and reproducible.

Review the process below before moving on to the actual environment installation steps in the technical lesson.

### [1. Install Python](#dpPanel0)

Start by installing Python, which for you should already be done. This step ensures you have the necessary venv and pip toolkit, both of which come pre-built into newer Python versions.

### [2. Create New Environment](#dpPanel1)

For each new project, create an isolated environment using venv commands to keep your work organized and avoid conflicts between different packages and project requirements. Activate the environment to start working within it.

### [3. Install Necessary Packages](#dpPanel2)

Install the required packages for your project using pip terminal commands. This simplifies package installations. There are two general ways to install packages, either directly by name or by utilizing an existing requirements.txt file.

### [4. Develop Your Project/Analysis](#dpPanel3)

Use your preferred IDE, like VSCode, to work in a Jupyter Notebook or Python file on your data science project.

### [5. Update and Manage Packages](#dpPanel4)

Update and add any additional packages you might need during your project. You can always add in packages as you determine you need them via pip commands.

### [6. Save and Share Environment](#dpPanel5)

Export the final environment to a **requirements.txt** file to capture the exact configuration. This is useful for sharing and reproducing the environment. Share the environment file with collaborators to ensure they can replicate your environment. Include it in your project repository.

Following this structured process ensures that you:

* Have isolated environments for different projects, avoiding conflicts.
* Manage dependencies efficiently, reducing the chances of compatibility issues.
* Can easily share and reproduce your environment, ensuring consistency in collaborative projects.
* Keep your development system organized and maintainable.

### Best Practices for Virtual Environments

#### Virtual Environments

Always use virtual environments. Even for simple scripts, it's good practice to work in isolated environments.

#### Root Level Projects

Open project at root level. Always open VSCode at your project's root directory where your virtual environment folder is located.

#### Verify Before Coding

Always check to confirm you're using the right environment before starting work.

#### Consistent Naming

Use descriptive names for your virtual environments that match your project names.

#### Environment Folder

Don't commit the environment folder. Add your venv folder to .gitignore. Only commit the requirements.txt file, not the entire environment.

#### Pin Your Versions

Use exact package version numbers (==) in requirements file for maximum reproducibility.

#### Extensions

Install the official VSCode Python extension from Microsoft, which provides the best integration with virtual environments.

#### Updated Requirements File

Keep requirements file updated.  Whenever you install new packages, update your requirements file with pip freeze > requirements.txt.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243465

Scraped At: 2026-05-14T20:44:00.835238
