#!/usr/bin/env python
""" CSSTidy, tidies up your css """

from setuptools import setup
from setuptools.command.install import install as _install
import subprocess


class install(_install):
    """ Extends default installation class to run script after install """

    def run(self):
        _install.run(self)
        subprocess.call(['scons', '-C ./csstidy'])

setup(name='csstidy',
      version='1.4',
      description='Package to tidy up css and optimize the selectors',
      url='https://github.com/froont/CSSTidy',
      author='Florian Schmitz, Thierry Charbonnel, Will Mitchell',
      author_email='hello@froont.com',
      license='GPL',
      # scons commented out for now, because it of errors in pip install
      # install_requires=['scons'],
      package_data={'':[
        'source/*.cpp',
        'source/*.hpp',
        'source/*.h',
        'source/*.rc',
        'AUTHORS',
        'BUGS',
        'ChangeLog',
        'COPYING',
        'INSTALL',
        'NEWS',
        'REDME',
        'SConstruct',
        'TODO',
        'csstidy/*'
      ]},
      packages=['csstidy'],
      cmdclass={'install': install},
      zip_safe=True)
