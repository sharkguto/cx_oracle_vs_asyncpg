CREATE SCHEMA test;

CREATE TABLE test.company (
    id integer NOT NULL,
    name text NOT NULL,
    age integer NOT NULL,
    address VARCHAR(50),
    salary float
);

INSERT INTO test.company VALUES (10, 'b', 2, 'n', 2.0999999);
INSERT INTO test.company VALUES (9, 'b', 2, 'n', 2.1999999);
INSERT INTO test.company VALUES (8, 'b', 2, 'n', 2.2999999);
INSERT INTO test.company VALUES (7, 'b', 2, 'n', 2.3999999);
INSERT INTO test.company VALUES (6, 'b', 2, 'n', 2.4999999);
INSERT INTO test.company VALUES (5, 'b', 2, 'n', 2.5999999);
INSERT INTO test.company VALUES (4, 'b', 2, 'n', 2.6999999);
INSERT INTO test.company VALUES (3, 'b', 2, 'n', 2.7999999);
INSERT INTO test.company VALUES (2, 'b', 2, 'n', 2.8999999);
INSERT INTO test.company VALUES (1, 'b', 2, 'n', 2.9999999);