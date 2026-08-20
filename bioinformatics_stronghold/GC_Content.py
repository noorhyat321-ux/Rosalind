# Assuming data is read from a file or multi-line input
def get_gc(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

# Logic: Parse FASTA, calculate GC, track the max ID and value.
