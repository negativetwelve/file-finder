#! /usr/bin/env python

from os import getcwd
from os import listdir
from os.path import isdir
from os.path import isfile
from os.path import join
import sys


BLACKLISTED_FILE_NAMES = []
BLACKLISTED_FILE_EXTS = []
HELP_FLAGS = ['-h', '--help']


def make_relative_path(path):
    relative_path = path.replace(STARTING_PATH, ".")
    relative_path += '/'
    return relative_path

def print_output(relative_path, filename, line):
    full_path = relative_path + filename
    path_length = len(full_path)
    num_spaces = 50 - path_length
    print "{0}{1}{2}".format(full_path, " " * num_spaces, line.strip())

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
    for line in lines:
        line = line.rstrip('\n')
        if text_to_find in line:
            relative_path = make_relative_path(path)
            print_output(relative_path, f, line)

def explore(path):
    subdirectories, files = search_dir(path)
    for path, f in files:
        search_file(path, f)
    for subdir in subdirectories:
        explore(subdir)

if __name__ == '__main__':
    options = sys.argv[1].split(' --')
    if len(options) == 1:
        if options[0] in HELP_FLAGS:
            print "Use ff to find text within files."
            sys.exit(1)

    text_to_find = options.pop(0)
    print text_to_find
    print sys.argv
    print options
    STARTING_PATH = getcwd()
    if sys.argv[1]:
        explore(STARTING_PATH)
    else:
        print "Please enter text to search for."
        sys.exit(0)


