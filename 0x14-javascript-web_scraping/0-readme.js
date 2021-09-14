#!/usr/bin/node

const fs = require('fs');
const fname = process.argv[2];
fs.readFile(fname, 'utf-8', function(error, log) {
    if (error) {
        console.log(error);
    } else {
        console.log(log);
    }
    }
);