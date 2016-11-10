'''
Runs the WalkSAT algorithm as implemented by aima-python. 
The algorithm is run on a randomly generated set of clauses.

The clauses are generated according to command-line parameters

@author: Matthew Wolff
'''

import logic
import sys
import string
import random

def main():
    if len(sys.argv) != 4:
        print("Usage: Main n m k")
        sys.exit(1)
    # remember that argv[0] is the script's name (in this case probably Main)
    # number of distinct propositional symbols
    # symbols must be alphabetic, capitals are distinct
    n = int(sys.argv[1])
    # number of clauses. A clause is either a literal or an OR'd sequence of literals
    m = int(sys.argv[2])
    # maximum number of literals in a clause
    k = int(sys.argv[3])
    
    if n>len(string.ascii_uppercase):
        print("Error: too many symbols supplied. Symbols must fit in [A-Z].")
        sys.exit(2)
    
    # list of generated symbols
    syms = []
    for i in range(n):
        syms += [logic.Symbol(string.ascii_uppercase[i])]
    
    # list of generated clauses
    clauses = []
    # create each clause
    for i in range(m):
        # determine how many literals will be in this clause
        num_lits = random.randrange(1,k)
        ors = []
        for j in range(num_lits):
            orterm = syms[random.randrange(len(syms))]
            # have some terms be negated
            ors += [orterm] if random.randint(0,1) else [~orterm]
        # or those terms together
        clause = ors[0]
        for l in range(1, num_lits):
            clause = clause | ors[l]
        clauses += [clause]
        
    print("Clauses:")
    for clause in clauses:
        print(clause)
        
    # Run WalkSAT on those clauses
    result = logic.WalkSAT(clauses, 0.5, 100)
    
    if (result == None):
        print("failure")
    else:
        print(result)

if __name__ == '__main__':
    main()
