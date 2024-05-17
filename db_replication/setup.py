from setuptools import find_packages, setup

setup(
    name="db_replication",
    # packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster",
        "pandas",
        "dagster-embedded-elt",
        "dagster_dbt",
        "dbt-bigquery"
        
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
