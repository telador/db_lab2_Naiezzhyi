import psycopg2
import matplotlib.pyplot as plt

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

    cur.execute(query_1)
    x = []
    y = []
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y, width=0.1)
    plt.show()

    print('\n2.')
    x = []
    y = []
    cur.execute(query_2)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.pie(y, labels=x)
    plt.show()

    print('\n3.')
    x = []
    cur.execute(query_3)
    for row in cur:
        x.append(row[0])
    plt.bar(range(len(x)) ,x)
    plt.show()