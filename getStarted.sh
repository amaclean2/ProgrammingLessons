#!/bin/bash

command cd $HOME/Documents || return

mkdir PythonNotes
command cd PythonNotes

# ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime

git init
git clone https://github.com/amaclean2/ProgrammingLessons.git

command cd ProgrammingLessons
open -a "Safari" FirstInstructions.html