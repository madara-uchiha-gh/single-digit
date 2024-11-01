from unicodedata import digit


def digit_number(n):
    y=0
    while n >= 10:
        n = sum(int(digit)for digit in str (n))
        return n
n=int(input())
for i in range (n):
    n = sum(int(digit) for digit in str(n))
print(n)








































