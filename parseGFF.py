#! /usr/bin/python3

import csv
import argparse
from Bio import SeqIO #search pip3 list to see you have installed succesfully 

# this script will parse a GFF file and extract each feature from the genome 
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA FORMAT)

#create an argument parser object
parser = argparse.ArgumentParser(description = 'this script will parse a GFF file and extract each feature from the genome')

# add postional arguments (docs require for the script to run, the order matters), we put them beside the name of the script with spaces#

parser.add_argument("gff", help = 'name of the gff file')
parser.add_argument("fasta", help = 'name of the FASTA file')


# parse the arguments

args = parser.parse_args()

#print(args.gff)
#we don't longer need this 
# GFF filename 
#gff_input = 'watermelon.gff'

# fasta filename 
#fasta_input = 'watermelon.fsa'

# read in FASTA file  needs to go first because once with parse the gff we want to work with info in the fasta file
genome = SeqIO.read(args.fasta,'fasta')#you have to use fasta will not recognize fsa, fa
print(genome.id)
print(len(genome.seq)) #seq is a method created by python

# open and read in GFF file
#with open(gff_input, 'r') as gff_in:  no longer gff_input exist
with open(args.gff, 'r') as gff_in: #gff because that is how we named it 
    #create a csv reader object
    reader = csv.reader(gff_in, delimiter = '\t') #separated by columns in a list

    #loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        start = line[3]
        end = line[4]
        strand = line[6]
        #print(start)
        
        #  extract the sequence 
        print(len(genome.seq))
    #for l in gff_in:
        #columns = l.split('\t') #tab
        #print(columns[3],columns[4])
#print (start) #will printed only once beacuse is not in th eloop 



# parse the GFF file