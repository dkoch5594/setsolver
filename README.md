setsolver.py

Inspired by the following exceprt taken from Hacking: The Art of Exploitation, 2nd Edition by Jon Erickson (https://nostarch.com/hacking2.htm)
  "Use each of the numbers 1, 3, 4, and 6 exactly once with any of the four basic math operations (addition, subtraction, multiplication, and division) to total 24. 
  Each number must be used once and only once, and you may define the order of operations; for example, 3 * (4 + 6) + 1 = 31 is valid, however incorrect, since it
  doesn't total 24." (Erickson, 1)

Given a list of numbers and a desired answer, identifies all equations that use all of the numers in the list and the four basic math operations to evaluate to the 
desired answer.
