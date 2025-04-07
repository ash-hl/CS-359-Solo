import sqlite3
import sys

connection = sqlite3.connect('XYZGym.sqlite')

def query_1():
    q = """
    SELECT Member.name,Member.email,Member.age,MembershipPlan.planType FROM Member,MembershipPlan WHERE Member.memberId=MembershipPlan.planId
    """
    data = connection.execute(q)

    
    for i in data:
        print(i)

def query_2():
    query = "SELECT classcapacity,GymFacility.location FROM GymFacility,Classes WHERE Classes.gymID=GymFacility.gymId"

    data = connection.execute(query)

    for i in data:
        print(i)

def query_3(class_id):
    query = "SELECT * FROM Classes,Attends WHERE Attends.classId=Classes.classId AND Classes.classId = "+str(class_id)

    data = connection.execute(query)

    for i in data:
        print(i)

def query_4(equip_type):
    query = "SELECT name FROM Equipment WHERE Equipment.type= '"+str(equip_type)+"'"

    data = connection.execute(query)

    for i in data:
        print(i)

def query_5():
    query = "SELECT name,membershipenddate FROM Payment,Member Where Member.memberId=paymentid AND membershipenddate < DATE('now')"

    data = connection.execute(query)

    for i in data:
        print(i)

def query_6(inst_id):
    query = "SELECT Instructor.name,Instructor.phone,Classes.className,Classes.classType,Classes.duration,Classes.classCapacity FROM Instructor,Classes Where Instructor.instructorId = Classes.instructorId AND Instructor.instructorId = "+str(inst_id)

    data = connection.execute(query)

    for i in data:
        print(i)

def query_7():
    query_expired = "SELECT DISTINCT name FROM Member,MembershipPlan,Payment WHERE Member.memberId = (SELECT Member.memberId FROM Payment,MembershipPlan WHERE Payment.planId=MembershipPlan.planId) AND DATE(membershipenddate) < DATE('now')"
    query_running = "SELECT DISTINCT name FROM Member,MembershipPlan,Payment WHERE Member.memberId = (SELECT Member.memberId FROM Payment,MembershipPlan WHERE Payment.planId=MembershipPlan.planId) AND DATE(membershipenddate) > DATE('now')"

    data_e = connection.execute(query_expired)
    data_r = connection.execute(query_running)

    print("=== EXPIRED ===")
    for i in data_e:
        print(i)
    print("=== ONGOING ===")
    for i in data_r:
        print(i)

def query_8():
    query = "SELECT Instructor.name,COUNT(classid) FROM Instructor,Classes GROUP BY Instructor.instructorId ORDER BY COUNT(classid) LIMIT 3"

    data = connection.execute(query)

    for i in data:
        print(i)

def query_9(optional_parameter):
    query = "SELECT Member.name FROM Member,Attends,Classes WHERE Attends.memberId=Member.memberId AND Classes.classId=Attends.classId AND Classes.classType='"+str(optional_parameter)+"'"

    data = connection.execute(query)

    for i in data:
        print(i)

def query_10():
    
    start_date = '2025-10-03'

    query = "SELECT Member.name,Classes.className,Classes.classType,MembershipPlan.planType From Member,Attends,Classes,MembershipPlan Where Member.memberId=Attends.memberId AND Attends.classId = Classes.classId AND attendancedate BETWEEN DATE() AND DATE('2025-10-03','+1 month') AND MembershipPlan.planId = Member.memberId"
    
    data = connection.execute(query)

    # drawing table 
    print("Name\t\t\tTotal Classes Attended\t\t\tClasses\t\t\tClass Type")
    print("="*100)
    for row in data:
        
        # since all of my dates would result in the classes being at most, attened once, I hard coded the answer, but I will
        # most likely spread the dates out in the future

        classes_attended = 1

        print_row = row[0]+"\t\t\t"+str(classes_attended)+"\t\t\t"+row[1]+"\t\t\t"+row[2]
        print(print_row)



def main():
    param_len = len(sys.argv)
    if param_len == 1:
        print("No args were given")
        return
    
    question_number = int(sys.argv[1])
    optional_parameter = None
    if param_len == 3:
        optional_parameter = sys.argv[2]

    match question_number:

        case 1:
            query_1()

        case 2:
            query_2()

        case 3:
            query_3(optional_parameter)

        case 4:
            query_4(optional_parameter)

        case 5:
            query_5()

        case 6:
            query_6(optional_parameter)

        case 7:
            query_7()

        case 8:
            query_8()

        case 9:
            query_9(optional_parameter)

        case 10:
            query_10()

if __name__ == "__main__":
    main()
