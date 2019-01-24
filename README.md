# BioInfoUtils library

[![Build Status](https://travis-ci.org/RemiGascou/bioinfoutils.svg?branch=master)](https://travis-ci.org/RemiGascou/bioinfoutils)
[![PyPi Version](https://badge.fury.io/py/bioinfoutils.svg)](https://badge.fury.io/py/bioinfoutils.svg)

Some algorithms needed in bioinformatics to process data.

## Installation

```python
pip install bioinfoutils
```

## Formats supported

Supports FASTA and FASTQ formats.

## Algorithms

```python
from bioinfoutils.algorithms import *
```

Algorithms :

```python
GC_content(dna)
dna_to_protein(dna)
protein_mass(prot)
```


## Input Outputs (IO)

```python
from bioinfoutils.io import *
```

Methods :

```python
file_read_fasta(fastafilename)
file_write_fasta(fastafilename, data)
file_read_fastq(fastqfilename)
file_write_fastq(fastqfilename, data)
fasta_to_fastq(fasta_in, fastq_out)
fastq_to_fasta(fastq_in, fasta_out)
file_fasta_to_fastq(data)
file_fastq_to_fasta(data)
```



---

## Developpers

### Run unit tests

To run unit tests :

```bash
make tests
```
