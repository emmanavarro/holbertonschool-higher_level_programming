#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      occurence += 1;
    }
  }
  return occurence;
};
