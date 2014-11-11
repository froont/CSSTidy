#!/usr/bin/env python
""" CSSTidy, tidies up your css

!!! WARNING !!!
SCons must be installed before running this!
Unfortunately SCons cannot be added to pip requirements at this time
because of SCons pip installation error!

TODO: when SCons installation error is solved, please add SCons to
      install_requires list below.
"""

from setuptools import setup
from setuptools.command.install import install as _install
import os, subprocess


class install(_install):
    """ Extends default installation class to run script after install """

    def run(self):
        install_dir = os.path.join(os.getcwd(), self.config_vars['dist_name'])
        subprocess.call(['scons', '-C' + install_dir])

        _install.run(self)


setup(name='csstidy',
      version='1.1',
      description='Package to tidy up css and optimize the selectors',
      url='https://github.com/froont/CSSTidy',
      author='Florian Schmitz, Thierry Charbonnel, Will Mitchell',
      author_email='hello@froont.com',
      license='GPL',
      # scons commented out for now, because it of errors in pip install
      # install_requires=['scons'],
      package_data={'':['source/*.cpp',
                        'source/*.hpp',
                        'source/*.h',
                        'source/*.rc',
                        'source/SConscript',
                        'AUTHORS',
                        'BUGS',
                        'ChangeLog',
                        'COPYING',
                        'INSTALL',
                        'NEWS',
                        'REDME',
                        'SConstruct',
                        'TODO',
                        'csstidy/*.o',
                        'csstidy/csstidy',
                        '.sconsign.dblite']},
      packages=['csstidy'],
      cmdclass={'install': install},
      zip_safe=False)
