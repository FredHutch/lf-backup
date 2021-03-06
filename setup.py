from setuptools import setup
import codecs

__version__ = "0.4.5"

#try:
#    from pypandoc import convert
#    read_md = lambda f: convert(f, 'rst')
#except ImportError:
#    print("warning: pypandoc module not found, could not convert Markdown to RST")
#    read_md = lambda f: open(f, 'r').read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Customer Service",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Information Technology",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX",
    "Operating System :: POSIX :: Linux",
    "Operating System :: POSIX :: Other",
    "Operating System :: Unix",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Unix Shell",
    "Topic :: Desktop Environment :: File Managers",
    "Topic :: Internet",
    "Topic :: System :: Archiving",
    "Topic :: System :: Archiving :: Backup",
    "Topic :: System :: Filesystems",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities"
]

setup(
    name='lf-backup',
    version=__version__,
    description='''\
lf-backup is a tool for backing up large files to object storage
, e.g. swift.''',
    long_description=codecs.open('README.rst', 'r').read(),
    packages=['lf_backup'],
    scripts=['lf_backup/lf-backup'],
    author = 'Jeff Katcher',
    author_email = 'dp@nowhere.com',
    url = 'https://github.com/FredHutch/lf-backup', 
    download_url = 'https://github.com/FredHutch/lf-backup/tarball/%s' % __version__,
    keywords = ['openstack', 'swift', 'cloud storage'], # arbitrary keywords
    classifiers = CLASSIFIERS,
    # 'python-swiftclient>=2.5,<3','python-keystoneclient>=1.5,<2'
    install_requires=[
        'python-swiftclient>=3.2.0',
        'python-keystoneclient>=2,<3',
        'psycopg2>=2.6'
        ],
    entry_points={
        # we use console_scripts here to allow virtualenv to rewrite shebangs
        # to point to appropriate python and allow experimental python 2.X
        # support.
        'console_scripts': [
            'lfbackup.py=lf_backup.lfbackup:main',
        ]
    }
)
