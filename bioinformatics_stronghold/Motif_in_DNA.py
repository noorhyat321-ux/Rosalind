#explanation: Find all 1-based start positions where a substring (motif) occurs in a main string.

s = input()
t = input()
for i in range(len(s)):
    if s[i:].startswith(t):
        print(i + 1, end=" ")
