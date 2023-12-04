def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return None

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i

    return n

while True:
    try:
        number = int(input("Enter a number greater than or equal to 2: "))
        factor = find_smallest_factor(number)
        
        if factor is not None:
            print(f"The smallest factor of {number} other than 1 is {factor}\n")
        
        if number < 2:
            break

    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")