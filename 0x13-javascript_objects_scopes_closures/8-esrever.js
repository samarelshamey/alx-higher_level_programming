#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1;
  let i = 0;
  while ((length - i) > 0) {
    const x = list[length];
    list[length] = list[i];
    list[i] = x;
    i++;
    length--;
  }
  return list;
};
