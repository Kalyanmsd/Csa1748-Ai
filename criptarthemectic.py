import itertools
def is_valid_solution(letters, digits):
    s, e, n, d, m, o, r, y = digits
    send = s*1000 + e*100 + n*10 + d
    more = m*1000 + o*100 + r*10 + e
    money = m*10000 + o*1000 + n*100 + e*10 + y
    return send + more == money
def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in itertools.permutations(range(10), len(letters)):
        if perm[0] != 0 and perm[4] != 0:  
            if is_valid_solution(letters, perm):
                s, e, n, d, m, o, r, y = perm
                print(f"Solution found: S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
                return
    print("No solution found")
solve_cryptarithmetic()
