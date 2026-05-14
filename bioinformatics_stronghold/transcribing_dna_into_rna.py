#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t:formed by replacing all occurrences of 'T' in t with 'U' 

DNA = ''
def transcription (DNA):
  RNA = '' # Initialize RNA as an empty string
  for base in DNA :
    if base == 'T':
      RNA += 'U' # Append 'U' if base is 'T'
    else :
      RNA += base # Apend base as is 
  return RNA
print(transcription(DNA))
