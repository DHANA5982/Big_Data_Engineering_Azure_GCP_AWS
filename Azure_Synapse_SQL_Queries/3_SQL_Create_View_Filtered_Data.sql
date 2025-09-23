USE OlistDB;

CREATE VIEW adlsSilver.finalTableFiltered
AS
SELECT *
FROM 
    OPENROWSET(
        BULK 'https://storageaccountolistecomm.blob.core.windows.net/olistdatacontainer/CleanedData/',
        FORMAT = 'PARQUET'
    ) AS result2
WHERE order_status = 'delivered';