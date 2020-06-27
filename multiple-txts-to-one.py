import sys
import glob

folder = sys.argv[1]
filename = sys.argv[2]

files = glob.glob(folder + '/*.txt')

with open(filename + '.txt', 'w') as outfile:
    for file in files:
        with open(file, 'r') as infile: 
            data = infile.read().split('\n')[:-1]
            for d in data:
                if(len(d) > 0):
                    outfile.write(d + '\n')
        
        outfile.write('\n')