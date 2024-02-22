from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))
# Get the long description from the README file
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.2.0'
DESCRIPTION = 'A simple DNA sequence translator'

# Setting up
setup(
    name="nctranslator",
    version=VERSION,
    author="Karthikeyan Velayudhapani",
    author_email="karthikeyan.vpani@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nctranslator = nctranslator.nctranslator:main'
        ]
    },
    install_requires=["biopython"],
    keywords=['python', 'DNA', 'sequence', 'translator'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
# Compare this snippet from nctranslator/__init__.py:
