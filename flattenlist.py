lists = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
joinedlist = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            joinedlist.append(i)

flatten(lists)
print(joinedlist)