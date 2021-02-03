import redis

conn = redis.Redis()

registrations = conn.execute_command('RG.DUMPREGISTRATIONS')

for reg in registrations:
  id = reg[1]
  conn.execute_command('RG.UNREGISTER', id)

file = open('wasm-gear.py')
gear = file.read()
file.close()

conn.execute_command('RG.PYEXECUTE', gear, 'REQUIREMENTS', 'wasmtime')
