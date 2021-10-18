#!/usr/bin/env python
#                   ,*++++++*,                ,*++++++*,
#                *++.        .+++          *++.        .++*
#              *+*     ,++++*   *+*      *+*   ,++++,     *+*
#             ,+,   .++++++++++* ,++,,,,*+, ,++++++++++.   *+,
#             *+.  .++++++++++++..++    *+.,++++++++++++.  .+*
#             .+*   ++++++++++++.*+,    .+*.++++++++++++   *+,
#              .++   *++++++++* ++,      .++.*++++++++*   ++,
#               ,+++*.    . .*++,          ,++*.      .*+++*
#              *+,   .,*++**.                  .**++**.   ,+*
#             .+*                                          *+,
#             *+.                   Coqui                  .+*
#             *+*              +++ Trainer +++             *+*
#             .+++*.            .          .             *+++.
#              ,+* *+++*...                       ...*+++* *+,
#               .++.    .""""+++++++****+++++++"""".     ++.
#                 ,++.              ****              .++,
#                   .++*                            *++.
#                       *+++,                  ,+++*
#                           .,*++++::::::++++*,.
#


import os
import subprocess
import sys
from distutils.version import LooseVersion

import numpy
import setuptools.command.build_py
import setuptools.command.develop
from setuptools import find_packages, setup

if LooseVersion(sys.version) < LooseVersion("3.6") or LooseVersion(
    sys.version
) > LooseVersion("3.10"):
    raise RuntimeError(
        "Coqui-Trainer requires python >= 3.6 and <=3.10 "
        "but your Python version is {}".format(sys.version)
    )


cwd = os.path.dirname(os.path.abspath(__file__))

cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "trainer", "VERSION")) as fin:
    version = fin.read().strip()


class build_py(
    setuptools.command.build_py.build_py
):  # pylint: disable=too-many-ancestors
    def run(self):
        setuptools.command.build_py.build_py.run(self)


class develop(setuptools.command.develop.develop):
    def run(self):
        setuptools.command.develop.develop.run(self)


# The documentation for this feature is in server/README.md


def pip_install(package_name):
    subprocess.call([sys.executable, "-m", "pip", "install", package_name])


requirements = open(os.path.join(cwd, "requirements.txt"), "r").readlines()

with open("README.md", "r", encoding="utf-8") as readme_file:
    README = readme_file.read()

setup(
    name="Trainer",
    version=version,
    url="https://github.com/coqui-ai/Trainer",
    author="Eren Gölge",
    author_email="egolge@coqui.ai",
    description="General purpose model trainer that is more flexible than it should be, by 🐸Coqui.",
    long_description=README,
    long_description_content_type="text/markdown",
    license="Apache2",
    include_dirs=numpy.get_include(),
    # package
    include_package_data=True,
    packages=find_packages(include=["TTS*"]),
    package_data={
        "Trainer": [
            "VERSION",
        ]
    },
    project_urls={
        "Documentation": "https://github.com/coqui-ai/Wav2Tech/wiki",
        "Tracker": "https://github.com/coqui-ai/Wav2Tech/issues",
        "Repository": "https://github.com/coqui-ai/Wav2Tech",
        "Discussions": "https://github.com/coqui-ai/Wav2Tech/discussions",
    },
    cmdclass={
        "build_py": build_py,
        "develop": develop,
    },
    install_requires=requirements,
    python_requires=">=3.6.0, <3.10",
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Development Status :: 4 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    zip_safe=False,
)