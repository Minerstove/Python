#Isosceles
"""
a, b, c = map(int, input().split())

if a == b or b == c or c == a:
    print("Yes")
else:
    print("No")
"""

#Perfect
"""
N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for k in range(K)]
corrects = [[False] * M for n in range(N)]

answer = []
for a, b in AB:
    a -= 1
    b -= 1
    corrects[a][b] = True
    if all(corrects[a]):
        answer.append(a+1)

if answer:
    print(*answer)
"""

#New Skill Acquired
import sys
from collections import deque

tokens = iter(map(int, sys.stdin.buffer.read().split()))
num_skills = next(tokens)

dependents = [[] for _ in range(num_skills + 1)]
is_learned = [False] * (num_skills + 1)
skills_to_check = deque() 

for skill_id in range(1, num_skills + 1):
    prereq_a = next(tokens)
    prereq_b = next(tokens)

    if prereq_a == 0 and prereq_b == 0:
        is_learned[skill_id] = True
        skills_to_check.append(skill_id)
    else:
        dependents[prereq_a].append(skill_id)
        dependents[prereq_b].append(skill_id)

while skills_to_check:
    current_skill = skills_to_check.popleft()
    for unlocked_skill in dependents[current_skill]:
        if not is_learned[unlocked_skill]:
            is_learned[unlocked_skill] = True
            skills_to_check.append(unlocked_skill)

print(sum(is_learned)) #answer

