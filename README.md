# cx_oracle_vs_asyncpg

bench tests

## env variables .env file

```bash
SWAGGER_DOCS=1
DB_SERVER_PSQL=db-postgres
DB_SERVER_OSQL=db-oracle
#DB_SERVER_PSQL=localhost
#DB_SERVER_OSQL=localhost
DB_O_USER=system
DB_P_USER=postgres
DB_PASSWORD=oracle
DB_NAME=benchx
DB_POOL_SIZE=10
LD_LIBRARY_PATH=/opt/oracle/instantclient_19_8
```

## problems with oracle

1. its impossible to import big text in oracle easily

   ```bash
   db-oracle_1    | SP2-0027: Input is too long (> 2499 characters) - line ignored
   ```

2. needs to load lib paths before run the api

    ```bash
    export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_8/
    ```

3. does not have a `TEXT` data type ... the close is CLOB
