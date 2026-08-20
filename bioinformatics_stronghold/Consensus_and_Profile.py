# explanation: Given multiple DNA strings, create a profile matrix of nucleotide counts at each position and derive the consensus string.

import numpy as np
# 1. Store sequences in a 2D array
# 2. For each column, count A, C, G, T
# 3. Consensus = base with the highest count in that column
