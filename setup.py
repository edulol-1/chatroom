from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='chatroom',
    version='0.1dev0',
    author='Eduardo Montano Gomez', 
    author_email='edu3000@gmail.com',
    packages=find_packages(),
    long_description=open('README.md').read()
)
