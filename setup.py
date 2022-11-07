from setuptools import setup, find_packages
from typing import List

PROJECT_NAME="zomato-rating-prediction"
VERSION="0.0.1"
AUTHOR="Sahruday Sherla"
DESRCIPTION="This is Zomato Rating Prediction"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List:
    with open(REQUIREMENT_FILE_NAME) as requirement:
        requirement_list = requirement.readlines()
        requirement_list = [requirements.replace("/n", "") for requirements in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages= find_packages(),
    requires=get_requirements_list()

)
