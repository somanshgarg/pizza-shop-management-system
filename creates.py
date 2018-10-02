import tkinter as tk
from tkinter.constants import GROOVE
from datetime import datetime
import admin, manager, cashier, validation as valid, takeorder


class CreatePizza(tk.Tk):
    
    def __init__(self, empid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.frames = {} #DICTIONARY OF FRAMES
        container.configure(bg = "#7fff00")
        self.title("CREATE PIZZA @ PSMS")
        
        label = tk.Label(container, text = "      CREATE PIZZA      ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
  
        
        self.name  = tk.StringVar()
        self.price_s = tk.StringVar()
        self.price_m = tk.StringVar()
        self.price_l = tk.StringVar()
        self.shortcut = tk.StringVar()
        self.type = tk.StringVar()
        self.details = tk.StringVar()
        
        l3 = tk.Label(container, text = "NAME : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l3.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e1 = tk.Entry(container, textvariable = self.name, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l4 = tk.Label(container, text = "PRICE SMALL : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l4.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e2 = tk.Entry(container, textvariable = self.price_s, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l5 = tk.Label(container, text = "PRICE MEDIUM : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l5.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e3 = tk.Entry(container, textvariable = self.price_m, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l6 = tk.Label(container, text = "PRICE LARGE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l6.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e4 = tk.Entry(container, textvariable = self.price_l, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e4.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l7 = tk.Label(container, text = "SHORTCUT : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l7.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e5 = tk.Entry(container, textvariable = self.shortcut, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e5.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l8 = tk.Label(container, text = "TYPE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l8.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "w")
        
        types = ["VEG","NON-VEG"]
        sm= tk.OptionMenu(container, self.type, *types)
        sm.grid(row = 6, column = 1, padx = 10, pady = 10)
        menu = sm.nametowidget(sm.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        self.type.set("VEG")
    
        
        l9 = tk.Label(container, text = "DETAILS : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l9.grid(row = 7, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.disp = tk.Text(container, height = 5, width = 18, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        self.disp.grid(row = 8, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "CREATE", command = self.update, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 9, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 10, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 10, column = 1, padx = 10, pady = 10, sticky = "we")
        
        
    def mainmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
  
      
        if des == "MANAGER" :
            manager.startManager(self.empid, self.cur)
            
        elif des == "ADMIN":
            admin.startAdmin(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
     
        if des == "MANAGER":
            x = manager.Manager(self.empid, self.cur)
            x.back("Menu")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("Menu")
    
    def update(self):
        self.cur.execute("select max(prid) from menu")
        res = self.cur.fetchall()
        prid = res[0][0]+1
        
        self.cur.execute("select name,shortcut from menu")
        res = self.cur.fetchall()
        lonm = []
        loshrt = []
        for i in res:
            lonm.append(i[0].upper())
            loshrt.append(i[1].upper())
        name = self.name.get()
        name = name.upper()
        prices = self.price_s.get()
        pricem = self.price_m.get()
        pricel = self.price_l.get()
        shortcut = self.shortcut.get()
        shortcut = shortcut.upper()
        type  = self.type.get()
        details = self.disp.get("1.0", "end-1c")
        chk_name = valid.validPizzaNameandDetails(name)
        
        if chk_name:
            chk_name = False
            
            for i in lonm:
               
                if name == i:
                    chk_name = False
                    break
                chk_name = True
            if chk_name:
                if len(name) < 25:
                    chk_prices = valid.validNumber(prices)
                    chk_pricem = valid.validNumber(pricem)
                    chk_pricel = valid.validNumber(pricel)
                    
                    if chk_prices and chk_pricem and chk_pricel:
                            chk_shrt = False
                           
                            for i in loshrt:
                                if shortcut == i:
                                    chk_shrt = False
                                    break
                                chk_shrt = True
                            if chk_shrt:
                                if len(shortcut)<9:
                                    self.cur.execute("insert into menu(name,price_s,price_m,price_l,type,shortcut,details,prid) values(:1,:2,:3,:4,:5,:6,:7,:8)",(name,prices,pricem,pricel,self.type.get(),shortcut.upper(),details,prid))
                                    self.cur.execute("commit")
                                    tk.messagebox.showinfo(title = "SUCCESSFULLY CREATED", message = "PIZZA CREATED SUCCESSFULLY !")
                                else:
                                    tk.messagebox.showerror(title = "SHORTCUT TOO LONG", message = "SHORTCUT SHOULD BE LESS THAN 9 CHARATCERS !")
                            else:
                                tk.messagebox.showerror(title = "INVALID SHORTCUT", message = "SHORTCUT ALREADY EXISTS  !")
                    
                    else:
                        tk.messagebox.showerror(title = "INVALID INPUT", message = "PRICE SHOULD BE NUMERIC ONLY !")
                    
                else:
                    tk.messagebox.showerror(title = "TOO LONG NAME", message = "NAME SHOULD BE OF LESS THAN 25 CHARACTERS !")
            else:
                tk.messagebox.showerror(title = "INVALID NAME", message = "NAME ALREADY EXISTS !")
        else:
            tk.messagebox.showerror(title = "INVALID NAME", message = "NAME SHOULD BE ONLY CHARACTERS !")
            
class CreateEmployee(tk.Tk):
    
    def __init__(self, empid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        container.configure(bg = "#7fff00")
        self.title("CREATE EMPLOYEE @ PSMS")
        
        label = tk.Label(container, text = "           CREATE   EMPLOYEE        ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
      
       
        
        self.name  = tk.StringVar()
        self.address= tk.StringVar()
        self.dob = tk.StringVar()
        self.doj = tk.StringVar()
        self.gender = tk.StringVar()
        self.mobile = tk.StringVar()
        self.password = tk.StringVar()
        self.salary = tk.StringVar()
        self.designation = tk.StringVar()

     
        lab3= tk.Label(container, text = "NAME : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab3.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e1= tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        
        lab4= tk.Label(container, text = "MOBILE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab4.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e2= tk.Entry(container, textvariable = self.mobile, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 3, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        
        lab5= tk.Label(container, text = "ADDRESS : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab5.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e3= tk.Entry(container, textvariable = self.address, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 4, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        
        lab6= tk.Label(container, text = "DATE OF BIRTH dd/mm/yyyy : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab6.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e4= tk.Entry(container, textvariable = self.dob, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e4.grid(row = 5, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        
        lab7= tk.Label(container, text = "GENDER :", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab7.grid(row = 6, column = 0, padx = 1, pady = 1, sticky = "w")
        
        self.gender.set("MALE")
        genders = ["MALE","FEMALE","OTHER"]
        opt1= tk.OptionMenu(container, self.gender, *genders)
        opt1.grid(row = 6, columnspan = 2, padx = 10, pady = 10,sticky = "e")
        menu = opt1.nametowidget(opt1.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        
        lab8= tk.Label(container, text = "DATE OF JOINING dd/mm/yyyy : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab8.grid(row = 7, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e5= tk.Entry(container, textvariable = self.doj, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e5.grid(row = 7, column = 1, padx = 1, pady = 1, sticky = "we")
        
        but1 = tk.Button(container, text = "TODAY   ", command = self.today, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold") )
        but1.grid(row = 7, column = 2, padx = 1, pady = 1, sticky = "e")
        
        lab9= tk.Label(container, text = "  PASSWORD ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab9.grid(row = 8, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e6= tk.Entry(container, textvariable = self.password, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e6.grid(row = 8, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        
        but2 = tk.Button(container, text = "DEFAULT", command = self.default, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold") )
        but2.grid(row = 8, column = 2, padx = 1, pady = 1, sticky = "e")
        
        lab10= tk.Label(container, text = "  SALARY ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab10.grid(row = 9, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e7= tk.Entry(container, textvariable = self.salary, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e7.grid(row = 9, columnspan = 2, padx = 1, pady = 1, sticky = "e")
        
        lab11= tk.Label(container, text = "DESIGNATION ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab11.grid(row = 10, column = 0, padx = 1, pady = 1, sticky = "w")
        
        self.designation.set("CASHIER")
        des = ["CASHIER","MANAGER","ADMIN"]
        opt1= tk.OptionMenu(container, self.designation, *des)
        opt1.grid(row = 10, columnspan = 2, padx = 10, pady = 10, sticky = "e")
        menu = opt1.nametowidget(opt1.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)

        but3 = tk.Button(container, text = "CREATE", command = self.create,fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 11, columnspan = 3, padx = 10, pady = 10,sticky = "we")
        
        but4 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 12, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but5 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row= 12,column = 2, padx = 10, pady = 10, sticky = "we")
    
    def today(self):
        x= datetime.now().date()
        a,b,c = str(x).split('-')
        x = c+"/"+b+"/"+a
        self.doj.set(x)
        
    def default(self):
        self.password.set("PSMSOM1@")
       
    def mainmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]

        if des == "ADMIN":
            admin.startAdmin(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]

        if des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("HireFireRehire")
    
    def create(self):
        name = self.name.get()
        mobile = self.mobile.get()
        dob = self.dob.get()
        doj = self.doj.get()
        gender = self.gender.get()
        address = self.address.get()
        sal = self.salary.get()
        chk_sal = valid.validNumber(sal)
        passd = self.password.get()
        chk_pass = valid.validPassword(passd)
        
        chk_name = valid.validName(name)
        chk_dob = valid.validDate(dob)
        chk_doj = valid.validDate(doj)
        chk_mobile = valid.validMobile(mobile)
        
        empty_name = False
        empty_add  = False
        empty_salary = False
        if len(name)==0:
            empty_name = True
        if len(address)== 0:
            empty_add = True
        if len(sal) == 0:
            empty_salary = True
        if empty_name:
            tk.messagebox.showerror(title = "INVALID NAME", message = "NAME CANNOT BE EMPTY !")
            
        else:
            if empty_add:
                tk.messagebox.showerror(title = "INVALID ADDRESS", message = "ADDRESS CANNOT BE EMPTY !")
            else:
                if empty_salary:
                    tk.messagebox.showerror(title = "INVALID SALARY", message = "SALARY CANNOT BE EMPTY !")
                else:
                    
                    if chk_name:
                        if chk_dob and chk_doj:
                            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                               
                            a,b,c = dob.split('/')
                            dob = a+"-"+mon[int(b)]+"-"+c
                            a,b,c = doj.split('/')
                            doj = a+"-"+mon[int(b)]+"-"+c
                            
                                     
                            if chk_mobile:
                                chk2 = False
                                self.cur.execute("select mobile from employees")
                                res = self.cur.fetchall()
                                
                                for i in res:
                                    if str(i[0]) == mobile:
                                        chk2 = False
                                        break
                                    chk2 = True
                                        
                                if chk2:
                                    if chk_sal:
                                        if chk_pass:
                                            self.cur.execute("select max(empid) from employees")
                                            res = self.cur.fetchall()
                                            employeeid = res[0][0] + 1
                                            self.cur.execute("insert into employees(mobile,address,gender,dob,doj,name,password,salary,designation,empid,status) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)",(int(mobile),address,gender,dob,doj,name,passd,int(sal),self.designation.get(),employeeid,"ACTIVE"))
                                            self.cur.execute("commit")
                                            st = "EMPLOYEE CREATED!\n ID : " + str(employeeid)+ " \nPASWORD : "+passd
                                            tk.messagebox.showinfo(title = "SUCCESS", message = st)
                                        else:
                                            tk.messagebox.showerror(title = "INVALID PASSWORD", message = "PASSSWORD MUST BE OF ATLEAST 8 CHARACTERS !\n MUST CONTAIN ATLEAST 1 DIGIT!! \n MUST CONTAIN ATLEAST 1 SPECIAL CHARACTER!!! \n MUST CONTAIN ATLEAST 1 ALPHABET!!!! \n")
                                    else:
                                        tk.messagebox.showerror(title = "INVALID SALARY", message = "SALARY SHOULD BE NUMERIC ONLY !")
                                else:
                                    tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE NUMBER ALREADY EXISTS !")
                    
                            else:
                                tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE SHOULD BE NUMERIC AND OF 10 DIGITS ONLY !")
                    
                        else:
                            tk.messagebox.showerror(title = "INVALID DATE", message = "DATE SHOULD BE VALID AND FORMAT - dd/mm/yyyy !")
                    
                            
                    else:
                        tk.messagebox.showerror(title = "INVALID NAME", message = "NAME SHOULD BE ONLY OF CHARACTERS !")
            

class CreateCustomer(tk.Tk):
    
    def __init__(self, empid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.frames = {} #DICTIONARY OF FRAMES
        container.configure(bg = "#7fff00")
        self.title("CREATE CUSTOMER @ PSMS")
        
        label = tk.Label(container, text = "    CREATE CUSTOMER   ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
  
        
        self.name  = tk.StringVar()
        self.mobile = tk.StringVar()
        self.gender = tk.StringVar()
        
        l1 = tk.Label(container, text = "ENTER NAME : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e1 = tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l2 = tk.Label(container, text = "ENTER MOBILE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e2 = tk.Entry(container, textvariable = self.mobile, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l3 = tk.Label(container, text = "ENTER GENDER : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l3.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        
        gender = ["MALE","FEMALE","OTHER"]
        self.gender.set("MALE")
        opt1 = tk.OptionMenu(container, self.gender, *gender)
        opt1.grid(row= 3, column = 1, padx = 10, pady  =10, sticky = "e")
        
        menu = opt1.nametowidget(opt1.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)

        
        but1 = tk.Button(container, text = "CREATE", command = self.create,fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 4, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but3 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row= 5,column = 1, padx = 10, pady = 10, sticky = "we")
    
    def create(self):
        chkname_empty = False
        chkmob_empty = False
        if len(self.name.get()) == 0:
            chkname_empty = True
        if len(self.mobile.get()) == 0:
            chkmob_empty = True
        
        chk_name = valid.validName(self.name.get())
        chk_mob = valid.validMobile(self.mobile.get())
        
        if chkname_empty:
            tk.messagebox.showerror(title = "INVALID NAME", message = "NAME CANNOT BE EMPTY !")
        else:
            if chkmob_empty:
                tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE CANNOT BE EMPTY !")
            else:
                if not chk_name:
                    tk.messagebox.showerror(title = "INVALID NAME", message = "NAME SHOULD CONTAIN LETTERS ONLY !")
                else:
                    if not chk_mob:
                        tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE SHOULD BE NUMERIC !\n MOBILE SHOULD BE OF 10 DIGITS ONLY !!")
                        
                    else:
                        self.cur.execute("select * from customers where mobile=:1",(int(self.mobile.get()),))
                        res = self.cur.fetchall()
                        if len(res) == 0:
                            
                            self.cur.execute('insert into customers(name,mobile,gender) values(:1,:2,:3)',(self.name.get(),int(self.mobile.get()),self.gender.get()))
                            self.cur.execute('commit')
                            tk.messagebox.showinfo(title = "SUCCESSFUL", message = "CUSTOMER CREATED SECCESSFULLY !")
                        else:
                            tk.messagebox.showerror(title = "INVALID CUSTOMER", message = "CUSTOMER ALREADY EXIST !")
                        
        
    def mainmenu(self):
        self.destroy()
    
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]

        if des == "ADMIN":
            admin.startAdmin(self.empid, self.cur)
        elif des == "MANAGER":
            manager.startManager(self.empid, self.cur)
        else:
            cashier.startCashier(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        takeorder.startOrder(self.empid, self.cur)

#-------------------------------------------------------------------------------------------------------------------