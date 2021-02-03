import redis

conn = redis.Redis()

conn.set('a', 42)

add_file = open('add.wasm')
add_bytes = add_file.read()
add_file.close()

conn.set('add', add_bytes)

subtract_file = open('subtract.wasm')
subtract_bytes = subtract_file.read()
subtract_file.close()

conn.set('subtract', subtract_bytes)

print(conn.execute_command('RG.TRIGGER', 'wasm', 'add', 23))
print(conn.execute_command('RG.TRIGGER', 'wasm', 'subtract', 23))

conn.delete('a')
