def merge_sorted_list(list1, list2):
    i, j = 0, 0
    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    if i < len(list1):
        merged_list.extend(list1[i:])
    if j < len(list2):
        merged_list.extend(list2[j:])

    return merged_list

list1 = list(map(int, input("Введите первый отсортированный список чисел через пробел: ").split()))
list2 = list(map(int, input("Введите второй отсортированный список чисел через пробел: ").split()))

merged = merge_sorted_list(list1, list2)
print(f"Результат слияния: {merged}")
