def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    x = 0
    for i in range(N):
        if (i+1)%2==0:
            x+=i 
    return x 

print(main(21))