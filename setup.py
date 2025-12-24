from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    
    requirements = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                req = line.strip()
                if req and req != "-e .":
                    requirements.append(req)

    except FileNotFoundError:
        raise FileNotFoundError("requirements.txt file not found")

    return requirements


setup(
    name="travel-agent",  
    version="0.0.1",
    author="Parth",
    author_email="parth00221@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
