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

1 connection

- postgresql

```bash
gustavo@terminator-T2900:~$ wrk -c 1 -t 1 -d 30 http://localhost:8080/v1/postgres --latency
Running 30s test @ http://localhost:8080/v1/postgres
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.53ms  313.27us  20.25ms   98.63%
    Req/Sec   659.80     29.38   727.00     81.00%
  Latency Distribution
     50%    1.51ms
     75%    1.57ms
     90%    1.63ms
     99%    1.92ms
  19709 requests in 30.01s, 390.37MB read
Requests/sec:    656.65
Transfer/sec:     13.01MB
```

- oracle

```bash
gustavo@terminator-T2900:~$ wrk -c 1 -t 1 -d 30 http://localhost:8080/v1/oracle --latency
Running 30s test @ http://localhost:8080/v1/oracle
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.23ms  110.12us   5.26ms   73.29%
    Req/Sec   813.84     44.07     0.97k    69.00%
  Latency Distribution
     50%    1.24ms
     75%    1.30ms
     90%    1.35ms
     99%    1.50ms
  24320 requests in 30.02s, 481.70MB read
Requests/sec:    810.23
Transfer/sec:     16.05MB
```

2 connections

- postgresql

```bash
gustavo@terminator-T2900:~$ wrk -c 2 -t 1 -d 30 http://localhost:8080/v1/postgres --latency
Running 30s test @ http://localhost:8080/v1/postgres
  1 threads and 2 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.64ms  178.03us   8.22ms   84.92%
    Req/Sec     1.22k    62.89     1.36k    75.33%
  Latency Distribution
     50%    1.60ms
     75%    1.68ms
     90%    1.81ms
     99%    2.20ms
  36555 requests in 30.01s, 724.03MB read
Requests/sec:   1218.03
Transfer/sec:     24.13MB
```

- oracle

```bash
gustavo@terminator-T2900:~$ wrk -c 2 -t 1 -d 30 http://localhost:8080/v1/oracle --latency
Running 30s test @ http://localhost:8080/v1/oracle
  1 threads and 2 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.35ms  135.20us   2.50ms   74.16%
    Req/Sec     1.49k    70.66     1.65k    72.00%
  Latency Distribution
     50%    1.33ms
     75%    1.41ms
     90%    1.51ms
     99%    1.78ms
  44362 requests in 30.01s, 0.86GB read
Requests/sec:   1478.03
Transfer/sec:     29.27MB
gustavo@terminator-T2900:~$
```

200 connections

- postgres

```bash
gustavo@terminator-T2900:~$ wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/postgres --latency
Running 30s test @ http://localhost:8080/v1/postgres
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   141.39ms  209.19ms   1.99s    87.93%
    Req/Sec     2.90k    99.15     3.11k    88.67%
  Latency Distribution
     50%   28.65ms
     75%  182.29ms
     90%  394.89ms
     99%    1.00s
  86540 requests in 30.01s, 1.67GB read
  Socket errors: connect 0, read 0, write 0, timeout 17
Requests/sec:   2883.50
Transfer/sec:     57.11MB
gustavo@terminator-T2900:~$
```

- oracle

```bash
gustavo@terminator-T2900:~$ wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/oracle --latency
Running 30s test @ http://localhost:8080/v1/oracle
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    79.87ms   62.10ms 511.67ms   78.35%
    Req/Sec     2.81k   345.50     3.37k    81.67%
  Latency Distribution
     50%   42.39ms
     75%  121.81ms
     90%  179.98ms
     99%  233.64ms
  83852 requests in 30.03s, 1.62GB read
Requests/sec:   2791.99
Transfer/sec:     55.30MB
```

## Results

cx_oracle and databases(with asyncpg) performs pretty well with more connections, but Oracle driver has better latency distribution. I need to tuning more the code from both sides, but I believe that when Oracle release the async driver , will be very interested to remake this benchmark.


