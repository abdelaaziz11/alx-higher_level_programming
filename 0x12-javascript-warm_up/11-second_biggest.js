#!/usr/bin/node

// searches the second biggest integer

if (!process.argv[2] || process.argv.lenght <= 3) {
  console.log(0);
} else {
  const s = process.argv.sort((a, b) => b - a);
  console.log(s.slice(3)[0]);
}
