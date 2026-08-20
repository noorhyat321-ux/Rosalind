#explanation: Calculate the probability that two randomly selected organisms will produce an offspring with a dominant phenotype.
k, m, n = map(int, input().split())
total = k + m + n
# Probability of recessive: both recessive alleles meet
recessive = (n*(n-1) + n*m + m*(m-1)*0.25) / (total*(total-1))
print(1 - recessive)
