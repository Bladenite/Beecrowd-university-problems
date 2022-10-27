def middleNode(head):
    new_list = []
    if (len(head) % 2 == 0):
        for i in range(int(len(head)/2), len(head)):
            new_list.append(head[i])
    else:
        for i in range(int(len(head)/2), len(head)):
            new_list.append(head[i])
    return new_list

print(middleNode([1,2,3,4,5]))