import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strawberry_py", # Replace with your own username
    version="0.0.1",
    author="Hobart2967",
    author_email="hobart@codewyre.net",
    description="REST Api Framework for serverless environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hobart2967/strawberry-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)