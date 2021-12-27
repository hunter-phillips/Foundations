# Command Line
## Hotkeys
- Ctrl + A
    - Beginning of Line
- Ctrl + E
    - End of Line
- Ctrl + U
    - Deletes from Current Position to Beginning of Line

## Fundamental Commands
- whoami
    - Returns User
- pwd -<flags>
    - Returns Present Working Directory
    - Flags
        - p
            - Returns full physical path with symlinks
- ls -<flags>
    - Returns all Visible Files and Directories
    - Flags
        - a
            - Lists all visible and invisible files
        - l
            - Returns more detailed information about the files, including modification time, size, and creator
        - h
            - Returns sizes in a human-readable format
        - S
            - Sorts by size (default is alphabetical)
        - t
            - Sorts by last modified time
        - r
            - Reverses order
    - Note: Flags can be used together, such as "ls -al"
- cd <directory>
    - Changes Directory
    - Directory Shorthand:
        - ..
            - Changes the directory to the parent
        - Only calling "cd" will return to home "~"
- echo
    - Prints Text to the Command Line
- cat <file>
    - Prints Contents of a File
- man <cmd>
    - Opens a Manual for the Command
- grep -<flags> <pattern>
    - Searches for a Pattern
    - Using Wildcard (*)
        - The wildcard can be used to search for patterns, such as all text files that start with b:
            - grep b*.txt
    - Flags
        - i
            - Ignores case
- sudo <cmd>
    - Placed Before a Command to Run it as Root

## File Manipulation
- ln -<flags> <source> <target>
    - Creates a Hard Link between Two Files
        - The target updates as the source changes and vice versa.
    - Flags
        - f
            - Forces a link if the target already exists
        - s
            - Creates a soft link that references the source file
    - Note: Flags are placed before file names
- mkdir -<flags> <dir>
    - Creates a New Directory
    - Flags
        - p <dir>/<dir>/<dir>
            - Creates nested directory
        - v
            - Prints results to console
- cp -<flags> <source> <target> <optional dir>
    - Copies Source to Target
    - Flags
        - R <source dir> <target dir>
            - Recursively copies all files from source directory to target directory
        - f 
            - Forces a copy if a file exists
        - i
            - Asks user to confirm overwrite if a file exists
- rm -<flags> <files>
    - Deletes Files
    - Flags
        - Uses the same flags as cp
- rmdir <dir>
    - Deletes a Directory
- mv -<flags> <source> <target>
    - Moves a File and Deletes the Original
    - Flags
        - Uses the same flags as cp
    - Note: Source and Target can be Paths

## Special Symbols
- <cmd> | <cmd>
    - Pipes the Output of the First Command as Input for the Second Command
- <cmd> > <target file>
    - Writes a Command's Output to a Target File
- <cmd> >> <target file>
    - Appends a Command's Output to a Target File

    

