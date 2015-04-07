from setuptools import setup
import platform

version = '1.0.0'
packages = [
        'configuration',
        ]
install_requires = [
        ]

setup(
    name='py-configuration',
    version=version,
    packages=packages,
    license='LGPL',
    url='http://www.mastec.com/',
    author='Bob Uhl',
    author_email='robert.uhl@mastec.com',
    install_requires=install_requires,
    )
