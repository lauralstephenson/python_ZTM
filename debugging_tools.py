# debugging tools
# use print after each line in buggy code
# use pdb, the python debugger
import pdb


def add(num1, num2):
    # use pdb.set_trace() to walk through your
    # code in the command line
    pdb.set_trace()
    return num1 + num2


# obviously a bug, have a string and an int
add(4, "where")
