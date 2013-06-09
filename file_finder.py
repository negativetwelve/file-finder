#!/usr/bin/env python

from os import getcwd
from os import listdir
from os.path import isdir
from os.path import isfile
from os.path import join
import sys
from termcolor import colored


BLACKLISTED_FILE_NAMES = []
BLACKLISTED_FILE_EXTS = []
HELP_FLAGS = ['-h', '--help']


def make_relative_path(path):
    relative_path = path.replace(STARTING_PATH, ".")
    relative_path += '/'
    return relative_path

def print_output(relative_path, filename, line_number, line):
    full_path = relative_path + filename
    path_length = len(full_path)
    num_spaces = 50 - path_length
    print "{0}{1}\t{2}\t{3}".format(full_path, " " * num_spaces, colored(line_number, 'red'), line.strip())

def formatted_options(options):
    new_options = {}
    for option in options:
        option_text = option.split()
        command, args = option_text[0], option_text[1:]
        new_options[command] = args
    return new_options

def check_extension(filename, extensions):
    if not extensions:
        return True
    filename_list = filename.split('.')

    # If the file does not have an extension.
    if len(filename_list) == 1:
        return False

    # In case the file has multiple extensions, we only check the last one.
    return filename_list[-1] in extensions

def search_dir(path):
    files = []
    subdirectories = []
    for f in listdir(path):
        full_path = join(path, f)
        if isfile(full_path):
            files.append([path, f])
        elif isdir(full_path):
            relative_path = f
            subdirectories.append(full_path)
    return subdirectories, files

def search_file(path, f):
    lines = open(join(path, f)).readlines()
    line_number = 1
    for line in lines:
        line = line.rstrip('\n')
        if text_to_find in line:
            relative_path = make_relative_path(path)
            print_output(relative_path, f, line_number, line)
        line_number += 1

def explore(path, options=None):
    subdirectories, files = search_dir(path)
    for path, f in files:
        if check_extension(f, options.get('ext')):
            search_file(path, f)
    for subdir in subdirectories:
        explore(subdir, options=options)

if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) == 1:
        print 'Please enter text to search for or add the flag -h for help.'
        sys.exit(0)

    arguments = ' '.join(arguments[1:])
    options = arguments.split(' --')
    if len(options) == 1:
        if options[0] in HELP_FLAGS:
            print "Use ff to find text within files."
            sys.exit(1)

    text_to_find = options.pop(0)
    options = formatted_options(options)

    STARTING_PATH = getcwd()
    if sys.argv[1]:
        explore(STARTING_PATH, options=options)


