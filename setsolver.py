#!/usr/bin/python3

import argparse

def permutate(num_list):
    permutations = []
    
    for num in num_list:
        copy = num_list.copy()
        copy.remove(num)
        remainder = permutate(copy)
        if len(remainder) > 0:
                for r in remainder:
                    permutations.append([num] + r)
        else:
            permutations.append([num])
    return permutations

def getBaseEquations(num_list,op_num=1):
    operators = ["+","-","*","/"]
    equations = []

    op_index = op_num * 2 - 1
    if op_index <= len(num_list) - 1:
        for o in operators:
            copy = num_list.copy()
            copy.insert(op_index,o)
            equations += getBaseEquations(copy,op_num + 1)
    else:
        equations.append(num_list)
    return equations

def orderOperations(equation):
    ordered_equations = []

    for o in range(len(equation)-2):
        if isinstance(equation[o],float):
           open_copy = equation.copy()
           open_copy.insert(o,"(")
           for c in range(o+2,len(open_copy)):
               if isinstance(open_copy[c],float):
                   close_copy = open_copy.copy()
                   close_copy.insert(c+1,")")
                   ordered_len = len(close_copy[o+1:c+1])
                   if ordered_len > 3 and ordered_len < len(equation):
                       prelude = close_copy[:o+1]
                       postlude = close_copy[c+1:]
                       suborders = orderOperations(close_copy[o+1:c+1])
                       for s in suborders:
                           ordered_equations.append(prelude + s + postlude)
                   else:  
                       ordered_equations.append(close_copy)
    return ordered_equations

if __name__ == "__main__":

    # Add some arguments
    parser = argparse.ArgumentParser(description="Find an equation over a list of numbers that evaluates to a given answer.")
    parser.add_argument("--version", "-V", action="version", version="%(prog)s 1.0")
    parser.add_argument("numbers", nargs="+", metavar="N", type=float, help="List of numbers to base use in equation")
    parser.add_argument("--answer", "-a", "-A", metavar="ANSWER", type=float, required=True, help="Desired answer to equation")

    # parse the arguments
    args = parser.parse_args()
    print("SET: ",args.numbers)
    print("ANSWER: ",args.answer)

    perms = permutate(args.numbers)
    print("Found {} permutations of the set".format(len(perms)))

    base_eqs = []
    for p in perms:
        base_eqs += getBaseEquations(p)
    print("Found {} base equations".format(len(base_eqs)))

    ordered_eqs = []
    for be in base_eqs:
        ordered_eqs += orderOperations(be)
    print("Found {} ordered equations".format(len(ordered_eqs)))
   
    solutions = []
    for oe in ordered_eqs:
        for i in range(len(oe)):
            oe[i] = str(oe[i])

        evaluatee = "".join(oe)
        try:
            if eval(evaluatee) == args.answer:
                solutions.append(evaluatee)
        except ZeroDivisionError:
            continue

    print("Found {} solutions".format(len(solutions)))
    for s in solutions:
        print(s)


