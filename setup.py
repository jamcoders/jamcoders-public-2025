from setuptools import setup, find_packages

setup(
    name='jamcoders',
    version='2024.0.1',
    author='Jamcoders TAs',
    author_email='orrp@jamcoders.org.jm',
    description='Utilities for JamCoders',
    packages=find_packages(),
    install_requires=[
        'termcolor',
    ],
)
