## File Finder

## Setup

Add the following function to either your `~/.bash_profile` or `~/.zprofile`:

    ff() {
      python ~/path_to_file_finder/file_finder.py "$*";
    }

Make sure that you source the file that you add this to. 

## Usage

By default, ff will search all files in the current directory AND all
subdirectories. You can now run the following:

    ff def my_function

And it will output the filename, line number, and actual line of text that this
phrase is found on. There are a number of options that you can use with this function.

## Options

    -h, --help
    -e, --ext extensions
          Only look for certain extensions listed after -e or --ext


