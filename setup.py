from setuptools import setup, find_packages

setup(
    name='jamcoders-2023',
    version='1.0.0',
    author='Jamcoders',
    author_email='jamcoders@jamcoders.com',
    description='Utilities for JamCoders',
    packages=find_packages(),
    install_requires=[
        'termcolor',
    ],
)