from setuptools import find_packages,setup

setup(name="e-commerce-bot",
       version="0.0.1",
       author="suman",
       author_email="svemula520@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])