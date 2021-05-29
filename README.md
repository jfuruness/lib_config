# lib\_config
This package contains helper functions for accessing a config file. Basically a wrapper for [the default Raw Config Parser](https://docs.python.org/3/library/configparser.html)

* [lib\_config](#lib_config)
* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Credits](#credits)
* [Licence](#license)

## Package Description
* [lib\_config](#lib_config)

This package contains wrapper functions useful for accessing credentials for various services. Utilizes [the default Raw Config Parser](https://docs.python.org/3/library/configparser.html)


## Usage
* [lib\_config](#lib_config)

```python
from lib_config import Config
# This is used as a context manager, which returns a dict to write to
# Default path is /etc/config/main.ini
with Config() as conf_dict:
	conf_dict["db"] = {"password": "test", "port": 5432}
# When context manager is over, the config is written

# To use without writing, with a different config path:
with Config(write=False, path="/tmp/conf.ini") as conf_dict:
	print(conf_dict["db"]["port"])
```

Config file format is as follows:
```
[db]
password = test
port = 5432
```

## Installation
* [lib\_config](#lib_config)

The base path starts with /etc, but any OS can use it if you specify the path

Install python and pip if you have not already. Then run:

```bash
pip3 install lib_config
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:
```bash
git clone https://github.com/jfuruness/lib_config.git
cd lib_config
python3 setup.py develop
```

To test the development package: [Testing](#testing)


## Testing
* [lib\_config](#lib_config)

You can test the package if in development by moving/cd into the directory where setup.py is located and running:
(Note that you must have all dependencies installed first)
```python3 setup.py test```

To test from pip install:
```bash
pip3 install wheel
# janky but whatever. Done to install deps
pip3 install lib_config
pip3 uninstall lib_config
pip3 install lib_config --install-option test
```

## Development/Contributing
* [lib\_config](#lib_config)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Email me at jfuruness@gmail.com because idk how to even check those messages

## History
* [lib\_config](#lib_config)
* 0.2.0 Changed config structure
* 0.1.2 Fixed deps
* 0.1.1 Deps update
* 0.1.0 First production release

## Credits
* [lib\_config](#lib_config)

Credits to Drew Monroe and the UITS team for inspiring this library.

## License
* [lib\_config](#lib_config)

BSD License (see license file)
