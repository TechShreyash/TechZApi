with open("README.md", encoding="utf8") as readme:
    LONG_DESCRIPTION = readme.read()

from setuptools import setup

VERSION = "1.2.1"
DESCRIPTION = "Python wrapper for the TechZApi"

setup(
    name="techzapi",
    version=VERSION,
    license="MIT",
    author="TechShreyash",
    author_email="techshreyash123@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/TechShreyash/TechZApi",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=["techzapi"],
    install_requires=["requests"],
    keywords=[
        "API",
        "TechZApi",
        "TechZAPI",
        "TechZBots",
        "GogoAnime",
        "Anime",
        "AnimeAPI",
        "MkvCinemas",
        "MkvCinemasAPI",
        "Scrapper",
    ],
)
