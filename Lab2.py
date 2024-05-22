#print("ET0735 (DevOps for AIOT) - Lab 2 - Introduction to Python")

# def funcName (parameter 1, parameter 2) : 
 #   print("This is a dummy function")
 #   return 10
'''
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    user_input = input()
    string_list = user_input.split(",")
    global float_list
    float_list = list(map(float, string_list))
    return float_list

def calc_average():
    print("calc_average")
    x = len(float_list)
    y = sum(float_list)
    return y/x

def find_min_max():
    print("find_Min_max")
    mini = min(float_list)
    maxi = max(float_list)
    min_max = [mini, maxi]
    return min_max

def sort_temperature():
    print("sort_temperature")
    float_list.sort()
    return float_list

def calc_median_temperature():
    print("calc_median_temperature")
    float_list.sort()
    size = len(float_list)
    if size % 2 :
     return float_list[size//2]
    else :
     return (float_list[size//2] + float_list[1+ size//2]) / 2
    '''
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    user_input = input()
    string_list = user_input.split(",")
    float_list = list(map(float, string_list))
    return float_list

def calc_average(float_list):
    print("calc_average")
    x = len(float_list)
    y = sum(float_list)
    return y/x

def find_min_max(float_list):
    print("find_Min_max")
    mini = min(float_list)
    maxi = max(float_list)
    min_max = [mini, maxi]
    return min_max

def sort_temperature(float_list):
    print("sort_temperature")
    float_list.sort()
    return float_list

def calc_median_temperature(float_list):
    print("calc_median_temperature")
    float_list.sort()
    size = len(float_list)
    if size % 2 :
     return float_list[size//2]
    else :
     return (float_list[size//2] + float_list[1+ size//2]) / 2
#Main code
def main():
    display_main_menu()
    v1 = get_user_input()
    print(calc_average(v1))
    print(find_min_max(v1))
    print(sort_temperature(v1))
    print(calc_median_temperature(v1))

if __name__ == "__main__":
    main()