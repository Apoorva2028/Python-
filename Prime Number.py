import math

def is_prime(number):
    """Returns True if number is prime, otherwise returns False."""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    print("Prime Number Checker and Prime List Generator")
    while True:
        try:
            num = int(input("Enter a number to check if it's prime: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
            
            # Generate and display all primes up to the entered number
            primes = [i for i in range(2, num + 1) if is_prime(i)]
            print(f"Prime numbers up to {num}: {', '.join(map(str, primes))}")
            break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == '__main__':
    main()
