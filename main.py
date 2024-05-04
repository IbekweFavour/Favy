#num = [2,3,3,3,1,2]
def remove_duplicates(num):
    empty_list = []
    for i in num:
        if i not in empty_list:
            empty_list.append(i)
    return set(empty_list)
answer = remove_duplicates([3,3,1,2,11,12,1,1])
print(answer)