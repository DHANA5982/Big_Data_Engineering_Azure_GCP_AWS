USE OlistDB;

CREATE EXTERNAL FILE FORMAT extFileFormat WITH (
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
);

CREATE EXTERNAL DATA SOURCE goldLayer WITH (
    LOCATION = 'https://storageaccountolistecomm.blob.core.windows.net/olistdatacontainer/FinalAggregatedData/',
    CREDENTIAL = AdminSekar
);

-- https://storageaccountolistecomm.blob.core.windows.net/olistdatacontainer/CleanedData/_SUCCESS

CREATE SCHEMA adlsGold;

CREATE EXTERNAL TABLE adlsGold.finalTable WITH (
    LOCATION = 'finalServing',
    DATA_SOURCE = goldLayer,
    FILE_FORMAT = extFileFormat
) AS
SELECT *
FROM 
    OPENROWSET(
        BULK 'https://storageaccountolistecomm.blob.core.windows.net/olistdatacontainer/CleanedData/',
        FORMAT = 'PARQUET'
    ) AS result3;