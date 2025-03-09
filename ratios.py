#euklid algorihm
def gcd(a, b):
    while b != 0:
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
        ratio[i] = round((ratio[i]/minim)*100000)
        
    gcd_ratio = gcd_list(ratio)
    for i in range(len(ratio)):
        ratio[i] = ratio[i]//gcd_ratio
        
    return ratio 
