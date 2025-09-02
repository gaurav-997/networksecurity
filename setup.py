"""
setup.py is used for packaging and distributing the python project.
It is used by setuptools to define the configuration of your project
such as metadata, dependencies, and more.
"""

from setuptools import find_packages, setup
from pathlib import Path
from typing import List


def get_requirements() -> List[str]:
    requirements_file = Path(__file__).parent.parent / "requirments.txt"
    requirements: List[str] = []
    try:
        with open(requirements_file, "r") as f:
            for line in f:
                req = line.strip()
                # ignore empty lines, extra spaces, and editable installs
                if req and not req.startswith("-e"):
                    requirements.append(req)
    except FileNotFoundError:
        print(f"{requirements_file} not found")
    return requirements

print(get_requirements())

# setup metadata
setup(
    name="cybersecurity_ds_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements(),
)
