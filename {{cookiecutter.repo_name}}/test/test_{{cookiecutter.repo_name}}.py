""" Test suite for the {{ cookiecutter.app_name }} application.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the package is actually
being tested. If the package is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from yaml import dump

import pytest


def test_version():
    """ Test the application version.

    """
    from {{ cookiecutter.app_name }} import __version__
    assert "{{ cookiecutter.project_version }}" == __version__
    return


def test_main():
    """ Test the main entry point.

    """
    from {{ cookiecutter.app_name }} import main
    with pytest.raises(NotImplementedError):
        main()
    return


def test_cli():
    """ Test the cli module.

    """
    from {{ cookiecutter.app_name }}.cli import main
    with pytest.raises(NotImplementedError):
        main()
    return


def test_gui():
    """ Test the gui module.

    """
    from {{ cookiecutter.app_name }}.gui import main
    with pytest.raises(NotImplementedError):
        main()
    return


def test_web():
    """ Test the web module.

    """
    from {{ cookiecutter.app_name }}.web import main
    with pytest.raises(NotImplementedError):
        main()
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))
