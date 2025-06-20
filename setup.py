from setuptools import setup, find_packages

setup(
    name='pyvectors',  # unique PyPI name (check if available)
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # dependencies
    author='Rustam Singh Bhadouriya',
    author_email='rustamsinghbhadouriya7@gmail.com',
    description='Custom vector class like C++ STL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Developers-of-development/Vectors-in-python',  # GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
