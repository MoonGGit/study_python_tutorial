""" 2022.02.07(월)
https://www.acmicpc.net/problem/1631
1631번: 오영식의 보물

문제
오영식의 보물은 베트남의 하노이에 있는 하노이 탑(Tower of Hanoi)의 모형이다. 하노이 탑은 3개의 막대로 이루어져 있다. 막대는 왼쪽부터 차례대로 A, B, C로 이름이 매겨져 있고, N개의 디스크로 이루어져있다. N개의 디스크 크기는 1부터 N으로 차례대로 이루어져있다. 처음에 모든 디스크들은 막대 A에 놓여져있다. 디스크는 크기가 큰 것이 반드시 크기가 작은 것의 밑에 있어야 한다. 따라서 처음에는 모두 막대 A의 가장 아래에 N크기의 디스크가 있고, 가장 위에는 1크기의 디스크가 있다. 디스크를 이동할 때는 한 번에 하나씩만 이동할 수 있다.

민식이는 영식이랑 같이 하노이 탑을 이동시키면서 놀고 싶었다. 마침 둘은 처음 상태에서 모든 디스크를 C로 이동시키는 게임을 너무 많이 했기 때문에, 새로운 규칙이 필요했다. 마침 민식이의 근처에 살던 다솜이는 새로운 규칙을 만들어 주었다. 일단 다솜이가 규칙에 맞게 적절히 이동한 상태를 보여준다. 그럼 두 사람이 그 상태로 최소 이동횟수로 이동시켜야 한다. 그 최소 이동횟수의 방법대로 M번 움직였을 때, 하노이탑의 상태를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 디스크의 개수 N과 움직여야하는 횟수 M이 주어진다. 둘째 줄에 이동해야하는 다솜이가 규칙에 맞게 적절히 이동한 상태가 문자열로 주어진다. 모든 문자는 A, B, C중 하나이며, 그 문자열의 0번째 원소는 1번 디스크가 있는 위치, 1번째 원소는 2번째 디스크가 있는 위치와 같은 순서이다. i번째 원소는 i+1번째 디스크가 있는 위치이다. N은 30보다 작거나 같은 자연수이고, M은 0보다 크거나 같고, m보다 작거나 같은 자연수이다. m은 입력으로 주어진 상태로 만드는데 드는 최소 이동 횟수이다.

출력
첫째 줄에 입력으로 주어진 것과 같은 형식으로 하노이탑의 상태를 출력한다.
"""

import sys

# INPUT 1 LINE : 디스크 개수 N, 최소한의 경로로 이동한 횟수 M
# INPUT 2 LINE : 각 1~N크기의 디스크의 위치
N, M = list(map(int, sys.stdin.readline().split()))
location = list(sys.stdin.readline())

# 막대 A, B, C
A, B, C = [], [], []

# 각 막대에 배치
for disk, stick in enumerate(location, 1):
    if(stick == 'A'):
        A.append(disk)

    if(stick == 'B'):
        B.append(disk)

    if(stick == 'C'):
        C.append(disk)

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

cur_disk = N
for idx, disk in enumerate(C):
    wanna_disk = N - idx

    if(wanna_disk == disk):
        cur_disk -= 1
    else:
        break

move_counts = 0


def move(N, from, by, to):
    if(M == move_counts):
        return

    if(N == 1):
        ...


result = list(0 for _ in range(N))
