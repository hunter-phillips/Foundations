# Git and GitHub Basics
## Setting up Git
### Setting up the Config
- `git config --global user.name "Your Name"` sets the name.
- `git config --global user.email "yourname@example.com"` sets the email.
- `git config --global color.ui auto` enables colorful output.
- `git config --get <user.name or user.email>` shows the user name and email in the config.
- `git --version` shows the version of git installed.
- `git config --global init.defaultBranch` sets the default branch.
### Create an SSH Key
- If `ls ~/.ssh/id_rsa.pub` returns "No such file or directory," then the following command will generate an SSH key:
    - `ssh-keygen -C <youremail>`
        - Press `Enter` when prompted for a location.
        - Enter a password if wanted.
### Connecting to GitHub
- In `Settings`, click on `SSH and GPG keys`, and hit the `New SSH Key` button.
    - Give the key a descriptive name.
- Copy the output of the following command to get the SSH Key from the command line:
    - `cat ~/.ssh/id_rsa.pub`
- Paste the key into the key field on GitHub and click `Add SSH Key`.
### Verify SSH Connection
- Enter `ssh -T git@github`
- Verify that the warning fingerprint is one of the following:
    - `SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8 (RSA)`
    - `SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM (ECDSA)`
    - `SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU (Ed25519)`
- Type `yes`, and a successfully authenticated message will appear.


## From GitHub to Git
- After creating a respository on GitHub, click on the `Code` button, select the `SSH` option and copy the link, which should follow this format:
    - `git@github.com:USER-NAME/REPOSITORY-NAME.git`
- In the terminal, use the following command to clone the repository:
    - `git clone git@github.com:USER-NAME/REPOSITORY-NAME.git`

## Checking the Status
- When working on files in the repository, there are several stages which they can be in, which can be checked with `git status`:
    - Red means that the file is not staged.
    - Green means that the file has been staged and is ready to be committed.


## Staging a File
- To stage all files, use `git add  .` or, for a more specific file, `git add <file>`.
- A staged file is ready to be committed.

## Committing a File
- Assuming a commit template is created, the following command will commit all files and opens a text editor for an appropriate commit message:
    - `git commit`


## Logs
- To see the various versions of a file, there are a few commands that can be used:
    - `git log` shows indepth details of all commits.
    - `git shortlog` shows commit subjects for by user.
    - `git log --oneline` displays only the subject line of each commit.

## Pushing a File to the Remote Repository
- After committing, `git push origin main` can be used to push the committed files to the main remote branch for updating.