def vsymbol(arg, col=list()):
    if arg.isalpha() and not arg in col and len(col) < 5:
        return True
    return False

def vcode(arg):
    acceptable_codes = ['100', '101', '102', '103', '200', '201', '202', '203', '300']
    return (arg in acceptable_codes)