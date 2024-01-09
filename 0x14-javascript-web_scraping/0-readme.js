#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Usage: node script.js <file-path>');
  process.exit(1); // Exit with an error code
}

// Read the content of the file specified in the command-line argument
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', function (err, contents) {
  if (err) {
    // If an error occurred during reading, print the error object
    console.error(err);
  } else {
    // Print the contents of the file
    console.log(contents);
  }
});

