from setuptools import setup, find_packages

setup(
    name='restapi',
    version='0.1.dev0',
    description="Morepath Exercise Starter",
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'morepath',
        'webtest',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'start = restapi.main:main',
        ]
    },
)
