import csv 

def write_into_csv(detail):
    filename = 'MyCaptain_project1.csv'
    
    with open(filename, 'w') as csv_file: 
        field = ['Name' , 'Age' , 'Contact Number' , 'Address' , 'Email ID']
        csv_writer = csv.writer(csv_file) 
        csv_writer.writerow(field)
        csv_writer.writerow(detail)
        

loop_condition = True

while loop_condition:
    ask_user = input('Do you want to enter student information ? (yes/no) : ')
    ask_user = ask_user.lower()
    
    if ask_user == 'yes':
        Details = []
        confirm_condition = True
        
        while confirm_condition:
            Student_name = input('Enter Student Name : ')
            Student_age = int(input('Enter Student Age :'))
            Student_contact = int(input('Enter Student Contact Number :'))
            Student_address = input('Enter Student Address :')
            Student_email = input('Enter Student Email ID :')
            dict_info = {'Name' : Student_name , 'Age' : Student_age , 'Contact Number' : Student_contact , 
            'Address' : Student_address , 'Email ID' : Student_email}
            for key , value in dict_info.items():
                print(key , ':' , value)

            ask_confirm = input('Are the details entered for {} correct ? (yes/no) :'.format(Student_name))
            ask_confirm = ask_confirm.lower()

            if ask_confirm == 'yes':
                for value in dict_info.values():
                    Details.append(value)
                write_into_csv(Details)
                confirm_condition = False
                
            else:
                confirm_condition = True
                
        loop_condition = True
        
    else:
        loop_condition = False 
