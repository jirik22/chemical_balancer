import ratios
from scipy.linalg import null_space

# todo
# charges

# testes
# smallest_int_ratio

# pretty code

# error handling


def parse_eq_to_left_right(eqation: str) -> str:  
    eqation = eqation.replace(" ", "")
    
    # split the equation to reactants and products
    eqation = eqation.split("=")
    
    # split to the compounds
    left = eqation[0].split("+")
    right = eqation[1].split("+")
    
    return left, right
    
    
def comp_to_dict(comp: str) -> dict:
    """
    Function to convert a chemical compound to a dictionary with the elements and their quantities.
    Args:
        comp: string with the chemical compound
    Returns:
        comp_dict: dictionary with the elements and their quantities
    """

    comp_dict = {}      # dictionary to store the elements and their quantities
    exponents = [1]     # stack of multipliers during the iteration
    exp = 1             # last multiplier
    ele_name = ""       # element name
    reading_num = False # reading number

    
    # reverse the compound to make it easier to iterate
    comp = comp[::-1]

    # iterating over all characters in compound
    for let in comp:
        # reading number
        if let.isnumeric():
            if reading_num:
                #horner scheme
                exp = int(let) * 10**len(str(exp)) + exp
            else:
                exp = int(let)
                reading_num = True
        else:
            reading_num = False

        # reading element
        if let.isalpha() and let.isupper():
            # create name of element
            ele_name = let + ele_name
            
            if len(ele_name) > 2:
                raise ValueError(f"Invalid element name in: {comp[::-1]}")
            # add element to dictionary
            if ele_name in comp_dict:
                comp_dict[ele_name] += exp * exponents[-1]
            else:
                comp_dict[ele_name] = exp * exponents[-1]
            ele_name = ""
            exp = 1

        # lower case means the element name has two letters
        elif let.isalpha() and let.islower():
            ele_name += let
            
        # reading brackets
        elif let == "(" or let == "[":
            exponents.pop()
        elif let == ")" or let == "]":
            exponents.append(exp * exponents[-1])
            exp = 1
            
        # code for parsing hydrates
        elif let == "*":
            #reset the exponents
            exponents = [1]
            for el in comp_dict:
                comp_dict[el] *= exp
            exp = 1
  
    return comp_dict


def split_equation(left: list, right: list) -> list:
    """
    Function to split the equation in the reactants, products and elements
    Args:
        left: list with all compounds in the left side of the equation
        right: list with all compounds in the right side of equation
    Returns:
        reactants: list of dictionaries with the elements and their quantities in the reactants
        (each dictionary is one compound)

        products: list of dictionaries with the elements and their quantities in the products,
        (each dictionary is one compound)

        elements: list with the elements in the equation

    """
    
    elementsR = []      # elements in the reactants
    reactants = []      # dictionaries with elements and their quantities for every reactant
    elementsP = []      # elements in the products
    products = []       # dictionaries with elements and their quantities for every product
 
    # go through all reactants and parse them to dictionaries
    for reactant in left:
        dictR = comp_to_dict(reactant)
        reactants.append(dictR)
        
        # update elements list
        for element in dictR :
            if element not in elementsR:
                elementsR.append(element)
    
    # go through all products and parse them to dictionaries
    for product in right:
        dictP = comp_to_dict(product)
        products.append(dictP)
       
        # update elements list
        for element in dictP:
            if element not in elementsP:
                elementsP.append(element)

    # check if the elements in the reactants and products are the same if not --> impossible to balance
    if sorted(elementsR) != sorted(elementsP):
        raise ValueError("Equation is unbalancable")

    return reactants, products, elementsR


def balance_equation(reactants: list, products: list, elements: list) -> list:
    """
    Function to solve the stechiometry of a chemical equation using number of atoms of each element.
    Args:
        reactants: list of dictionaries with the elements and their quantities in the reactants
        products: list of dictionaries with the elements and their quantities in the products
        elements: list with the elements in the equation
    Returns:
        ratio: list with the float ratio of the compounds in the equation
    """
    reactN = len(reactants) # number of reactants
    prodN = len(products)   # number of products
    
    # create matrix of coefficients
    M_coeff = [[0 for i in range(reactN + prodN)] for j in range(len(elements))]
    
    # create equation for every element
    for i, ele in enumerate(elements):
        for j, reactant in enumerate(reactants):
            if ele in reactant:
                M_coeff[i][j] = int(reactant[ele])
        for j, product in enumerate(products):
            if ele in product:
                M_coeff[i][j + reactN] = -int(product[ele])

    # compute the null space of the matrix
    null = null_space(M_coeff)
    
    #if there is no value in the null space, the equation is unbalancable
    if null.size == 0:
        raise ValueError("Equation is unbalancable")

    null = list(null[:, 0])
    # find smallest integer solution
    ratio = ratios.float_to_ratio(null)
    return ratio


def build_balanced_equation(left: list, right: list, ratio: list) -> str:
    """
    Function to compose balanced equation from the ratio of the elements
    Args:
        left: list with all compounds in the left side of the equation
        right: list with all compounds in the right side of the equation
        ratio: list with the float ratio of the compounds in the equation

    Returns:
        balanced_eq: string with the balanced equation

    """
    balanced_eq = ""    #string to store the balanced equation
    
    # write down reactants
    for i, reactant in enumerate(left):
        coefficient = ratio[i]
        if coefficient == 1: # dont write ones
            balanced_eq += reactant + " + "
        else:
            balanced_eq += str(coefficient) + reactant + " + "
            
    # equal sign
    balanced_eq = balanced_eq[:-3] + " = "
    
    # write down products
    for j, product in enumerate(right):
        coefficient = ratio[j+len(left)]
        if coefficient == 1: # dont write ones
            balanced_eq += product + " + "
        else:
            balanced_eq += str(coefficient) + product + " + "
        
    balanced_eq = balanced_eq[:-3]
    return balanced_eq


def main(inp):
    left, right = parse_eq_to_left_right(inp)
    react, prod, elem = split_equation(left, right)  
    
    print(left, right)
    ratio = balance_equation(react, prod, elem)
    
    print(ratio)
    balanced_equation = build_balanced_equation(left, right, ratio)
    return balanced_equation
    
if __name__ == "__main__":
    #inp = "H2O2 + KI + H2S2O3 = H2O + I2 + K2S4O6O4"
    #inp = "H2O2 + KI = K2S4O6O4"
    #inp = "CuSO4*5H2O = CuSO4 + H2O"
    inp = "CuSO4*5H2O = CuSO4 + H2O"
    out = main(inp)
    print(out)
