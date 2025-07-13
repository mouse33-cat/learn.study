def locate(percentage, years, początkowa_wartość):
    result = początkowa_wartość * (1 + percentage / 100) ** years
    return result
