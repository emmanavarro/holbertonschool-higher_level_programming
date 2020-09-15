#!/usr/bin/node
/*
Script that prints that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
const args = process.argv;
if (parseInt(args[2])) {
  console.log(`My number: ${parseInt(args[2])}`);
} else {
  console.log('Not a number');
}
