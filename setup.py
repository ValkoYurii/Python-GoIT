from setuptools import setup, find_packages

setup(
    name = 'cleanfolder',
    version = '1',
     entry_points={
        'console_scripts': [
                'cleanfolder = cleanfolder.clean:main',
            ]
    },
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    description= 'clean folder script'
)