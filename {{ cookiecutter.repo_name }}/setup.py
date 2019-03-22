from setuptools import find_packages, setup
from pathlib import Path


# Read __version__ programmatically to avoid loading dependencies from src/__init__.py
dir = Path(__file__).resolve().parent

exec(open(dir / 'src/__version__.py').read())

setup(
    name='src',
    packages=find_packages(),
    version=__version__,
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
)
