first_strings = [
    'Elon', 'Musk', 'Programmer', 
    'Monitors', 'Variable'
    ]
second_strings = [
    'Task', 'Git', 'Comprehension', 
    'Java', 'Computer', 'Assembler'
    ]

first_result = [
    len(name)
    for name in first_strings
    if len(name) >= 5
    ]

second_result = [
    (first_name, second_name)
    for first_name in first_strings
    for second_name in second_strings
    if len(first_name) == len(second_name)
    ]

third_result = {
    name: len(name)
    for name in (first_strings + second_strings)
    if len(name) % 2 == 0
    }

print(first_result)
print(second_result)
print(third_result)
