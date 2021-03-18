import functions



print("Enter a command, or \'help\' to see commands")
command = str()
commands = ['done', 'gen', 'cleanup', 'archive']

while command != "done":
    # input collection at top of loop
    input_list = input(">>> ").split(' ')
    command = input_list[0]
    args = input_list[1:]
    p_args = list()

    # checks if command is acceptable
    if not command in commands:
        print(' '.join(["Command", command, "not recognized"]))
        continue

    # checks if there are arguments, and parses them if present
    if len(args) > 0:
        for arg in args:
            if arg[0] == '-':
                p_arg = arg.replace('-', '')
                p_args.append(p_arg)
            elif arg[0] == '\"' or arg[0] == '\'':
                p_arg = arg.strip('\'')
                p_arg = p_arg.strip('"')
                p_arg = p_arg.replace('_', ' ')
                p_args.append(p_arg)
            else:
                print("Arguments must start with \'-\' or be in quotes")
                break

    if command == "gen":
        functions.generate_chart()

    elif command == "cleanup":
        functions.image_cleanup(p_args)
    
    elif command == "archive":
        functions.archive(p_args)
