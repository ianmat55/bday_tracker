DROP TABLE IF EXISTS birthdays;

CREATE TABLE birthdays (
	id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	name text NOT NULL UNIQUE,
	birthday text NOT NULL --YYYY-MM-DD
	--how to automatically calculate age from current date and birthday value?
);