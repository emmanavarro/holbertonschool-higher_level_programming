#!/usr/bin/node
// Script that computes and prints a factorial

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}

const args = process.argv;
console.log(factorial(parseInt(args[2])));
