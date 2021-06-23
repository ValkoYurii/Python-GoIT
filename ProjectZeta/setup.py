from setuptools import setup, find_packages

setup(
    name = 'projectcli',
    version = '1',
     entry_points={
        'console_scripts': [
                'projectcli = projectcli:main',
            ]
    },
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    description= 'projectcli'
)