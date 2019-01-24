# -*- coding: utf-8 -*-

class algorithms(object):
    """docstring for algorithms."""
    def __init__(self, parent):
        super(algorithms, self).__init__()
        self.__parent = parent

    def GC_content(self, dna):
        """
            @params String dna or dna as a list of ACGT
            @returns float GC content between 0 and 100
        """
        dna = dna.upper()
        if len(dna) == 0:
            return 0
        else :
            return ((dna.count('G')+dna.count('C'))/len(dna))*100

    def dna_to_protein(self, dna):
        """
            @params String dna or dna as a list of ACGT
            @returns String protein
        """
        prot, dna = "", dna.upper()
        for k in range(int(len(dna)/3)):
            prot += self.__parent.data.rna_codon_table[dna[3*k:3*(k+1)]]
        return prot

    def protein_mass(self, prot):
        """
            @params String protein or protein as a list of ACDEFGHIKLMNPQRSTVWY
            @returns String protein
        """
        totalmass, prot = 0, prot.upper().replace("START", "").replace("STOP", "")
        for c in prot:
            totalmass += self.__parent.data.protein_mass[c]
        return totalmass
