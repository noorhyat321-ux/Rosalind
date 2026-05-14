#The Secondary and Tertiary Structures of DNA
#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol .
DNA = 'add here'
def complementary_strand(DNA):
  complementary = ''
  for base in DNA :
    if base == 'A':
      complementary += 'T'
    elif base == 'T':
      complementary += 'A'
    elif base == 'G':
      complementary += 'C'
    elif base == 'C':
      complementary += 'G'
  complementary = complementary[::-1] # Reverse the entire string after the loop
  return complementary
print(complementary_strand(DNA))
