def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    if fruits[0]="apple" :
        fruits.remove("apple")
    if fruits[1]=="apple" :
        fruits.remove("apple")
    if fruits[2]=="apple" :
        fruits.remove("apple")
    if fruits[3]=="apple" :
        fruits.remove("apple")
    if fruits[4]=="apple" :
        fruits.remove("apple")
    return fruits 
fruits=["banana", "apple", "avacado", "apple","apple"]
print(main(fruits)) 

