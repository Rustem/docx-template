import codecs
import os
import re
from setuptools import setup, find_packages

def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

install_requires = []
with open('requires.txt', 'r') as fh:
    install_requires = map(lambda s: s.strip(), filter(
        lambda l: not l.startswith('-e'), fh.readlines()))

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = """

"""

setup(name="docx_template",
      version=find_version('docx', '__init__.py'),
      description="Working with docx document.",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
      ],
      keywords='django tornado common mobiliuz constants',
      author='Almacloud',
      author_email='r.kamun@gmail.com',
      url = 'https://github.com/Rustem/docx-template.git',
      license='MIT',
      packages=find_packages(),
      install_requires=install_requires,
      zip_safe=False,
      )
