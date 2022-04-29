def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    split = phrase.split()
    res = split[0].capitalize();
    for item in split[1:]:
        res += f' {item.capitalize()}'
    return res

# OR just return phrase.title()
