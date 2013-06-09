## File Finder

### Setup

Clone this repo and move the `file_finder.py` file into /usr/bin as `ff`. That
will make the command available for you to use.

After you move the file, make sure you run:

    $ [sudo] chmod +x /usr/bin/ff

Finally, make sure you have Pip, then run:

    pip install termcolor

### Usage

By default, ff will search all files in the current directory AND all
subdirectories. You can now run the following:

    ff def my_function

And it will output the filename, line number, and actual line of text that this
phrase is found on. There are a number of options that you can use with this function.

### Options

`-h, --help`

`--ext extensions` Only look for certain extensions listed after --ext

For example:

    ff def my_function --ext py

The above command will only look for the text `def my_function` in files with the extension `py`.
You can chain on multiple extensions.


