import setuptools

# setuptools is a package used by many other packages to handle their installation from source code (and tasks related to that)
# This file setup.py is an extremely important file to various aspects of this jfrog assignment and it enables configuration.

with open("README.md", "r") as fh:
    #readme.md is a file that contains a short description of the project
    long_description = fh.read()

#setuptools.setup is a function that is used to configure the installation of the package
setuptools.setup(
    name="jordantingling", 
    version="1.0",
    author="Jordan Tingling",
    author_email="jordantingling@gmail.com",
    description="Jordan Tingling's submission to JFrog's Production Engineering Academy - Home Assignment", #short description of the package
    long_description=long_description, #long description of the package
    long_description_content_type="text/markdown", #long description of the package
    url= "https://testerfrog.jfrog.io/artifactory/tingling-jfrog-assignment/",
    packages=["jfrog-project"],#setuptools.find_packages() is a function that finds all the packages in the current directory
    install_requires=[
        'requests'], #install_requires is a list of packages that are required to run the package
    classifiers=[
        "Programming Language :: Python :: 3", #Python 3 is the default language for this project
        "License :: OSI Approved :: MIT License", #MIT License is the default license for this project
    ],
    python_requires='>=3.6', #Python 3.6 is the minimum version of Python that this project can run on
)