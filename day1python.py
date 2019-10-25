import json

def readjsonf():
    read_jsonfile = input("Type the filename: ")
    with open(read_jsonfile, "r+") as file:
        contents = json.load(file)
    
    print(contents)

def writejsonf():
    write_jsonfile = input("Type the filename: ")
    what_to_write = input("Type what to write: ")
    with open(write_jsonfile, "w+") as file:
        check = file.write(json.dumps(what_to_write))
        print(check)

def main():

    flag = True
    while flag:
        user_input = input("\n Type 'readjsonf' to read a JSON file and type 'writejsonf' to write in a JSON file. \n Type 'close' to end program. \n")
        if user_input == "readjsonf":
            readjsonf()
            input("Hit enter to continue...")
        elif user_input == "writejsonf":
            writejsonf()
            input("Hit enter to continue...")
        elif user_input == "close":
            flag = False

main()