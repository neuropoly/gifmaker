from setuptools import setup, find_packages

import gifmaker as gm

with open('requirements.txt') as f:
    requirements = f.readlines()

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='gifmaker',
    version=gm.__version__,
    author=gm.__author__,
    author_email=gm.__email__,
    packages=find_packages(),
    url='',
    license='LICENSE',
    description='Convert a series of images into a gif animation.',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'gifmaker = gifmaker.gifmaker:main',
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.5',
    )
