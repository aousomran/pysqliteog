from pysqliteog import dbapi2

table_sql = """
		CREATE TABLE IF NOT EXISTS example_table (
			id INTEGER PRIMARY KEY,
			name TEXT,
			age INTEGER,
			height REAL,
			is_student INTEGER
		);
"""


def say_hello(x):
    return f'hello {x}'


def square(x):
    return int(x) * int(x)


def test_connection():
    db = dbapi2.connect('localhost', '9090', 'testpy.db')
    db.create_function('say_hello', 1, say_hello)
    db.create_function('square', 1, square)
    with db.cursor() as cur:
        cur.execute(table_sql)

    with db.cursor() as cur:
        cur.execute("select square(?)", params=[2])
        print(cur.fetchone())

    with db.cursor() as cur:
        cur.execute("select say_hello(?)", params=['ao'])
        print(cur.fetchone())

    with db.cursor() as cur:
        sql = """INSERT INTO example_table (name, age, height, is_student) values(?,?,?,?)"""
        cur.execute(sql, params=["mike jones", 40, 192, True])
        cur.execute("SELECT * FROM example_table")
        print(cur.fetchall())
    db.close()


if __name__ == "__main__":
    test_connection()
