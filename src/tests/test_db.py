import unittest
import pysqliteog

table_sql = """
		CREATE TABLE IF NOT EXISTS example_table (
			id INTEGER PRIMARY KEY,
			name TEXT,
			age INTEGER,
			height REAL,
			is_student INTEGER
		);
"""


def hello(x):
    return f'hello {x}'


def square(x):
    return int(x) * int(x)


class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = pysqliteog.connect('localhost', '9091', 'testpy.db')
        self.db.create_function('say_hello', 1, hello)
        self.db.create_function('square_number', 1, square)
        with self.db.cursor() as cur:
            cur.execute(table_sql)
            cur.execute("""DELETE FROM example_table;""")

    def tearDown(self):
        self.db.close()

    def test_crud(self):
        with self.db.cursor() as cur:
            insert_sql = """INSERT INTO example_table (name, age, height, is_student) values(?,?,?,?)"""
            cur.execute(insert_sql, ["mike jones", 40, 192, True])
            id = cur.lastrowid
            self.assertGreater(id, 0)

            update_sql = """UPDATE example_table SET age=?, height=? WHERE id=?"""
            cur.execute(update_sql, [99, 200, id])
            self.assertEqual(id, cur.lastrowid)

            select_sql = """SELECT * FROM example_table WHERE id=?"""
            cur.execute(select_sql, [id])
            row = cur.fetchone()
            self.assertEqual(id, row[0])
            self.assertEqual('mike jones', row[1])
            self.assertEqual(99, row[2])
            self.assertEqual(200, row[3])

            delete_sql = """DELETE FROM example_table WHERE id=?"""
            cur.execute(delete_sql, [id])

            cur.execute("select count(*) from example_table")
            res = cur.fetchone()
            self.assertEqual(0, res[0])

    def test_custom_functions(self):
        sql = """INSERT INTO example_table (name, age, height, is_student) values(?,?,?,?)"""
        with self.db.cursor() as cur:
            cur.execute(sql, ["John", 25, 180, True])
            id = cur.lastrowid
            self.assertGreater(id, 0)

            cur.execute("""SELECT square_number(age) FROM example_table WHERE id=?""", [id])
            self.assertEqual(cur.fetchone()[0], 625)

if __name__ == '__main__':
    unittest.main()