"""
env_vars - environment-variable-based settings

settings = Settings(foo={'name': 'ENV_FOO', 
                           'default': 123,
                           'mandatory': False})
"""

import os



class MissingEnvironmentVariable(Exception):
    pass


class MalformedSpecification(Exception):
    pass


class EnvironmentSettings(object):
    def __init__(self, **specs):
        for spec in specs:
            if type(specs[spec]) == dict:
                setattr(self, spec, self._getenv(**specs[spec]))
            elif type(specs[spec]) in (str, unicode):
                setattr(self, spec, self._getenv(specs[spec]))
            else:
                raise MalformedSpecification(specs[spec])

    @classmethod
    def _getenv(self, name, default=None, mandatory=True):
        if default or not mandatory:
            return os.getenv(name, default)
        else:
            impossible_val = {'question': 'answer'}
            var = os.getenv(name, impossible_val)
            if var == impossible_val:
                raise MissingEnvironmentVariable(name)
        return var
