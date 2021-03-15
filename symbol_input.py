# collector list for user entered symbols
symbols = list()

# checks if the symbol is valid
def symbol_validated(s):
    if s.isalpha() and not s in symbols:
        return True
    return False

# manages input handling and returns list of symbols
def collect_symbols():

    print("Enter command, or \'help\' to show commands (max allowed is five symbols)")
    command = input(">>> ")

    # collects input until command is 'done'
    # all invalid commands are simply ignored
    while command != "done":
        # the add command prompts for symbol
        if command == "add":
            # the symbol is raised to uppercase for consistency
            symbol = input("Symbol: ").upper()

            # checks to ensure the symbol is valid and there is room in the list
            # list capacity is limited by the number of colors in r script
            if symbol_validated(symbol) and len(symbols) < 5:
                symbols.append(symbol)
            else:
                print("Invalid symbol, or there are too many")

        # the list command will print current list of symbols
        elif command == "list":
            print("Your symbols currently are: ")
            for symbol in symbols:
                print(symbol)

        # remove will delete a symbol from the list
        elif command == "remove":
            # again, raised to upper for consistency
            symbol_to_remove = input("Symbol: ").upper()
            for s in symbols:
                if s == symbol_to_remove:
                    symbols.remove(symbol_to_remove)
                    break

        # help command will print each command and a description of what it does
        elif command == "help":
            print("\'add\' - adds a symbol to the list")
            print("\'remove\' - removes a symbol previously added to the list")
            print("\'list\' - shows the list of currently added symbols")

        command = input(">>> ")

    return symbols
