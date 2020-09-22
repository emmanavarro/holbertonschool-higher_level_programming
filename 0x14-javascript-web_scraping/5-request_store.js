#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const toFile = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(toFile, body, function (error) {
      if (error) console.log(error);
    });
  }
});
