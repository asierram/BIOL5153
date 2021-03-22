#! /usr/bin/env python3

#set he name of input DNA sequence file
filename = 'DNA.txt'  

#open the input file, assign to file handle called 'infile' 
infile = open (filename, 'r' )

#print (infile)
dna_sequence = infile.read().rstrip()

#print(dna_sequence)

infile.close()

#print(dna_sequence)

#calculating the sequence length 

seqlen= len(dna_sequence)

print('Sequence length:', seqlen)

#calculating the frequency of A in the file 
numA= dna_sequence.count('A')
FreqA= numA/seqlen
print("Freq of A:",FreqA)

#calculating the frequency of C in the file 
numC= dna_sequence.count('C')
FreqC= numC/seqlen
print("Freq of C:",FreqC)

#calculating the frequency of G in the file 
numG= dna_sequence.count('G')
FreqG= numG/seqlen
print("Freq of G:",FreqG)

#calculating the frequency of T in the file 
numT= dna_sequence.count('T')
FreqT= numT/seqlen
print("Freq of T:",FreqT)

#calculating the G+C content of the file 
numGC=numC+numG
GC_content=numGC/seqlen
print("G+C content:",GC_content)

#simple check inside the script to make sure that the frequencies sum is equal to 1.
Frequencies=FreqA+FreqC+FreqG+FreqT
print('Frequencies sum:',Frequencies)


#Creating the output file

outfile = open('nucleotide_composition.txt', 'w')

outfile.write('sequence length:'+ str(seqlen)+ '\n')
outfile.write("Freq of A:" + str(FreqA)+ '\n')
outfile.write("Freq of C:" + str(FreqC)+ '\n')
outfile.write("Freq of G:" + str(FreqG)+ '\n')
outfile.write("Freq of T:" + str(FreqT)+ '\n')
outfile.write("G+C content:" + str(GC_content)+ '\n')
outfile.write("Frequencies sum:" + str(Frequencies)+ '\n')

outfile.close()
