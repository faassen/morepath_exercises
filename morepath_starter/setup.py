from setuptools import setup, find_packages

setup(
    name='morepath_starter',
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
    ],
    entry_points={
        'console_scripts': [
            'start = morepath_starter.main:main',
        ]
    },
)
