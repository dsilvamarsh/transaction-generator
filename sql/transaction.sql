CREATE  TABLE core.transaction(
	id bigserial primary key,
	src_acc integer,
	tgt_acc integer,
	transfer_amount numeric(18,3),
	create_ts timestamp,
	exchange_rate numeric(5,3),
	currency_code varchar(10),
	status varchar(20)

) tablespace dev;

alter table core.transaction
	owner to dev;
