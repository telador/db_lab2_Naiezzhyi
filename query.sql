SELECT acc_age, acc_followers FROM accounts ORDER BY acc_age

SELECT TRIM(lang_name), count(users.user_lang) FROM  users left join langs on users.user_lang=langs.user_lang GROUP BY lang_name

SELECT user_age - acc_age FROM users join accounts on accounts.user_id = users.user_id