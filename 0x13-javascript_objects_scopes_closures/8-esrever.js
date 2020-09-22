#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  let index = 0;
  for (index = list.length - 1; index >= 0; index--) {
    reverseList.push(list[index]);
  }
  return reverseList;
};
