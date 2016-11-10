backtrace
=========

[![Travis Build Status](https://travis-ci.org/nir0s/backtrace.svg?branch=master)](https://travis-ci.org/nir0s/backtrace)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/kuf0x8j62kts1bpg/branch/master?svg=true)](https://ci.appveyor.com/project/nir0s/backtrace)
[![PyPI Version](http://img.shields.io/pypi/v/backtrace.svg)](http://img.shields.io/pypi/v/backtrace.svg)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/backtrace.svg)](https://img.shields.io/pypi/pyversions/backtrace.svg)
[![Requirements Status](https://requires.io/github/nir0s/backtrace/requirements.svg?branch=master)](https://requires.io/github/nir0s/backtrace/requirements/?branch=master)
[![Code Coverage](https://codecov.io/github/nir0s/backtrace/coverage.svg?branch=master)](https://codecov.io/github/nir0s/backtrace?branch=master)
[![Code Quality](https://landscape.io/github/nir0s/backtrace/master/landscape.svg?style=flat)](https://landscape.io/github/nir0s/backtrace)
[![Is Wheel](https://img.shields.io/pypi/wheel/backtrace.svg?style=flat)](https://pypi.python.org/pypi/backtrace)

Backtrace manipulates Python tracebacks to make them more readable.
It provides different configuration options for coloring and formatting.


## Alternatives

* [colored_traceback]()


## Installation

backtrace supports Linux, Windows and OSX on Python 2.6, 2.7 and 3.4+

```shell
pip install backtrace
```

For dev:

```shell
pip install https://github.com/nir0s/backtrace/archive/master.tar.gz
```

## Usage

backtrace provides two methods for manipulating your tracebacks.

* Piping to backtrace using its CLI
* Using backtrace from within your code


### Piping

```bash
$ backtrace
Usage: ghost [OPTIONS] COMMAND [ARGS]...

  Ghost generates a secret-store in which you can keep your secrets
  encrypted. Ghost isn't real. It's just in your head.

Options:
  -h, --help  Show this message and exit.

Commands:
  delete   Delete a key from the stash
  export   Export all keys to a file
  get      Retrieve a key from the stash
  init     Init a stash
  list     List all keys in the stash
  load     Load all keys from an exported key file to...
  migrate  Migrate all keys from a source stash to a...
  purge    Purge the stash from all of its keys
  put      Insert a key to the stash


$ python my-program.py | backtrace
```

### Inside your application

```python
import backtrace

backtrace.rehook()


```

## Testing

```shell
git clone git@github.com:nir0s/backtrace.git
cd backtrace
pip install tox
tox
```

## Contributions..

See [CONTRIBUTIONS](https://github.com/nir0s/backtrace/blob/master/CONTRIBUTING.md)

Pull requests are always welcome..
