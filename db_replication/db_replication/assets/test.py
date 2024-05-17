from pathlib import Path

DBT_DIRECTORY = Path(__file__).joinpath("..", "..", "..", "dbt_analytics").resolve()
print(DBT_DIRECTORY)