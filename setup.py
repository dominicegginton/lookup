"""setup"""
from setuptools import setup

setup(
    name='ip-lookup',
    version='1.2',
    py_modules=['lookup'],
    platforms='any',
    license='MIT',
    author='Dominic Egginton',
    url='https://github.com/dominicegginton/lookup',
    author_email='dominic.egginton@gmail.com',
    description='IP lookup via the command line',
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
