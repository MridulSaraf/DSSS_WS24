from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    description="A math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mridul Saraf",
    author_email="sarafmridul87@gmail.com",
    url="https://github.com/MridulSaraf/DSSS_WS24/math_quiz",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
