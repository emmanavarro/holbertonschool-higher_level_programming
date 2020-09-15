#!/usr/bin/node
/*
Script that prints the first argument passed to it
*/
const args = process.argv;
if (args[2]) {
  console.log('Holberton');
} else {
  console.log('No argument');
}
