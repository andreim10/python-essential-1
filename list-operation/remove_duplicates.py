#We remove duplicates from the list while preserving the original order.
def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique

#We remove duplicates from the list without preserving the original order.
def remove_duplicates_pythonic(numbers):
    return list(set(numbers))


if __name__ == "__main__":
    data = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

    print("The original list:", data)
    print("Duplicate list with order preserved:", remove_duplicates(data))
    print("Duplicate list with order not preserved:", remove_duplicates_pythonic(data))
