"""setup"""
import os
from setuptools import setup

def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as fp:
        return fp.read()

setup(
    name='ip-lookup',
    version='1.3',
    py_modules=['lookup'],
    platforms='any',
    license='MIT',
    author='Dominic Egginton',
    url='https://github.com/dominicegginton/lookup',
    author_email='dominic.egginton@gmail.com',
    description='IP lookup via the command line',
    long_description=read_file('README.md'),
    keywords='ip lookup ping tracerout',
    entry_points={
        'console_scripts': [
            'lookup = lookup:main',
        ]
    },
    install_requires=[
        'requests',
        'colorama'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
