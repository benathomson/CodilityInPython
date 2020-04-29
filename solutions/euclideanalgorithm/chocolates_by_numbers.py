# This is the solution for Euclidean Algorithm > Chocolate by Numbers
#
# This is marked as PAINLESS difficulty


def find_gcd(a, b):
    if a % b == 0:
        return b
    else:
        return find_gcd(b, a % b)


def solution(N, M):
    gcd = find_gcd(N, M)
    return N // gcd


print(solution(10, 4))

print(solution(9, 6))

print(solution(10, 11))

