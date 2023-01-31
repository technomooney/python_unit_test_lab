def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """
    try:
        number_of_items = len(item_prices)
        if number_of_items >= 3:
            return min(item_prices)
        return None
    except TypeError:
        return None
if __name__ == '__main__':
    main()