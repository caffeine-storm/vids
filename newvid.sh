#!/bin/bash

if ! [ -x `which manim` ] ; then
  echo 1>&2 "create/activate a pyenv first!"
  exit 1
fi

if [ -z "$1" ] ; then
  echo 1>&2 "usage: $0 <vid-name>"
  exit 1
fi

if [ -e "$1" ] ; then
  echo 1>&2 "error: $1 already exists"
  exit 1
fi

# Create a new manim 'project'; a collection of scenes.
manim init project -d $1

# Add a default Makefile for building and previewing the project.
cat >$1/Makefile <<EOF
all: it

it: main.py manim.cfg
	manim -ql -p ./main.py
EOF

# Add a .gitignore to the new project directory to ignore intermediate
# files/caches built by manim.
echo media > $1/.gitignore
