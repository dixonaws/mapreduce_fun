mapreduce_fun is a simple program that contains functions that might
resemble map() and reduce() functions in a hadoop system

enhanements:
- take input files as parameters
- simulate shared storage, pass a byte range to reduce() function instead of reading the entire file  
- mp to simulate processing on a multi-node cluster
- logging levels
- visualization feature