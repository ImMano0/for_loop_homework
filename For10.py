def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    k=[]
    for i in list1:
        if str(i).islower():
            k.append(str(i).capitalize())
    return k 
print(main(['Aziz','Laylo','Shoakbar']))