def proteins(strand):
    '''
    strand: string, chain of codons to be converted into a protein sequence
    returns: list of strings, see README
    '''
    codon_indices = range(3, len(strand) + 1, 3)
    codon_dict = {'AUG':'Methionine', 'UUU':'Phenylalanine',
                  'UUC':'Phenylalanine', 'UUA':'Leucine', 'UUG':'Leucine', 
                  'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine',
                  'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine', 
                  'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan',
                  'UAA':'STOP', 'UAG':'STOP', 'UGA':'STOP'}
    protein_list = []
    for index in codon_indices:
        protein = codon_dict[strand[(index-3):index]]
        if protein == 'STOP':
            break
        protein_list.append(protein)
    return protein_list
