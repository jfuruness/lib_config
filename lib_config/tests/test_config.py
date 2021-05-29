import os

import pytest

from lib_utils.file_funcs import delete_paths

from ..config import Config


class Paths:
    valid_path = "/tmp/test/test_conf.ini"
    # Requires permissions
    requires_permissions_path = "/etc/test_config/test.ini"


class PytestConfig(Config):
    """Pytest class that contains more info"""
    def __enter__(self):
        return super(PytestConfig, self).__enter__(), self.path, self._dir


@pytest.mark.config
class TestConfig:
    """Tests the wrapper around the ini file"""

    test_section = "test"
    test_dict = {"key1": "val1", "key2": "val2"}

    def test_requires_permissions_path(self):
        """Tests that the path that requires permissions doesn't exist"""

        assert not os.path.exists(Paths.requires_permissions_path)
        _dir = os.path.split(Paths.requires_permissions_path)[0]
        assert not os.path.exists(_dir)

    def teardown(self):
        """Deleted after every test"""

        delete_paths([Paths.valid_path,
                      Paths.requires_permissions_path,
                      # Directory for valid path
                      os.path.split(Paths.valid_path)[0]])
        with Config() as conf_dict:
            try:
                del conf_dict[self.test_section]
            # Just removing garbage. If it's not in there don't worry
            except KeyError:
                pass

    @pytest.mark.parametrize("path", [Paths.valid_path, None])
    def test_init_no_write_valid_paths(self, path):
        """Tests the init func with no path and no write

        NOTE: this will fail if the config dir is not created
        """

        conf = PytestConfig(write=False, path=path)
        assert os.path.exists(conf._dir)

    @pytest.mark.parametrize("write", [True, False])
    def test_init_invalid_path(self, write):
        """Tests the init func with invalid path with every write option"""

        with pytest.raises(PermissionError):
            PytestConfig(write=write, path=Paths.requires_permissions_path)

    @pytest.mark.parametrize("path", [Paths.valid_path, None])
    def test_init_yes_write_valid_paths(self, path):
        """Tests the init func with no path and yes write

        NOTE: This will fail if config dir is not created"""

        conf = PytestConfig(write=True, path=path)
        assert os.path.exists(conf._dir)

    @pytest.mark.parametrize("path", [Paths.valid_path, None])
    def test_context_manager_no_write_valid_paths(self, path):
        """Tests the context_manager func with no path and no write

        NOTE: this will fail if the config dir is not created
        """

        with PytestConfig(write=False, path=path) as (_, __, _dir):
            assert os.path.exists(_dir)

    @pytest.mark.parametrize("write", [True, False])
    def test_context_manager_no_write_invalid_path(self, write):
        """Tests the context_manager func with invalid path and no write"""

        with pytest.raises(PermissionError):
            with PytestConfig(write=write,
                              path=Paths.requires_permissions_path):
                pass

    @pytest.mark.parametrize("path", [Paths.valid_path, None])
    def test_context_manager_yes_write_valid_paths(self, path):
        """Tests the context_manager func with no path and yes write

        NOTE: This will fail if config dir is not created"""

        with PytestConfig(write=True, path=path) as (conf_dict, _path, _dir):
            assert os.path.exists(_dir)
            conf_dict[self.test_section] = self.test_dict
        assert os.path.exists(_path)

        # Ensure the file was written correctly
        with PytestConfig(write=False, path=path) as (conf_dict, _, __):
            assert conf_dict[self.test_section] == self.test_dict

    def test_context_manager_yes_write_invalid_path(self):
        """Tests the context_manager func with invalid path and yes write"""

        with pytest.raises(PermissionError):
            kwargs = {"write": True, "path": Paths.requires_permissions_path}
            with PytestConfig(**kwargs) as (_, path, _dir):
                # Make sure file isnt' written until context manager is done
                assert not os.path.exists(path)
                assert os.path.exists(_dir)
