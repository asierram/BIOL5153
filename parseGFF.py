#! /usr/bin/python3

import csv
import argparse
from Bio import SeqIO 

# this script will parse a GFF file and extract each feature from the genome 
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA FORMAT)

#create an argument parser object
parser = argparse.ArgumentParser(description = 'this script will parse a GFF file and extract each feature from the genome')

# add postional arguments

parser.add_argument("gff", help = 'name of the gff file')
parser.add_argument("fasta", help = 'name of the FASTA file')


# parse the arguments

args = parser.parse_args()


# read in FASTA file  
genome = SeqIO.read(args.fasta,'fasta')#you have to use fasta will not recognize fsa, fa

print(genome.seq)
# open and read in GFF file
#with open(gff_input, 'r') as gff_in:  no longer gff_input exist
with open(args.gff, 'r') as gff_in: 
    #create a csv reader object
    reader = csv.reader(gff_in, delimiter = '\t')

    #loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        start = int(line[3])-1
        end = int(line[4])+1
        strand = line[6]
        feature = line[8]

        if strand=='-':
            print('>',genome.id,feature)
            print(genome.seq[start:end].reverse_complement())
        elif strand=='+':
            print('>',genome.id,feature)
            print(genome.seq[start:end])
    	