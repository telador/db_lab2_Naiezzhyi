import psycopg2

username = 'postgres'
password = '1341'
database = 'L2'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT acc_age, acc_followers FROM accounts ORDER BY acc_age
'''

query_2 = '''
SELECT TRIM(lang_name), count(users.user_lang) FROM  users left join langs on users.user_lang=langs.user_lang GROUP BY lang_name
'''

query_3 = '''
SELECT user_age - acc_age FROM users join accounts on accounts.user_id = users.user_id
'''


conn = psycopg2.connect(user = username, password = password, dbname = database, host = host, port = port)

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    print('1.')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.')
    cur.execute(query_3)
    for row in cur:
        print(row)