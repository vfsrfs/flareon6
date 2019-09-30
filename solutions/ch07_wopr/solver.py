from z3 import BitVec, Solver, unsat, unknown, Z3Exception


def _solve(*args, **keywords):
    s = Solver()
    s.set(**keywords)
    s.add(*args)
    if keywords.get('show', False):
        print(s)
    r = s.check()
    if r == unsat:
        print("no solution")
    elif r == unknown:
        print("failed to solve")
        try:
            return s.model()
        except Z3Exception as e:
            print(e)
            return
    else:
        return s.model()


def get_solution():
    x = [BitVec(f"x{i}", 8) for i in range(16)]
    b = [115, 29, 32, 68, 106, 108, 89, 76, 21, 71, 78, 51, 75, 1, 55, 102]

    equations = [
        b[0] == x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[11] ^ x[14],
        b[1] == x[0] ^ x[1] ^ x[8] ^ x[11] ^ x[13] ^ x[14],
        b[2] == x[0] ^ x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[8] ^ x[9] ^ x[10] ^ x[13] ^ x[14] ^ x[15],
        b[3] == x[5] ^ x[6] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[15],
        b[4] == x[1] ^ x[6] ^ x[7] ^ x[8] ^ x[12] ^ x[13] ^ x[14] ^ x[15],
        b[5] == x[0] ^ x[4] ^ x[7] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[13] ^ x[14] ^ x[15],
        b[6] == x[1] ^ x[3] ^ x[7] ^ x[9] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[15],
        b[7] == x[0] ^ x[1] ^ x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[10] ^ x[11] ^ x[14],
        b[8] == x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[12],
        b[9] == x[6] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[15],
        b[10] == x[0] ^ x[3] ^ x[4] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[14] ^ x[15],
        b[11] == x[0] ^ x[2] ^ x[4] ^ x[6] ^ x[13],
        b[12] == x[0] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[12] ^ x[15],
        b[13] == x[2] ^ x[3] ^ x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[11] ^ x[12] ^ x[13] ^ x[14],
        b[14] == x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[7] ^ x[11] ^ x[13] ^ x[14] ^ x[15],
        b[15] == x[1] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[13] ^ x[15]
    ]


    model = _solve(equations)
    solution = []
    for x_i in x:
        solution += [model[x_i].as_long().real]
    print(f"launch code: {bytes(solution)}")
    print(f"(as array: {solution})")
    return solution

get_solution()
