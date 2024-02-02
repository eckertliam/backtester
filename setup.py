from setuptools import setup

setup(
    name='backtester',
    version='0.1',
    description='a simple backtester for bitcoin',
    author='Liam Eckert',
    license='Apache License 2.0',
    packages=['backtester'],
    install_requires=[
        'pandas',
        'backtrader'
    ])