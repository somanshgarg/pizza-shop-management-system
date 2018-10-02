import cx_Oracle
import admin, manager, cashier, changes, customer, validation as valid
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.constants import GROOVE
from tkinter import messagebox #NEEDE FOR MESSAGE BOX


class logEmp(tk.Tk):
    
    def __init__(self, cur,*args, **kwargs):
     
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        label = tk.Label(container, text = "       LOGIN EMPLOYEE      ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.chance = 3
        self.title("LOGIN @ PSMS")
        container.configure(bg = "#7fff00")
        
        self.img = ImageTk.PhotoImage(Image.open("dom.png"))
        limage = tk.Label(container, image = self.img,bg = "#7fff00")
        limage.grid(row = 2, columnspan = 2,padx = 10, pady = 10,sticky = "nwe")
        
        l1 = tk.Label(container, text = "ENTER YOUR ID ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.empid = tk.StringVar()
        self.pwd = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.empid, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "we")
        
        l2 = tk.Label(container, text = "ENTER YOUR PASSSWORD ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "we")
        
        e2 = tk.Entry(container, textvariable = self.pwd, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE, show = "*")
        e2.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "LOGIN", command = self.loginEmployee, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 5, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.back,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 6, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "EXIT", command = self.exit,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky = "we")
    
    def back(self):
        self.destroy()
        StartLogin(self.cur).mainloop() 
        
    def exit(self):
        yn = tk.messagebox.askyesno(title = "EXIT", message = "ARE YOU SURE ABOUT YOUR EXIT FROM APPLICATION ?")
        if yn == True:
            
            st = """
            THANKYOU FOR USING  PIZZA SHOP MANAGEMENT SYSTEM
            ----------------COME BACK AGAIN----------------- 
            ----------------HAVE A NICE DAY-----------------
                                            by- S&G PVT LTD.
            """
            tk.messagebox.showinfo(title = "GOODBYE ! ", message = st)
            self.destroy() 

    def loginEmployee(self):
        
        cur = self.cur
        empid = self.empid.get()
        pwd = self.pwd.get()
        chk = valid.validNumber(empid)
        if chk:
            cur.execute("select status,locks,designation,password,name from employees where empid=:1",(empid,))
            res = cur.fetchall()
            if len(res) == 0:
                tk.messagebox.showerror(title = " ERROR LOGIN" ,message = "EMPLOYEE ID DOES NOT EXIST !\n PLEASE TRY AGAIN !!")
            else:#IF ID EXISTS
                res = res[0]
                if res[0] == 'INACTIVE':
                    tk.messagebox.showerror(title = " ERROR LOGIN" ,message = "YOU ARE NO LONGER AN EMPLOYEE ! \n ACCESS DENIED !!")
                   
                else:
                    if res[1] == 'LOCKED':
                        if res[2] == 'CASHIER':
                            tk.messagebox.showerror(title = " ERROR LOGIN" ,message = "YOUR ACCOUNT IS LOCKED! \n PLEASE CONTACT YOUR MANAGER OR ADMIN !! ACCESS DENIED!!!")
                        else:
                            tk.messagebox.showerror(title = " ERROR LOGIN" ,message = "YOUR ACCOUNT IS LOCKED! \n PLEASE CONTACT YOUR ADMIN !! ACCESS DENIED!!!")
                    else:
                        if pwd == res[3]:
                            self.destroy()
                            if res[2] == "CASHIER":
                                cashier.startCashier(int(empid), cur)
                            elif res[2] == "MANAGER":
                                manager.startManager(int(empid), cur)
                            else:
                                admin.startAdmin(int(empid), cur)
                                
                           
                        else:
                            tk.messagebox.showerror(title = " ERROR LOGIN" ,message = "INCORRECT ID OR PASSWORD ! PLEASE TRY AGAIN !!")
                            self.chance = self.chance - 1
                            if res[2] in ['CASHIER','MANAGER']:
                                
                                if self.chance <= 0:
                                    changes.changeEmployeeLockLogin(empid, cur)
                                    tk.messagebox.showerror(title = "ACCOUNT LOCKED " ,message = "DUE TO 3 CONSECUTIVE FAILED LOGIN ATTEMPT ! \nYOUR ACCOUNT HAS BEEN LOCKED !!")
                                   
                                else:
                                    show = "YOU HAVE ONLY "+ str(self.chance) + " LEFT !!"
                                    tk.messagebox.showwarning(title = "ERROR LOGIN " ,message = show)

                            else:
                                if self.chance <= 0:
                                    tk.messagebox.showwarning(title = "ERROR LOGIN " ,message = "YOU HAVE TRIED YOU MAXIMUM LIMIT FOR NOW !PLEASE TRY AFTER SOME TIME ! \n")
                                    
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "ID SHOULD BE ONLY NUMERIC")    


class StartLogin(tk.Tk):
    
    def __init__(self, cur,*args, **kwargs):
     
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        label = tk.Label(container, text = "PIZZA SHOP \nMANAGEMENT SYSTEM", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.title("WELCOME TO PSMS")
        container.configure(bg = "#7fff00")
        
        self.img = ImageTk.PhotoImage(Image.open("dom.png"))
        limage = tk.Label(container, image = self.img,bg = "#7fff00")
        limage.grid(row = 1, columnspan = 2,padx = 10, pady = 10,sticky = "nwe")
        
        
        but3 = tk.Button(container, text = "CUSTOMER", command = self.startCustomer, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 2, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "EMPLOYEE", command = self.startEmployee, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "EXIT", command = self.exit,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.after(1500, self.welcome)
    
    def startCustomer(self):
        self.destroy()
        logCustomer(self.cur).mainloop()
    
    def startEmployee(self):
        self.destroy()
        logEmp(self.cur).mainloop()
     
    def welcome(self):
        st = """
        WELCOME TO PIZZA SHOP MANAGEMENT SYSTEM
                    by- S&G PVT LTD.
                """
        tk.messagebox.showinfo(title = "WELCOME ! ", message = st)
            
    def exit(self):
        yn = tk.messagebox.askyesno(title = "EXIT", message = "ARE YOU SURE ABOUT YOUR EXIT FROM APPLICATION ?")
        if yn == True:
            
            st = """
            THANKYOU FOR USING  PIZZA SHOP MANAGEMENT SYSTEM
            ----------------COME BACK AGAIN----------------- 
            ----------------HAVE A NICE DAY-----------------
                                            by- S&G PVT LTD.
            """
            tk.messagebox.showinfo(title = "GOODBYE ! ", message = st)
            self.destroy()
            
class logCustomer(tk.Tk):
    
    def __init__(self, cur,*args, **kwargs):
     
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        label = tk.Label(container, text = "        LOGIN CUSTOMER        ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.title("LOGIN @ CUSTOMER - PSMS")
        container.configure(bg = "#7fff00")
        
        self.img = ImageTk.PhotoImage(Image.open("dom.png"))
        limage = tk.Label(container, image = self.img,bg = "#7fff00")
        limage.grid(row = 2, columnspan = 2,padx = 10, pady = 10,sticky = "nwe")
        
        l1 = tk.Label(container, text = "ENTER YOUR MOBILE NUMBER ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.mobile = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.mobile, font = ("arial black",12, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "we")
      
        but3 = tk.Button(container, text = "LOGIN", command = self.verify, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 4, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.back,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "EXIT", command = self.exit,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "we")
    
    def verify(self):
        chk = valid.validMobile(self.mobile.get())
        if chk:
            self.cur.execute("select * from customers where mobile=:1",((int(self.mobile.get())),))
            res = self.cur.fetchall()
            if len(res)==0:
                tk.messagebox.showerror(title = "INVALID MOBILE NUMBER", message = "CUSTOMER DOES NOT EXIST ! \n PLEASE TRY AGAIN !!")
            else:
                self.customerlogin()
        else:
            tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE NUMBER SHOULD BE NUMERIC AND OF 10 DIGITS ONLY !")
    
    def customerlogin(self):
        self.destroy()
        customer.startCustomer(int(self.mobile.get()), self.cur)
    
    def back(self):
        self.destroy()
        StartLogin(self.cur).mainloop() 
        
    def exit(self):
        yn = tk.messagebox.askyesno(title = "EXIT", message = "ARE YOU SURE ABOUT YOUR EXIT FROM APPLICATION ?")
        if yn == True:
            
            st = """
            THANKYOU FOR USING  PIZZA SHOP MANAGEMENT SYSTEM
            ----------------COME BACK AGAIN----------------- 
            ----------------HAVE A NICE DAY-----------------
                                            by- S&G PVT LTD.
            """
            tk.messagebox.showinfo(title = "GOODBYE ! ", message = st)
            self.destroy() 
            
if __name__ == "__main__":
    con = cx_Oracle.connect("PDS/somansh@127.0.01/xe")
    cur = con.cursor()
    StartLogin(cur).mainloop()
    
#-------------------------------------------------------------------------------------------------------------------