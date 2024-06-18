Drop table core.account;
CREATE TABLE core.account(
	id serial primary key,
	customer_id int REFERENCES core.customer(id),
	balance numeric(18,3),
	acc_type varchar(20),
	create_ts timestamp
	
) tablespace dev;

alter table core.account
	owner to dev;
