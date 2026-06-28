start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sum_primes = 0
print("Prime numbers:")
for num in range(start, end+1):
    if is_prime(num):
        print(num, end=" ")
        sum_primes += num

print(f"\nSum of primes = {sum_primes}")