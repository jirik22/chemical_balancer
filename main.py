import ratios

# todo
# charges
# testes
# smallest_int_ratio
# pretty code
# error handling
# dont write ones
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
            # add element to dictionary
            if ele_name in comp_dict:
                comp_dict[ele_name] += exp * exponents[-1]
            else:
                comp_dict[ele_name] = exp * exponents[-1]
            ele_name = ""
            exp = 1

        # lower case means the element name has two letters
        elif let.isalpha() and let.islower():
            ele_name = let
            
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



def split_equation(eqation):
    """
    Function to split the equation in the reactants, products and elements
    Args:
        eqation: string with the equation
    Returns:
        reactants: list of dictionaries with the elements and their quantities in the reactants
        (each dictionary is one compound)

        products: list of dictionaries with the elements and their quantities in the products,
        (each dictionary is one compound)

        elements: list with the elements in the equation

    """

    eqation = eqation.replace(" ", "")
    # split the equation in the two sides
    eqation = eqation.strip().split("=")
    # split the compounds in the sides
    left = eqation[0].split("+")
    right = eqation[1].split("+")

    # list of elements in the equation
    elements = []

    reactants = []
    for reactant in left:
        dictR = comp_to_dict(reactant)

        # add the elements to the list of elements
        for element in dictR:
            if element not in elements:
                elements.append(element)

        reactants.append(dictR)

    products = []
    for product in right:
        dictP = comp_to_dict(product)

        products.append(dictP)

    return reactants, products, elements


def balance_equation(reactants: list, products: list, elements: list) -> list:
    """
    Function to solve the stechiometry of a chemical equation using number of atoms of each element.
    Args:
        reactants: list of dictionaries with the elements and their quantities in the reactants
        products: list of dictionaries with the elements and their quantities in the products
        elements: list with the elements in the equation


    """

    import numpy as np

    reactN = len(reactants)
    prodN = len(products)

    # matrix of coefficients

    M_coeff = np.zeros((len(elements), reactN + prodN))
    M_coeff = M_coeff.astype(int)

    # create equation for every element
    for i, ele in enumerate(elements):
        for j, reactant in enumerate(reactants):
            if ele in reactant:
                M_coeff[i, j] = int(reactant[ele])
        for j, product in enumerate(products):
            if ele in product:
                M_coeff[i, j + reactN] = -int(product[ele])

    from scipy.linalg import null_space

    # compute the null space of the matrix
    null = list(null_space(M_coeff)[:, 0])

    # find smallest integer solution
    ratio = ratios.float_to_ratio(null)
    return ratio


def print_equation(ratio: list, inp: str):
    """
    Function to compose balanced equation from the ratio of the elements
    Args:
        ratio: list with the ratio of the elements
        inp: string with the input equation

    Returns:
        balanced_eq: string with the balanced equation

    """

    # parse input
    inp = inp.replace(" ", "")
    eqation = inp.split("=")
    eqation[0] = eqation[0].split("+")
    eqation[1] = eqation[1].split("+")

    # print the balanced equation
    balanced_eq = ""
    

    # add reactants
    for i, reactant in enumerate(eqation[0]):
        balanced_eq += str(ratio[i]) + reactant + " + "
        
    balanced_eq = balanced_eq[:-3] + " = "
    
    # add products
    for j, product in enumerate(eqation[1]):

        balanced_eq += str(ratio[j+len(eqation[0])]) + product + " + "
        
    balanced_eq = balanced_eq[:-3]
    return balanced_eq


def main(inp):
    
    react, prod, elem = split_equation(inp)
    ratio = balance_equation(react, prod, elem)
    balanced_equation = print_equation(ratio, inp)
    print(balanced_equation)
    return balanced_equation
    


if __name__ == "__main__":
    inp = "H2O2 + Cr = CrO3 + H2O"
    main(inp)
