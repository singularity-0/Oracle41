"""
Module packaging: Oracle.
"""

from setuptools import setup, find_packages

setup(
    name='Oracle',
    description='Backup / rebuild of annwn',
    long_description=open('README.md').read(),

    license='MIT',
    author='Clan Oracle',
    author_email='singularity00100@gmail.com',

    version='0.0.1-alpha',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'spec*']),
    include_package_data=True,
    install_requires=['beautifulsoup4', 'pylint'],
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
