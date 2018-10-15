from setuptools import setup

setup(
    name = 'nightowlcli',
    version = '0.1.0',
    packages = ['nightowlcli'],
    entry_points = {
        'console_scripts': [
            'nightowlcli = nightowlcli.__main__:main'
        ]
    })
