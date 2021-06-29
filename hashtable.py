"""
Author:         Elaine Chan Yun Ru
Assignment:     PA2_HashTables
Date:           2/12/2021
Description:    contains the class HashTable - to create a hash table to store data
"""
#import statements here
from collections import deque
from entry import Entry

class HashTable(object):
    #constructor for HashTable class
    def __init__(self):
        #initialize __table attribute here
        self.__table = dict()

    #put record into hash table
    def insert(self, k, v):
        #insert value into specific indexed positions in table
        #value is an instance of class Entry which stores both the L-mer string, and its occurence
        #if collision occurs, implement linkedlist technique to handle extra values of different L-mer strings
        #if collision occurs, and it's the same L-mer string as the one stored in the indexed position, add the count by 1
        if k in self.__table.keys():
            extra_entry = None
            for i in self.__table[k]:
                string = getattr(i, "_Entry__key")          #represents the L-mer string
                if v == string:
                    value = getattr(i, "_Entry__value")     #represents the count of L-mer string
                    value += 1
                    setattr(i, "_Entry__value", value)
                else:
                    extra_entry = Entry()
                    setattr(extra_entry, "_Entry__key", v)
                    setattr(extra_entry, "_Entry__value", 1)
            if extra_entry is not None:
                self.__table[k].append(extra_entry)
            else:
                pass
        else:
            llist = deque()         #use deque function from collections module to implement linekdlist technique
            new_entry = Entry()
            setattr(new_entry, "_Entry__key", v)
            setattr(new_entry, "_Entry__value", 1)
            llist.append(new_entry)
            self.__table[k] = llist


    #retrieve value in key-value record stored in the table. Return None if record isn't there
    def lookup(self, k):
        try:
            return self.__table[k]
        except KeyError:
            return None

    #remove and return value in key-value record stored in the table
    #return None if record isn't there
    def remove(self, k):
        try:
            value = self.__table[k]
            del self.__table[k]
            return value
        except KeyError:
            return None

    #compute hash value of entry key and return the result
    def hash(self, k):
        #get total hash value of L-mer string by getting the total decimal ASCII value of each character in string
        #hard-coded ascii string is used to determine the proper decimal ASCII code of character
        #   example: if character is "a", its ASCII value would be 97 + index value of "a" from ascii string
        ascii = "abcdefghijklmnopqrstuvwxyz"
        k = k.lower()
        total_value = 0
        for v in k:
            for i in ascii:
                if v == i:
                    value = 97 + ascii.index(i)
                    total_value += value
        return total_value

    #clear all entries stored in the table (just clear the data reference for each table node)
    def clear(self):
        self.__table.clear()

