# Challenge 01-1: Put your cursor on the second "p" in "properly"
# This function turns coffee into code, but only if you're properly caffeinated!

# Challenge 01-2: Put your cursor at the end of the word "Space" on the third line
# Jenny was working late on a project and accidentally merged a branch named
# `feature/space_invaders` into production. The next morning, her colleagues
# found the office’s code editor had transformed into a pixelated game of Space
# Invaders. Jenny grinned, “I guess the code needed a bit of a break!” The team
# spent the day trying to debug while dodging virtual aliens, turning an
# unexpected bug into an office-wide game day.

# Challenge 01-3: Change the name of this function to "sum_evens"
def sum_of_evens(numbers):
    """
    This function takes a list of integers and returns the
    sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Challenge 01-4: Replace the name "Alex" with the name "Jenny"
"""
Once upon a time, in a land filled with bugs and feature requests,
there lived a coder named Alex. Alex was known far and wide for
their ability to turn vague requirements into elegant code.

One day, Alex was tasked with building a program that could calculate
the number of jellybeans in a jar... but only if the jar was made of glass,
the jellybeans were red, and it was raining outside. Confused, yet determined,
Alex dove deep into their code editor, armed only with Python and caffeine.

Days turned into nights as Alex wrestled with edge cases like:
- What if the jar had a crack?
- What if it was drizzling, not raining?
- Could blue jellybeans be secretly disguised as red?

Finally, after what felt like an eternity, the program was done.
It didn't just count jellybeans... it counted life’s complexities.
Legend says Alex still dreams of jellybeans to this day.
"""

# Challenge 01-5: Upper case the word `very`
# That soup was very hot.

# Challenge 01-6: Delete the 2 lines of the buggy if statement
def calculate_discount(price, discount):
    """
    This function applies a discount to a price,
    but there's a buggy if statement that needs removal.
    """
    if discount < 0:  # This check is unnecessary and introduces a bug
        discount = 0
    
    final_price = price - (price * discount / 100)

    # Ensure the final price isn't negative
    if final_price < 0:
        final_price = 0
    
    return final_price

print(calculate_discount(100, 20))  # Output: 80

# Challenge 01-7: Add a comma (,) to the end of each line of this poem, apart from the last one
# In the realm of code we dive  
# Variables and loops come alive  
# Functions call, and bugs appear  
# Debugging with a cup of cheer  
# Syntax errors dance in sight  
# Fix them all, and code takes flight.

# Challenge 01-8: Move your cursor to the first line of this file.
