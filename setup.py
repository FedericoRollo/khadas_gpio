from setuptools import setup, find_packages

package_name = 'khadas_gpio'

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[],
    install_requires=[],
    zip_safe=True,
    url='https://github.com/FedericoRollo/khadas_gpio.git',
    maintainer='Federico Rollo',
    maintainer_email='rollo.f96@gmail.com',
    description='This package contains functions useful for GPIO usage on khadas vim boards using python',
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
