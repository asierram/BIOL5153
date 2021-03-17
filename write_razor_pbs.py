#! /usr/bin/env python3

#This scripts generateds a PBS files for the AHPCC razor cluster

# define some variables
job = 'test'
queue = 'med16core'
wall = 3 # this is in hours
nodes = 1 # num nodes
ppn = 1 # num ppn

# This sectiom prints the header/required info for the PBS script
# ''' everything after this is a comment use again ''' to end the comment
print('#PBS -N', job) #Job name
print('#PBS -q', queue) #Which queue to use
print('#PBS -j oe')#Join the STDOUT and STDERR into a single file
print('#PBS -o',job +'.$PBS_JOBID')#set the name of the output file
print('#PBS -l nodes='+ str(nodes)+':ppn='+ str(ppn))#How many resource to ask for (nodes= num nodes, ppn= num processors)
print('#PBS -l walltime='+ str(wall) + ':00:00') #Set the wall time (default to 1 hour) 
print()

#cd into working directory 
print('cd $PBS_O_WORKDIR')
print ()

#load the necssary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0 blast mafft/7.304b')
print()

#commands for this job
print('# insert commands here')



