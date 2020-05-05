from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lambdata_terrainthesky35", # the name that you will install via pip
    version="1.37",
    author="Lesley Rich",
    author_email="lesley.t.rich@gmail.com",
    description="Datetimeextractor and train, val, test splitter",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/terrainthesky-hub/my_lambdata_terrainthesky35",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)