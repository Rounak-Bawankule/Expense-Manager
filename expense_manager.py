# Expenses manager

import time
import os

def current_time():
    ctime = time.asctime(time.localtime(time.time()))
    return ctime
    
def view_file():
    """ funtion to view created databases """
    
    with open("log.txt" , "r") as fv:
        print(fv.read())
    file_open = input("Enter the file name you want to view : ")
    with open(f"{file_open}" , "r") as fo:
        content = fo.read()
        print(content)
   
    
def exp_single_entry(fs):
    """ funtion to enter data foe a single user database """
    
    expense_name = input("Enter the expense name : ")
    expense_cost = int(input("Enter the amount you spent : "))
    fs.write(f"{ctime} - {expense_name} : {expense_cost} \n")
    choice_s = input("Do you want to add more? (y)yes , (n)no:")
    if choice_s == 'y':
        exp_single_entry(fs)
    elif choice_s == 'n':
        exit()
        
def exp_group_entry(fg):
    """ Funtion to enter data for a group based database """
    person_name = input("Enter the name of the person doing the transaction : ")
    expense_name = input("Enter the expense name : ")
    expense_cost = int(input("Enter the amount you spent : "))
    fg.write(f"{ctime} - {person_name} -- {expense_name} : {expense_cost} \n")
    choice_s = input("Do you want to add more? (y)yes , (n)no:")
    if choice_s == 'y':
        exp_single_entry(fg)
    elif choice_s == 'n':
        exit()
            
def new_file():
    """ function to create a new file """
    st = input("Is it a group expense or a personal expense? (p)personal , (g)group : ")
    if st == "p":
        file_name = input("Enter a name for the new database:")
        with open(f"{file_name}","a") as fs:
            exp_single_entry(fs)
    elif st == "g":
        file_name = input("Enter a name for the new database:")
        with open(f"{file_name}","a") as fg:
            exp_group_entry(fg)
    else:
        print("Please enter a valid choice")
        st = input()
    with open("log.txt" , "a") as fl:
        fl.write(file_name)
        fl.write("\n")

def update_data():
    """ Function to update data in an existing file """
    
    st = input("Is it a group expense or a personal expense? (p)personal , (g)group : ")
    with open("log.txt" , "r") as fu:
        print(fu.read())
    if st == "p":
        file_update = input("Enter the name of database you want to update from above mentioned:")
        with open(f"{file_update}","a") as fus:
            exp_single_entry(fus)
    elif st == "g":
        file_update = input("Enter the name of database you want to update from above mentioned:")
        with open(f"{file_update}","a") as fug:
            exp_group_entry(fug)
    else:
        print("Please enter a valid choice")
        st = input()

def delete_file():
    """ Function to delete a created file """
    
    with open("log.txt" , "r") as fg:
       print(fg.read())
    delete_f = input("Choose a file from above list you want to delete : ")
    os.remove(f"{delete_f}")
    
    
        
if __name__ == '__main__':
    
    ctime = current_time()
    
    start = input("Enter the opration you want to perform : \n(1) - View a database \n(2) - create a new datbase \n(3) - update existing database \n(4) - Delete a database : ")
    if start == '1':
        view_file()
        
    elif start == '2':
        new_file()   
        
    elif start == '3':
        update_data()
        
    elif start == '4':
        delete_file()
        
    else:
        print("Please enter a valid choice")
        start = input()
        
    
