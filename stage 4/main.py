import sqlite3 

path = 'XYZGym.sqlite'

# ==========

def main_menu():
    print("=" * 5 + " Select An Option " + "=" * 5)
    print("   1. Members Menu")
    print("   2. Classes Menu")
    print("   3. Equipment Menu")
    print("   0. Exit\n")

    inp = int(input())

    match inp:
        case 1:
            menu_members()
        case 2:
            menu_classes()
        case 3:
            menu_equipment()
        case 0:
            quit()
        case _:
            print("Unknown action..")
            main_menu()

def menu_members():
    print("=" * 5 + " MEMBERS " + "=" * 5)
    print("   1. Show All Members")
    print("   2. Add New Member")
    print("   3. Update Member")
    print("   4. Delete Member")
    print("   0. Back\n")
    
    inp = int(input())

    match inp:
        case 1:
            act_display_all_members()
        case 2:
            act_add_new_member()
        case 3:
            act_update_member_info()
        case 4:
            act_delete_member()
        case 0:
            main_menu()
        case _:
            print("Unknown action..")
            menu_members()

def menu_classes():
    print("=" * 5 + " CLASSES " + "=" * 5)
    print("   1. List Classes and Attendance")
    print("   2. Add New Class")
    print("   3. Update Class Info")
    print("   4. Delete Class")
    print("   5. List All members in Class")
    print("   0. Back\n")

    inp = int(input())

    match inp:
        case 1:
            act_list_classes_and_attendance()
        case 2:
            act_add_new_class()
        case 3:
            act_update_class_info()
        case 4:
            act_delete_class()
        case 5:
            act_find_members_by_class()
        case 0:
            main_menu()
        case _:
            print("Unknown action..")
            menu_classes()

def menu_equipment():
    print("=" * 5 + " EQUIPMENT " + "=" * 5)
    print("   1. Show Equipment Details")
    print("   2. Insert New Equipment")
    print("   3. Update Equipment Info")
    print("   4. Delete Equipment")
    print("   0. Back\n")

    inp = int(input())

    match inp:
        case 1:
            act_show_equipment_details()
        case 2:
            act_insert_new_equipment()
        case 3:
            act_update_equipment_details()
        case 0:
            main_menu()
        case 4:
            act_delete_equipment()
        case _:
            print("Unknown action..")
            menu_equipment()

def cmd_logout_and_exit():
    return

# ==========

# members
def act_display_all_members():
    q = "SELECT name FROM Member"
    result = connection.execute(q)

    print("Members in gym..")
    for entry in result:
        print(entry)
    menu_members()


def act_add_new_member():
    cursor = connection.cursor()
    mID = float(input("Insert Member ID"))
    name = input("Insert Member Name")
    email = input("Insert Member Email")
    phone = input("Insert Member Phone number")
    address = input("Insert Member Address")
    age = float(input("Insert Member Age"))
    msStart = input("Insert Membership START Date (YEAR-MONTH-DAY)")
    msEnd= input("Insert Membership END Date (YEAR-MONTH-DAY)")
    cursor.execute(f"INSERT INTO Member(memberId,name,email,phone,address,age,membershipStartDate,membershipEndDate)  VALUES({mID},{name},{email},{phone},{address},{age},{msStart},{msEnd})")
    connection.commit()

    menu_members()

def act_update_member_info():
    cursor = connection.cursor()
    mID = float(input("Enter Member ID to update"))
    col = input("What column to edit?")
    val = input("What will this value be now? : Include quotes if the value is a string")

    q = f"UPDATE MEMBER SET {col} = {val} WHERE memberId ={mID}"
    cursor.execute(q)
    connection.commit()

    menu_members()

def act_delete_member():
    cursor = connection.cursor()

    mID = int(input("Enter a member ID to delete"))

    q = f"DELETE FROM Member WHERE memberId ={mID}"
    cursor.execute(q)
    connection.commit()
    

    menu_members()

# classes
# need to finish
def act_list_classes_and_attendance():
    cursor = connection.cursor()

    cID = int(input("Enter a class ID"))

    q =f"SELECT className FROM Classes WHERE classId ={cID}"
    q2 =f"SELECT Member.name FROM Member, Attends WHERE Member.memberId = 2 AND Attends.classId = {cID}"

    result = cursor.execute(q)

    print("Class: ")
    for entry in result:
        print(entry)
    
    result2 = cursor.execute(q2)
    print("Students in Class: ")
    for entry in result2:
        print(entry)
    
def act_add_new_class():
    cursor = connection.cursor()

    cID = int(input("Enter a new Class ID"))
    cName = input("Enter a new Class name")
    cType = input("Enter a new Class type : 'Yoga', 'HIIT', 'Weights', 'Zumba' ")
    duration = (input("Enter a Class duration in minutes"))
    cCapacity = int(input("Enter Class capacity"))
    iID = int(input("Enter an instructor ID"))
    gID = int(input("Enter a gym ID"))

    cursor.execute(f'INSERT INTO Classes(classId,className,classType,duration,classCapacity,instructorId,gymID) VALUES({cID},"{cName}","{cType}",{duration},{cCapacity},{iID},{gID})')
    connection.commit()


def act_update_class_info():
    cursor = connection.cursor()
    mID = float(input("Enter Class ID to update"))
  
    valid_edits = ["className","classType","duration","classCapacity","instructorId","gymID"]


    col = input("What column to edit? : className, classType, duration, classCapacity, instructorId, gymID")
    val = input("What will this value be now?")

    if (col not in valid_edits):
        print("Not a valid column")
        menu_classes()

    if (col == "classType" and val not in ["Yoga","Zumba","HIIT","Weights"]):
        print("Invalid class type")
        menu_classes()

    if (col in ["className","classType"]):
        val = '"'+val+'"'
    else:
        val = int(val)


    q = f"UPDATE CLASSES SET {col} = {val} WHERE classId ={mID}"
    cursor.execute(q)
    connection.commit()

    menu_classes()

# need to finish this
def act_delete_class():
    cursor = connection.cursor()

    cID = int(input("Enter a class ID to delete"))

    q = f"DELETE FROM Classes WHERE classId ={cID}"
    cursor.execute(q)
    connection.commit()
    
    menu_members()

def act_find_members_by_class():
    cursor = connection.cursor()

    cID = int(input("Enter a class ID"))

    q =f"SELECT className FROM Classes WHERE classId ={cID}"
    q2 =f"SELECT Member.name FROM Member, Attends WHERE Member.memberId = 2 AND Attends.classId = {cID}"

    result = cursor.execute(q)

    print("Class: ")
    for entry in result:
        print(entry)
    
    result2 = cursor.execute(q2)
    print("Students in Class: ")
    for entry in result2:
        print(entry)

# equipment
def act_show_equipment_details():
    cursor = connection.cursor()

    q = "SELECT * FROM Equipment"
    result = cursor.execute(q)

    print("Details : \nID, Name, Type, Quantity, GymID")
    for entry in result:
        print(entry)

def act_insert_new_equipment():
    cursor =  connection.cursor()

    eName = input("Enter name for this Equipment")
    eType = input("Enter type for this Equipment. : 'Cardio', 'Flexibility', 'Recovery'")
    eQuantity = int(input("Enter quantity"))
    eGID = int(input("Enter Gym ID for this Equipment"))
    
    cursor.execute(f'INSERT INTO Equipment(name,type,quantity,gymId) VALUES("{eName}","{eType}",{eQuantity},{eGID})')
    connection.commit()
    menu_equipment()


def act_update_equipment_details():
    cursor = connection.cursor()

    valid_edits = ["name","type","quantity","gymId"]

    eID = int(input("Enter an Equipment ID to update"))
    col = input("Enter a column to edit: name, type, quantity, gymId")
    
    if (col not in valid_edits):
        print("\nNot a valid column to edit\n")
        menu_equipment()
    
    val = input("Enter a value")

    if (col == "name" or col == "quantity"):
        val = '"'+val+'"'
    else:
        val = int(val)


    q = f"UPDATE EQUIPMENT SET {col} = {val} WHERE equipmentId ={eID}"
    cursor.execute(q)
    connection.commit()
    menu_equipment()

def act_delete_equipment():
    cursor = connection.cursor()

    eID = int(input("Enter an Equipment ID to delete"))

    q=f"DELETE FROM Equipment WHERE equipmentId ={eID}"
    cursor.execute(q)
    connection.commit()
    menu_equipment()

# ========


# Asks the user to give the name of a database


def req_connection():
    # print("Please enter the name of the database file to open...")
    # path = input()
    # connection = sqlite3.connect(path)
    # data = connection.execute("SELECT name FROM Member")
    connection = sqlite3.connect('XYZGym.sqlite')
    main_menu()

connection : sqlite3.Connection = sqlite3.connect('XYZGym.sqlite')

if __name__ == "__main__":
    req_connection()
    main_menu()
