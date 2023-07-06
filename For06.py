def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    x = 0
    for i in range(A,B):
        x+=i
    return x 

print(main(10,11))