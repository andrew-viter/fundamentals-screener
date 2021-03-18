import functions

print("Enter a command, or \'help\' to see commands")
input_list = input(">>> ").split(' ')
command = input_list[0]
args = input_list[1:]

while command != "done":
    if command == "generate":
        functions.chart_generation()

    elif command == "clean":
        functions.image_cleanup()
    
    elif command == "archive":
        functions.archive()

    input_list = input(">>> ").split(' ')
    command = input_list[0]
    args = input_list[1:]
