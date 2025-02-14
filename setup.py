from setuptools import find_packages, setup

from typing import List


HYPHEN_E_DOT='-e .'


def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requiremets=[]
    with open(file_path,'r') as file:
        requiremets=file.readlines()
        requiremets=[req.replace("\n"," ") for req in requiremets]
        
        if HYPHEN_E_DOT in requiremets:
            requiremets.remove(HYPHEN_E_DOT)
    return requiremets










setup(
    name='ML_project',
    version='0.1',
    author='RAJ KUMAR',
    author_email='raj05896@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)

