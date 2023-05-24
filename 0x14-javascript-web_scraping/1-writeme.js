#!/usr/bin/node

const fs = require('fs');

function writeFile(filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

const args = process.argv.slice(2);
const filePath = args[0];
const content = args[1];

writeFile(filePath, content);
