from setuptools import setup, find_packages

with open("ReadME.md", "r", encoding="utf-8") as f:
    long_description = f.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setup(
    name="genpass",
    version="0.0.1",
    author="Ford Pickert",
    author_email="fordpickert@gmail.com",
    license="MIT",
    description="Simple password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    py_modules=["genpass", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        genpass=genpass:cli
        '''
)
