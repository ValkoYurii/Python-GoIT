from setuptools import setup, find_packages

setup(
    name = 'project_zeta',
    version = '1',
     entry_points={
        'console_scripts': [
                'project_zeta = project_zeta:main',
            ]
    },
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    description= 'project_zeta'
)
