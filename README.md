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

4. OCI-21500: internal error code, arguments: [kgepop: no error frame to pop to], [], [], [], [], [], [], []

## benchmark

POSTGRESQL

- debug mode

```bash
wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/postgres --latency
Running 30s test @ http://localhost:8080/v1/postgres
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   331.20ms  375.54ms   1.66s    89.50%
    Req/Sec   353.90     43.99   404.00     41.81%
  Latency Distribution
     50%   58.65ms
     75%  565.46ms
     90%  995.39ms
     99%    1.59s
  10560 requests in 30.02s, 410.55MB read
  Socket errors: connect 0, read 0, write 0, timeout 390
Requests/sec:    351.75
Transfer/sec:     13.68MB

```

- production mode

```bash
wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/postgres --latency
Running 30s test @ http://localhost:8080/v1/postgres
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   153.21ms  246.77ms   2.00s    88.55%
    Req/Sec     2.90k   195.28     3.13k    93.33%
  Latency Distribution
     50%   28.93ms
     75%  161.37ms
     90%  452.75ms
     99%    1.21s
  86557 requests in 30.01s, 1.67GB read
  Socket errors: connect 0, read 0, write 0, timeout 43
Requests/sec:   2884.25
Transfer/sec:     57.12MB

```
