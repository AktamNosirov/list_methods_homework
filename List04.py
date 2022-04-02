def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    numbers.pop(i)
    return numbers  
numbers = [ "behi", "shaftoli","nok"] 
print(main(numbers,1))