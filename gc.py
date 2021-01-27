from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search
from Bio import SeqIO



arquivo = open("rosalindgc.fasta", "r")
for i in SeqIO.parse(arquivo, "fasta"):
    print(GC(arquivo))
