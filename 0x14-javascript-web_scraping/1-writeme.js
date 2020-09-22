#!/usr/bin/node
const fileSystem = require('fs');
const filePATH = process.argv[2];
const fileText = process.argv[3];

fileSystem.writeFile(filePATH, fileText, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
