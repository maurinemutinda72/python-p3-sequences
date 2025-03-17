#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the list with the first two Fibonacci numbers
    fib_list = [0, 1]
    
    # If length is 0 or 1, slice the list accordingly
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    # Generate Fibonacci numbers until the list reaches the desired length
    while len(fib_list) < length:
        # Next number is the sum of the last two numbers
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    # Print the list up to the specified length
    print(fib_list[:length])