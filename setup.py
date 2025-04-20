# it is used to create a setup library types which anyone can use/install for their use
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace ("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Lakshay',
author_email='jlakshay05@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)