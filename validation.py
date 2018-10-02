import re


def validName(name):#TESTED
    reg = "(^([a-z,A-Z]*)$)|(^([a-z,A-Z])*\s([a-z,A-Z])*$)"#CHECKS FOR NAME OR NAME AND LAST NAME
    confirm = re.search(reg,name)
    if confirm == None:
        return False
    else:
        return True

def validMobile(mobile):#TESTED
    reg = "^[1-9]\d{9}$"#CHECKS FOR 10 DIGITS WHERE FIRST DIGIT SHOULD NOT BE ZERO
    confirm = re.search(reg,mobile)
    if confirm == None:
        return False
    else:
        return True
    
def validPassword(password):
    length = len(password)
    if length<8:
        #"Password should be of at least 8 characters"
        return False
    letter = re.search("[a-z,A-Z]",password)
    if letter == None:
        #"Password should contain at least 1 alphabet"
        return False
    digit = re.search("\d",password)
    if digit == None:
        #"Password should contain at least 1 digit"
        return False
    spc = re.search("\W|[_]",password)
    if spc == None:
        #"Password should contain at least 1 special character"
        return False
    return True
    
def validDate(dat):
    dat = re.split("[./-]",dat)
    if len(dat) != 3:
        #"Date should take exactly 3 parameters"
        return False
    try:
        day,month,year = list(map(int,dat))
    except Exception as e:
        #"Invalid entry should be only Integer"
        return False
    if not(year>=1000 and year<=9999):
        #"Correct year format is 'yyyy' and between 1950 - 2018"
        return False
    if not(month>=1 and month<=12):
        #"Invalid month , should be between 1 - 12"
        return False
    if day<=0:
        #"Day cannot be zero or negative"
        return False
    mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if (year%400==0) or (year%4==0 and year%100!=0):
        mon[2] = 29#if leap year
    if day>mon[month]:
        #" month cannot have more than these much days
        return False
    return True

def validSalary(salary):
    salary = str(salary)
    res = re.search("^\d*$",salary)
    if res == None:
        return False
    else:
        return True
    
def validPizzaNameandDetails(pizza):
    res = re.search("^[\w\s,.-]*$", pizza)
    if res == None:
        return False
    else:
        return True
    
def validNumber(num):
    num = str(num)
    res = re.search("^\d*$", num)
    if res == None:
        return False
    else:
        return True

#-------------------------------------------------------------------------------------------------------------------