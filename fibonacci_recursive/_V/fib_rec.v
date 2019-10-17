module fib_rec

pub fn fib(n u64) u64 {
  if n <= 2 {
    return 1
  } else {
    return fib(n - u64(1)) + fib(n - u64(2))
  }
}

// println(fib(10))