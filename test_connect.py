import psycopg2

try:
    conn = psycopg2.connect(user='webdb',
                     password='webdb',
                     host='192.168.1.191',
                     port='5432',
                     database='webdb')
    cursor = conn.cursor()
    cursor.execute('select * from pet')
    record = cursor.fetchone()
    print(record)
except Exception as e:
    print('err: ', e)
finally:
    'conn' in locals() and conn and conn.close()