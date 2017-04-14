def input_and_validate_integer(question = 'Zahl: ', number_of_tries = 3):
    """ this function takes an user input
    and tries to convert it into a number
    on error ...
    """
    for t in range(1, number_of_tries + 1):
        try:
            i = input(question)
            a = int(i)
            break
        except ValueError:
            print("[%s] ist keine gueltige Zahl" % (i))
            a = 0
    else:
        print('zu bloed')
        exit()
    return a