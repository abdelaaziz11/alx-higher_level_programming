#!/usr/bin/node
// imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const ocurr = dict[key];
  newDict[ocurr] = [];
  for (const keys in dict) {
    if (dict[keys] === ocurr) {
      newDict[ocurr].push(keys);
    }
  }
}
console.log(newDict);
