""" 2022.03.03(목)
https://www.acmicpc.net/problem/1897
1897번: 토달기

문제
희현이는 원장선생님 말씀에 토를 다는 것을 몹시 좋아한다. 토를 단다는 것은 원장선생님께서 어떤 단어를 말씀하시면 그 단어의 맨 앞이나 중간, 혹은 맨 뒤에 한 글자를 끼워 넣어서 새로운 단어를 만드는 것으로, 버릇없는 행동과는 아무런 관계가 없는 순수한 단어 놀이이다.

희현이는 사전에 등재된 단어만을 사용한다. 사전은 d개의 단어로 구성되어 있으며, 각 단어는 80자 이내의 알파벳 소문자로만 이루어져 있다. 희현이는 원장선생님께서 어떤 단어를 말씀하셨을 때, 한 글자씩 토를 달아 사전에 등재된 단어를 계속 만들어 갈 경우, 가장 긴 단어를 만들려면 어떻게 해야 하는지가 궁금해졌다. 이를 해결하는 프로그램을 작성하라.

입력
첫 줄에 사전에 등재된 단어의 수 d와, 원장님이 처음 말씀하신 단어가 주어진다. (1 ≤ d ≤ 1,000) 원장님이 처음 말씀하신 단어의 길이는 세 글자이며, 사전에 있는 단어를 말씀하셨다. 다음 d개의 줄에는 사전에 등재된 단어가 한 줄에 하나씩 주어진다.

출력
첫 줄에 토달기 규칙을 지키며 단어를 만들어 갈 때, 만들 수 있는 단어 중 가장 긴 것을 출력한다. 답이 여럿일 경우 어느 것이나 상관없다.
"""
import sys
import re

d, word = list(sys.stdin.readline().split())
dictionary = []
sorted_by_len = {}
adjacent_words = []
for idx in range(int(d)):
    i_w = sys.stdin.readline().strip()
    dictionary.append(i_w)
    adjacent_words.append([])

    # 글자 길이 별 배열
    try:
        sorted_by_len[len(i_w)].append(idx)
    except:
        sorted_by_len[len(i_w)] = [idx]

# 인접 단어들(해당 글자수 +_ 1)
for idx, w in enumerate(dictionary):
    p = list(w)
    p = re.compile('?'.join(p) + '?')

    try:
        for w_less_idx in sorted_by_len[len(w) - 1]:
            m = p.match(dictionary[w_less_idx])
            if m is not None and len(m.group()) is len(w) - 1:
                adjacent_words[idx].append(w_less_idx)
    except:
        None

    p = list(w)
    p.insert(0, '.?')
    p.append('.?')
    p = re.compile('.?'.join(p))

    try:
        for w_greater_idx in sorted_by_len[len(w) + 1]:
            if p.match(dictionary[w_greater_idx]) is not None:
                adjacent_words[idx].append(w_greater_idx)
    except:
        None

# dfs
visited = [False for _ in range(len(dictionary))]
stack = [dictionary.index(word)]
result = word

while stack:
    cur_word_idx = stack.pop()

    if visited[cur_word_idx] is False:
        visited[cur_word_idx] = True
        stack.extend(adjacent_words[cur_word_idx])

        if len(dictionary[cur_word_idx]) > len(result):
            result = dictionary[cur_word_idx]

print(result)
