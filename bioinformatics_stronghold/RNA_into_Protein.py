#explanation: Translate an RNA string into an amino acid sequence using a codon table until a 'Stop' codon is reached.
codon_table = {"UUU":"F", "CUU":"L", ...} # Standard RNA Codon Table
s = input()
protein = ""
for i in range(0, len(s), 3):
    amino = codon_table[s[i:i+3]]
    if amino == "Stop": break
    protein += amino
print(protein)
