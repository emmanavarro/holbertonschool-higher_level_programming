#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const element in dict) {
  if (newDict[dict[element]]) {
    newDict[dict[element]] = newDict[dict[element]].concat([element]);
  } else {
    newDict[dict[element]] = [element];
  }
}
console.log(newDict);
