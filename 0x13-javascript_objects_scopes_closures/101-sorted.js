#!/usr/bin/node

const { dict } = require('./101-data');

const invertedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!(occurrences in invertedDict)) {
    invertedDict[occurrences] = [];
  }

  invertedDict[occurrences].push(userId);
}

console.log(invertedDict);
