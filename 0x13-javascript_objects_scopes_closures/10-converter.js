#!/usr/bin/node
exports.converter = function (base) {
  function numToBase (numToConvert) {
    return numToConvert.toString(base);
  }
  return numToBase;
};
