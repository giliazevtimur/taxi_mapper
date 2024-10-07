from setuptools import setup, find_packages

setup(
    name="taxi_mapper",
    version="0.1",
    packages=find_packages(),
    install_requires=["osmnx", "networkx", "shapely", "geopandas"],
    author="Timur",
    description="A taxi route mapping library using OpenStreetMap data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/timur-g/taxi_mapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
