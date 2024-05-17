{{
    config(
        materialized="table",
        alias="employee_clean",
        schema="analytics"
    )
}}

SELECT
    businessentityid,
    nationalidnumber,
    REPLACE(loginid, 'adventure-works\\', '') AS loginid,
    REGEXP_REPLACE(jobtitle, r' - .*', '') AS jobtitle,
    birthdate,
    maritalstatus,
    gender
FROM {{source('person', 'employee')}}