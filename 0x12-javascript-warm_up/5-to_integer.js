#!/usr/bin/node
const x = isNaN(process.argv[2])
if (!(x === true)) {
console.log('Not a number');
} else {
console.log('My number: ' + x);
}
