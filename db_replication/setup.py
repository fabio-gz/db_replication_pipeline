from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster",
        "pandas",
        "dagster-embedded-elt",
        
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
