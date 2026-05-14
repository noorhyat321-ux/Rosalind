#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers  counting the number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

DNA =''
def nucleotide_numbers(DNA):
  a_count= DNA.count('A')
  c_count= DNA.count('C')
  g_count= DNA.count('G')
  t_count= DNA.count('T')
  return a_count, c_count, g_count, t_count

# Call the function and print its result in the desired format
a, c, g, t = nucleotide_numbers(DNA)
print(f"{a} {c} {g} {t}")
