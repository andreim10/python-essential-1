
import math    #Here we use the math module, a library containing advanced mathematical functions.

#We check if the number is prime
def is_prime(num: int) -> bool:   
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False  # Remove all even numbers

    # We only check the odd numbers up to the square root.
    limita = int(math.isqrt(num))
    for j in range(3, limita + 1, 2):
        if num % j == 0:
            return False
    return True

#Main function
def main():
    print("Prime numbers between 2 and 20:")
    for num in range(2, 21):
        if is_prime(num):
            print(num, end=" ")
    print()  #New line at the final

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
