# -*- coding: utf-8 -*-

class io(object):
    """docstring for io."""
    def __init__(self, parent):
        super(io, self).__init__()
        self.__parent = parent

    def read_fasta(self, fastafilename):
        d = {}
        f = open(fastafilename, "r")
        lines = f.readlines()
        f.close()
        key, dna = "", ""
        for line in lines:
            if line.startswith(">"):
                key = line[1:].replace("\n", "")
                d[key] = ""
            else :
                d[key] += line.replace("\n", "")
        return d

    def write_fasta(self, fastafilename, data):
        def split_by_size(s, size=60, sep="\n"):
            out = ""
            for k in range(int(len(s)//size)):
                out += s[k*size:(k+1)*size] + sep
            out += s[int(len(s)//size)*size:] + sep
            return out
        if not fastafilename.lower().endswith(".fasta"):
            fastafilename += ".fasta"
        f = open(fastafilename, "w")
        for key in data:
            f.write(">" + key + "\n")
            f.write(data[key] + "\n")
        f.close()

    def read_fastq(self, fastqfilename):
        pass

    def write_fastq(self, fastqfilename):
        pass
