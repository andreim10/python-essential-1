def bubble_sort(numbers):
    #sort a list using the bubble sort algorithm
    n = len(numbers) #returns the length, the number of elements
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers

 #Read the numbers to be sorted from the user.
def get_numbers_from_user():
    count = int(input("How many numbers do you want to be sorted?"))
    numbers = [float(input("Number {i + 1}: ")) for i in range(count)]
    return numbers

#The main part of the program, where the functions defined above are executed.
if __name__ == "__main__":
    data = get_numbers_from_user()
    print("The entered list:", data)
    sorted_data = bubble_sort(data)
    print("Sorted list:", sorted_data)
