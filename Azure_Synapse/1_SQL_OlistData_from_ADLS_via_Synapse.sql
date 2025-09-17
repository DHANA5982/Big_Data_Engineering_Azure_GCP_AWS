SELECT TOP 100 *
FROM OPENROWSET(
    BULK 'https://storageaccountolistecomm.dfs.core.windows.net/olistdatacontainer/CleanedData/',
    FORMAT = 'PARQUET'
) AS result1

---https://storageaccountolistecomm.blob.core.windows.net/olistdatacontainer/CleanedData/_SUCCESS