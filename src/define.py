# coding=utf-8
import os
import glob
import sys

import yaml


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCE_PATH = PROJECT_ROOT + '/resources'
SWAGGER_PATH = PROJECT_ROOT + '/swagger'
TEMPLATES_PATH = RESOURCE_PATH + '/templates'
STATIC_PATH = RESOURCE_PATH + '/static'


if sys.version >= '3':
    PY3 = True
    load_yaml = yaml.full_load
else:
    PY3 = False
    load_yaml = yaml.load


def list_swagger_files():
    paths = glob.glob(SWAGGER_PATH + '/*.yaml')
    excluded_names = {
        '_metadata',
        '_parameters',
        '_definitions',
    }
    names = [
        path.split('swagger/')[1].split('.yaml')[0]
        for path in paths]
    names = [
        n for n in names
        if n not in excluded_names]
    return sorted(names)
