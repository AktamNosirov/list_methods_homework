def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    a=numbers.pop(i)
    return a 
numbers = [ 1,2,3,4,45] 
print(main(numbers,1))