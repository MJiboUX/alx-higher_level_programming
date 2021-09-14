#!/usr/bin/node

const req = require('request');
const Firstarg = process.argv[2];
req.get(Firstarg, function(error,response){
 console.error('error:', error);
 console.log('code:', response && response.statusCode);
});
