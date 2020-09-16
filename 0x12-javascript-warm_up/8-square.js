#!/usr/bin/node
// Script that prints a square
const printX = parseInt(process.argv[2]);
let num;

if (!printX) {
  console.log('Missing size');
} else {
  for (num = 0; num < printX; num++) {
    console.log('X'.repeat(printX));
  }
}
