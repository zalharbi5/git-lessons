print("Hello version control")
print("Welcome all!")
print("New print")

"""
To config:
git config --global user.name "your name"
git config --global user.email "your email"

To check your current config:
git config user.name
git config user.email
"""

# cls == clear current terminal screen (windows)
# clear == clear current terminal screen (linux)
# git init == make current dir a repo in git (git initialization)
# git add . == (adds every file in current dir to repo)
# git add exm.py exm2.py exm3.py == add multiple files to repo
# git commit -m "what you have done" == update with comment stating what you did
# ^^ always when you modify anaything do (add) then (commit)
# git status == show the current status (tells you if anything is modified but not uploaded to repo)
# git log == show all previous commits
"""
For git log command:
Scroll down: Use j or the down arrow key.
Scroll up: Use k or the up arrow key.
Page down: Use Spacebar or Page Down.
Page up: Use b or Page Up.
Quit the pager: Use q.
"""
# git commit --amend -m "your modified comment" == moddify a commit comment that you passed
# git branch branch-name == create new branch
# git branch == list the branches you have created
# ^^ the green colored branch is the current branch you are working on
# git checkout branch-name == moves you to the specified branch
# git checkout -b branch-name = create a new branch then move to it (2 commands in 1)

"""
to merge sub-branch with master-branch:
1- move to master-branch (git checkout master)
2- merge sub-branch with master-branch (git merge sub-branch)
"""
# git branch -d branch-name == removes a branch
# ^^ It's a better practice to delete a sub-branch after merging it with master-branch

# push existing repo to GitHub:
"""
git remote add origin https://github.com/zalharbi5/git-lessons.git
git branch -M main
git push -u origin main
"""
# git remote == shows you the variable named (origin) which contains the github repo link 

"""
>> git branch -M main
>> git push -u origin main ::
transfer all your works and commits to GitHub
using -u allows you to use:
git push
without specifying anything.

if you didn't use -u, you have to write:
git push origin
everytime you want to push your modifications.

^^ Search more about these two commands
"""
# git pull == Brings the changes in online-repo in GitHub to your local-repo on your device
