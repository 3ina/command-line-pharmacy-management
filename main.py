from DataBaseManagement import DataBaseManagement

flag = True
database = DataBaseManagement("files/doctor.txt", "files/patient.txt", "files/drug.txt")

while (flag):
    print("""
        please select from menu
        1)Insert
        2)Update
        3)Delete
        4)Search
    
    """)
    menu_select = input()
    match int(menu_select):
        # Insert
        case 1:
            print("""
                please select from menu
                1)Doctors
                2)drugs
                3)patient

            """)
            choice = input()
            match int(choice):
                case 1:
                    database.insert(1)
                case 2:
                    database.insert(2)
                case 3:
                    database.insert(3)
                case _:
                    print("please inter true number")

        # Update
        case 2:
            print("""
                please select from menu
                1)Doctors
                2)patient

                """)
            choice = input()
            match int(choice):
                case 1:
                    database.update(1)
                case 2:
                    database.update(2)
                case _:
                    print("please inter true number")

        # delete
        case 3:
            print("""
                please select from menu
                1)Doctors
                2)drugs
                3)patient

                 """)
            choice = input()
            match int(choice):
                case 1:
                    database.delete(1)
                case 2:
                    database.delete(2)
                case 3:
                    database.delete(3)
                case _:
                    print("please inter true number")
        # search
        case 4:
            print("""
                        please select from menu
                        1)Doctors
                        2)drugs
                        3)patient

                         """)
            choice = input()
            match int(choice):
                case 1:
                    database.search(1)
                case 2:
                    pass
                case 3:
                    database.search(3)
                case _:
                    print("please inter true number")
        case _:
            print("please inter true number")

    flag_value = input("Do you want to continue the program? y or n : ")
    if flag_value.lower() == "n":
        flag = False
    elif flag_value.lower() == "y":
        pass
    else:
        print("please enter correct choice")
