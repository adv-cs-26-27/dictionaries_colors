"""
=================================================================
            DICTIONARY PRACTICE feat. TERMINAL COLORS
=================================================================

ANSI escape sequences are special strings that tell the terminal to 
change how text looks (color, bold, underline, etc.) instead of 
printing as normal characters

structure:
"\033["  +  a code number  +  "m"
ex. "\033[31m" turns the text after it red

resetting:
"\033[0m" turns all the formatting back off
ALWAYS reset at the end, or everything printed afterward stays colored!

ex. print("\033[31m" + "danger!" + "\033[0m")   prints  danger!  in red

common codes:
    30 black    31 red      32 green    33 yellow
    34 blue     35 magenta  36 cyan     37 white
    1  bold     4  underline

careful!
printing a whole list or dictionary shows the codes as text ('\x1b[31m'),
not as colors. print one string at a time to see the colors.
"""

# This dictionary maps color names to their ANSI escape sequences
COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "reset": "\033[0m"
}

#--------------------------------------------------------------#
# PART 1: WARM-UP
#--------------------------------------------------------------#

"""
TODO:
1. Using the COLORS dictionary (not by typing the codes yourself!),
   print the word "Hello" in blue.
2. Add a new key/value pair to COLORS for "magenta". Its code is 35.
3. Add another key/value pair for "bold". Its code is 1.
4. Print the word "Dictionaries" in magenta.
"""

# TODO: your code here


#--------------------------------------------------------------#
# PART 2: colorize
#--------------------------------------------------------------#

"""
TODO: Write a function colorize(text, color) that takes a string text
and a string color, and returns text wrapped in that color's code
and the reset code.

If color is not a key in COLORS, return text unchanged.

ex. colorize("hi", "red") should return "\033[31mhi\033[0m"
"""

def colorize(text, color):
    # TODO: your code here
    pass

# colorize tests
def test_colorize():
    """ Tests for colorize """
    print( "colorize('hi', 'red')     == '\\033[31mhi\\033[0m'  should be True :",  colorize('hi', 'red') == '\033[31mhi\033[0m' )
    print( "colorize('go', 'green')   == '\\033[32mgo\\033[0m'  should be True :",  colorize('go', 'green') == '\033[32mgo\033[0m' )
    print( "colorize('', 'blue')      == '\\033[34m\\033[0m'    should be True :",  colorize('', 'blue') == '\033[34m\033[0m' )
    print( "colorize('plain', 'pink') == 'plain'              should be True :",  colorize('plain', 'pink') == 'plain' )   # not a key!
    print( "colorize('plain', '')     == 'plain'              should be True :",  colorize('plain', '') == 'plain' )
    print( "this should look yellow :",  colorize('yellow text', 'yellow') )   # check with your eyes!

# TODO: call the test function here to check your work!

#--------------------------------------------------------------#
# PART 3: grade_report
#--------------------------------------------------------------#

"""
TODO: Write a function grade_report(scores) that takes a dictionary
mapping student names to test scores. For each student, print one line
like "Ana: 92", colored based on the score:

    90 or above  -> green
    70 to 89     -> yellow
    below 70     -> red

The function should also RETURN the number of students who scored
70 or above.

Hint: use your colorize function!
"""

def grade_report(scores):
    # TODO: your code here
    pass


# grade_report tests
def test_grade_report():
    """ Tests for grade_report """
    class_scores = {"Ana": 92, "Ben": 78, "Cleo": 65, "Dev": 90, "Eli": 70}
    print( "grade_report(class_scores) should print 5 colored lines, then return 4 :" )
    print( grade_report(class_scores) )   # Ana and Dev green, Ben and Eli yellow, Cleo red

    print( "grade_report({'Zoe': 100}) should return 1 :",  grade_report({'Zoe': 100}) )
    print( "grade_report({'Max': 12})  should return 0 :",  grade_report({'Max': 12}) )
    print( "grade_report({})           should return 0 :",  grade_report({}) )   # empty dictionary!

# TODO: call the test function here to check your work!

#--------------------------------------------------------------#
# PART 4: count_colors
#--------------------------------------------------------------#

"""
TODO: Write a function count_colors(words) that takes a list of words
and returns a dictionary that counts how many times each color name
from COLORS appears in the list. Words that are not color names
should be ignored. "reset" and "bold" should also be ignored.

ex. count_colors(["red", "cat", "red", "blue"]) should return
    {"red": 2, "blue": 1}

Then, print each color's count IN THAT COLOR, one per line.
(Do the printing outside the function, below the tests.)
"""

def count_colors(words):
    # TODO: your code here
    pass

# count_colors tests
def test_count_colors():
    """ Tests for count_colors """
    print( "count_colors(['red', 'cat', 'red', 'blue'])  should be {'red': 2, 'blue': 1} :",  count_colors(['red', 'cat', 'red', 'blue']) )
    print( "count_colors(['green', 'green', 'green'])   should be {'green': 3} :",  count_colors(['green', 'green', 'green']) )
    print( "count_colors(['dog', 'pink', 'tree'])       should be {} :",  count_colors(['dog', 'pink', 'tree']) )   # no colors
    print( "count_colors(['reset', 'bold', 'red'])      should be {'red': 1} :",  count_colors(['reset', 'bold', 'red']) )   # not real colors
    print( "count_colors([])                            should be {} :",  count_colors([]) )

# TODO: call the test function here to check your work!

# Now use count_colors to print each count in its own color for the following list:
favorite_colors = ["blue", "red", "blue", "green", "pizza", "blue", "red", "yellow"]

# TODO: your code here

#--------------------------------------------------------------#
# PART 5: pairs_to_dict
#--------------------------------------------------------------#

"""
TODO: Write a function pairs_to_dict(pairs) that takes a nested list,
where each inner list has two items: a name and a color. It should
return a dictionary mapping each name to its color.

If a name shows up more than once, the LAST color wins.

ex. pairs_to_dict([["Ana", "red"], ["Ben", "blue"]]) should return
    {"Ana": "red", "Ben": "blue"}

Then, use your dictionary to print each student's name in their
favorite color. (Do the printing outside the function, below the tests.)
"""

def pairs_to_dict(pairs):
    # TODO: your code here
    pass

# pairs_to_dict Tests
def test_pairs_to_dict():
    """ Tests for pairs_to_dict """
    print( "pairs_to_dict([['Ana', 'red'], ['Ben', 'blue']])   should be {'Ana': 'red', 'Ben': 'blue'} :",  pairs_to_dict([['Ana', 'red'], ['Ben', 'blue']]) )
    print( "pairs_to_dict([['Cleo', 'green']])                 should be {'Cleo': 'green'} :",  pairs_to_dict([['Cleo', 'green']]) )
    print( "pairs_to_dict([['Ana', 'red'], ['Ana', 'green']])  should be {'Ana': 'green'} :",  pairs_to_dict([['Ana', 'red'], ['Ana', 'green']]) )   # last one wins
    print( "pairs_to_dict([])                                  should be {} :",  pairs_to_dict([]) )

# TODO: call the test function here to check your work!

# Now print each student's name in their favorite color:
favorite_pairs = [["Ana", "red"], ["Ben", "blue"], ["Cleo", "green"], ["Dev", "yellow"]]

# TODO: your code here


#--------------------------------------------------------------#
# PART 6: draw_grid
#--------------------------------------------------------------#

"""
TODO: Write a function draw_grid(grid) that takes a nested list of
color names and draws it as pixel art. Each row of the grid should
print on its own line, and each item should print as "██" in that color.

Items that aren't colors in COLORS (like "") should print as two
spaces "  " instead. "reset" and "bold" count as not-colors too.

The function should also RETURN a dictionary counting how many
pixels of each color were drawn. Blank spaces are not counted.

ex. draw_grid([["red", "blue"], ["", "red"]]) should print:
    ████          (the first block in red, the second in blue)
      ██          (two spaces, the second block in red)
    and return {"red": 2, "blue": 1}

Hint: build up each row as a string, then print the whole row at once.
"""

def draw_grid(grid):
    # TODO: your code here
    pass

# a grid to test with
test_grid = [
    ["",       "yellow", "yellow", "yellow", ""      ],
    ["yellow", "blue",   "yellow", "blue",   "yellow"],
    ["yellow", "yellow", "yellow", "yellow", "yellow"],
    ["yellow", "red",    "red",    "red",    "yellow"],
    ["",       "yellow", "yellow", "yellow", ""      ]
]

# draw_grid tests
def test_draw_grid():
    """ Tests for draw_grid """
    print( "draw_grid(test_grid) should draw a test_grid face, then return {'yellow': 16, 'blue': 2, 'red': 3} :" )
    print( draw_grid(test_grid) )

    print( "draw_grid([['red', 'green']]) should draw 2 pixels, then return {'red': 1, 'green': 1} :" )
    print( draw_grid([['red', 'green']]) )

    print( "draw_grid([['', 'pink'], ['red', '']]) should draw 1 pixel, then return {'red': 1} :" )   # pink isn't in COLORS
    print( draw_grid([['', 'pink'], ['red', '']]) )

    print( "draw_grid([]) should draw nothing, then return {} :" )
    print( draw_grid([]) )

# TODO: call the test function here to check your work!

#--------------------------------------------------------------#
# EXTENSION 1: rainbow
#--------------------------------------------------------------#

"""
TODO: Write a function rainbow(text) that returns text with each
character in a different color, cycling through this list in order:

    ["red", "yellow", "green", "blue", "magenta"]

Only add one reset code, at the very end.

ex. rainbow("hi") should return "\033[31mh\033[33mi\033[0m"
"""

def rainbow(text):
    # TODO: your code here
    pass

# rainbow tests
def test_rainbow():
    """ Tests for rainbow """
    print( "rainbow('hi')  == '\\033[31mh\\033[33mi\\033[0m' should be True :",  rainbow('hi') == '\033[31mh\033[33mi\033[0m' )
    print( "rainbow('')    == '\\033[0m'                     should be True :",  rainbow('') == '\033[0m' )
    print( "this should look like a rainbow :",  rainbow('Dictionaries are awesome!') )


#--------------------------------------------------------------#
# EXTENSION 2: swap_colors
#--------------------------------------------------------------#

"""
TODO: Write a function swap_colors(grid, swaps) that takes a nested
list of color names and a dictionary mapping old colors to new colors.
It should return a NEW grid where every color that is a key in swaps
is replaced with its value. Colors that aren't keys stay the same.

Two important rules:
    1. Don't change the original grid! Build a brand new nested list.
    2. Each pixel is only swapped once. With {"red": "blue", "blue": "red"},
       red pixels become blue and blue pixels become red.

ex. swap_colors([["red", "blue"]], {"blue": "yellow"}) should return
    [["red", "yellow"]]

When your tests pass, use swap_colors and draw_grid together to draw
the test_grid with a green face and red eyes!
"""

def swap_colors(grid, swaps):
    # TODO: your code here
    pass

# swap_colors tests
def test_swap_colors():
    """ Tests for swap_colors """
    original = [["red", "blue"], ["blue", "green"]]
    print( "swap_colors(original, {'blue': 'yellow'})           should be [['red', 'yellow'], ['yellow', 'green']] :",  swap_colors(original, {'blue': 'yellow'}) )
    print( "swap_colors([['red', 'blue']], {'red': 'blue', 'blue': 'red'}) should be [['blue', 'red']] :",  swap_colors([['red', 'blue']], {'red': 'blue', 'blue': 'red'}) )   # each pixel only swapped once
    print( "swap_colors([['', 'red']], {'red': 'green'})        should be [['', 'green']] :",  swap_colors([['', 'red']], {'red': 'green'}) )
    print( "swap_colors(original, {})                           should be [['red', 'blue'], ['blue', 'green']] :",  swap_colors(original, {}) )   # nothing to swap
    print( "swap_colors([], {'red': 'blue'})                    should be [] :",  swap_colors([], {'red': 'blue'}) )
    print( "original after all those swaps                      should be [['red', 'blue'], ['blue', 'green']] :",  original )   # unchanged!

# Now draw the test_grid with a green face and red eyes:

# TODO: your code here