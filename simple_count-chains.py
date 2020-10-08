from typing import List, Tuple
import math


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    num = len(circles)
    for i, circ1 in enumerate(circles):
        for j in range(i+1, len(circles)):
            # d = math.sqrt((circ1[0] - circles[j][0]) ** 2 + (circ1[1] - circles[j][1]) ** 2)
            d = ((circ1[0] - circles[j][0]) ** 2 + (circ1[1] - circles[j][1]) ** 2) ** (1 / 2)
            print(circ1, circles[j])
            if d < circ1[2] + circles[j][2]  and d != circ1[2] and d != circles[j][2]:
                print('d=',d)
                num -= 1

    print('num = ', num)
    return num if num > 0 else 1


if __name__ == '__main__':
    print("Example:")
    # print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))
    print(count_chains([[0,0,2],[1,0,3],[3,0,1],[2,1,1],[-2,-2,1],[0,0,4],[-3,0,1]]))
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    # assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    # assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    # assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    # assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    # assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    # print("Coding complete? Click 'Check' to earn cool rewards!")
