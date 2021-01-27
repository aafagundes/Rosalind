from Bio.Seq import Seq

arquivo=open('rosalind_revc.txt').readline()
sequencia=Seq(arquivo)
revc=sequencia.reverse_complement()
print(revc)
