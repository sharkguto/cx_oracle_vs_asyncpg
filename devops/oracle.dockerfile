#FROM oracleinanutshell/oracle-xe-11g

FROM wnameless/oracle-xe-11g-r2

ADD devops/sql-scripts/test_o.sql /docker-entrypoint-initdb.d/
