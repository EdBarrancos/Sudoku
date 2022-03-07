def Sort(lst):
    def list_bin(lines):
        to_be_sorted = list()
        for line in lines:
            item = bin(int("".join(map(str, line))))
            to_be_sorted.append(item)

        return to_be_sorted

    lst = list_bin(lst)
    swap = 1
    def Sort_(pivot):
        if lst[pivot] > lst[pivot + 1]:
            lst[pivot], lst[pivot + 1] = lst[pivot + 1], lst[pivot]
            return 1
        else:
            return 0
    
    while swap != 0:
        swap = 0
        for i in range(len(lst) - 1):
            swap += Sort_(i)
    
    return lst

def bin_list(lst):
    new_lst = list()
    for nbr in lst:
        item = [int(x) for x in str(nbr)]
        new_lst.append(item)

    return new_lst

def list_bin(lines):
        to_be_sorted = list()
        for line in lines:
            item = int("".join(map(str, line)))
            to_be_sorted.append(item)

        return to_be_sorted

a = [[1,0,0],[0,1,0],[0,0,1]]
print(bin_list(list_bin(a)))
#The 0's are staying behind

 