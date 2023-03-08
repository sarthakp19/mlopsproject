from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requiements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[i.replace('\n',"") for i in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
name='mlproject',
version ='0.0.1',
author='sarthak',
author_email='sarthakparande19@gmail.com',
pakages=find_packages(),
install_requires=get_requirements('requirements.txt')
)