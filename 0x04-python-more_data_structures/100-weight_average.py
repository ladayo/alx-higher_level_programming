#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        new_list = []
        for i in my_list:
            a, b = i
            new_list.append(a*b)
        total_dem = 0
        for j in my_list:
            total_dem = total_dem + j[1]
        total_num = 0
        for i in new_list:
            total_num = total_num + i
        w_avg = total_num/total_dem
        return (w_avg)
    else:
        return (0)
