module fib_iter

pub fn fib(n u64) u64 {
  mut a := u64(0)
  mut b := u64(1)
  mut c := u64(1)
  for i := u64(0); i < u64(n); i++ {
    c = a
    a = b + a
    b = c
    // a += b
  }
  return a
}

// println(fib(u64(10)))