#!/usr/bin/env python3
# MIT License. This file is part of telegram_me.
#
# Copyright (c) 2020 Hearot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import re

from setuptools import find_packages
from setuptools import setup

GITHUB_REPOSITORY = "https://github.com/hearot/telegram_me/blob/v%s/"


with open("telegram_me/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    long_description = f.read().replace("./", GITHUB_REPOSITORY % version)

with open("requirements.txt", encoding="utf-8") as r:
    requirements = [p.strip() for p in r]

setup(
    author="Hearot",
    author_email="gabriel@hearot.it",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    description="A simple scraper for getting information from t.me links",
    install_requires=requirements,
    keywords="bot bots chat messenger mtproto python telegram telegram_me me telegramme scraping",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="telegram_me",
    packages=find_packages(),
    project_urls={
        "Tracker": "https://github.com/hearot/telegram_me/issues",
        "Source": "https://github.com/hearot/telegram_me",
    },
    python_requires=">=3.6.*",
    url="https://github.com/hearot/telegram_me",
    version=version,
)
