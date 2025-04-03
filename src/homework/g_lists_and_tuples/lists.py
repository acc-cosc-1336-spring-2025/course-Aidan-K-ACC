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

def get_p_distance(list1,list2):
    dif= 0
    for item in range(0,len(list1)):
        if list1[item] != list2[item]:
            dif+= 1
    p_dis= dif/len(list1)
    return p_dis

def get_p_distance_matrix(data_matrix):
    result_matrix= []
    for itema in range(0,len(data_matrix)):
        temp_list= []
        for itemb in range(0,len(data_matrix)):
            list1=data_matrix[itema]
            list2= data_matrix[itemb]
            temp_list.append(get_p_distance(list1,list2))
        result_matrix.append(temp_list)    
    return result_matrix

