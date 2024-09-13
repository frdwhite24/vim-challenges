# NOTE: the starting point of each challenge is in Normal mode on column 0 of
# the challenge statement i.e. on the # in "# Challenge 03-1"

# Challenge 03-1: Increase the variable "constant" by 5 without leaving normal mode
def apply_constant(value):
    constant = 3
    return value * constant

print(apply_constant(5))

# Challenge 03-2: Sort this list of items alphabetically
nouns = [
# banana,
# zebra,
# apple,
# monkey,
# grape,
# elephant,
# cherry,
# kite,
]

# Challenge 03-3: Uncomment the list of items above without moving your cursor off the
# starting position of this challenge

# Challenge 03-4: Uncomment the lines in the function below without moving your cursor
# off the starting position of this challenge
def modify_numbers(num_list, factor):
    result = []
    
    for num in num_list:
        # multiplied = num * factor
        squared = num ** 2
        # divided = multiplied / 2
        # result.append(squared + divided)

    # result.reverse()
    return result

print(modify_numbers([2, 4, 6, 8], 3))

# Challenge 03-5: Rename "boban" to "bobanita", but only for lines that aren't
# commented out. Again, you must not move your cursor off the starting position

#boban = None
#toUpper(boban)
boban = 1
c = boban
#toLower(boban)

# Challenge 03-6: Put all of the items in the array below onto the same line, including
# the brackets
car_brands = [
    "Toyota",
    "Honda",
    "Ford",
    "BMW",
    "Tesla"
]

# Challenge 03-7: Delete all blank lines in the code below without moving the cursor.
def clean_list(items):
    
    cleaned = []
    
    for item in items:
        if item:
            cleaned.append(item)
            
    return cleaned

# Challenge 03-8: Replace the first "a - b" occurrence with "a + b" and change
# the "inner" property on dict_example to be equal to 3, instead of "[3, 4]"
def calculate(a, b):
    result = ((a + b) * (a - b)) / (a + (b * (a - b)))
    
    nested_list = [1, [2, [3, 4]], 5]
    
    dict_example = {
        "first": [1, 2],
        "second": {"inner": [3, 4]},
        "third": (5, 6)
    }
    
    return result, nested_list, dict_example

print(calculate(10, 2))

