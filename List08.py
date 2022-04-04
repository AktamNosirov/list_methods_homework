def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    n= 0
    if fruits[n]=="apple":
        fruits.remove("apple")
    else:
        n += 1
    if fruits[n]=="apple":
        fruits.remove("apple")
    else:
        n += 1
    if fruits[n]=="apple":
        fruits.remove("apple")
    else:
        n += 1
    if fruits[n]=="apple":
        fruits.remove("apple")
    else:
        n += 1
    if fruits[n]=="apple":
        fruits.remove("apple")
    else:
        n += 1
    return fruits 
fruits=["banana", "apple", "avacado", "apple","apple"]
print(main(fruits)) 
