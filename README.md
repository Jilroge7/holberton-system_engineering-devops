# holberton-system_engineering-devops
[Github Holberton Devops Project](https://github.com/Jilroge7/holberton-system_engineering-devops.git)

This repository contains my project for 0x00 Shell, basics.
### 0. Where am I? echo $PWD
* Write a script that prints the absolute path name of the current working directory.
### 1. Whats in there? (ls)
* Display the contents list of your current directory.
### 2. There is no place like home (cd~) 
* Write a script that changes the working directory to the users home directory.
### 3. The long format (ls -l)
* Display current directory contents in a long format.
### 4. Hidden files (ls -la)
* Display current directory contents, including hidden files (starting with .). Use the long format.
### 5. I love numbers mandatory (ls -la -v1)
* Display current directory contents.
i. Long format
i. with user and group IDs displayed numerically
i. And hidden files (starting with .)
### 6. Welcome holberton (mkdir /tmp/holberton)
* Create a script that creates a directory named holberton in the /tmp/ directory.
### 7. Betty in Holberton (mv /tmp/betty /tmp/holberton)
* Move the file betty from /tmp/ to /tmp/holberton.
### 8. Bye bye Betty (rm /tmp/holberton/betty)
* Delete the file betty.
### 9. Bye bye Holberton (rm -r /tmp/holberton) 
* Delete the directory holberton that is in the /tmp directory.
### 10. Back to the future (cd -)
* Write a script that changes the working directory to the previous one.
### 11. Lists mandatory (ls -la . .. /boot) 
* Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
### 12. File type (file /tmp/iamafile)
* Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
### 13. We are symbols, and inhabit symbols (ln -s /bin/ls __ls__)
* Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
### 14. Copy HTML files (cp -u *.html ..) 
* Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
### 15. Lets move (mv [[:upper:]]* -t /tmp/u) 
* Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
### 16. Clean Emacs (rm *~)
* Create a script that deletes all files in the current working directory that end with the character ~.
### 17. Tree (mkdir -p welcome/to/holberton)
* Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.
### 18. Life is a series of commas, not periods (ls -1amp)
* Write a command that lists all the files and directories of the current directory, separated by commas (,).