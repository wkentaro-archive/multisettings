#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import sys
import subprocess
from setuptools import setup, find_packages


# publish helper
if sys.argv[-1] == 'publish':
    for cmd in [
            'python setup.py sdist upload',
            'git tag {0}'.format(__import__('multisettings').__version__),
            'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

setup(
    name='multisettings',
    version=__import__('multisettings').__version__,
    packages=find_packages(),
    description=('Tool to handle multiple settings for editor, '
                 'shell and other command line tools.'),
    long_description=open('README.rst').read(),
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/multisettings',
    install_requires=open('requirements.txt').readlines(),
    license='MIT',
    keywords='utility',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
        ],
    entry_points={'console_scripts': ['multisettings=multisettings:main']},
)
