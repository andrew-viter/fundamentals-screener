# validation methods for different data collected through collect_input

def vsymbol(arg, col=list()):
    if arg.isalpha() and not arg in col and len(col) < 5:
        return True
    return False

def vcode(arg):
    acceptable_codes = ['100', '101', '102']
    return (arg in acceptable_codes)