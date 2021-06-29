"""
Author:         Elaine Chan Yun Ru
Assignment:     PA2_HashTables
Date:           2/12/2021
Description:    contains the class MCLMerFinder - to use other classes to search for the most common L-mer string that is in a dna string
"""
#import statements here
from hashtable import HashTable

class MCLMerFinder(object):
    #constructor for MCLMerFinder class
    def __init__(self):
        #initialize attribute __table
        self.__table = HashTable()

    #find most common I-mer in string dna_string. Print the string and how many times it appears
    def findMCLMer(self, dna_string, I):
        #split up the dna_string into L-mer strings according to the provided number of character per substring
        dna_len = len(dna_string)
        split_strings = []              #to store each substring of the dna_strand which is split up accordingly
        index_value_list = []           #to store the index value of each substring (index value of substring is the remainder of the total decimal ASCII value of the substring by the amount of substrings)
        res_index_value_list = []       #to store the index value of L-mer string without duplicates
        value_list = dict()
        m = 0                           #represents the amount of substrings per dna strand
        for index in range(0, dna_len, I):
            split_strings.append(dna_string[index:index + I])
            m+=1
        #calculate the index value per substring and store into index_value_list
        for i in split_strings:
            hash_value = self.__table.hash(i)
            index_value = hash_value%m
            index_value_list.append(index_value)
            self.__table.insert(index_value, i)
        #store the index value of the substrings without duplicates into res_index_value_list
        [res_index_value_list.append(x) for x in index_value_list if x not in res_index_value_list]
        #get the values of the stored data and store into value_list
        #look for the most common L-mer string
        for i in range(len(res_index_value_list)):
            llist = self.__table.lookup(res_index_value_list[i])
            for i in llist:
                if getattr(i, "_Entry__key") in value_list.keys():
                    pass
                else:
                    value_list[getattr(i, "_Entry__key")] = getattr(i, "_Entry__value")
        #return and print the most common L-mer string and its number of occurence
        most_common = max(value_list, key=lambda x: value_list[x])
        most_common_value = value_list[most_common]
        print(f"The most common I-mer string is {most_common} with a value of {most_common_value}")












