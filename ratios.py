def gcd(a:int, b:int) -> int:
    """Function to Calculate the greatest common divisor of a and b using the Euclidean algorithm."""
    while b > 10: # 10 because numbers in last decimal digit are rounded
        a, b = b, a % b
    return a


def gcd_list(lst:list):
    """Function to find greatest common divisor of integers in list"""
    res = lst[0]
    for num in lst:
        res = gcd(res, num)
    return res


def float_to_ratio(ratio:list) -> list:
    """
    Function to convert float ratio to smallest integer ratio
    Args:
        ratio: float ratio
    Returns:
        ratio: ratio of integers
    
    """
    #convert to int ration
    minim = min(ratio)
    
    for i in range(len(ratio)):
        ratio[i] = round((ratio[i]/minim)*10e5)
      
    gcd_ratio = gcd_list(ratio)
    for i in range(len(ratio)):
        ratio[i] = round(ratio[i]/gcd_ratio)
        
    return ratio 