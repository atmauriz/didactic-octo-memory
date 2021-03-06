import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testfolder-atmauriz",  # Replace with your own username
    version="0.0.6",
    author="Maurizio Bussi",
    author_email="maurizio.bussi.mb@gmail.com",
    description="Python Test Automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atmauriz/didactic-octo-memory",
    project_urls={
        "Bug Tracker": "https://github.com/atmauriz/didactic-octo-memory/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
