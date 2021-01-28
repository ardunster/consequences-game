# Consequences

A Python implementation of the [Consequences game](https://en.wikipedia.org/wiki/Consequences_(game))

Consequences is a Mad Libs-style game in which pieces of text are filled in by
category, then combined to create a (usually hilarious) whole. This code can
make use of templates to fit both a Mad Libs kind of text block or the more
classic style Consequences game.

## Requirements

Built in Python 3.9.0, using PySide6.
Uses:

``` pip
PySide6==6.0.0
shiboken6==6.0.0
```

## Install

The following commands assume that you have Python3.9 installed (although the
game will probably run on earlier versions of Python3 as well) and running from
your command line, and that you have cloned the repository into a folder called
`consequences-game`.

Set up a python3 virtual environment and then install the requirements:

On a Linux based system, use the following commands:

``` bash
consequences-game $ python3.9 -m venv venv
consequences-game $ venv/bin/pip install --upgrade pip
consequences-game % venv/bin/pip install -r requirements.txt
# Then run the game:
consequences-game % venv/bin/python3 -m consequences
```

On Windows, the commands are fairly similar:

``` cmd
\consequences-game> python -m venv venv
\consequences-game> venv\scripts\python.exe -m pip install --upgrade pip
\consequences-game> venv\scripts\python.exe -m pip install -r requirements.txt
# Then run the game:
\consequences-game> venv\scripts\python.exe -m consequences
```

## Content

To create user content, copy the template file in the `/content/` directory. If
you want to create content not tracked by git, the `.gitignore` file is set up
to ignore a `/private/` directory inside content.
