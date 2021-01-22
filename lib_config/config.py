#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This package contains a config file"""

__authors__ = ["Justin Furuness"]
__credits__ = ["Justin Furuness"]
__Lisence__ = "BSD"
__maintainer__ = "Justin Furuness"
__email__ = "jfuruness@gmail.com"
__status__ = "Development"

from configparser import NoSectionError, ConfigParser as SCP

class Config:
    def __init__(self, package):
        self.path = f"/etc/{package}.conf"
        if not os.path.exist:
            with open(self.path, "w+") as f:
                pass
    def write_section(self, section: str, kwargs: dict):
        _config = SCP()
        _config.read(self.path)
        _config[section] = kwargs
        with open(self.path, "a") as f:
            _config.write(f)

    def read_section_tag(self, section: str, tag: str):
        try:
            return SCP().read(self.path).get(section, tag, raw=raw)
        except NoSectionError as e:
            input("Fill in desired section, then press enter")
            return self.read_section_tag(section, tag)
