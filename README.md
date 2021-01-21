# Consequences

A Python implementation of the [Consequences game](https://en.wikipedia.org/wiki/Consequences_(game))

Consequences is a Mad Libs-style game in which pieces of text are filled in by
category, then combined to create a (usually hilarious) whole. This code can
make use of templates to fit both a Mad Libs kind of text block or the more
classic style Consequences game.

## Requirements

Built in Python 3.9.0, using PySide2.
Uses:

``` pip
PySide2==5.15.2
shiboken2==5.15.2
```

## Install

Set up a python3 virtual environment and then install the requirements. On a
Linux based system, use the following commands:

``` bash
consequences-game $ python3.9 -m venv venv
consequences-game $ venv/bin/pip install --upgrade pip
consequences-game % venv/bin/pip install -r requirements.txt
```

You can then run the game using the command `venv/bin/python3 -m consequences`

## Content

To create user content, copy the template file in the `/content/` directory. If
you want to create content not tracked by git, the `.gitignore` file is set up
to ignore a `/private/` directory inside content.
