def get_highest_list_value(list):
    h= list[0]
    for item in list:
        if float(item) > float(h):
            h= item
    return h

def get_lowest_list_value(list):
    l= list[0]
    for item in list:
        if float(item) < float(l):
            l= item
    return l

