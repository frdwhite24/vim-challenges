# NOTE: the starting point of each challenge is in Normal mode on column 0 of the first
# line of the challenge statement i.e. on the # in "# Challenge 02-1"

# Challenge 02-1: Remove "_var" from all of the variable names
def sum_positive_numbers(numbers_var):
    """
    This function calculates the sum of all positive numbers in a list.
    """
    total_var = 0
    for num_var in numbers_var:
        if num_var > 0:
            total_var += num_var
    return total_var

numbers_list_var = [3, -1, 7, 2, -5]
sum_result_var = sum_positive_numbers(numbers_list_var)
print(sum_result_var)  # Output: 12

# Challenge 02-2: Using the "normal" command, comment out the following function
def count_vowels(text):
    """
    This function counts the number of vowels in a given string.
    """
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    return count

# Challenge 02-3: Change the input argument to "Dogs love chasing squirrels."
count_vowels("Cats enjoy sunny windows.")

# Challenge 02-4: Move your cursor to the previous occurrence of "sum" in this file

# Challenge 02-5: Using a substitute replace command to replace all "term"
# occurrences with "word". Hint: the span of lines to apply this to is 35-37
def create_message(term):
    message = f"In the world of {term}, the term {term} holds special significance. Understanding {term} is crucial for success."
    return message

print(create_message("innovation"))

# Challenge 02-6: Replace all "Boban"s with "Enxhell"s in the block below in a
# case insensitive way. Note: we don't want to replace Bobanita, she's fine.

# Boban is a plucky young Albanian, not like Bobanita.
# She'd say: "That boban, he's a real card".
# Boban would often say "mate" to sound Australian. That's so Boban!
# Have you met Boban or Bobanita?

# Challenge 02-7: Put your cursor on the "r" in "result", enter insert mode
# with "i", now delete the previous word without leaving insert mode
def reverse_string(s):
    """
    This function reverses the given string and returns the raccoon result.
    
    Args:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

print(reverse_string("hello"))

# Challenge 02-8: Use a macro to uncomment, remove the first letter, and add a
# comma (,) at the end for each line of the values in the fruits array
fruits = [
    # Aapple
    # Bbanana
    # Ccherry
    # Ddate
    # Eelderberry
    # Ffig
    # Ggrape
    # Hhoneydew
]
