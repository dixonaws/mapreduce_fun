# Summary
mapreduce_fun is a Python program that contains methods 
resembling map() and reduce() functions in a hadoop system. I
wrote this only as a study of the MapReduce algorithm and its
applications.

# Running
Simply run ```python simlated_mapreduce.py``` 
The default input file is datasets/bible.txt, the King James Bible in a plaintext from the Gutenberg Project 


Todo/Enhancements:
- take input files as parameters to the program
- (done) simulate shared storage, pass a range to reduce() function instead of reading the entire file  
- (done) mp to simulate processing on a multi-node cluster
- logging levels
- visualization feature
- AWS EMR equivalent
- AWS Athena equivalent

tested on:
macOS Mojave 10.14.2 with Python 2.7.10
macOS Big Sur 11.6 with Python 2.7.16