import sys


def test_version():
    system_major = sys.version_info.major
    required_major = 3

    assert system_major == required_major, \
        "This project requires Python {}. Found: Python {}".format(required_major, sys.version)
