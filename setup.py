from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='gifmaker',
    version='0.1',
    author='Julien Cohen-Adad',
    author_email='jcohen@polymtl.ca',
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
