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
- pwd -&lt;flags&gt;
    - Returns Present Working Directory
    - Flags
        - p
            - Returns full physical path with symlinks
- ls -&lt;flags&gt;
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
- cd &lt;directory&gt;
    - Changes Directory
    - Directory Shorthand:
        - ..
            - Changes the directory to the parent
        - Only calling "cd" will return to home "~"
- echo
    - Prints Text to the Command Line
- cat &lt;file&gt;
    - Prints Contents of a File
- man &lt;cmd&gt;
    - Opens a Manual for the Command
- grep -&lt;flags&gt; &lt;pattern&gt;
    - Searches for a Pattern
    - Using Wildcard (*)
        - The wildcard can be used to search for patterns, such as all text files that start with b:
            - grep b*.txt
    - Flags
        - i
            - Ignores case
- sudo &lt;cmd&gt;
    - Placed Before a Command to Run it as Root

## File Manipulation
- ln -&lt;flags&gt; &lt;source&gt; &lt;target&gt;
    - Creates a Hard Link between Two Files
        - The target updates as the source changes and vice versa.
    - Flags
        - f
            - Forces a link if the target already exists
        - s
            - Creates a soft link that references the source file
    - Note: Flags are placed before file names
- mkdir -&lt;flags&gt; &lt;dir&gt;
    - Creates a New Directory
    - Flags
        - p &lt;dir&gt;/&lt;dir&gt;/&lt;dir&gt;
            - Creates nested directory
        - v
            - Prints results to console
- cp -&lt;flags&gt; &lt;source&gt; &lt;target&gt; &lt;optional dir&gt;
    - Copies Source to Target
    - Flags
        - R &lt;source dir&gt; &lt;target dir&gt;
            - Recursively copies all files from source directory to target directory
        - f 
            - Forces a copy if a file exists
        - i
            - Asks user to confirm overwrite if a file exists
- rm -&lt;flags&gt; &lt;files&gt;
    - Deletes Files
    - Flags
        - Uses the same flags as cp
- rmdir &lt;dir&gt;
    - Deletes a Directory
- mv -&lt;flags&gt; &lt;source&gt; &lt;target&gt;
    - Moves a File and Deletes the Original
    - Flags
        - Uses the same flags as cp
    - Note: Source and Target can be Paths

## Special Symbols
- &lt;cmd&gt; | &lt;cmd&gt;
    - Pipes the Output of the First Command as Input for the Second Command
- &lt;cmd&gt; &gt; &lt;target file&gt;
    - Writes a Command's Output to a Target File
- &lt;cmd&gt; &gt;&gt; &lt;target file&gt;
    - Appends a Command's Output to a Target File

    

