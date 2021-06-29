"""
Author:         Elaine Chan Yun Ru
Assignment:     PA2_HashTables
Date:           2/12/2021
Description:    Main function of program is here - to run the program
"""
#import statements here
from finder import MCLMerFinder
from hashtable import HashTable

def main():
    #hardcode a dna string and the L value
    dna = "ATTAGCATTCCGATT"
    L = 3
    #create instances of MCLMerFinder and HashTable
    lmer_finder = MCLMerFinder()
    hash_table = HashTable()
    table = dict()

    #make sure each element has an empty list
    setattr(hash_table, '_HashTable__table', table)
    setattr(lmer_finder, '_MCLMerFinder__table', hash_table)

    #find and print most common L-mer in dna
    lmer_finder.findMCLMer(dna, L)

    #clear all values when done
    getattr(lmer_finder, '_MCLMerFinder__table').clear()

if __name__ == '__main__':
    main()