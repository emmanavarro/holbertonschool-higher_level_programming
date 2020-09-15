#!/usr/bin/node
// Script that prints x times “C is fun”
const args = process.argv;
let printTimes = args[2];

if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  for (printTimes; printTimes > 0; printTimes--) {
    console.log('C is fun');
  }
}
