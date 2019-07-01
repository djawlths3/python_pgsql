import psycopg2
import config


def test_insert():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()
        cursor.execute("insert into pet values('멍멍이', 'ky','dog','m','2019-01-31)")

    except Exception as e:
        print('err: ', e)
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())

def test_select():
    try:
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("select * from pet")
        records = cursor.fetchall()

        for record in records:
            print(record, type(record))

    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        conn and conn.close()

def main():
    #test_insert()
    test_select()
    # print('=================================================')
    # test_delete()
    # test_select()
    # print('=================================================')
    # test_update()
    # test_select()

__name__ == '__main__' and main()