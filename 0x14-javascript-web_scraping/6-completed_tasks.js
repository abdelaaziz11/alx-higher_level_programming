#!/usr/bin/node

const request = require('request');
const urlAPI = process.argv[2];

request.get(urlAPI, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const CompletedTask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!CompletedTask[todo.userId]) {
        CompletedTask[todo.userId] = 1;
      } else {
        CompletedTask[todo.userId] += 1;
      }
    }
  });
  console.log(CompletedTask);
});
