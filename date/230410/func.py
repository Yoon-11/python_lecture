def gcd(n1, n2):
    gcd = 1
    k = 2

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd

    # Check whether number is prime


def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            divisor += 1

    return True  # number is prime


def printPrimeNumbers(numberOfPrimes):
    NUMBER_OF_PRIMES = 50  # Number of primes to display
    NUMBER_OF_PRIMES_PER_LINE = 10  # Display 10 per line
    count = 0  # Count the number of prime numbers
    number = 2  # A number to be tested for primeness

    # Repeatedly find prime numbers
    while count < numberOfPrimes:
        # Print the prime number and increase the count
        if isPrime(number):
            count += 1  # Increase the count

            print(number, end=" ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
                # Print the number and advance to the new line
                print()

        # Check if the next number is prime
        number += 1


def main():
    print("The first 50 prime numbers are")
    printPrimeNumbers(50)


main()  # Call the main function

