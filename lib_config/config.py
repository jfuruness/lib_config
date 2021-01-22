#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This package contains a config file"""

__authors__ = ["Justin Furuness"]
__credits__ = ["Justin Furuness"]
__Lisence__ = "BSD"
__maintainer__ = "Justin Furuness"
__email__ = "jfuruness@gmail.com"
__status__ = "Development"

import os

from configparser import NoSectionError, ConfigParser as SCP

from lib_utils import utils

class Config:
    def __init__(self, package="custom_config"):
        self.path = f"/etc/{package}.conf"
        if not os.path.exists(self.path):
            try:
                with open(self.path, "w+") as f:
                    pass
            except PermissionError as e:
                utils.run_cmds([f"sudo touch {self.path}",
                                f"sudo chmod -R 777 {self.path}"])
    def write_section(self, section: str, kwargs: dict):
        _config = SCP()
        _config.read(self.path)
        _config[section] = kwargs
        with open(self.path, "a") as f:
            _config.write(f)

    def read(self, section: str, tag: str, raw: bool = True):
        try:
            _conf = SCP()
            _conf.read(self.path)
            return _conf.get(section, tag, raw=raw)
        except (NoSectionError, AttributeError) as e:
            input(f"Fill in desired section in {self.path}, then press enter")
            return self.read(section, tag)

    def discord_creds(self):
        """Returns email and password"""

        return [self.read("Discord", tag) for tag in ["email", "password"]]
