from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in projectfu/__init__.py
from projectfu import __version__ as version

setup(
	name="projectfu",
	version=version,
	description="this is a project for foss united",
	author="mangesh",
	author_email="mangeshrex@tutanota.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
