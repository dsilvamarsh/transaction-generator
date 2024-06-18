
DROP TABLE warehouse.transaction;
CREATE  TABLE warehouse.transaction(
	id integer,
	src_acc integer,
	tgt_acc integer,
	transfer_amount decimal(18,3),
	create_ts timestamp,
	exchange_rate decimal(5,3),
	currency_code string,
	status string,
	reference string,
	expense_id integer

)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
;


