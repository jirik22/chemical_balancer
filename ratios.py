#euklid algorihm
def gcd(a, b):
    while b > 10: # 10 because numbers in last decimal digit is rounded
        a, b = b, a % b
    return a

#find the nsd for a list of numbers
def gcd_list(lst):
    res = lst[0]
    for num in lst:
        res = gcd(res, num)
    return res

def float_to_ratio(ratio:list) -> list:
    #convert to int ration
    minim = min(ratio)
    
    for i in range(len(ratio)):
        ratio[i] = round((ratio[i]/minim)*10e5)
      
    gcd_ratio = gcd_list(ratio)
    for i in range(len(ratio)):
        ratio[i] = round(ratio[i]/gcd_ratio)
        
    return ratio 

"""print(float_to_ratio([10/60, 8/60, 7/60]))
print(float_to_ratio([2/53, 5/53, 8/53, 6/53, 12/53, 62/53, 154/53]))
print(float_to_ratio([1/3,2/3]))
print(float_to_ratio([0.5, 0.25, 0.75]))
print(float_to_ratio([2**(1/2),2*(2**(1/2)) ]))

print(2/53)"""