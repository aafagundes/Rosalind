line = open('rosalind_dna (1).txt').readline()
result = [0, 0, 0, 0]

for base in range(len(line)):
    if line[base]=='A':
        result[0]+=1
    elif line[base]=='C':
        result[1]+=1
    elif line[base]=='G':
        result[2]+=1
    elif line[base]=='T':    
        result[3]+=1

print(result)

