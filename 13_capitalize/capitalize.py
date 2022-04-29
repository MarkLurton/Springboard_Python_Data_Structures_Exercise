def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    res = phrase[0].upper()
    
    for letter in phrase[1:]:
        res += letter
    
    return res
    