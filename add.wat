(module
  (import "" "get_a" (func $get_a (result i32)))

  (export "run" (func $run))

  (func $run (param $b i32) (result i32)
    call $get_a
    local.get $b
    i32.add
  )
)
