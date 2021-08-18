CREATE VIEW v_bdays
SELECT 
name, birthday
, CASE 
	WHEN strftime('%m',date('now')) > strftime('%m',date(birthday)) THEN strftime('%Y',date('now')) - strftime('%Y',date(birthday))
	WHEN strftime('%m',date('now')) = strftime('%m',date(birthday)) THEN 
		CASE 
			WHEN strftime('%d',date('now')) >= strftime('%d',date(birthday)) THEN strftime('%Y',date('now')) - strftime('%Y',date(birthday))
			ELSE strftime('%Y',date('now')) - strftime('%Y',date(birthday)) - 1
		END
	WHEN strftime('%m',date('now')) < strftime('%m',date(birthday)) THEN strftime('%Y',date('now')) - strftime('%Y',date(birthday)) - 1

END AS 'age'

FROM birthdays