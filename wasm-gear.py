from wasmtime import Store, Module, Instance, Func, FuncType, ValType

def get_a():
  return int(execute('GET', 'a'))

def invoke_wasm(data):

  wasm_key = data[1]
  operand_b = int(data[2])

  wasm = execute('GET', wasm_key)
  wasm_bytes = bytes(wasm, 'ascii')

  store = Store()
  module = Module.validate(store, wasm_bytes)
  module = Module(store.engine, wasm_bytes)

  get_a_func = Func(store, FuncType([], [ValType.i32()]), get_a)

  instance = Instance(store, module, [get_a_func])

  return instance.exports["run"](operand_b)

gb = GearsBuilder('CommandReader')
gb.map(invoke_wasm)
gb.register(trigger='wasm')