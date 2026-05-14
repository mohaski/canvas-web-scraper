# Technical Lesson: Configuring Git and GitHub

# Technical Lesson: Configuring Git and GitHub

## ![](https://moringa.instructure.com/courses/1406/files/624674/preview) Technical Lesson: Configuring Git and GitHub

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:**[15-20 minutes]

Now that you have Git installed locally, it’s time to configure Git and integrate it with GitHub. This setup will allow you to manage your local repositories and collaborate effectively. Follow the steps below to set up your Git configuration and link it to your GitHub account.

### Instructions for Configuring Git and GitHub

### Step 1: Set up your Name and Email Address

1. **Set up Your Name**

* In your terminal window, type `git config --global user.name`
* If it returns your name, you’re set! If not, type `git config --global user.name “Your Name”`.
* Replace "Your Name" with your real first and last name, not your GitHub username.

1. **Set Up Your Email**

* In your terminal window, type

  ```
  git config --global user.email
  ```
* If it returns your email address, you’re set! If not, type

  ```
  git config --global user.email your@email.com
  ```
* Replace "your@email.com" with your actual email address.

**Note:** These settings are important because they will be attached to any contributions you make to a project via Git and GitHub.

### Step 2: Signing up for a Github account

1. **Sign Up on GitHub**

* Go to the [GitHub main page


  Links to an external site.](https://github.com/) and click on the “Sign up” button.
* Follow the instructions to set up your account:

* Enter your email address.
* Create a password.
* Enter your new GitHub username.
* Complete the verification process.

1. **Complete Account Setup**

* After completing the security checks, enter the launch code sent to your email.
* Log in to GitHub with your new username and password.
* Skip the personalization steps for now.

### Step 3: Enabling Two-Factor Authentication

To enhance the security of your GitHub account, enable two-factor authentication.

1. **Enable 2FA**

* Click on your account icon at the top right and select “Settings.”
* Go to “Passwords and Authentication” and click the green button “Enable two-factor authentication.”

1. **Set Up an Authenticator App**

* Scan the QR code with an authenticator app on your phone (e.g., Microsoft Authenticator).
* Enter the verification code from the app into GitHub.

1. **Download Recovery Codes**

* Save the GitHub recovery codes in a safe place for future use.

1. **Log In with 2FA**

* Log out and log back in to GitHub using your password and the 2FA code from your authenticator app.

**Optional:** By default, you will need to use your authenticator app whenever you want to log in to GitHub. This can be somewhat onerous, so some good options are downloading the GitHub mobile app and using it for 2FA. Another option is to configure a Passkey. This will allow you to create and use a PIN number or face recognition on your laptop or phone for authentication. All of these options are under Settings > Passwords and Authentication. We encourage you to choose whatever works for you and flex your Googling and YouTube skills if you get stuck along the way.

### Step 4: Linking Git and GitHub - Setting up an SSH Key for GitHub

The Secure Shell (SSH) protocol is a method for securely sending commands to a computer over an unsecured network. You will enable [Secure Shell Protocol (SSH)


Links to an external site.](https://en.wikipedia.org/wiki/Secure_Shell) key access to GitHub via terminal in this step, which will enable you to use Git with GitHub over SSH and will automate your credentials so that you won’t need to keep supplying authentication when talking to GitHub.

1. **Generate SSH Key**

* Open a terminal window and enter:

```
ssh-keygen -t ed25519 -C "your_email@example.com".
```

* Replace “your\_email@example.com” with the email address associated with your GitHub account.
* You should see an output that looks something like this: `Generating public/private ed25519 key pair.`
* When prompted to “Enter a file in which to save the key,” press **ENTER** to accept the default file location:

`> Enter a file in which to save the key (/Users/you/.ssh/id_ed25519): [Press enter]`

* When prompted to “Enter passphrase,” press ENTER to leave it empty:

    
  `> Enter passphrase (empty for no passphrase): [Type a passphrase]`  
  `> Enter same passphrase again: [Type passphrase again]`

1. **Start the SSH Agent**

* In your terminal, type:  `eval "$(ssh-agent -s)"`

1. **Add SSH Key to SSH Agent**

* Add the SSH private key to the SSH agent:

`ssh-add ~/.ssh/id_ed25519`

1. **Copy the SSH Key to Clipboard**

* For macOS:`pbcopy < ~/.ssh/id_ed25519.pub`
* For WIndows:`clip < ~/.ssh/id_ed25519.pub`

1. **Add SSH Key to GitHub**

* Navigate to your [GitHub SSH settings


  Links to an external site.](https://github.com/settings/keys).
* Click “New SSH key” or “Add SSH key.”
* In the “Title” field, add a descriptive label for the new key, such as “Personal MacBook Air.”
* Paste the SSH key from your clipboard into the “Key” text box.
* Click “Add SSH key.”
* If prompted, confirm your GitHub password.

1. **Verify SSH Connection**

* In your terminal, type: `ssh -T git@github.com`
* If prompted with the following, type **yes** and press **ENTER.**

  ```
  > The authenticity of host 'github.com (IP ADDRESS)' can't be established.   
    
  > RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.  
    
  > Are you sure you want to continue connecting (yes/no)?
  ```
* If successful, you should see:

  ```
  > Hi username! You've successfully authenticated, but GitHub does not  
    
  > provide shell access.
  ```

1. **Set SSH as the Global Authentication Protocol**

* In your terminal, type: `git config --global url.ssh://git@github.com/.insteadOf https://github.com/`

After completing these steps, you should be able to download and manage remote repositories from GitHub using SSH, streamlining your workflow and enhancing security.

### Next Steps

With Git and GitHub configured, you are now ready to start managing your projects efficiently. You can create, clone, and manage repositories, collaborate with others, and track your project’s history seamlessly.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1406/modules/items/243461

Scraped At: 2026-05-14T20:43:47.353661
