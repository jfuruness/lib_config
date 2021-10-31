from configparser import RawConfigParser
import os
from pathlib import Path


class Config:
    """Wrapper around RawConfigParser that also deals with db conn

    originally from lib_bgp_data"""

    default_path = Path("/etc/main/main.ini")

    def __init__(self, write=True, path=None):
        """Initialize it with a specific section to work with"""

        self.path = path if path else self.default_path
        self.write = write
        self._conf = None
        # Makes the directory
        self.path.parent.mkdirs(parent=True)

    def __enter__(self) -> RawConfigParser:
        """Enters context manager, returns a dict like object"""

        self._conf = self._get_conf_dict()
        return self._conf

    def __exit__(self, _type, _value, _traceback):
        """Exits context manager"""

        if self.write:
            self._write_conf()

    def _get_conf_dict(self) -> RawConfigParser:
        """Reads in the config as a dict like object"""

        conf = RawConfigParser()
        conf.read(self.path)
        return conf

    def _write_conf(self):
        """Writes the config"""

        with open(self.path, "w+") as config_file:
            self._conf.write(config_file)

    @property
    def _dir(self) -> str:
        """Returns the directory for the path of the config file"""

        return os.path.split(self.path)[0]
