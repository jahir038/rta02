from setuptools import find_packages,setup


def get_requirements(file_path):
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    
    return requirements

setup(
name='RTA02',
version='0.0.1',
author='Jahir',
author_email='iamjahirhussain@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
