
DROP TABLE core.expense;
create  table core.expense(
	id serial primary key,
	name varchar not null ,
	cost numeric(18,3) not null,
	description varchar ,
	type varchar,
	next_break smallint


) tablespace dev;
alter table core.expense
	owner to dev;


Insert into core.expense (name,cost,description,type,next_break)
values
('Cofee',25,'Need refreshment from sleep/work','Drink',4),
('Sandwitch',45,'the day needs energy ','Breakfast',12),
('Idli sambar ',40,'the day needs dry energy ','Breakfast',9),
('Mendu Wada sambar ',70.50,'the day needs sambar energy ','Breakfast',12),
('Coke',20,'I am thirsty its too hot ','Drink',3),
('Mango Lassi',30.65,'I am thirsty and hungry ','Drink',6),
('Fried Rice',150,'I need Rice','Lunch',15),
('Manchurian Rice',170,'I need chicken manchurian Rice','Lunch',13),
('Pork Roast',250,'I need Pork ','Lunch',20),
('Chicken 65',190,'I need curry chicken','Lunch',12),
('Chicken Satye',160.50,'I need chicken satye','Lunch',15),
('Pomphret curry ',350,'I need Fish','Dinner',15),
('Pomphret fry with rice ',300,'I need Fish','Dinner',15),
('Mutton curry with rice ',450,'I need Meat','Dinner',15),
('Paneer Tikka ',250,'I need Veg','Dinner',15),

('Tea',15,'Need refreshment from sleep/work','Drink',3)