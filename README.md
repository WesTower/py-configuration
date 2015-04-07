py-configuration
================

A simple little library intended to abstract away various means of
setting configuration (e.g. environment variables, YAML/JSON/.ini
files, configuration dæmons &c.).  Currently, only environment
variables are supported, as those were all that we needed.

Usage
-----

    import configuration
    settings = configuration.EnvironmentSettings(a_mandatory_setting='SOME_ENV_VAR',
                                                 an_optional_setting={'name': 'ANOTHER_VAR,
                                                                      'mandatory': False}
                                                 a_defaulted_setting={'name'='A_THIRD_VAR',
                                                                      'default'='defaulted',
                                                                      'mandatory': False})

In actual use, we only ever really bothered with the mandatory
settings.
