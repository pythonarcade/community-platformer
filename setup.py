from setuptools import setup

exec(open("platformer/version.py").read())
setup(version=__version__)
