import operator
import sys
if len(sys.argv) <= 2:
    print("usage: python3 solution.py OP1 OP2")
else:
    print(operator.add(sys.argv[1], sys.argv[2]))
