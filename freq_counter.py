def frequency_counter(numbers):
    
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 2]
print(frequency_counter(numbers))                