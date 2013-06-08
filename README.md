## Text Finder

## Setup

Add the following function to either your `~/.bash_profile` or `~/.zprofile`:

    tf() {
      python ~/path_to_text_finder/text_finder.py "$*";
    }

Make sure that you source the file that you add this to. 

## Usage

You can now run the following:

    tf def my_function

And it will output the filename, line number, and actual line of text that this
phrase is found on. It will start by looking in the current directory and then
recursively search in all subdirectories. There are a number of options that you
can use with this function.

## Options




