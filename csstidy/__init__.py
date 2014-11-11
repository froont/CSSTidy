#!/usr/bin/env python
""" CSSTidy, tidies up your css """

import sys
import os
import subprocess

__version__ = '1.4'


def _get_executable_name():
    """ Returns the full path to CSSTidy executable """
    filename = 'csstidy'
    this_dir = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(this_dir, filename, filename)


def csstidy(soruce_file, output_file=None, **args):
    """ Tidies up your CSS and returns it or writes to file

    :param source_file: path to file to be tidied up
    :param output_file: path to output file or None to return
    :return: if no output_file passed  returns css string
    """

    # Default setting is first in the value list
    settings = {
        'allow_html_in_templates': [False, True],
        'compress_colors': [True, False],
        'compress_font-weight': [True, False],
        'discard_invalid_properties': [False, True],
        'lowercase_s': [False, True],
        'preserve_css': [False, True],
        'remove_bslash': [True, False],
        'remove_last_;': [False, True],
        'silent': [True, False],
        'sort_properties': [True, False],
        'sort_selectors': [True, False],
        'timestamp': [False, True],
        'merge_selectors': [2, 1, 0],
        'case_properties': [0, 1, 2],
        'optimise_shorthands': [1, 2, 0],
        'template': ['low', 'default', 'filename', 'high', 'highest']
    }

    # Applying settings
    arguments = [_get_executable_name(), soruce_file]

    for setting, val in settings.iteritems():
        arg_val = str(args[setting]).lower() \
            if setting in args and args[setting] in val \
            else str(val[0]).lower()
        arguments.append("--%s=%s" % (setting, arg_val))

    if output_file:
        arguments.append(soruce_file)
        return subprocess.call(arguments)

    return subprocess.check_output(arguments)
