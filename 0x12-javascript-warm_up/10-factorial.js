#!/usr/bin/node
function factorial (n) {
  let result = 1;
  while (n >= 1) {
      result = result * n;
  }
  return (result);
}
console.log(factorial(parseInt(process.argv[2])));
