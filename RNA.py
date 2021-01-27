from Bio.Seq import Seq

arquivo=open('rosalind_rna.txt').readline()
sequencia=Seq(arquivo)
rna=sequencia.transcribe()
print(rna)
