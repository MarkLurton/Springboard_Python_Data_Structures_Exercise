def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dig_count1 = {}
    dig_count2 = {}

    for dig in str(num1):
        dig_count1[dig] = dig_count1.get(dig, 0) + 1
    
    for dig in str(num2):
        dig_count2[dig] = dig_count2.get(dig, 0) + 1
    
    return dig_count1 == dig_count2
    