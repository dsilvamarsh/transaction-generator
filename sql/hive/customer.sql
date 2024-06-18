Drop table warehouse.customer;
CREATE table warehouse.customer(
	id integer,
	name string,
	tax_id string,
    email string,
    contact string,
    create_ts timestamp,
    type string
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
;

