def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flip_str = ''

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter.lower() == letter:
                flip_str += letter.upper()
            else:
                flip_str += letter.lower()
        else:
            flip_str += letter

    return flip_str