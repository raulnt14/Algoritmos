from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!

    combinaciones = My_Iterator(num_queens, num_queens)
    for c in combinaciones.next():


        setC = set(c)
        setDiagonal45 = set()
        setDiagonal135 = set()
        if (len(c) == len(setC)):
            for i in range(num_queens):
                setDiagonal45.add(c[i]-i)
                if (len(c) == len(setDiagonal45)):
                   for i in range(num_queens):
                        setDiagonal135.add(c[i] + i)
                        if (len(c) == len(setDiagonal135)):
                            solutions_list.append(c)

    return solutions_list