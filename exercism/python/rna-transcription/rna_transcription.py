def to_rna(dna_strand):
    rna_str=''
    for i in range(len(dna_strand)) :
        if dna_strand[i] not in ['C','G','T','A'] :
            raise ValueError('Could not find %c in CGTA' %dna_strand[i])
        elif dna_strand[i] is 'C' :rna_str+='G'
        elif dna_strand[i] is 'G' : rna_str+='C'
        elif dna_strand[i] is 'T' : rna_str+='A'
        elif dna_strand[i] is 'A' : rna_str+='U'
    return rna_str
