#explanation: Use a modified Fibonacci sequence where each pair produces k offspring pairs.

n, k = map(int, input().split())
a, b = 1, 1
for i in range(n - 2):
    a, b = b, b + (a * k)
print(b)
