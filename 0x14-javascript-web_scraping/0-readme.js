#!/usr/bin/node
const fileSystem = require('fs');
const filePATH = process.argv[2];

fileSystem.readFile(filePATH, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
