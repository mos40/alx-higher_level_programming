#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

// Extract file paths from command-line arguments
const [, , file1, file2, destination] = process.argv;

// Read the content of the first file
fs.readFile(file1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(err1.message);
    process.exit(1);
  }

  // Read the content of the second file
  fs.readFile(file2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(err2.message);
      process.exit(1);
    }

    // Concatenate the contents of the two files
    const concatenatedContent = data1 + data2;

    // Write the concatenated content to the destination file
    fs.writeFile(destination, concatenatedContent, (err3) => {
      if (err3) {
        console.error(err3.message);
        process.exit(1);
      }

      console.log(`Files ${file1} and ${file2} successfully concatenated to ${destination}`);
    });
  });
});
