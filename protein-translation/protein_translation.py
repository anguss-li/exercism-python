from typing import List

CODONS = {**{codon: 'Methionine' for codon in ('AUG',)},
          **{codon: 'Phenylalanine' for codon in ('UUU', 'UUC')},
          **{codon: 'Leucine' for codon in ('UUA', 'UUG')},
          **{codon: 'Serine' for codon in ('UCU', 'UCC', 'UCA', 'UCG')},
          **{codon: 'Tyrosine' for codon in ('UAU', 'UAC')},
          **{codon: 'Cysteine' for codon in ('UGU', 'UGC')},
          **{codon: 'Tryptophan' for codon in ('UGG',)},
          **{codon: 'STOP' for codon in ('UAA', 'UAG', 'UGA')}}


def proteins(strand: str) -> List[str]:
    '''Find what protein each codon in strand represents.'''
    proteins = [CODONS[strand[i-3:i]] for i in range(3, len(strand)+1, 3)]
    if 'STOP' in proteins:
        proteins = proteins[:proteins.index('STOP')]
    return proteins
