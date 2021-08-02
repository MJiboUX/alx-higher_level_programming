#!/usr/bin/node
import { argv } from 'process';
argv.forEach((val) => {
  if (val){
  console.log(`Argument found`);
  } else {
  console.log(`No argument`);
  }
});
