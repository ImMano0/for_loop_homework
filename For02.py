def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    ans = "0"
    for i in range(1,n):
        ans+=','+str(i)

    return ans 

print(main(10))
print(type("ans"))