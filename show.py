import tkinter as tk
import validation as valid, cashier, manager, admin, customer
from tkinter.constants import DISABLED, INSERT, NORMAL
from datetime import datetime
from tkinter.constants import GROOVE


class ShowSinglePizza(tk.Tk):
    
    def __init__(self, empid, prid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.title("SINGLE PIZZA DETAILS @ PSMS")
        self.frames = {} #DICTIONARY OF FRAMES
        cur.execute("select * from menu where prid=:1",(prid,))
        res = cur.fetchall()
        res = res[0]
        st = "\n"
        st += "PRODUCT ID : "+str(res[0])
        st += "\nPRODUCT NAME : "+str(res[1])
        st += "\nPRICE-    SMALL: "+str(res[2])+"    MEDIUM: "+str(res[3])+"    LARGE: "+str(res[4])
        st += "\nSHORTCUT : "+str(res[5])
        st += "\nTYPE : "+str(res[6])
        st += "\nDETAILS : "+str(res[7])
        container.configure(bg = "#7fff00")
        
        l1 = tk.Label(container, text = "      SINGLE   PIZZA   DETAILS       ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        l1.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        disp = tk.Text(container)
        disp.insert(INSERT, st)
        disp.configure(state = DISABLED)
        disp.grid(row = 1, columnspan = 2, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "we")
        
        
    def mainmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
        if des == "CASHIER":
            
            cashier.startCashier(self.empid, self.cur)
            
        elif des == "MANAGER" :
            manager.startManager(self.empid, self.cur)
            
        elif des == "ADMIN":
            admin.startAdmin(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
        if des == "CASHIER":
           
            x = cashier.Cashier(self.empid, self.cur)
            x.back("SinglePizza")
        
        elif des == "MANAGER":
            x = manager.Manager(self.empid, self.cur)
            x.back("SinglePizza")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("SinglePizza")

            
class CustomerDetailsOrder(tk.Tk):
    
    def __init__(self, empid,custid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        container.configure(bg = "#7fff00")
        self.cur = cur
        self.frames = {} #DICTIONARY OF FRAMES
        self.title("CUSTOMER ORDER DETAILS @ PSMS")
        self.custid = custid
        cur.execute('select name from customers where mobile=:1',(custid,))
        res = cur.fetchall()
        name = res[0][0]
        cur.execute('select * from orders where custid=:1 order by ordid desc',(custid,))
        res = cur.fetchall()
        st = "\n NAME : "+name.upper()+"\n\n"
       
        for last in res:
            
            st += "\nORDER ID : "+str(last[0])
            st += "\nDATE : "+str(last[3])
            st += "\nBILL AMOUNT: "+str(last[4])
            st += "\nBILL DETAILS : "+str(last[5])+"\n"
            st += "********************************************************************************"
        
        l1 = tk.Label(container, text = "  CUSTOMER   ORDER   DETAILS   ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        l1.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        disp = tk.Text(container)
        disp.insert(INSERT, st)
        disp.configure(state = DISABLED)
        disp.grid(row = 1, columnspan = 2, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "we")
        
        
    def mainmenu(self):
        self.destroy()
        if int(self.empid) == 0:#FUCNTION IS CALLED BY CUSTOMER
            customer.startCustomer(self.custid, self.cur)
        else:#FUCNTION IS CALLED BY EMPLOYEE
            self.cur.execute("select designation from employees where empid = :1",(self.empid,))
            res = self.cur.fetchall()
            des = res[0][0]
            
            if des == "CASHIER":
                
                cashier.startCashier(self.empid, self.cur)
                
            elif des == "MANAGER":
                manager.startManager(self.empid, self.cur)
                
            elif des == "ADMIN":
                admin.startAdmin(self.empid, self.cur)
                
    def backmenu(self):
        self.destroy()
        if int(self.empid) == 0:#FUCNTION IS CALLED BY CUSTOMER
            customer.startCustomer(self.custid, self.cur)
        else:#FUCNTION IS CALLED BY EMPLOYEE
            self.cur.execute("select designation from employees where empid = :1",(self.empid,))
            res = self.cur.fetchall()
            des = res[0][0]
            
            if des == "CASHIER":
               
                x = cashier.Cashier(self.empid, self.cur)
                x.back("OrderCustomer")
                
            elif des == "MANAGER":
                x = manager.Manager(self.empid, self.cur)
                x.back("OrderCustomer")
                
            elif des == "ADMIN":
                x = admin.Admin(self.empid, self.cur)
                x.back("OrderCustomer")
            
class CustomerDetails(tk.Tk):
    
    def __init__(self, empid,custid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.custid = custid
        self.title("CUSTOMER DETAILS @ PSMS")
        container.configure(bg = "#7fff00")
        
        self.frames = {} #DICTIONARY OF FRAMES
        st = "\n"
        cur.execute('select max(ordid) from orders where custid=:1',(custid,))
        res = cur.fetchall()
        res = res[0]
        cur.execute("select * from orders where ordid=:1",(res[0],))
        last = cur.fetchall()
        last = last[0]
        cur.execute('select * from customers where mobile=:1',(custid,))
        res = cur.fetchall()
        res = res[0]
        st += "\nNAME : "+res[0]
        st += "\nMOBILE : "+str(res[1])
        st += "\nGENDER : "+res[2]
        st += "\nDATE OF FIRST ORDER : "+str(res[3]).split()[0]
        st += "\nPOINTS : "+str(res[4])
        st +="\n\nLAST ORDER WAS :"
        st += "\n ORDER ID : "+str(last[0])+"\n DATE : "+str(last[3])+"\n BILL AMOUNT : "+str(last[4])+"\n BILL DETAILS : "+str(last[5])
      
        
        l1 = tk.Label(container, text = "        CUSTOMER     DETAILS         ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        l1.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        disp = tk.Text(container)
        disp.insert(INSERT, st)
        disp.configure(state = DISABLED)
        disp.grid(row = 1, columnspan = 2, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "we")
        
        
    def mainmenu(self):
        self.destroy()
        if int(self.empid) == 0:#FUCNTION IS CALLED BY CUSTOMER
            customer.startCustomer(self.custid, self.cur)
        else:#FUCNTION IS CALLED BY EMPLOYEE
            self.cur.execute("select designation from employees where empid = :1",(self.empid,))
            res = self.cur.fetchall()
            des = res[0][0]
            
            if des == "CASHIER":
                
                cashier.startCashier(self.empid, self.cur)
            elif des == "MANAGER":
                manager.startManager(self.empid, self.cur)
            
            elif des == "ADMIN":
                admin.startAdmin(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        if int(self.empid) == 0:#FUCNTION IS CALLED BY CUSTOMER
            customer.startCustomer(self.custid, self.cur)
        else:#FUCNTION IS CALLED BY EMPLOYEE
            self.cur.execute("select designation from employees where empid = :1",(self.empid,))
            res = self.cur.fetchall()
            des = res[0][0]
          
            if des == "CASHIER":
               
                x = cashier.Cashier(self.empid, self.cur)
                x.back("DetailsCustomer")
                
            elif des == "MANAGER":
                x = manager.Manager(self.empid, self.cur)
                x.back("DetailsCustomer")
            
            elif des == "ADMIN":
                x = admin.Admin(self.empid, self.cur)
                x.back("DetailsCustomer")
            
class ShowParticularEmployee(tk.Tk):
    
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
        self.title("PARTICULAR EMPLOYEE @ PSMS")
        self.frames = {} #DICTIONARY OF FRAMES
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "PARTICULAR EMPLOYEE ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        l1 = tk.Label(container, text = "ENTER EMPLOYEE ID : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.employee_id = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.employee_id, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(container, text = "SHOW", command = self.show, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        st = "WELCOME TO VIEW PARTICULAR EMPLOYEE"
        self.disp = tk.Text(container, width = 45, height = 15)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 4, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "ew")
        
        
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
            x.back("ViewEmployeeDetails")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ViewEmployeeDetails")
            
    def show(self):
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des_empid = res[0][0]
        
        viewid = self.employee_id.get()
        chk = valid.validNumber(viewid)
        
        if chk:
            self.cur.execute("select empid from employees")
            res = self.cur.fetchall()
            loemp = []
            for i in res:
                loemp.append(str(i[0]))
            if viewid in loemp:
                self.cur.execute("select designation from employees where empid = :1",(int(viewid),))
                res = self.cur.fetchall()
                des_vid = res[0][0]
                if des_empid == "MANAGER":
                    if des_vid == "CASHIER":
                        self.screen(viewid)
                    else:
                        tk.messagebox.showerror(title = "NOT AUTHORIZED", message = "YOU ARE NOT AUTHORIZED TO VIEW THIS ACCOUNT !")
                else:
                    self.screen(viewid)
        
                
            else:
                tk.messagebox.showerror(title = "INVALID ID", message = "EMPLOYE ID DOES NOT EXIST !")
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "EMPLOYEE ID SHOULD BE NUMERIC ONLY !")
    
    def screen(self, viewid):
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        st = ""
        
        self.cur.execute('select * from employees where empid=:1',(int(viewid),))
        res = self.cur.fetchall()
        res = res[0]
        st += "\nEMPLOYEE ID : "+str(res[0])
        st += "\nNAME : "+res[1]
        st += "\nMOBILE NUMBER : "+ str(res[2])
        st += "\nADDRESS : "+ res[3]
        st += "\nGENDER : "+res[4]
        st += "\nDATE OF BIRTH : "+ str(res[5])
        st += "\nDATE OF JOINING : "+ str(res[6])
        if res[8] == "INACTIVE":#TO CHECK WHETHER EMPLOYEE IS STILL ACTIVE OR FIRED
            st += "\nDATE OF FIRED : "+str(res[7])
        st += "\nSTATUS : "+ res[8]
        st += "\nPASSWORD : "+res[9]
        st += "\nSALARY : "+ str(res[10])
        st +="\nDESIGNATION : "+res[11]
        st += "\nLOCK STATUS : "+res[12]
        
        self.disp.insert("1.0", st)
        
class ShowAllEmployee(tk.Tk):
    
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
        self.title("ALL EMPLOYEE @ PSMS")
        self.frames = {} #DICTIONARY OF FRAMES
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "      ALL   EMPLOYEE   ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        st = "WELCOME TO VIEW ALL EMPLOYEE"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 1, columnspan = 3, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "HIRED", command = lambda : self.show("ACTIVE"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(container, text = "FIRED", command = lambda : self.show("INACTIVE"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "ALL", command = lambda : self.show("ALL"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
        but4 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 3, columnspan =2 , padx = 10, pady = 10,sticky = "we")
        
        but5 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
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
            x.back("ViewEmployeeDetails")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ViewEmployeeDetails")
            
    def show(self, par):
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des= res[0][0]
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        query = ''
        if des == "MANAGER":
            if par == "ACTIVE":
                query = "select * from employees where designation = 'CASHIER' and STATUS = 'ACTIVE' order by empid"
            
            elif par == "INACTIVE":
                query = "select * from employees where designation = 'CASHIER' and STATUS = 'INACTIVE' order by empid "
                
            else:
                query = "select * from employees where designation = 'CASHIER' order by empid"
                
        else:
            if par == "ACTIVE":
                query = "select * from employees where STATUS = 'ACTIVE' order by empid"
            
            elif par == "INACTIVE":
                query = "select * from employees where STATUS = 'INACTIVE' order by empid"
                
            else:
                query = "select * from employees order by empid"
        
        self.cur.execute(query)
        i = self.cur.fetchall()
        st = ''
        for res in i:
            st += "\nEMPLOYEE ID : "+str(res[0])
            st += "\nNAME : "+res[1]
            st += "\nMOBILE NUMBER : "+ str(res[2])
            st += "\nADDRESS : "+ res[3]
            st += "\nGENDER : "+res[4]
            st += "\nDATE OF BIRTH : "+ str(res[5])
            st += "\nDATE OF JOINING : "+ str(res[6])
            if res[8] == "INACTIVE":#TO CHECK WHETHER EMPLOYEE IS STILL ACTIVE OR FIRED
                st += "\nDATE OF FIRED : "+str(res[7])
            st += "\nSTATUS : "+ res[8]
            st += "\nPASSWORD : "+res[9]
            st += "\nSALARY : "+ str(res[10])
            st +="\nDESIGNATION : "+res[11]
            st += "\nLOCK STATUS : "+res[12]
            st += "\n--------------------------------------------------\n"
        
        
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)

class SalesByEmployee(tk.Tk):
    
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
        self.title("SALES BY EMPLOYEE @ PSMS")
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "            SALES       BY       EMPLOYEE            ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        l1 = tk.Label(container, text = "ENTER EMPLOYEE ID", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, columnspan = 3, padx = 10, pady = 10, sticky = "we")
        
        self.employeeid = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.employeeid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, columnspan = 3, padx = 10, pady = 10, sticky = "we")
        
        l2 = tk.Label(container, text = "ENTER PARTICULAR DAY - dd/mm/yyyy", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.particularday = tk.StringVar()
        e2 = tk.Entry(container, textvariable = self.particularday, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(container, text = "DISPLAY", command = self.salePDay, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = "we")
        
        l3 = tk.Label(container, text = "ENTER MONTH NUMBER OR NAME", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l3.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.month = tk.StringVar()
        e3 = tk.Entry(container, textvariable = self.month, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(container, text = "DISPLAY", command = self.salePMonth, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 4, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
        
        st = "WELCOME TO SALES BY EMPLOYEE"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(rowspan = 4, columnspan = 2, padx = 10, pady = 10)
        
        l4 = tk.Label(container, text = "CURRENT MONTH", font = ("arial black",12, "bold"), fg = "black", bg = "white", relief = GROOVE)
        l4.grid(row = 5, column = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "HIGHEST EMPLOYEE SALE", command = self.highestEmpSale, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 6, column = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(container, text = "LOWEST EMPLOYEE SALE", command = self.lowestEmpSale, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 7, column = 2, padx = 10, pady = 10, sticky = "we")
        
        but5 = tk.Button(container, text = "ALL EMPLOYEE SALE", command = self.AllEmpSale, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but5.grid(row = 8, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
        but6 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 9, column = 0, padx = 10, pady = 10,sticky = "we")
        
          
        but7 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but7.grid(row = 9, column = 2, padx = 10, pady = 10, sticky = "we")
    
    def salePMonth(self):
        chk = self.verify()
        mon1 = [' ','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        mon2 = [' ','JANUARY','FEBRAURY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
        chk_month = False
        mn = ''
        if valid.validNumber(self.month.get()):
            if self.month.get() == '':
                chk_month = False
                tk.messagebox.showerror(title = "INVALID MONTH NUMBER", message = "MONTH SHOULD NOT BE EMPTY !")
            else:
                if int(self.month.get()) in range(1,13):
                    chk_month = True
                    mn = int(self.month.get())
                else:
                    tk.messagebox.showerror(title = "INVALID MONTH NUMBER", message = "MONTH SHOULD BE BETWEEN 1-12 !")
        else:
            mn = self.month.get()
            mn = mn.upper()
            if self.month.get() != '':
                chk_month = False
                if mn in mon1:
                    mn = mon1.index(mn)
                    chk_month = True
                elif mn in mon2:
                    mn = mon2.index(mn)
                    chk_month = True
                else:
                    tk.messagebox.showerror(title = "INVALID MONTH NAME", message = "NO SUCH MONTH EXISTS !")
            else:
                tk.messagebox.showerror(title = "INVALID MONTH NAME", message = "NO SUCH MONTH EXISTS !")
        if chk:
            
            if chk_month:
                st = ''
                month = mn
                self.cur.execute('select sum(bill), count(ordid), count(DISTINCT custid) from orders where EXTRACT(month from time) = :1 and empid = :2',(month,int(self.employeeid.get())))
                res = self.cur.fetchall()
                res= res[0]
                if res[0] == None:
                    st = "NO RECORD TO DISPLAY, PLEASE ENTER VALID MONTH OR EMPLOYEE ID"
                else:
                    st += "\nEMPLOYEE ID : "+self.employeeid.get()
                    self.cur.execute("select name from employees where empid=:1",(int(self.employeeid.get()),))
                    res2 = self.cur.fetchall()
                    name = res2[0][0]
                    st += "\nNAME : "+name
                    mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                    st += "\nMONTH : "+mon[month]
                    st += "\nTOTAL SALES : RS "+str(res[0])
                    st += "\nORDERS TAKEN : "+str(res[1])
                    st += "\nNUMBER OF DISTINCT CUSTOMERS : "+str(res[2])
                
                self.disp.configure(state = NORMAL)
                self.disp.delete("1.0", tk.END)   
                self.disp.insert("1.0", st)
                self.disp.configure(state = DISABLED)
            
    
    def salePDay(self):
        chk = self.verify()
        if chk:
            chk_date = valid.validDate(self.particularday.get())
            if chk_date:
                day = self.particularday.get()
                a,b,c = day.split('/')
                mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                day = a+"-"+mon[int(b)]+"-"+c
                self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 and empid=:2",(day,int(self.employeeid.get())))
                res = self.cur.fetchall()
                st = "\n"
                res = res[0]
                if res[2] == None:
                    st = "NO RECORD TO DISPLAY"
                else:
                    self.cur.execute('select empid,name,mobile,gender from employees where empid=:1',(int(self.employeeid.get()),))
                    res2 = self.cur.fetchall()
                    res2 = res2[0]
                    st += "\nTOTAL SALE DONE BY "+str(res2[1])+" is "+str(res[2])
                    st +=  "\nNUMBER OF ORDERS FULFILLED : "+str(res[0])
                    st += "\nNUMBER OF CUSTOMERS HANDLED : "+str(res[1])
                    st += "\n\nOTHER DETAILS :"
                    st += "\nEMPID : "+str(res2[0])
                    st += "\nNAME : "+str(res2[1])
                    st += "\nMOBILE : "+str(res2[2])
                    st += "\nGENDER : "+str(res2[3])
                self.disp.configure(state = NORMAL)
                self.disp.delete("1.0", tk.END)   
                self.disp.insert("1.0", st)
                self.disp.configure(state = DISABLED)
            else:
                tk.messagebox.showerror(title = "INVALID DATE INPUT", message = "DATE SHOULD BE IN dd/mm/yyyy FORMAT ! \n INVALID INPUT !!")
    
    def verify(self):
        chk = valid.validNumber(self.employeeid.get())
        if chk:
            self.cur.execute("select empid from employees")
            res = self.cur.fetchall()
            chk2 = False
            for i in res:
                if self.employeeid.get() == str(i[0]):
                    chk2 = True
                    break
            if chk2:
                return True
            else:
                tk.messagebox.showerror(title = "INVALID EMPLOYEE ID", message = "EMPLOYEE ID DOES NOT EXIST !")
                
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NOT A VALID EMPLOYEE ID ! SHOULD BE ONLY NUMERIC !!")
        return False
    
    def highestEmpSale(self):
        current = datetime.now().month
        month = int(current)
        self.cur.execute('select empid from(select sum(bill) as BILL, empid from orders where EXTRACT(month from time) = :1 group by empid order by BILL desc) where rownum = 1',(month,))
        res = self.cur.fetchall()
        employeeid = res[0][0]
        
        self.cur.execute('select sum(bill), count(ordid), count(DISTINCT custid) from orders where EXTRACT(month from time) = :1 and empid = :2',(month,employeeid))
        res = self.cur.fetchall()
        res= res[0]
        st = "\n"
        if res[0] == None:
            st += "NO RECORD TO DISPLAY, PLEASE ENTER VALID MONTH OR EMPLOYEE ID"
        else:
            self.cur.execute("select name from employees where empid=:1",(employeeid,))
            x= self.cur.fetchall()
            nm = x[0][0].upper()
            st = "HIGHEST SALES DONE BY : \n"
            st += "\nEMPLOYEE ID : "+str(employeeid)
            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
            st += "\nNAME : "+nm
            st += "\nMONTH : "+mon[month]
            st += "\nTOTAL SALES : RS "+str(res[0])
            st += "\nORDERS TAKEN : "+str(res[1])
            st += "\nNUMBER OF DISTINCT CUSTOMERS : "+str(res[2])
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
    def lowestEmpSale(self):
        current = datetime.now().month
        month = int(current)
        self.cur.execute('select empid from(select sum(bill) as BILL, empid from orders where EXTRACT(month from time) = :1 group by empid order by BILL) where rownum = 1',(month,))
        res = self.cur.fetchall()
        employeeid = res[0][0]
       
        
        self.cur.execute('select sum(bill), count(ordid), count(DISTINCT custid) from orders where EXTRACT(month from time) = :1 and empid = :2',(month,employeeid))
        res = self.cur.fetchall()
      
        res= res[0]
        st = "\n"
        if res[0] == None:
            st += "NO RECORD TO DISPLAY, PLEASE ENTER VALID MONTH OR EMPLOYEE ID"
        else:
            self.cur.execute("select name from employees where empid=:1",(employeeid,))
            x= self.cur.fetchall()
            nm = x[0][0].upper()
            st = "LOWEST SALES DONE BY : \n"
            st += "\nEMPLOYEE ID : "+str(employeeid)
            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
            st += "\nNAME : "+nm
            st += "\nMONTH : "+mon[month]
            st += "\nTOTAL SALES : RS "+str(res[0])
            st += "\nORDERS TAKEN : "+str(res[1])
            st += "\nNUMBER OF DISTINCT CUSTOMERS : "+str(res[2])
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
    
    def AllEmpSale(self):
        current = datetime.now().month
        month = int(current)
        self.cur.execute('select DISTINCT empid from orders where EXTRACT(month from time) = : 1',(month,))
        res = self.cur.fetchall()
        st = "ALL SALES BY : \n"
        for tup in res :
            employeeid = tup[0]
       
            
            self.cur.execute('select sum(bill), count(ordid), count(DISTINCT custid) from orders where EXTRACT(month from time) = :1 and empid = :2',(month,employeeid))
            res = self.cur.fetchall()
            
            res= res[0]
            if res[0] == None:
                st = "NO RECORD TO DISPLAY, PLEASE ENTER VALID MONTH OR EMPLOYEE ID"
                break
            else:
                self.cur.execute("select name from employees where empid=:1",(employeeid,))
                x= self.cur.fetchall()
                nm = x[0][0].upper()
             
                st += "\nEMPLOYEE ID : "+str(employeeid)
                mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                st += "\nNAME : "+nm
                st += "\nMONTH : "+mon[month]
                st += "\nTOTAL SALES : RS "+str(res[0])
                st += "\nORDERS TAKEN : "+str(res[1])
                st += "\nNUMBER OF DISTINCT CUSTOMERS : "+str(res[2])
                st += "\n**************************************************"
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
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
            x.back("Sales")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("Sales")
            
            
class SalesByMonth(tk.Tk):
    
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
        self.title("SALES BY MONTH @ PSMS")
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "              SALES        BY        MONTH              ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        l2 = tk.Label(container, text = "ENTER PARTICULAR DAY - dd/mm/yyyy", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.particularday = tk.StringVar()
        e2 = tk.Entry(container, textvariable = self.particularday, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(container, text = "DISPLAY", command = self.salePDay, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = "we")
        
        l3 = tk.Label(container, text = "ENTER MONTH NUMBER OR NAME", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l3.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.month = tk.StringVar()
        e3 = tk.Entry(container, textvariable = self.month, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(container, text = "DISPLAY", command = self.salePMonth, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 4, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
        
        st = "WELCOME TO SALES BY MONTH"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(rowspan = 4, columnspan = 2, padx = 10, pady = 10)
        
        l4 = tk.Label(container, text = "CURRENT MONTH SALES", font = ("arial black",12, "bold"), bg = "white", fg = "black", relief = GROOVE)
        l4.grid(row = 5, column = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "CURRENT MONTH", command = self.currentMonth, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 6, column = 2, padx = 10, pady = 10, sticky = "we")
        
        l5 = tk.Label(container, text = "TODAY SALES", font = ("arial black",12, "bold"), bg = "white", fg = "black", relief = GROOVE)
        l5.grid(row = 7, column = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(container, text = "TODAY", command = self.today, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 8, column = 2, padx = 10, pady = 10, sticky = "we")
   
        
        but6 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 9, column = 0, padx = 10, pady = 10,sticky = "we")
        
          
        but7 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but7.grid(row = 9, column = 2, padx = 10, pady = 10, sticky = "we")
    
    def salePMonth(self):
        
        mon1 = [' ','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        mon2 = [' ','JANUARY','FEBRAURY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
        chk_month = False
        mn = ''
        if valid.validNumber(self.month.get()):
            if self.month.get() == '':
                chk_month = False
                tk.messagebox.showerror(title = "INVALID MONTH NUMBER", message = "MONTH SHOULD NOT BE EMPTY !")
            else:
                if int(self.month.get()) in range(1,13):
                    chk_month = True
                    mn = int(self.month.get())
                else:
                    tk.messagebox.showerror(title = "INVALID MONTH NUMBER", message = "MONTH SHOULD BE BETWEEN 1-12 !")
        else:
            mn = self.month.get()
            mn = mn.upper()
            if self.month.get() != '':
                chk_month = False
                if mn in mon1:
                    mn = mon1.index(mn)
                    chk_month = True
                elif mn in mon2:
                    mn = mon2.index(mn)
                    chk_month = True
                else:
                    tk.messagebox.showerror(title = "INVALID MONTH NAME", message = "NO SUCH MONTH EXISTS !")
            else:
                tk.messagebox.showerror(title = "INVALID MONTH NAME", message = "NO SUCH MONTH EXISTS !")
        
        if chk_month:
            st = ''
            monthnum = mn
            self.cur.execute('SELECT count(ordid), count( DISTINCT custid),sum(bill) FROM orders WHERE EXTRACT(month from time) = :1',(monthnum,))
            res = self.cur.fetchall()
            res = res[0]
            st = ''
            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
            if res[2] == None:
                st = "NO RECORD OF THE MONTH "+mon[monthnum]+" EXISTS"
            else:
                st += "\nRECORD OF THE MONTH : "+mon[monthnum]
                st += "\nTOTAL SALES : RS "+str(res[2])
                st += "\nTOTAL ORDERS : "+str(res[0])
                st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
                self.cur.execute('select BILL,DY from (select sum(bill) as BILL,trunc(time) as DY from orders WHERE EXTRACT(month from time) = :1 group by trunc(time)order by BILL desc ) where rownum = 1',(monthnum,))
                res = self.cur.fetchall()
                res = res[0]
                x = str(res[1])
                dat = x.split()
                dat = dat[0]
                a,b,c = dat.split('-')
                datee = c+"/"+b+"/"+a
                st += "\n--------------------------------------------------"
                st += "\nHIGHEST SALES DAY WAS: "+str(datee)
                day = datee
                a,b,c = day.split('/')
                mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                day = a + "-"+mon[int(b)]+"-"+c
                
                self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
                res = self.cur.fetchall()
                res = res[0]
                if res[2] == None:
                    st += "\nNO RECORD TO DISPLAY"
                else:
                    st += "\nTOTAL SALES : RS "+ str(res[2])
                    st += "\nTOTAL ORDERS : "+str(res[0])
                    st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
                st +="\n--------------------------------------------------"
                
                self.cur.execute('select BILL,DY from (select sum(bill) as BILL,trunc(time) as DY from orders WHERE EXTRACT(month from time) = :1 group by trunc(time)order by BILL ) where rownum = 1',(monthnum,))
                res = self.cur.fetchall()
                res = res[0]
                x = str(res[1])
                dat = x.split()
                dat = dat[0]
                a,b,c = dat.split('-')
                datee = c+"/"+b+"/"+a
                st += "\nLOWEST SALES DAY WAS: "+str(datee)
                day = datee
                a,b,c = day.split('/')
                mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                day = a + "-"+mon[int(b)]+"-"+c
                
                self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
                res = self.cur.fetchall()
                res = res[0]
                if res[2] == None:
                    st += "\nNO RECORD TO DISPLAY"
                else:
                    st += "\nTOTAL SALES : RS "+ str(res[2])
                    st += "\nTOTAL ORDERS : "+str(res[0])
                    st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
                st +="\n--------------------------------------------------"
                
            
            self.disp.configure(state = NORMAL)
            self.disp.delete("1.0", tk.END)   
            self.disp.insert("1.0", st)
            self.disp.configure(state = DISABLED)
            
    
    def salePDay(self):
        chk_date = valid.validDate(self.particularday.get())
        if chk_date:
            day = self.particularday.get()
            a,b,c = day.split('/')
            mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            day = a+"-"+mon[int(b)]+"-"+c
            
            self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
            res = self.cur.fetchall()
            st = ''
            res = res[0]
            if res[2] == None:
                st = "NO RECORD TO DISPLAY OF " + day
            else:
                st = day
                st += "\nTOTAL SALES : RS "+str(res[2])
                st += "\nTOTAL ORDERS : "+str(res[0])
                st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
                
            self.disp.configure(state = NORMAL)
            self.disp.delete("1.0", tk.END)   
            self.disp.insert("1.0", st)
            self.disp.configure(state = DISABLED)
            
        else:
            tk.messagebox.showerror(title = "INVALID DATE INPUT", message = "DATE SHOULD BE IN dd/mm/yyyy FORMAT ! \n INVALID INPUT !!")
    
    def today(self):
        day = ((str(datetime.today())).split())[0]
        a,b,c = day.split('-')
        mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        day = c+"-"+mon[int(b)]+"-"+a
        
        self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
        res = self.cur.fetchall()
        st = ''
        res = res[0]
        if res[2] == None:
            st = "NO RECORD TO DISPLAY OF " + day
        else:
            st = day
            st += "\nTOTAL SALES : RS "+str(res[2])
            st += "\nTOTAL ORDERS : "+str(res[0])
            st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
            
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
    def currentMonth(self):
        monthnum = datetime.now().month
        
        self.cur.execute('SELECT count(ordid), count( DISTINCT custid),sum(bill) FROM orders WHERE EXTRACT(month from time) = :1',(monthnum,))
        res = self.cur.fetchall()
        res = res[0]
        st = ''
        mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
        if res[2] == None:
            st = "NO RECORD OF THE MONTH "+mon[monthnum]+" EXISTS"
        else:
            st += "\nRECORD OF THE MONTH : "+mon[monthnum]
            st += "\nTOTAL SALES : RS "+str(res[2])
            st += "\nTOTAL ORDERS : "+str(res[0])
            st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
            self.cur.execute('select BILL,DY from (select sum(bill) as BILL,trunc(time) as DY from orders group by trunc(time)order by BILL desc ) where rownum = 1')
            res = self.cur.fetchall()
            res = res[0]
            x = str(res[1])
            dat = x.split()
            dat = dat[0]
            a,b,c = dat.split('-')
            datee = c+"/"+b+"/"+a
            st += "\n--------------------------------------------------"
            st += "\nHIGHEST SALES DAY WAS: "+str(datee)
            day = datee
            a,b,c = day.split('/')
            mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            day = a + "-"+mon[int(b)]+"-"+c
            
            self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
            res = self.cur.fetchall()
            res = res[0]
            if res[2] == None:
                st += "\nNO RECORD TO DISPLAY"
            else:
                st += "\nTOTAL SALES : RS "+ str(res[2])
                st += "\nTOTAL ORDERS : "+str(res[0])
                st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
            st +="\n--------------------------------------------------"
            
            self.cur.execute('select BILL,DY from (select sum(bill) as BILL,trunc(time) as DY from orders group by trunc(time)order by BILL ) where rownum = 1')
            res = self.cur.fetchall()
            res = res[0]
            x = str(res[1])
            dat = x.split()
            dat = dat[0]
            a,b,c = dat.split('-')
            datee = c+"/"+b+"/"+a
            st += "\nLOWEST SALES DAY WAS: "+str(datee)
            day = datee
            a,b,c = day.split('/')
            mon = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            day = a + "-"+mon[int(b)]+"-"+c
            
            self.cur.execute("select count(ordid), count( DISTINCT custid),sum(bill) from orders where trunc(time)= :1 ",(day,))
            res = self.cur.fetchall()
            res = res[0]
            if res[2] == None:
                st += "\nNO RECORD TO DISPLAY"
            else:
                st += "\nTOTAL SALES : RS "+ str(res[2])
                st += "\nTOTAL ORDERS : "+str(res[0])
                st += "\nTOTAL NUMBER OF DISTINCT CUSTOMERS : "+str(res[1])
            st +="\n--------------------------------------------------"
            
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
    
    def AllEmpSale(self):
        current = datetime.now().month
        month = int(current)
        self.cur.execute('select DISTINCT empid from orders where EXTRACT(month from time) = : 1',(month,))
        res = self.cur.fetchall()
        st = "ALL SALES BY : \n"
        for tup in res :
            employeeid = tup[0]
       
            
            self.cur.execute('select sum(bill), count(ordid), count(DISTINCT custid) from orders where EXTRACT(month from time) = :1 and empid = :2',(month,employeeid))
            res = self.cur.fetchall()
         
            res= res[0]
            if res[0] == None:
                st = "NO RECORD TO DISPLAY, PLEASE ENTER VALID MONTH OR EMPLOYEE ID"
                break
            else:
                self.cur.execute("select name from employees where empid=:1",(employeeid,))
                x= self.cur.fetchall()
                nm = x[0][0].upper()
             
                st += "\nEMPLOYEE ID : "+str(employeeid)
                mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
                st += "\nNAME : "+nm
                st += "\nMONTH : "+mon[month]
                st += "\nTOTAL SALES : RS "+str(res[0])
                st += "\nORDERS TAKEN : "+str(res[1])
                st += "\nNUMBER OF DISTINCT CUSTOMERS : "+str(res[2])
                st += "\n**************************************************"
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
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
            x.back("Sales")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("Sales")
            
class ShowAllPizza(tk.Tk):
    
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
        self.title("ALL PIZZA @ PSMS")
        self.frames = {} #DICTIONARY OF FRAMES
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "             ALL     PIZZA          ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        st = "WELCOME TO VIEW ALL PIZZA"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 1, columnspan = 3, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "ONLY VEG", command = lambda : self.show("VEG"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(container, text = "ONLY NON-VEG", command = lambda : self.show("NON-VEG"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "EVERYTHING", command = lambda : self.show("ALL"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
        but4 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 3, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but5 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu, width = 17,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = "we")
        
        
    def mainmenu(self):
        self.destroy()
        if len(str(self.empid)) == 10:#IT'S A CUSTOMER
            customer.startCustomer(self.empid, self.cur)
        else:
            
            
            self.cur.execute("select designation from employees where empid = :1",(self.empid,))
            res = self.cur.fetchall()
            des = res[0][0]
    
            if des == "MANAGER" :
                manager.startManager(self.empid, self.cur)
                
            elif des == "ADMIN":
                admin.startAdmin(self.empid, self.cur)
                
            else:
                cashier.startCashier(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        if len(str(self.empid)) == 10:#IT'S A CUSTOMER
            customer.startCustomer(self.empid, self.cur)
        else:
            self.cur.execute("select designation from employees where empid = :1",(self.empid,))
            res = self.cur.fetchall()
            des = res[0][0]
          
            if des == "MANAGER":
                x = manager.Manager(self.empid, self.cur)
                x.back("ViewMenu")
                
            elif des == "ADMIN":
                x = admin.Admin(self.empid, self.cur)
                x.back("ViewMenu")
                
            else:
                x = cashier.Cashier(self.empid, self.cur)
                x.back("Menu")
                
            
    def show(self, par):
        
        query = ''
        if par == "ALL":
            query = "select * from menu order by prid"
        elif par == "VEG":
            query = "select * from menu where type = 'VEG' order by prid"
        else:
            query = "select * from menu where type = 'NON-VEG' order by prid"
       
             
        self.cur.execute(query)
        i = self.cur.fetchall()
        st = "\n"
        for res in i:
            
            st += "PRODUCT ID : "+str(res[0])
            st += "\nPRODUCT NAME : "+str(res[1])
            st += "\nPRICE-    SMALL: "+str(res[2])+"    MEDIUM: "+str(res[3])+"    LARGE: "+str(res[4])
            st += "\nSHORTCUT : "+str(res[5])
            st += "\nTYPE : "+str(res[6])
            st += "\nDETAILS : "+str(res[7])+"\n\n"
            st += "--------------------------------------------------"

        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
#-------------------------------------------------------------------------------------------------------------------