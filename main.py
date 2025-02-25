def smallest_int_ratio(lst:list) -> list:
    #todo
    minimum = min(lst)
    print(lst)

    lst = [round(i*2/minimum) for i in lst]
    print(lst)
    return lst


def comp_to_dict(comp:str) -> dict:
    """
    Function to convert a chemical compound to a dictionary with the elements and their quantities.
    Args:  
        comp: string with the chemical compound
    Returns:
        comp_dict: dictionary with the elements and their quantities
    """
    #reverse the compound to make it easier to iterate
    comp = comp[::-1]
    
    #dictionary to store the elements and their quantities
    comp_dict = {}
    
    #stack of multipliers during the iteration
    exponents = [1]
    
    #last multiplier
    exp = 1
    
    #element name
    ele = ""
    
    #element quantity
    num = 0
    reading_num = False
    
    #iterating over all characters in compound
      
    for let in comp:
        
        if let.isnumeric():
            if reading_num:
                num = int(let)*10 + num
            else:
                num = int(let)
                reading_num = True
                
            exp = int(num)
        else:
            reading_num = False
            
        if let.isalpha() and let.isupper():
            #create name of element
            ele = let + ele
            #add element to dictionary
            if ele in comp_dict:
                comp_dict[ele] += exp*exponents[-1]
            else:
                comp_dict[ele] = exp*exponents[-1]
            ele = ""
            exp = 1
            
        elif let.isalpha() and let.islower():
            ele = let 
        elif let == "(" or let == "[":
            exponents.pop()
        elif let == ")" or let == "]":
            exponents.append(exp*exponents[-1])
            exp = 1
    return comp_dict
            
def split_equation(eqation):
    eqation = eqation.replace(" ", "")
    #split the equation in the two sides
    eqation = eqation.strip().split("=")
    #split the compounds in the sides
    left = eqation[0].split("+")
    right = eqation[1].split("+")
    
    
    #list of elements in the equation
    elements = []
    
    reactants = []
    for reactant in left:
        dictR = comp_to_dict(reactant)
        
        #add the elements to the list of elements
        for element in dictR:
            if element not in elements:
                elements.append(element)
                
        reactants.append(dictR)
        
    products = []
    for product in right:
        dictP = comp_to_dict(product)

        products.append(dictP)
        
    return reactants, products, elements
        
    
    
def balance_equation(reactants:list, products:list, elements:list) -> list:
    import numpy as np
    
    
    reactN = len(reactants)
    prodN = len(products)
    
    #matrix of coefficients

    M_coeff = np.zeros((len(elements), reactN + prodN))
    M_coeff = M_coeff.astype(int)
    
    #create equation for every element
    for i,ele in enumerate(elements):
        for j,reactant in enumerate(reactants):
            if ele in reactant:
                M_coeff[i,j] = int(reactant[ele])
        for j,product in enumerate(products):
            if ele in product:
                M_coeff[i,j+reactN] = -int(product[ele])
    
    
    from scipy.linalg import null_space
    #compute the null space of the matrix
    null = list(null_space(M_coeff)[:,0])

    #find smallest integer solution
    
    ratio = smallest_int_ratio(null)
    return ratio
    
def print_equation(ratio:list, inp:str):
    
    #parse input
    inp = inp.replace(" ", "")
    eqation = inp.split("=")
    eqation[0] = eqation[0].split("+")
    eqation[1] = eqation[1].split("+")

    
    #print the balanced equation
    out = ""
    for i,reactant in enumerate(eqation[0]):
        out += str(ratio[i]) + reactant + " + "
    out = out[:-2] + " = "
    for i,product in enumerate(eqation[1]):
        out += str(ratio[-i]) + product + " + "
    out = out[:-2]
    print(out)
        
   
        
def main():   
    inp = "Cu + HNO3 = Cu(NO3)2 + NO + H2O"
    react, prod, elem = split_equation(inp)
    print(prod)

    ratio = balance_equation(react, prod, elem)
    print_equation(ratio, inp)
    
if __name__ == "__main__":
    main()        






    
"""    
#comp_to_dict("(NH4)2SO4") # {'S': 1, 'O': 4, 'N': 2, 'H': 8}
#varios testes
#comp_to_dict("H2O") # {'H': 2, 'O': 1}
comp_to_dict("Cu[N22Po]21[(H2Fr)15(NO37)5]52") # {'Na': 1, 'Cl': 1}
comp_to_dict("Cs(PO(ONa14)3CS)2") # {'Cs': 1, 'P': 2, 'O': 8, 'Na': 6}

"""


