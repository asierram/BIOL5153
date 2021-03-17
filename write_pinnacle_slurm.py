#! /usr/bin/env python3

 # define some variables
job = 'Trinity-assembly'
queue = 'med16core'
time = 3 # this is in hours
nodes = 1 # num nodes
ppn = 1 # num ppn

print('#SBATCH -J', job)#Job name
print('#SBATCH --partition comp06')
print('#SBATCH -o', job +'.txt')#set the name of the output file
print('#SBATCH -e', job+'.err')#set the name of the error file
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=asierram@uark.edu')  
print('#SBATCH --nodes='+ str(nodes))#How many resource to ask for (nodes= num nodes)
print('#SBATCH --ntasks-per-node='+ str(ppn))#How many resource to ask for (ppn= num processors)
print('#SBATCH --time=' + str(time) + ':00:00') #Set the wall time (default to 1 hour) 
print()


#load the necssary modules 
print('# load required modules')
print ('module load samtools')
print ('module load jellyfish')
print ('module load bowtie2')
print ('module load salmon/0.8.2')
print ('module load java')
print ('module load gcc/7.2.1') 
print ('module load python/3.6.0-anaconda')
print()

#cd into working directory 
print ('# cd into the directory where you are submitting this script')
print ('cd $SLURM_SUBMIT_DIR')
print()

#commands for this job
print('# insert commands here')
print()