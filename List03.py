def main(fruits1, fruits2):
    """
    You will be given a list of several fruits called fruits1 and fruits2. Return the result by adding the second to the first list.
    Args:
        fruits1(list): parameter
        fruits2(list): parameter
    Returns:
        list: return answer
    """
    return fruits2+fruits1
fruits1 = ["olma", "uzum", "anor"] 
fruits2 = [ "behi", "shaftoli"] 
print(main(fruits1,fruits2))