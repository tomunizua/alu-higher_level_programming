#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < Math.floor(list.length / 2); i++) {
    [list[i], list[list.length - 1 - i]] = [list[list.length - 1 - i], list[i]];
  }
  return list;
};
