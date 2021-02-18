from setuptools import setup, find_packages

setup(
    name='MassRecon',
    version='0.1.0',
    url='https://github.com/VMBoehm/MassRecon',
    author='Vanessa Boehm',
    description='PAE code for lensing data',
    packages=find_packages(),
    install_requires=['tensorflow_datasets', 'astropy', 'numpy'],
)


