#explanation: Calculate the Hamming distance (number of differing characters) between two strings of equal length.

s1 = input()
s2 = input()
print(sum(1 for a, b in zip(s1, s2) if a != b))
