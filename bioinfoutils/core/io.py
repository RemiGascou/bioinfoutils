# -*- coding: utf-8 -*-

class io(object):
    """docstring for io."""
    def __init__(self, parent):
        super(io, self).__init__()
        self.__parent = parent

    def file_read_fasta(self, fastafilename):
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

    def file_write_fasta(self, fastafilename, data):
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

    def file_read_fastq(self, fastqfilename):
        def readheader(header):
            """@<instrument>:<run_number>:<flowcell_ID>:<lane>:<tile>:<x-pos>:<y-pos> <read>:<is_filtered>:<control_number>:<sample_number>"""
            if header.startswith("@"):
                s = header[1:].split(" ")
                data = [e for e in s[0].split(":")] + [e for e in s[1].split(":")]
                d = { "instrument" : data[0],  "run_number" : int(data[1]), "flowcell_id" : data[2],    "lane" : data[3],
                      "tile" : data[4],        "x_pos" : data[5],           "y_pos" : data[6],          "read" : data[7],
                      "is_filtered" : data[8], "control_number" : data[9],  "sample_number" : data[10]}
                return d
            else:
                return None

    def file_write_fastq(self, fastqfilename):
        pass

    def fasta_to_fastq(self, fasta_in, fastq_out):
        pass

    def fastq_to_fasta(self, fastq_in, fasta_out):
        pass

    def file_fasta_to_fastq(self):
        pass

    def file_fastq_to_fasta(self):
        pass
