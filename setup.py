# // this will act as a program which will convert my entire ML project to a package whcih can be used for other ml projects

from setuptools import find_packages,setup
# //acts as a metadata
from typing import List
HYPHEN_NOT='-e .'
# //this HYPHEN_NOT should only be in REQUIREMENTS.TXT SO THAT IT CAN AUTOMATICALLY TRIGGER SETUP.TXT 

def get_requirements(file_path:str)->List[str]:
    # //file path is a string and it will return a list and for that i imported list from typing
    '''
    this fucntion will return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # //it will read the requirements.txt line by line but as it is different lines hence that space is added in form of \n
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPHEN_NOT in requirements:
            requirements.remove(HYPHEN_NOT)
    return requirements 
       
setup(
name='mlproject',
version='0.0.1',
author='Anirudh',
author_email='anirudhsanthosh1731@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') 

# //ACCEPTS ONLY LIST HENCE GET REQUIREMENTS WILL RETURN LIST
)


# /// SO THIS WILL INSTALL ALL THE REQUIRED FILES /