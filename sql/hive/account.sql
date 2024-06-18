Drop table core.account;
CREATE TABLE core.account(
	id integer,
	customer_id integer,
	balance decimal(18,3),
	acc_type string,
	create_ts timestamp
	
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
;
