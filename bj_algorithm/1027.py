""" 2022.03.17(목)
https://www.acmicpc.net/problem/1027
1027번: 고층 건물

문제
세준시에는 고층 빌딩이 많다. 세준시의 서민 김지민은 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고 한다. 빌딩은 총 N개가 있는데, 빌딩은 선분으로 나타낸다. i번째 빌딩 (1부터 시작)은 (i,0)부터 (i,높이)의 선분으로 나타낼 수 있다. 고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다. 가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 빌딩의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에 1번 빌딩부터 그 높이가 주어진다. 높이는 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
"""

import sys

N = int(sys.stdin.readline())
buildings = [{'height': height, 'line': 0} for height in map(int, sys.stdin.readline().split())]


# 옥상에서의 바라본 빌딩의 시선
def eye_line(src, dest):
    # 기울기
    g = eye_gradient(src, dest)
    # y절편
    y = src['y'] - (g * src['x'])

    # 거리에 따른 시선 높이
    def get_height_by_x(x):
        return (g * x) + y

    return get_height_by_x


# 시선의 기울기
def eye_gradient(src, dest):
    return (dest['y'] - src['y']) / (dest['x'] - src['x'])


# 전체 빌딩을 순회
for idx, building in enumerate(buildings):
    if(len(buildings) - 1 > idx):
        building['line'] += 1
        next_building = buildings[idx+1]
        next_building['line'] += 1

        src = {'x': idx, 'y': building['height']}
        get_height_by_x = eye_line(src, {'x': idx+1, 'y': next_building['height']})

    # 두칸 뒤에 위치한 빌딩부터 순회
    for c_idx, c_building in enumerate(buildings[idx+2:]):
        if(c_building['height'] > get_height_by_x(idx + 2 + c_idx)):
            building['line'] += 1
            c_building['line'] += 1

            get_height_by_x = eye_line(src, {'x': idx + 2 + c_idx, 'y': c_building['height']})

result = 0
for idx, building in enumerate(buildings):
    if(building['line'] > result):
        result = building['line']

print(result)
