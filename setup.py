from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jail-scraper",
    version="0.0.1",
    keywords="jail, scraper, data",
    license="GPLv3",
    author="Guthrie McAfee Armstrong",
    author_email="guthrie.armstrong@gmail.com",
    description="Web scraper for the county jails of Georgia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3"
        "Topic :: Internet :: WWW/HTTP"
        ],
    install_requires=[
        "requests"
        ]
)
