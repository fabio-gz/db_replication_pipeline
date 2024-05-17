{{
    config(
        materialized="table",
        alias="person_data",
        schema="analytics"
    )
}}

SELECT 
    p.persontype,
    p.namestyle,
    p.title,
    CONCAT(p.firstname, ' ', p.lastname) as name,

FROM {{source('person', 'person')}} as p