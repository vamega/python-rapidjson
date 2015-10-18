# Copyright (c) 2015 Ken Robbins
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import os.path
import re

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

def find_version():
    with open(os.path.join(ROOT_PATH, 'python-rapidjson/version.h')) as f:
        data = f.read()

    v = re.search(r'PYTHON_RAPIDJSON_VERSION\s+(\S+)', data).group(1)
    return v.replace('"', '')

def find_author():
    with open(os.path.join(ROOT_PATH, 'python-rapidjson/version.h')) as f:
        data = f.read()

    author = re.search(r'PYTHON_RAPIDJSON_AUTHOR\s+(\S+)', data).group(1)
    email = re.search(r'PYTHON_RAPIDJSON_AUTHOR_EMAIL\s+(\S+)', data).group(1)
    return (author.replace('"', ''), email.replace('"', ''))

with open('README.rst') as f:
    long_description = f.read()

rapidjson = Extension(
    'rapidjson',
    sources=['./python-rapidjson/rapidjson.cpp'],
    include_dirs=['./thirdparty/rapidjson/include'],
    extra_compile_args=['-O3'],
)

setup(
    name='python-rapidjson',
    version=find_version(),
    description='Python wrapper around rapidjson',
    long_description=long_description,
    license='MIT License',
    keywords='json rapidjson',
    author=find_author()[0],
    author_email=find_author()[1],
    url='https://github.com/kenrobbins/python-rapidjson',
    download_url='https://github.com/kenrobbins/python-rapidjson',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ],
    ext_modules=[rapidjson],
)
