def get_hamming_distance(dna1,dna2):
    hamming= 0
    for char in range(len(dna1)):
        if dna1[char]!=dna2[char]:
            hamming+=1
    return hamming
            
def get_dna_complement(dna):
    rev= ''
    revcomp= ''
    for char in range(len(dna)):
        rev+=str(dna[-char-1])
    print(rev)
    for char in range(len(rev)):
        if str(rev[char]) in 'Aa':
            revcomp+= 'T'
        if str(rev[char]) in 'Tt':
            revcomp+= 'A'
        if str(rev[char]) in 'Cc':
            revcomp+= 'G'
        if str(rev[char]) in 'Gg':
            revcomp+= 'C'
    return revcomp

