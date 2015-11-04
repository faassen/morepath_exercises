from setuptools import setup, find_packages

setup(
    name='do_nothing',
    version='0.1.dev0',
    description="Morepath Do Nothing Exercise",
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
            'start = do_nothing.main:main',
        ]
    },
)
