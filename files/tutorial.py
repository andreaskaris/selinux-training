#!/bin/env python3.11
"""SELinux tutorial

Show instructions with `tutorial instructions` (alias i).
Validate that you followed instructions with `tutorial validate` (alias v).
Go to the next step with `tutorial next` (alias n).
Go to a previous step with `tutorial previous` (alias p).

Usage:
  tutorial instructions
  tutorial previous
  tutorial next
  tutorial step STEP
  tutorial validate
  tutorial help


Arguments:
  STEP          Number of step to skip to.

Options:
  -h --help     Show this screen.
"""

import os
import json
import sys
import subprocess
from docopt import docopt, DocoptExit

DIRECTORY = "/opt/tutorial/"
STEPS_DIRECTORY = DIRECTORY + "steps"
PROGRESS_FILE = DIRECTORY + "progress"


class Config:
    """ Config holds configuration """
    config_file = None
    max_steps = 0
    cfg = {
            "step": 0
    }

    def __init__(self, config_file, max_steps):
        self.config_file = config_file
        self.max_steps = max_steps
        try:
            self.load()
        except Exception:
            self.write()

    def load(self):
        """ load loads the configuration from file """
        with open(self.config_file, encoding='UTF-8') as reader:
            content = reader.read()
            self.cfg = json.loads(content)

    def write(self):
        """ write writes configuration to file """
        with open(self.config_file, 'w+', encoding='UTF-8') as writer:
            content = json.dumps(self.cfg)
            writer.write(content)

    def get_step(self):
        """ get_step returns the current step """

        return self.cfg["step"]

    def set_step(self, step):
        """ set_step sets the current step """
        if int(step) > self.max_steps - 1 or int(step) < 0:
            raise ValueError(f"Invalid value for step: '{step}'. " +
                             f"Must be in range 0 - {self.max_steps - 1}.")
        self.cfg["step"] = int(step)
        self.write()

    def is_first_step(self):
        """ is_first_step returns true if this is the first step """
        return self.cfg["step"] == 0

    def is_last_step(self):
        """ is_last_step returns true if this is the last step """
        return self.cfg["step"] >= self.max_steps - 1

    def next_step(self):
        """ next_step increases the current step """
        if not self.is_last_step():
            self.cfg["step"] = self.cfg["step"] + 1
            self.write()

    def previous_step(self):
        """ previous_step decreases the current step """
        if not self.is_first_step():
            self.cfg["step"] = self.cfg["step"] - 1
            self.write()


class Step:
    """ Step holds a single step """

    directory = ""
    number = 0

    def __init__(self, directory, number):
        self.directory = directory
        self.number = number

    def description(self):
        """ description prints the description of the current step """
        try:
            with open(self.directory + "/" + str(self.number) +
                      "/description.md", encoding='UTF-8') as reader:
                print(reader.read())
        except FileNotFoundError as fnfe:
            print(f'Could not find description file for step, err: {fnfe}')

    def validate(self):
        """ validate runs the validation steps """
        fname = self.directory + "/" + str(self.number) + "/validate"
        executable = os.access(fname, os.X_OK)
        if not executable:
            print(f'Could not find executable file {fname}')
            sys.exit(1)
        res = subprocess.run(fname, shell=True, check=False)
        return res.returncode == 0


COLORS = {
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'blue': '\033[0;34m',
        'nocolor': '\033[0m'
        }


def printc(color, text, end="\n"):
    """ printc prints color text to the console """
    if color not in COLORS:
        raise ValueError(f'Color {color} not in list of valid colors {COLORS}')
    print(COLORS[color], end="")
    print(text, end="")
    print(COLORS['nocolor'], end=end)


def printh(color, text):
    """ printh prints a header """
    printc(color, "************************************************")
    printc(color, text)
    printc(color, "************************************************")


def print_instructions(config, step):
    """ print_instructions prints instructions for the current step """
    printh('blue', f"Instructions for step {config.get_step()}:")
    step.description()
    printh('blue', "Run `tutorial validate` or `v` for validation.")


if __name__ == '__main__':
    # Check if STEPS_DIRECTORY exists and open PROGRESS_FILE.
    try:
        maximum_steps = len(os.listdir(STEPS_DIRECTORY))
    except FileNotFoundError as e:
        print(f'File not found, err: {e}')
        sys.exit(1)
    try:
        cfg = Config(PROGRESS_FILE, maximum_steps)
    except FileNotFoundError as e:
        print(f'File not found, err: {e}')
        sys.exit(1)

    # Parse command line options.
    arguments = []
    try:
        arguments = docopt(__doc__)
    except DocoptExit:
        print(__doc__, end="")
        sys.exit(1)

    # Show help text.
    if arguments['help']:
        print(__doc__, end="")
        sys.exit()

    # Act upon provided option.
    if arguments['previous']:
        if cfg.is_first_step():
            print("You are already at the first step.")
            sys.exit()
        cfg.previous_step()
        current_step = Step(STEPS_DIRECTORY, cfg.get_step())
        print_instructions(cfg, current_step)
        sys.exit()

    if arguments['next']:
        if cfg.is_last_step():
            printh('blue',
                   "Congratulations, you reached the end of the tutorial.")
            sys.exit()
        cfg.next_step()
        current_step = Step(STEPS_DIRECTORY, cfg.get_step())
        print_instructions(cfg, current_step)
        sys.exit()

    if arguments['step']:
        try:
            cfg.set_step(arguments['STEP'])
        except ValueError as e:
            printc('red', e)
            sys.exit(1)
        current_step = Step(STEPS_DIRECTORY, cfg.get_step())
        print_instructions(cfg, current_step)
        sys.exit()

    if arguments['validate']:
        current_step = Step(STEPS_DIRECTORY, cfg.get_step())
        if current_step.validate():
            printh('green', "All validation steps finished successfully.\n" +
                   "You may now run `tutorial next`  or `n` " +
                   "to go to the next step.")
            sys.exit()
        else:
            printh('red', "Validation steps failed.")
            sys.exit(1)

    if arguments['instructions']:
        current_step = Step(STEPS_DIRECTORY, cfg.get_step())
        print_instructions(cfg, current_step)
        sys.exit()
