#!/bin/env python3

import json
import subprocess

DIRECTORY = "/opt/tutorial/"
STEPS_DIRECTORY = DIRECTORY + "steps"
PROGRESS_FILE = DIRECTORY + "progress"


class Config:
    """ Config holds configuration """
    config_file = None
    cfg = {
            "step": 0
    }

    def __init__(self, config_file):
        self.config_file = config_file
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

    def next_step(self):
        """ next_step increases the current step """
        self.cfg["step"] = self.cfg["step"] + 1


class Step:
    """ Step holds a single step """

    directory = ""
    number = 0

    def __init__(self, directory, number):
        self.directory = directory
        self.number = number

    def description(self):
        """ description prints the description of the current step """
        with open(self.directory + "/" + str(self.number) + "/description.md",
                  encoding='UTF-8') as reader:
            print(reader.read())

    def validate(self):
        """ validate runs the validation steps """
        subprocess.run(self.directory + "/" + str(self.number) +
                       "/validate", shell=True, check=False)


cfg = Config(PROGRESS_FILE)
step = Step(STEPS_DIRECTORY, cfg.get_step())
step.description()
