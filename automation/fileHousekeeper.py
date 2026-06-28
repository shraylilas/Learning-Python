# I noticed that sometimes I have to drudge through my folders to delete tons of useless files
# Or maybe I want to mass rename certain files. Or I'm looking at a really massive directory and need to find a folder or something
# And etcetera etcetera. So I just learned that we can automate that stuff. So here's an attempt at that.
from pathlib import Path

# Control variable for the main loop
i = 1

def deleter(direct):
##  Delete files whose names contain a given string.
##  Asks for confirmation before each deletion.

    string = input("Enter string (if that string is present in a filename that file will be deleted) ").lower()
    for file in direct.iterdir():                     # iterate over every item in the directory
        if file.is_file() and string in file.name.lower():   # only regular files with matching name
            confirm = input(f"Delete {file.name}? y/n ")
            if confirm.lower() == "y":
                file.unlink()                         # permanently delete the file
            elif confirm.lower() == "n":
                continue                              # skip this file
            else:
                print("Error; skipping deletion")
                continue

def renamer(direct):
##    Rename files whose names contain a given string.
##    Appends a sequential number to the new base name.
##    Skips renaming if the target name already exists.

    string = input("Enter string (if that string is present in a filename that file will be renamed) ").lower()
    new_name = input("Enter new name of the file ")   # base name (without extension)
    copy = 1
    for file in direct.iterdir():
        if string in file.name.lower():               # file name contains the search string
            new_path = direct / f"{new_name}_{str(copy)}{file.suffix}"
            if new_path.exists():
                continue                              # target already exists – skip this file
            else:
                file.rename(new_path)                 # perform the rename
                copy += 1                             # increment counter for next file

def folder_checker(direct):
    ## List all subdirectories inside the given directory and count them.
    count = 0
    for folders in direct.iterdir():
        if folders.is_dir():                             # it's a folder, not a file
            print(folders)                               # print the full Path object
            count += 1
    print(f"There are {count} folders in this directory")

def finder(direct):
    """
    Find files either by a specific substring in the name, or by file extension.
    """
    type_find = input("Do you want to find a 'specific' file or files that are of the same 'type'? ")
    if type_find.lower() == "specific":
        string = input("Enter string (it will search for that string) ")
        for file in direct.iterdir():
            if string in file.name.lower():           # case‑insensitive
                print(file)
    elif type_find.lower() == "type":
        filetype = input("Enter filetype (py, pdf, etc.) ")
        for file in direct.iterdir():                 
            # Check that it's a file and that the extension (without the dot) matches
            if file.is_file() and filetype.lower() in file.suffix.lower():
                print(file)
    else:
        print("Error")                                # invalid choice

# ----- Main program -----
x = input("Enter folder location ")
direct = Path(x)                                      # create a Path object for the target directory

while i == 1:                                         # infinite loop until user chooses "Exit"
    choice = input("Do you want to delete, rename, or find a file(s)? Do you want to check what folders are in a directory (folder)? Exit? ")
    if choice.lower() == "delete":
        deleter(direct)
    elif choice.lower() == "rename":
        renamer(direct)
    elif choice.lower() == "folder":
        folder_checker(direct)
    elif choice.lower() == "find":
        finder(direct)
    else:
        print("Error; breaking the loop")
        break
