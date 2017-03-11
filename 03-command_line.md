# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> (1) show current working directory path
```console
$ pwd
```
>> (2) creating a directory called **Project**
```console
$ mkdir Project
```
>> (3) deleting an **empty** directory called **empty**
```console
$ rmdir empty
```
>> (4) deleting a **non-empty** directory **nonempty**
```console
$ rm -rf nonempty
```
>> (5) creating a file using `touch` command (name of the file: **pycode.py**)
```console
$ touch pycode.py 
```
>> (6) deleting a file called **pycode.py**
```console
$ rm pycode.py
```
>> (7) renaming a file: **pycode.py** to **python_code.py** 
```console
$ mv pycode.py python_code.py
```
>> (8) listing hidden files
```console
$ ls -a
```
>> (9) copying a file (**pycode.py**) from one directory (**FromThisDir**) to another (**ToThisDir**)
```console
$ cp FromThisDir/pycode.py ToThisDir/.
```
>> (10) check if a package is installed and where
```console
$ which emacs
```
>> (11) list recently used commands
```console
$ history
```
>> (12) show help file or manual for a command
```console
$ man ls
```


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> Commands | Description
------------- | -------------
`ls`          | List directory contents.
`ls -a`       | List contents including entries with names beginning with a dot (.).
`ls -l`       | Shows total number of files in the directory and its sub-directories. List files and sub-directories in alpha-numeric order with a summary of the contents. (See Example 1 below)
`ls -lh`      | Same as `ls -l` (-h used with the -l option) but shows unit suffixes: Byte, Kilobyte, Megabyte,Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 2 for sizes.
`ls -lah`     | Same as `ls -lh` but also includes directory entries whose names begin with a dot (.).
`ls -t`       | List dir contents sorted by time modified (most recently modified first) before sorting the operands by lexicographical order.
`ls -Glp`     | An extension ls of `ls -l`. ``-G`` enables colorized output. Different colors for different types of files and directories. ``-p`` Write a slash (``/``) after the name of a directory.


> > `ls`  
> > List directory contents.

> > `ls -a`  
> > Include directory entries whose names begin with a dot (.).

> > `ls -l`  
* Shows total number of files in the directory and its sub-directories. 
* List directory contents (files and sub-directories) in alpha-numeric order with a summary of the contents. 
> > Example of `ls -l` (terminal output):
``` console 
total 136
-rw-r--r--   1 susmitadatta  staff  2738 Mar 10 14:55 00-fork_repo.md
drwxr-xr-x   3 susmitadatta  staff   102 Mar 10 14:19 editors
```
>> Summary of the example above:
>> * dir or file, read-write-execution permissions
>> * Number of files (in a dir or the file iself)
>> * Owner's name
>> * Owner's designation
>> * File/dir size in KB 
>> * Creation/modification date. 
>> * File/dir name


> > `ls -lh`  
Same as `ls -l` (-h used with the -l option) but shows unit suffixes: 
Byte, Kilobyte, Megabyte,Gigabyte, Terabyte and Petabyte in order to reduce the number of digits to three or less using base 2 for sizes.

> > `ls -lah`  
Same as `ls -lh` but also includes directory entries whose names begin with a dot (.).

> > `ls -t` 
List dir contents sorted by time modified (most recently modified first) before sorting the operands by lexicographical order.

> > `ls -Glp`
An extension ls of `ls -l`. 
``-G`` enables colorized output. Different colors for different types of files and directories. 
``-p`` Write a slash (``/``) after the name of a directory.

> > Example of `ls -Glp` (terminal output):
```console
-rw-r--r--  1 susmitadatta  staff   648 Mar 10 14:19 football.csv
-rwxr-xr-x  1 susmitadatta  staff   940 Mar 10 14:19 markov.py
drwxr-xr-x  6 susmitadatta  staff   204 Mar 10 14:19 pandas/
```

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -lrt`
List contents according to creation and modification date.

> > `ls -F`
List contents flagging files and directories (with a trailing `/`).

> > `ls | less`
List contents in a single column (in apha-numeric order) and displays contents one page at a time (the number of lines that fit the terminal window).

> > `ls -R`
List contents of the directory and the sub-directories.

> > `ls -m` 
List contents as a comma-separated list.



### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

