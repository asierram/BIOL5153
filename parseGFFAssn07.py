#! /usr/bin/python3

import re
import csv
import argparse
from Bio import SeqIO 
from Bio.Seq import Seq
from collections import defaultdict

# this script will parse a GFF file and extract each feature from the genome 
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA FORMAT)

#create an argument parser object
parser = argparse.ArgumentParser(description = 'this script will parse a GFF file and extract each feature from the genome')

# add postional arguments

parser.add_argument("gff", help = 'name of the gff file')
parser.add_argument("fasta", help = 'name of the FASTA file')
parser.add_argument("feature_type", help = 'type of feature to extract')
# parse the arguments

args = parser.parse_args()


# read in FASTA file  
genome = SeqIO.read(args.fasta,'fasta')#you have to use fasta will not recognize fsa, fa

# Reverse complement function
def rev_comp(fragment, strand):
    if(strand == "-"):
        fragment = fragment.reverse_complement()
        return(fragment)
    elif (strand=='+'):
        return(fragment)

    

## Extracting the [CDS] 

#dictionary: key= gene name, value = list of exon(s) for that gene
gene_dict = defaultdict(dict)

# open and read in GFF file
#with open(gff_input, 'r') as gff_in:  no longer gff_input exist
with open(args.gff, 'r') as gff_in: 
    #create a csv reader object
    reader = csv.reader(gff_in, delimiter = '\t')

    #loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        #skip blank lines 
        if(not line): #if it is a blank line
            continue

        elif(re.search(r'^#', line[0])): #if it begins with a hash mark
            continue
            
        #else it is a data line
        else:
            start = line[3]
            end = line[4]
            strand = line[6]
            attributes = line[8] 
            feature = line[2]
            exon_num = re.search(r'exon\s?=?(\d)',attributes, re.I )
            gene = re.findall(r'Gene\s(.*?)\s', attributes)
            fragment = genome.seq[int(start)-1:int(end)]
            #header = '>'+ genome.id + ' '+ attributes # gene_key


            if (feature == args.feature_type):
                if (gene_dict[gene[0]]== {}):
                    gene_dict[gene[0]] = [strand, fragment]
                else:
                    gene_dict[gene[0]].append(fragment)

for gene_name in gene_dict:
    if (gene_dict[gene_name][0] == "-"):
        print('>'+ genome.id + '_' + gene_name) 
        merge= str('')
        for line in gene_dict[gene_name][1:]:
            merge += line
            CDS= merge.reverse_complement()
            print(CDS)

    if (gene_dict[gene_name][0] == "+"):
        print('>'+ genome.id + '_' + gene_name)
        merge= str('')
        for line in gene_dict[gene_name][1:]:
            merge += line
            CDS=merge
            print(CDS)