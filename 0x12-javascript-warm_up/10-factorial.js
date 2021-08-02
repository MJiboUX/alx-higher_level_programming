#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) == true) {
    return 1;
  }
  else if (n == 0 || n == 1) {
    return 1;
  }
  else {
    let result = n;
    while (n > 1) {
      result = result * (n - 1);
      n = n - 1;
    }
    return result;
  }
}
factorial(process.argv[2]);
