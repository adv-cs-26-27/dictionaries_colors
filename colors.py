"""
=================================================================
  DICTIONARIES + TERMINAL COLORS
=================================================================

ANSI escape sequence notes!

definition:
special strings that tell the terminal to change how text looks
(color, bold, underline, etc.) instead of printing as normal characters

how they're built:
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

#
# colorize Tests
#
def colorizeTests():
    print( "colorize('hi', 'red')     == '\\033[31mhi\\033[0m'  should be True :",  colorize('hi', 'red') == '\033[31mhi\033[0m' )
    print( "colorize('go', 'green')   == '\\033[32mgo\\033[0m'  should be True :",  colorize('go', 'green') == '\033[32mgo\033[0m' )
    print( "colorize('', 'blue')      == '\\033[34m\\033[0m'    should be True :",  colorize('', 'blue') == '\033[34m\033[0m' )
    print( "colorize('plain', 'pink') == 'plain'              should be True :",  colorize('plain', 'pink') == 'plain' )   # not a key!
    print( "colorize('plain', '')     == 'plain'              should be True :",  colorize('plain', '') == 'plain' )
    print( "this should look yellow :",  colorize('yellow text', 'yellow') )   # check with your eyes!

# TODO: call the test function to confirm your function works correctly!

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

#
# grade_report Tests
#
def grade_report_tests():
    class_scores = {"Ana": 92, "Ben": 78, "Cleo": 65, "Dev": 90, "Eli": 70}
    print( "grade_report(class_scores) should print 5 colored lines, then return 4 :" )
    print( grade_report(class_scores) )   # Ana and Dev green, Ben and Eli yellow, Cleo red

    print( "grade_report({'Zoe': 100}) should return 1 :",  grade_report({'Zoe': 100}) )
    print( "grade_report({'Max': 12})  should return 0 :",  grade_report({'Max': 12}) )
    print( "grade_report({})           should return 0 :",  grade_report({}) )   # empty dictionary!

# TODO: call the test function to confirm your function works correctly!

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

#
# count_colors Tests
#
def count_colors_tests():
    print( "count_colors(['red', 'cat', 'red', 'blue'])  should be {'red': 2, 'blue': 1} :",  count_colors(['red', 'cat', 'red', 'blue']) )
    print( "count_colors(['green', 'green', 'green'])   should be {'green': 3} :",  count_colors(['green', 'green', 'green']) )
    print( "count_colors(['dog', 'pink', 'tree'])       should be {} :",  count_colors(['dog', 'pink', 'tree']) )   # no colors
    print( "count_colors(['reset', 'bold', 'red'])      should be {'red': 1} :",  count_colors(['reset', 'bold', 'red']) )   # not real colors
    print( "count_colors([])                            should be {} :",  count_colors([]) )

# TODO: call the test function to confirm your function works correctly!

# Now print each count in its own color:
favorite_colors = ["blue", "red", "blue", "green", "pizza", "blue", "red", "yellow"]

# TODO: your code here


#--------------------------------------------------------------#
# BONUS: rainbow
#--------------------------------------------------------------#

"""
TODO: Write a function rainbow(text) that returns text with each
character in a different color, cycling through this list in order:

    ["red", "yellow", "green", "blue", "magenta"]

Only add one reset code, at the very end.

ex. rainbow("hi") should return "\033[31mh\033[33mi\033[0m"

Hint: the % operator helps you cycle back to the start of the list.
"""

def rainbow(text):
    # TODO: your code here
    pass

#
# rainbow Tests
#
def rainbowTests():
    print( "rainbow('hi')  == '\\033[31mh\\033[33mi\\033[0m' should be True :",  rainbow('hi') == '\033[31mh\033[33mi\033[0m' )
    print( "rainbow('')    == '\\033[0m'                     should be True :",  rainbow('') == '\033[0m' )
    print( "this should look like a rainbow :",  rainbow('Dictionaries are awesome!') )

# TODO: call the test function to confirm your function works correctly!
