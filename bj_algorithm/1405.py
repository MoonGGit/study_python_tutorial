""" 2022.02.10(목)
https://www.acmicpc.net/problem/1405
1405번: 미친 로봇

문제
통제 할 수 없는 미친 로봇이 평면위에 있다. 그리고 이 로봇은 N번의 행동을 취할 것이다.

각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오. 예를 들어, EENE와 ENW는 단순하지만, ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)

입력
첫째 줄에 N, 동쪽으로 이동할 확률, 서쪽으로 이동할 확률, 남쪽으로 이동할 확률, 북쪽으로 이동할 확률이 주어진다. N은 14보다 작거나 같은 자연수이고,  모든 확률은 100보다 작거나 같은 자연수 또는 0이다. 그리고, 동서남북으로 이동할 확률을 모두 더하면 100이다.

확률의 단위는 %이다.

출력
첫째 줄에 로봇의 이동 경로가 단순할 확률을 출력한다. 절대/상대 오차는 10-9 까지 허용한다.
"""

######################
# N > 8 부터, 1초 초과  #
######################

import sys
import copy

이동횟수, 동_확률, 서_확률, 남_확률, 북_확률 = list(map(int, sys.stdin.readline().split()))
동_확률 /= 100
서_확률 /= 100
남_확률 /= 100
북_확률 /= 100
단순_이동경로_정보 = {
    # 이동한 경로 1, 이동하지 않은 경로 0
    '이동경로': [[0 for _ in range(이동횟수 * 2 + 1)] for _ in range(이동횟수 * 2 + 1)],
    '마지막_위치': [이동횟수, 이동횟수],
    '단순_확률': 0,
    '다음경로': None  # {동: ..., 서: ..., 남: ..., 북: ...}
}

각_이동횟수의_마지막_경로 = []
단순_확률_합 = 0

for _ in range(이동횟수):
    단순_확률_합 = 0
    다음_단순_이동경로 = []

    # 첫 이동일 경우
    if(_ == 0):
        단순_이동경로_정보['이동경로'][이동횟수][이동횟수] = 1   # 시작위치 1로 설정
        단순_이동경로_정보['단순_확률'] = 1
        단순_이동경로_정보['다음경로'] = {
            '동': {
                '이동경로': copy.deepcopy(단순_이동경로_정보['이동경로']),
                '마지막_위치': [이동횟수 + 1, 이동횟수],
                '단순_확률': 동_확률,
                '다음경로': None
            },
            '서': {
                '이동경로': copy.deepcopy(단순_이동경로_정보['이동경로']),
                '마지막_위치': [이동횟수 - 1, 이동횟수],
                '단순_확률': 서_확률,
                '다음경로': None
            },
            '남': {
                '이동경로': copy.deepcopy(단순_이동경로_정보['이동경로']),
                '마지막_위치': [이동횟수, 이동횟수 - 1],
                '단순_확률': 남_확률,
                '다음경로': None
            },
            '북': {
                '이동경로': copy.deepcopy(단순_이동경로_정보['이동경로']),
                '마지막_위치': [이동횟수, 이동횟수 + 1],
                '단순_확률': 북_확률,
                '다음경로': None
            }
        }

        for 동서남북 in 단순_이동경로_정보['다음경로']:
            X, Y = 단순_이동경로_정보['다음경로'][동서남북]['마지막_위치']
            단순_이동경로_정보['다음경로'][동서남북]['이동경로'][X][Y] = 1
            단순_확률_합 += 단순_이동경로_정보['다음경로'][동서남북]['단순_확률']
            각_이동횟수의_마지막_경로.append(단순_이동경로_정보['다음경로'][동서남북])

        continue

    for 마지막_경로 in 각_이동횟수의_마지막_경로:
        # 3.5~ object spread syntax : **obj and list spread syntax : *list
        이동경로, 마지막_위치, 단순_확률, 다음경로 = 마지막_경로.values()
        X, Y = 마지막_위치
        마지막_경로['다음경로'] = {}

        # 동
        if(이동경로[X + 1][Y] != 1):
            새_경로 = copy.deepcopy(이동경로)
            새_경로[X + 1][Y] = 1
            단순_확률_합 += 단순_확률 * 동_확률
            마지막_경로['다음경로']['동'] = {
                '이동경로': 새_경로,
                '마지막_위치': [X + 1, Y],
                '단순_확률': 단순_확률 * 동_확률,
                '다음경로': None
            }

            다음_단순_이동경로.append(마지막_경로['다음경로']['동'])
            print('동')

        # 서
        if(이동경로[X - 1][Y] != 1):
            새_경로 = copy.deepcopy(이동경로)
            새_경로[X - 1][Y] = 1
            단순_확률_합 += 단순_확률 * 서_확률
            마지막_경로['다음경로']['서'] = {
                '이동경로': 새_경로,
                '마지막_위치': [X - 1, Y],
                '단순_확률': 단순_확률 * 서_확률,
                '다음경로': None
            }

            다음_단순_이동경로.append(마지막_경로['다음경로']['서'])
            print('서')

        # 남
        if(이동경로[X][Y - 1] != 1):
            새_경로 = copy.deepcopy(이동경로)
            새_경로[X][Y - 1] = 1
            단순_확률_합 += 단순_확률 * 남_확률
            마지막_경로['다음경로']['남'] = {
                '이동경로': 새_경로,
                '마지막_위치': [X, Y - 1],
                '단순_확률': 단순_확률 * 남_확률,
                '다음경로': None
            }

            다음_단순_이동경로.append(마지막_경로['다음경로']['남'])
            print('남')

        # 북
        if(이동경로[X][Y + 1] != 1):
            새_경로 = copy.deepcopy(이동경로)
            새_경로[X][Y + 1] = 1
            단순_확률_합 += 단순_확률 * 북_확률
            마지막_경로['다음경로']['북'] = {
                '이동경로': 새_경로,
                '마지막_위치': [X, Y + 1],
                '단순_확률': 단순_확률 * 북_확률,
                '다음경로': None
            }

            다음_단순_이동경로.append(마지막_경로['다음경로']['북'])
            print('북')

    각_이동횟수의_마지막_경로 = 다음_단순_이동경로

print(단순_확률_합)
