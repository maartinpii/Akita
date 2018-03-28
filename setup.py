import sys
import setuptools

from version import __version__ as version

if sys.version < (3, 4):
    sys.exit('Akita requires Python 3.4+')

setuptools.setup(
    name='akita',
    version=version,
    description='An HTTP log monitoring tool for your terminal',
    url='https://github.com/michael-lazar/Akita',
    author='Michael Lazar',
    author_email='lazar.michael22@gmail.com',
    license='MIT',
    keywords='http log apache nginx monitoring terminal console metrics',
    packages=['akita'],
    python_requires='python>=3.4',
    extras_require={'test': ['pytest']},  # "pip install akita[test]"
    entry_points={'console_scripts': ['akita=akita.__main__:main']},
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console :: Curses',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Terminals',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        ],
)
