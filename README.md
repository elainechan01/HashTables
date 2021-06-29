# HashTables
Program looks for the most common L-mer string in DNA string by implementation of Hash Tables 

## Program Description 
Program takes in a hard-coded DNA string and the L value. Implementing a hash table, the program stores the L-mer at its index, which is calculated as such:
```
Hash Value of L-mer string: Total decimal ASCII value of each character is L-mer string % total amount of substrings per DNA strand
```
When looping through the DNA string, a collision may occur when trying to store the L-mer string in an index of which a value has already been stored. To solve this problem, instead of searching for a new index value, the value stored at said index will increase by 1. Ultimately, this is the method of counting the occurences of L-mer strings. 

Finally, program outputs the most common L-mer string and the amount of occurences of said string.
