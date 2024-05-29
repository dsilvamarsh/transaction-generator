CREATE table core.customer(
	id serial primary key,
	name varchar(100),
	tax_id varchar(20),
    email varchar(100),
    contact varchar(20),
    create_ts timestamp
) tablespace dev;

ALTER TABLE core.customer
	OWNER to dev;

