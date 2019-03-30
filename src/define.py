# coding=utf-8
import os
import glob

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESOURCE_PATH = PROJECT_ROOT + '/resources'
SWAGGER_PATH = PROJECT_ROOT + '/swagger'
TEMPLATES_PATH = RESOURCE_PATH + '/templates'
STATIC_PATH = RESOURCE_PATH + '/static'


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
