from pathlib import Path

from setuptools import setup, find_packages

name = 'burdenko_glioma'

with open('requirements.txt', encoding='utf-8') as file:
    requirements = file.read().splitlines()

setup(
    name=name,
    packages=find_packages(include=(name,)),
    descriprion='Burdenko Radiotherapy dataset',
    install_requires=requirements,
    python_requires='>=3.7',
)