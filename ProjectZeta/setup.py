from setuptools import setup, find_packages

setup(
    name = 'ProjectZeta',
    version = '1.1',
    entry_points={'console_scripts': ['ProjectZeta = ProjectZeta:main']},
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    description= 'ProjectZeta CLI'
)