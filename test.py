def reverse_karatsuba(data) -> tuple:
    print(data)
    for lst in data:
        if isinstance(lst,list) == True:
            reverse_karatsuba(lst)
          
    first = data[0]
    last = data[len(data)-1]
    print("first , last")
    print(first, last)
    tpl = ((int(last[0]*10)+ int(first[0])), (int((last[1]*10)+int(first[1]))))
    return tpl

reverse_karatsuba([(2, 3), (6, 5), (4, 2)])# == (42,23)