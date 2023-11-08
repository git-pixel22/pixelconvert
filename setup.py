import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="pixelconvert",
    version="0.0.1",
    author="pixel22",
    author_email="workemail.rajat@gmail.com",
    description=("A cli tool to convert a file from one format to another"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/git-pixel22/pixelconvert",
    project_urls={
        "Bug Tracker": "https://github.com/git-pixel22/pixelconvert/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["Pillow", "pdf2docx"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pixelconvert = pixelconvert.main:main",
        ]
    }
)