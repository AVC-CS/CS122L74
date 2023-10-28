
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = list(map(int, input('Enter your input values: ').split())) 
    return numbers

def listSum(list1, list2):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = []
    
    return result


def main():
    list1 = getInput()
    list2 = getInput()
    ret = listSum(list1, list2)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
