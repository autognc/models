from setuptools import setup, find_packages
import os

setup(
    name='deeplab',
    version='0.0.1',
    description='Tensorflow deeplab semantic segmentation',
    package_dir={'deeplab': '.'},
    packages=['deeplab'] + ['deeplab.' + p for p in find_packages()],
    install_requires=[
        'tensorflow>=1.12.0',
        'pillow',
        'jupyter',
        'matplotlib',
        'slim@git+https://github.com/autognc/models#subdirectory=research/slim'
    ])
