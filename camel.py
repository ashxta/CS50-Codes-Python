camel_case_name = input("Enter a camel case variable name: ")
snake_case_name = ''
for char in camel_case_name:
    if char.isupper():
        snake_case_name += '_'
        snake_case_name += char.lower()
    else:
        snake_case_name += char
snake_case_name = snake_case_name.lstrip('_')
print("Snake case name:", snake_case_name)
