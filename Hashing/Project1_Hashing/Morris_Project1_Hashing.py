# Garrett Morris
# Project 1: Hashing
# CMPS 5243: Advanced Algorithm Analysis
# March 26, 2020
# The goal of this program is to create hash tables using load
# factors of 66% and 80% and collision resoltion policies of
# linear probing and double hashing. The program will be ran twice
# and produce two seperate output files. The average number of probes
# for each method will be printed for each run.
# The tables will not be printed for the output files that will
# be turned in, as that would produce too many pages. I can email you
# the original output files with the tables included if you wish.

import sys
CAPACITY = 311 #size of hash table
#direct output to output file
sys.stdout = open('Morris_Project1_Hashing2_tables.txt', 'w+') 
print("Garrett Morris")
print("Project 1: Hashing")
print("CMPS 5243: Advanced Algorithm Analysis")
print("March 26, 2020\n\n\n")

#Hashing class
class Hashing:

    #initialization function
    def __init__(self):
        self.capacity = CAPACITY
        self.size = 0
        #initialize tables to None
        self.keys = [None] * self.capacity
        #Variable used for linear probing
        self.step = 1

    #Hash function: Key mod capacity
    def Mod_Hash(self, key):
        hash = key % self.capacity
        return hash
    
    #linear probing method
    def Lin_Probe(self, key):
        probe = 1 #variable for tracking # of probes
        self.size += 1 #increment when adding new value to table
        index = self.Mod_Hash(key)
        
        #check if initial index is empty
        if self.keys[index] == None:
            self.keys[index] = key
        #rehash the key until spot is found
        else:
            while self.keys[index] != None and self.keys[index] != key:
                index = self.Lin_Probe_Rehash(index)
                probe += 1
                if self.keys[index] == None:
                    self.keys[index] = key 
        return probe
    #rehashing function for linear probing
    def Lin_Probe_Rehash(self, oldhash):
        newhash = (oldhash+self.step) % self.capacity
        return newhash

    #double hashing method
    def Double_Probe(self, key):
        probe = 1 #variable to keep track of probes
        self.size += 1 #increment when new value is added
        index = self.Mod_Hash(key)

        #check if initial index is empty
        if self.keys[index] == None:
            self.keys[index] = key
        #rehash until empty index is found
        else:
            while self.keys[index] != None and self.keys[index] != key:
                index = self.Double_Probe_Rehash(index, key)
                probe += 1
                if self.keys[index] == None:
                    self.keys[index] = key
        return probe
    
    #rehashing method for double hashing
    def Double_Probe_Rehash(self, oldhash, key):
        newhash = (oldhash + ((key%10)+1)) % self.capacity
        return newhash

    #Print the hash table in a uniform manner
    def Print_Table(self):
        print("Index   Keys")
        print("____   ____")
        for i in range(len(self.keys)):
            print(str(i).ljust(4) + '   ' + str(self.keys[i]))
        print("____   ____")

##################################
########## Main Program ##########
##################################

#initializing value list by reading from a file
#this will be used for load factor 80%
keys250 = []
f = open("RandomNumberFile2.txt", "r")
for line in f:
    keys250.append(int(line))
f.close()

#creating a copy of the initial list with only the first 205 values
#this will be used for load factor 66%
keys205 = []
for i in range(205):
    keys205.append(keys250[i])

percent = "%" #this is to make it easier to print the % sign

#create hash table using linear probing and an 66% load factor
Linear66 = Hashing()
probe_counter = 0 #track number of probes
for key in keys205: #hash each key into the hash table
    #store number of probes required for given key
    probe_counter += Linear66.Lin_Probe(key) 
print("Load factor 66% with Linear Probe:")
Linear66.Print_Table() #print the hash table
print("It took an average of " + 
      str(round(probe_counter/float(len(keys205)), 3)) +
      " probes per key\nto fill the hash table at a 66" + percent +
      " load factor with Linear Probing.\n\n\n")

#create hash table using linear probing and an 80% load factor
Linear80 = Hashing()
probe_counter = 0  # track number of probes
for key in keys250:  # hash each key into the hash table
    # store number of probes required for given key
    probe_counter += Linear80.Lin_Probe(key)
print("Load factor 80% with Linear Probe:")
Linear80.Print_Table()  # print the hash table
print("It took an average of " + 
      str(round(probe_counter/float(len(keys205)), 3)) +
      " probes per key\nto fill the hash table at a 80" + percent +
      " load factor with Linear Probing.\n\n\n")

#create hash table using double hashing and a 66% load factor
DoubleHash66 = Hashing()
probe_counter = 0  # track number of probes
for key in keys205:
    # store number of probes required for given key
    probe_counter += DoubleHash66.Double_Probe(key)
print("Load Factor 66% with Double Hashing:")
DoubleHash66.Print_Table()  # print the hash table
print("It took an average of " + 
      str(round(probe_counter/float(len(keys205)), 3)) +
      " probes per key\nto fill the hash table at a 66" + percent +
      " load factor with Double Hashing.\n\n\n")

#create hash table using double hashing and an 80% load factor
DoubleHash80 = Hashing()
probe_counter = 0  # track number of probes
for key in keys250:
    # store number of probes required for given key
    probe_counter += DoubleHash80.Double_Probe(key)
print("Load Factor 80% with Double Hashing:")
DoubleHash80.Print_Table()  # print the hash table
print("It took an average of " + 
      str(round(probe_counter/float(len(keys205)), 3)) +
      " probes per key\nto fill the hash table at a 80" + percent +
      " load factor with Double Hashing.\n\n\n")
