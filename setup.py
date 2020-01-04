# -*- coding: utf-8 -*-

import os
import setuptools

# ======================================================================================================================
# Fill in this information for each package.
# ======================================================================================================================

AUTHOR = "Hao Xue"
EMAIL = "xuehaoperth@gmail.com"
PACKAGE_NAME = "pytp"
DESCRIPTION = "Useful Tools for Trajectory Prediction."
REPO = "https://github.com/xuehaouwa/Trajectory-Prediction-Tools"

# ======================================================================================================================
# Automatic Package Setup Script.
# ======================================================================================================================


with open("version", "r") as f:
    VERSION = f.readline()


def find_packages_under(path):
    """ Recursive list all of the packages under a specific package."""
    all_packages = setuptools.find_packages()
    packages = []
    for package in all_packages:
        package_split = package.split(".")
        if package_split[0] == path:
            packages.append(package)
    return packages


def copy_version_to_package(path):
    """ Copy the single source of truth version number into the package as well. """
    init_file = os.path.join(path, "__init__.py")
    with open(init_file, "r") as original_file:
        lines = original_file.readlines()

    with open(init_file, "w") as new_file:
        for line in lines:
            if "__version__" not in line:
                new_file.write(line)
            else:
                new_file.write("__version__ = \"{}\"\n".format(VERSION))


copy_version_to_package(PACKAGE_NAME)

setuptools.setup(
    author=AUTHOR,
    author_email=EMAIL,
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    version=VERSION,
    url=REPO,
    packages=find_packages_under(PACKAGE_NAME),
    package_dir={PACKAGE_NAME: PACKAGE_NAME},
    install_requires=[
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6"
    ],
)

# ===================================================================================================
# Upload to PyPI. Get the user and password from the environment.
# ===================================================================================================

key_repo_user = "REPO_USER"
key_repo_pass = "REPO_PASS"

if key_repo_user in os.environ and key_repo_pass in os.environ:
    repo_user = os.environ[key_repo_user]
    repo_pass = os.environ[key_repo_pass]

    with open("upload_to_pypi.sh", 'w') as f:
        f.write('#!/usr/bin/env bash\n')
        f.write('pip install twine\n')
        f.write('twine upload -u {} -p {} dist/*\n'.format(repo_user, repo_pass))

