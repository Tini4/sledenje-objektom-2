from setuptools import setup, find_packages

setup(
    name="sledenje-objektom-2",
    version="0.0.12",
    description="sledenje-objektom-2",
    url="git@github.com:RoboLiga/sledenje-objektom-2.git",
    author="Jakob Maležič",
    author_email="jakob.malezic@gmail.com",
    license="unlicense",
    packages=find_packages(),
    install_requires=[
        'opencv-contrib-python==4.7.0.68',
        'numpy==1.24.1',
    ],
    zip_safe=False
)
