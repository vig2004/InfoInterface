# InfoInterface
Added line##############
1. Create account on GitHub.
2. Download git on your local pc from https://git-scm.com/download/win
3. Install Git. After installation make sure to mark "Launch Git Bash" checkbox before clicking "Finish" button. 
4. Create a folder where you will save the project/ repository. Use "mkdir git_directory" to create a directory if not present.
5. Open "git_directory" by running "cd git_directory".
6. Now we are inside "git_directory" (can check path using "pwd" command)
7. We start now by initialzing "git_directory" as a local Git repository.
  - *Run following commands*
    - git init \
      *This initialises the "git_directory" as a git repo*
    - git config --global user.email "you@example.com"\
     git config --global user.name "Your Name"\
      *Enter your git details here*
    - git clone https://github.com/vig2004/InfoInterface.git \
      *This would clone the remote(online/shared) repository locally*
  - *Basic git commands*
  
    *Commands written below will be used to pull/push changes from/to the remote repository*\
    - git fetch origin main\
      *Will fetch the latest version from the remote repo(i.e. the common repo on github) but won't make changes to your local repo.*
    - git merge origin/main\
      *The changes of the fetched repo will be merged with your local(in pc) repo.*
    - git push origin main\
      *To push all your committed changes to the remote repo that's visible to everyone*
    - git pull origin main\
      *This command fetches and merges the code in one go.*
    
    *Commands to commit changes locally*
    - git add file_name\
      *To track changes made to "file_path" use above command.*
    - git add . \
      *To track all newly created files or files with modifications use above command. This adds all untracked files to stagged phase*
    - git commit file_path -m "Message stating changes made" \
      *This commits all the changes made to particular file*
    
    
