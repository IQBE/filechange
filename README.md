# filechange
**A simple library to quicly edit files and directories.**


## Introduction
This file contians a detailed documentation of the *filechange* library and all it's commands.

## Setup
To use this library, u simply download it, put it in your project folder and use `import filechange` to import and use it.

## Commands

Here is the list of all the commands and their uses.

### To write a file we use the `write` command.

	write(file, text = "", mode = "w")

- `file` - the filename of the file you want to edit or make. If the file is in an other directory, give the (full) path to the file.

- `text` - the text you want to add to the file or the text you want to override the file with. Default is an empty string. ( `""` )

- `mode` - select which mode the write function should use. Mode `"w"` overrides the whole file, mode `"a"` appends the given `text` to the file and mode `"x"` creates a new empty file. Default is `"w"`.

#### Examples:

	write("test.txt")

This will create a new empty file called "test.txt" and does the same as `write("test.txt", "", "x")`. If however "test.txt" allready exists, all the contents will be deleted.


	write("test.txt", "Hi world!")

This will create a new file called "test.txt" and write "Hi world!" in it. If the file already exists, the contents wille be overwritten with "Hi world!".


	write("test.txt", "Hi world 2!", "a")

This will append "Hi world 2!" to the file "test.txt". If the file does not exist, it will create a new file containing "Hi world 2!".


	write("testfolder/test.txt", "Hi world!")

This will create a new empty file called "test.txt" in the directory `testfolder`. This will not create a new directory! If the directory or path does not exist, you will get an error.


### To read a file we use the `read` command.

	read(file, rLine = False, line = [1])

- `file` - the filename of the file you want to read. If the file is in an other directory, give the (full) path to the file.

- `rLine` - sets the mode to readline. If this mode is activated you will be able to read specific lines of the file. Default mode is `False`

- `line` - select which lines should be read. Requires `rLine = True`. To select lines, give a list of numbers. The lines will be read in the order given by the user. Default is `[1]`.

#### Examples:

	read("test.txt")

This will read all the contents of "test.txt".


	read("test.txt", True)

This will read the first line of "test.txt".


	read("test.txt", True, [1, 3, 4])

This will read the first, third and fourth line of "test.txt".


	read("test.txt", True, [1, 3, 2])

This will read in order: the first line, then the third line, then the second line of "test.txt".


### To make a path or directory we use the `dir` command.

	dir(dirName, multi = False)

- `dirName` - the name of the directory or path you want to create. If the directory should be made in an other directory, give the (full) path to that directory folowed by the directory or path you want to create.

- `multi` - selector to let the porgram know whether or not it should create a path rather than 1 directory. Default is `False`.

#### Examples:

	dir("testfolder")

This will create a directory named "testfolder".


	dir("testfolder/subfolder")

This will create a directory named "subfolder" in the directory "testfolder".


	dir("testfolder/subfolder", True)

This will create a path "testfolder/subfolder".


### To delete a file or directory we use the `delete` command.

	delete(file, sort = "file" , rec = True)

- `file` - the filename or the name of the directory you want to remove. If the file or directory is in an other directory, give the (full) path to the file or directory. A directory can **not** be removed if it is not empty.

- `sort` - selector to let the program know if you should delete a `"file"` or a `"directory"`. Default is `"file"`.

- `rec` - selector to let the program know if it should search recursively or not. Default is `True`.

#### Examples:

	delete("testfile.txt")

This will delete the file named "testfile.txt".


	delete("testfolder", "directory")

This will delete the directory named "testfolder". The directory must be empty.

	delete("testfolder/testfile.txt")

This will delete the file named "testfile.txt" in the directory "testfolder".


	delete("testfolder/subfolder", "directory")

This will delete the directory named "subfolder" in the directory "testfolder".


	delete("*.txt", "file")

This wil recursively delete all the files that end on ".txt".

	delete("*.txt", "file", False)

This wil non recursively delete all the files that end on ".txt".
