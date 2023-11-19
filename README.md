# pysqliteog

A client library for [sqlite-og](https://github.com/aousomran/sqlite-og), based on the
[Python Database API Specification v2.0](https://peps.python.org/pep-0249/)
specification.

# Installation

This library requires `grpc` to be installed

```shell
pip install grpcio grpcio-tools
```

# Usage

### Basic Usage

```python
import pysqliteog

# connect to the database
db = pysqliteog.connect('<host>', '<port>', '<db-name>')
with db.cursor() as cur:
    cur.execute('select 1')
    print(f"{cur.fetchone()}")
db.close()
```

### Using Callbacks

The client allows you to define custom function that
can be used directly in your queries.

```python
import pysqliteog


# define a custom callback function
def say_hello(x):
    return f'hello {x}'


# connect to the database
db = pysqliteog.connect('<host>', '<port>', '<db-name>')
# all custom function must be registered before creating the first cursor
db.create_function('say_hello', 1, say_hello)

with db.cursor() as cur:
    cur.execute('select say_hello(?)', params=['world'])
    # should print "hello world"
    print(f"{cur.fetchone()}")

db.close()
```
