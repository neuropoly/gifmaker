from setuptools import setup, find_packages

import gifmaker as gm

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='gifmaker',
    version=gm.__version__,
    author=gm.__author__,
    author_email=gm.__email__,
    packages=find_packages(),
    url='',
    license='LICENSE',
    description='Convert a series of images into a gif animation.',
    long_description=open('README.md').read(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'gifmaker = gifmaker.gifmaker:main',
            ]
        }
    )
