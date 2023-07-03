def intToStr(num):
    """ Convert integer to string
    """
    digits = '0123456789'
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = digits[num % 10] + result
        num = num//10
    return result
