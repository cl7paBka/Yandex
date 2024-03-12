P, V = map(int, input().split()) #P - номер дерева Васи, V - на сколько деревьев вася может отдалиться
Q, M = map(int, input().split()) #Q - номер дерева Маши, M - на сколько деревьев маша может отдалиться

vasya_min = P-V
vasya_max = P+V
maria_min = Q-M
maria_max = Q+M

trees_count = abs(vasya_max - vasya_min) + abs(maria_max - maria_min) + 2

vasya_pointer = vasya_min
maria_pointer = maria_min

while vasya_pointer <= vasya_max and maria_pointer <= maria_max:
    if vasya_pointer == maria_pointer:
        trees_count -= 1
        vasya_pointer += 1
        maria_pointer += 1
    elif vasya_pointer > maria_pointer:
        maria_pointer += 1
    else:
        vasya_pointer += 1
print(trees_count)

