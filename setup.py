from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Pavan',
    author_email='pavanpolagani2505@gmail.com',
    packages=find_packages(),
    intall_requires=get_requirements('requirements.txt')
)