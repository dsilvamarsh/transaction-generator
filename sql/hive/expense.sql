
DROP TABLE core.expense;
create  table core.expense(
	id integer,
	name string ,
	cost decimal(18,3),
	description string ,
	type string,
	next_break integer


) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
;
