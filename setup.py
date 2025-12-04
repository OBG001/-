from setuptools import setup, find_packages

try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'A simple utility package for Discord helper functions.'

setup(
    name='obg-utilities', 
    version='0.1.0',      
    packages=find_packages(),
    description='A Discord utility package for sending messages to verified members.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='OBG',
    url='https://github.com/OBG001/-',
    install_requires=[
        'discord.py>=2.0.0', 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
