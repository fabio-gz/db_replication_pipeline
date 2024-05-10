from dagster_embedded_elt.sling.resources import SlingConnectionResource, SlingResource
from dagster import EnvVar, AssetKey


source = SlingConnectionResource(
    name="MY_POSTGRES",
    type="postgres",
    host=EnvVar("POSTGRES_HOST"),
    port=EnvVar("POSTGRES_PORT"),
    database=EnvVar("POSTGRES_DATABASE"),
    user=EnvVar("POSTGRES_USER"),
    #password=EnvVar("POSTGRES_PASSWORD")
)

target = SlingConnectionResource(
    name="MY_BIGQUERY",
    type="bigquery",
    project=EnvVar("BQ_PROJECT"),
    dataset=EnvVar("BQ_DATASET"),
    key_file=EnvVar("KEY_FILE")
)

sling = SlingResource(
    connections= [source, target]
)

replication_config = {
    "source": "MY_POSTGRES",
    "target": "MY_BIGQUERY",

    "defaults":
        {"mode": "full-refresh",
        "object": "{stream_schema}_{stream_table}"
        },

    "streams":
        {"person.address": {"object": "person"},
        "humanresources.*": {"object": "humanresources"}
        }
}

