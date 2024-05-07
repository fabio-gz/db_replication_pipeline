from dagster_embedded_elt.sling.resources import SlingConnectionResource, SlingResource
from dagster import EnvVar


sling_resource = SlingResource(
    connections=[
        SlingConnectionResource(
            name="MY_POSTGRES",
            type="postgres",
            host=EnvVar("POSTGRES_HOST"),
            port=EnvVar("POSTGRES_PORT"),
            database=EnvVar("POSTGRES_DATABASE"),
            user=EnvVar("POSTGRES_USER"),
            password=EnvVar("POSTGRES_PASSWORD")
        ),
        SlingConnectionResource(
            name="MY_BIGQUERY",
            type="bigquery",
            dataset=EnvVar("BQ_DATASET"),
            key_file=EnvVar("KEY_FILE")
        )
    ]
)