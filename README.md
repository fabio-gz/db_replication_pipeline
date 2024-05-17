# Dagster replication pipeline

This repository contains a data pipeline that orchestrates table replications and transformations using Dagster, Sling, and dbt. The goal of this project is test the capabilities of the replications features to ensure correct data movement from a Postgres database to BigQuery


## Features

-   **Orchestration with Dagster**: Use Dagster to define the data pipelines.
-   **Table Replications with Sling**: Leverage Dagster embedded-etl using sling to replicate tables
-   **Transformations with dbt**: Use dbt for simple data transformations.

## Usage

Create a virtual env with the requirements file, then run the project with: 

	dagster dev