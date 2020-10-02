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

```bash
gustavo@terminator-T2900:~$ wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/postgres --latency
Running 30s test @ http://localhost:8080/v1/postgres
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   131.74ms  198.55ms   1.99s    89.23%
    Req/Sec     2.89k   136.56     3.11k    96.00%
  Latency Distribution
     50%   28.92ms
     75%  153.79ms
     90%  363.36ms
     99%  992.43ms
  86342 requests in 30.01s, 1.67GB read
  Socket errors: connect 0, read 0, write 0, timeout 9
Requests/sec:   2877.00
Transfer/sec:     56.98MB
gustavo@terminator-T2900:~$ wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/oracle --latency
Running 30s test @ http://localhost:8080/v1/oracle
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   188.63ms   24.53ms 504.33ms   82.33%
    Req/Sec     0.94k   171.69     1.09k    92.83%
  Latency Distribution
     50%  188.91ms
     75%  192.81ms
     90%  201.95ms
     99%  271.89ms
  26227 requests in 30.02s, 515.19MB read
  Socket errors: connect 0, read 1992, write 0, timeout 0
  Non-2xx or 3xx responses: 215
Requests/sec:    873.58
Transfer/sec:     17.16MB
gustavo@terminator-T2900:~$ wrk -c 200 -t 1 -d 30 http://localhost:8080/v1/oracle --latency
Running 30s test @ http://localhost:8080/v1/oracle
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   200.27ms   12.24ms 345.36ms   97.08%
    Req/Sec     1.00k    60.83     1.09k    92.00%
  Latency Distribution
     50%  199.77ms
     75%  201.68ms
     90%  205.34ms
     99%  229.34ms
  29825 requests in 30.01s, 589.83MB read
  Socket errors: connect 0, read 139, write 0, timeout 0
  Non-2xx or 3xx responses: 43
Requests/sec:    993.68
Transfer/sec:     19.65MB
gustavo@terminator-T2900:~$
```

## Results

Is not a fair fight, but as I can see cx_oracle performs pretty good with low workload, better than databases(with asyncpg). On the other hand, cx_oracle driver got a lot of crashes, invalidate some tests, when have more connections

```oracle crashes
OCI-21500: no message, kgebse recursion failure
OCI-21500: internal error code, arguments: [kgegpa:parameter corruption], [], [], [], [], [], [], []
```
