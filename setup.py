from setuptools import setup
import platform

version = '0.0.1'
packages = [
        'configuration',
        ]
install_requires = [
        ]

setup(
    name='py-configuration',
    version=version,
    packages=packages,
    license='MasTec proprietary',
    url='http://www.mastec.com/',
    author='Bob Uhl',
    author_email='robert.uhl@mastec.com',
    install_requires=install_requires,
    )
