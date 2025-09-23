USE OlistDB;

CREATE SCHEMA adlsSilver;

CREATE VIEW adlsSilver.finalTable
AS
SELECT *
FROM
    OPENROWSET(
        BULK 'https://storageaccountolistecomm.blob.core.windows.net/olistdatacontainer/CleanedData/',
        FORMAT = 'PARQUET'
    ) AS result2;