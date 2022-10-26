#!/usr/bin/env python

from setuptools import setup, find_packages

import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_parameter(name="PROJECT_NAME"):
    with open("config.mk") as fp:
        for line in fp:
            fline = line[:-1].split("=")
            if len(fline) == 2 and name == fline[0]:
                return fline[1]


def get_version():
    for filename in [f"{get_parameter()}/{f}" for f in ["__version__.py", "__init__.py"]]:
        if os.path.exists(filename):
            for line in read(filename).splitlines():
                if line.startswith("__version__"):
                    delim = '"' if '"' in line else "'"
                    return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


def get_console_scripts():
    scripts = []
    with open("config.mk") as fp:
        for line in fp:
            fline = line[:-1].split("=")
            if len(fline) == 2 and "SCRIPT:" in fline[0]:
                scripts.append(line[7:-1])
    return scripts


print(find_packages())

setup(
    # name=get_parameter(),
    name="hpcgpu",
    version=get_version(),
    author="Guillaume Therin",
    author_email="guillaume@therin.co",
    # packages=find_packages(),
    py_modules=[
        "magic_plugin",
        "v2.v2",
        "v1.v1",
        "common.helper",
        "hpcourse.hpcourse",
        "hpcourse.hpcourse3",
        "hpcourse.magics",
    ],
    # Dependencies
    install_requires=["pandas"],  # "thop"
    # Script info
    # entry_points={"console_scripts": get_console_scripts()},
    url="https://github.com/guydegnol/hpcgpu_course",
    license="LICENSE",
    description="Course on HPC with CUDA",
    # description='Jupyter notebook plugin to run CUDA C/C++ code',
    # long_description=open('README.md').read(),
)
