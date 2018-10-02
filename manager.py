import tkinter as tk
import validation as valid, takeorder, show, changes, creates, logins
from tkinter.constants import GROOVE
import time


class Manager(tk.Tk):
    
    def __init__(self, empid, cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.empid = empid
        self.cur = cur
        self.frames = {} #DICTIONARY OF FRAMES
        self.cur.execute("select name from employees where empid=:1",(empid,))
        res = self.cur.fetchall()
        res = res[0][0].split()[0]
        title = "MANAGER - "+res.upper()
        self.title(title)
        for F in (MainMenu,CustomerDetails, EmployeeDetails):
        
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nswe")
            
        for F in (ViewMenu, ViewProfile, EditProfile, ChangePassword,SinglePizza, ChangeMenu, Menu, ApplyOffers, ViewEmployeeDetails, ChangeEmployeeDetails, Sales, OrderCustomer, DetailsCustomer):
            x= F(empid, cur, container, self)
            self.frames[F] = x
            x.grid(row = 0, column = 0, sticky = "nswe")
       
        self.show_frame(MainMenu)
    
    def back(self,par):
        if par == "SinglePizza":
            self.show_frame(SinglePizza)
        elif par == "OrderCustomer":
            self.show_frame(OrderCustomer)
        elif par == "DetailsCustomer":
            self.show_frame(DetailsCustomer)
        elif par == "Menu":
            self.show_frame(Menu)
        elif par == "ApplyOffers":
            self.show_frame(ApplyOffers)
        elif par == "ViewEmployeeDetails":
            self.show_frame(ViewEmployeeDetails)
        elif par == "ChangeEmployeeDetails":
            self.show_frame(ChangeEmployeeDetails)
        elif par == "EmployeeDetails":
            self.show_frame(EmployeeDetails)
        elif par == "Sales":
            self.show_frame(Sales)
        elif par == "ChangeMenu":
            self.show_frame(ChangeMenu)
        elif par == "ViewMenu":
            self.show_frame(ViewMenu)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def refresh(self):
        self.destroy()
        startManager(self.empid, self.cur)
        
    def logout(self):
        
        yn = tk.messagebox.askyesno(title = "LOGOUT", message = "ARE YOU SURE ABOUT YOUR LOGGING OUT ?")
        if yn == True:
            self.destroy()
            logins.logEmp(self.cur).mainloop()
                
    def takeOrderBySelf(self):
        self.destroy()
        takeorder.startOrder(self.empid, self.cur)
        
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
            
        
class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "        MAIN  MENU     ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.configure(bg = "#7fff00")
        
        self.l1 = tk.Label(self, text = "DIGITAL CLOCK", fg = "red", bg = "white",width = 15, font = ("Courier", 20, "bold italic"), relief = GROOVE)
        self.l1.grid(row = 1, columnspan= 2,padx = 20, pady = 20, sticky = "news")
        
        but1 = tk.Button(self, text = "TAKE ORDER", command = controller.takeOrderBySelf, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2,columnspan = 2, padx = 10, pady = 10,sticky = "we")

        
        but2 = tk.Button(self, text = "PIZZA'S", command = lambda : controller.show_frame(Menu), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 3,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(self, text = "EMPLOYEE DETAILS", command = lambda : controller.show_frame(EmployeeDetails), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 4,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(self, text = "SALES", command = lambda : controller.show_frame(Sales), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 5,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but5 = tk.Button(self, text = "CUSTOMER DETAILS", command = lambda : controller.show_frame(CustomerDetails), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but5.grid(row = 6,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but6 = tk.Button(self, text = "CHANGE PASSWORD", command = lambda : controller.show_frame(ChangePassword), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but6.grid(row = 7,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but7 = tk.Button(self, text = "EDIT PROFILE", command = lambda : controller.show_frame(EditProfile), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but7.grid(row = 8,column = 0, padx = 15, pady = 15, sticky = "we")
        
        but9 = tk.Button(self, text = "VIEW PROFILE", command = lambda : controller.show_frame(ViewProfile), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but9.grid(row = 8,column = 1, padx = 15, pady = 15, sticky = "we")
        
        but10 = tk.Button(self, text = "EXIT", command = controller.exit,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but10.grid(row = 9,column = 0, padx = 10, pady = 10, sticky = "we")
        
        but11 = tk.Button(self, text = "LOGOUT", command = controller.logout,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but11.grid(row = 9,column = 1, padx = 10, pady = 10, sticky = "we")
        self.count = 0
        self.timer()
        
        
    def timer(self):
        tt = time.strftime('%H:%M:%S')
        tt = "TIME : "+tt
        self.l1.configure(text = tt)
        if self.count == 0:
            self.l1.configure(fg = "red", bg = "yellow")
            self.count = 1
            
        elif self.count == 1:
            self.l1.configure(fg = "blue", bg = "yellow")
            self.count = 0
        self.after(1000, self.timer)
        
    
        
class Menu(tk.Frame):
    
    def __init__(self, empid, cur,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "       PIZZA MENU      ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.empid = empid
        self.cur = cur
        self.controller = controller
        self.configure(bg = "#7fff00")
        
        but1 = tk.Button(self, text = "VIEW MENU", command = lambda : controller.show_frame(ViewMenu), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "CHANGE MENU", command = lambda : controller.show_frame(ChangeMenu), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(self, text = "CHANGE SHORTCUT", command = self.changeShortcut, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 3,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(self, text = "APPLY OFFERS", command = lambda : controller.show_frame(ApplyOffers), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 4,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but5 = tk.Button(self, text = "CREATE PIZZA", command = self.createPizza, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but5.grid(row = 5,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but6 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 6,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but7 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but7.grid(row = 6,column = 1, padx = 10, pady = 15, sticky = "we")
        
    def changeShortcut(self):
        self.controller.destroy()
        changes.ChangeShortcut(self.empid,self.cur).mainloop()
        
    def createPizza(self):
        self.controller.destroy()
        creates.CreatePizza(self.empid, self.cur).mainloop()

class ViewMenu(tk.Frame):
    
    def __init__(self,empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "       VIEW  MENU      ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.controller = controller
        self.empid = empid
        self.cur = cur
        self.configure(bg = "#7fff00")
        
        
        but1 = tk.Button(self, text = "SINGLE PIZZA", command = lambda : controller.show_frame(SinglePizza), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "ALL PIZZA", command = self.viewMenu, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(Menu),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 3,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 3,column = 1, padx = 10, pady = 15, sticky = "we")
        
     
    def viewMenu(self):
        self.controller.destroy()
        show.ShowAllPizza(self.empid, self.cur)


class SinglePizza(tk.Frame):
    
    def __init__(self,empid,cur, parent, controller):
        self.empid = empid
        self.cur = cur
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "     SINGLE  PIZZA    ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0,padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        l1 = tk.Label(self, text = "ENTER PIZZA ID/NAME/SHORTCUT", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, padx = 10, pady = 10, sticky = "we")
        
        self.pizzaid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.pizzaid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(self, text = "DISPLAY", command = self.displayPizza , fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3,padx = 10, pady = 15, sticky = "we")
        
                
        but2 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(ViewMenu),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4,padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 5,padx = 10, pady = 15, sticky = "we")
        
    def displayPizza(self):
        self.cur.execute('select prid,name,shortcut from menu')
        res = self.cur.fetchall()
        lotup = []#LOTUP TO CHECK FOR NAME INPRID,SHORTCUT,NAME
        for tup in res:
            a,b,c = tup[0],tup[1],tup[2]
            lotup.append((str(a),str(b).upper(),str(c).upper()))
        name = self.pizzaid.get()
        prid = 0  
        chk = False
        name = name.upper()
        for i in lotup:
            if name in i:
                chk = True
                name = i[1]
                prid = i[0]
        if not chk:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH PIZZA ID/NAME/SHORTUCT EXISTS ! PLEASE TRY AGAIN !!")
        else:
            self.controller.destroy()
            show.ShowSinglePizza(self.empid, str(prid), self.cur).mainloop()
           

class ChangeMenu(tk.Frame):
    
    def __init__(self,empid,cur, parent, controller):
        self.empid = empid
        self.cur = cur
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "    CHANGE MENU     ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0,padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        l1 = tk.Label(self, text = "ENTER PIZZA ID/NAME/SHORTCUT", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, padx = 10, pady = 10, sticky = "we")
        
        self.pizzaid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.pizzaid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(self, text = "DISPLAY", command = self.displayPizza , fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3,padx = 10, pady = 15, sticky = "we")
        
                
        but2 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(Menu),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4,padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 5,padx = 10, pady = 15, sticky = "we")
        
    def displayPizza(self):
        self.cur.execute('select prid,name,shortcut from menu')
        res = self.cur.fetchall()
        lotup = []#LOTUP TO CHECK FOR NAME INPRID,SHORTCUT,NAME
        for tup in res:
            a,b,c = tup[0],tup[1],tup[2]
            lotup.append((str(a),str(b).upper(),str(c).upper()))
        name = self.pizzaid.get()
        prid = 0  
        chk = False
        name = name.upper()
        for i in lotup:
            if name in i:
                chk = True
                name = i[1]
                prid = i[0]
        if not chk:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH PIZZA ID/NAME/SHORTUCT EXISTS ! PLEASE TRY AGAIN !!")
        else:
            self.controller.destroy()
           
            changes.ChangeMenu(self.empid, str(prid), self.cur).mainloop()
            
class ApplyOffers(tk.Frame):
    
    def __init__(self, empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "     APPLY OFFERS     ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.parent = parent
        self.controller = controller
        self.empid = empid
        self.cur = cur
        self.configure(bg = "#7fff00")
        
        
        but1 = tk.Button(self, text = "SINGLE PIZZA", command = self.SP, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "ALL PIZZA", command = self.AP, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(Menu),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 3,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 3,column = 1, padx = 10, pady = 15, sticky = "we")   
        
    def SP(self):
        self.controller.destroy()
        changes.ApplyOfferSingle(self.empid, self.cur).mainloop()
        
    def AP(self):
        self.controller.destroy()
        changes.ApplyOfferAll(self.empid, self.cur).mainloop()

class EmployeeDetails(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "EMPLOYEE  DETAILS", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.controller = controller
        self.configure(bg = "#7fff00")
        
        but1 = tk.Button(self, text = "VIEW EMPLOYEE DETAILS", command = lambda : controller.show_frame(ViewEmployeeDetails), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "CHANGE EMPLOYEE DETAILS", command = lambda : controller.show_frame(ChangeEmployeeDetails), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(self, text = "LOCK/UNLOCK EMPLOYEE ACCOUNT", command = self.lockunlock, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 3,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 5,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but5 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 5,column = 1, padx = 10, pady = 15, sticky = "we")
        
    def lockunlock(self):
        self.controller.destroy()
        changes.LockUnlockAccount(self.controller.empid, self.controller.cur)
        
class ViewEmployeeDetails(tk.Frame):
    
    def __init__(self, empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "    VIEW  EMPLOYEE ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.empid = empid
        self.cur = cur
        self.controller = controller
        self.configure(bg = "#7fff00")
        
        but1 = tk.Button(self, text = "PARTICLULAR EMPLOYEE", command = self.PEmployee, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "ALL EMPLOYEE", command = self.AllEmployee, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
       
        but4 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(EmployeeDetails),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 5,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but5 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 5,column = 1, padx = 10, pady = 15, sticky = "we")
        
    def PEmployee(self):
        self.controller.destroy()
        show.ShowParticularEmployee(self.empid, self.cur).mainloop()
        
    def AllEmployee(self):
        self.controller.destroy()
        show.ShowAllEmployee(self.empid, self.cur).mainloop()
        
           
class ChangeEmployeeDetails(tk.Frame):#CHANEG FOR ADMIN
    
    def __init__(self,empid,cur, parent, controller):
        self.empid = empid
        self.cur = cur
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "   CHANGE DETAILS  ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0,padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        l1 = tk.Label(self, text = "ENTER EMPLOYEE ID", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, padx = 10, pady = 10, sticky = "we")
        
        self.employeeid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.employeeid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(self, text = "CHANGE", command = self.verify , fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3,padx = 10, pady = 15, sticky = "we")
        
                
        but2 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(EmployeeDetails),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4,padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 5,padx = 10, pady = 15, sticky = "we")
    
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
                self.displayEmployee()
            else:
                tk.messagebox.showerror(title = "INVALID EMPLOYEE ID", message = "EMPLOYEE ID DOES NOT EXIST !")
                
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NOT A VALID EMPLOYEE ID ! SHOULD BE ONLY NUMERIC !!")
        
    def displayEmployee(self):
        self.cur.execute('select designation from employees where empid=:1',(self.employeeid.get(),))
        res = self.cur.fetchall()
        des = res[0][0]
        chk = False
        if des == "CASHIER" or (self.employeeid.get() == str(self.empid)):
            chk = True
        else:
            chk = False
        
        if not chk:
            tk.messagebox.showerror(title = "UNAUTHORIZED ACCESS", message = "YOU ARE NOT AUTHORIZED TO CHANGE THIS ACCOUNT !")
        else:
            self.controller.destroy()
            changes.ChangeEmployeeByManager(self.empid, self.employeeid.get(), self.cur).mainloop()
        
     
        
class Sales(tk.Frame):
    
    def __init__(self, empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "            SALES            ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        self.empid = empid
        self.cur = cur
        self.controller = controller
        self.configure(bg = "#7fff00")
        
        but1 = tk.Button(self, text = "SALES BY EMPLOYEE", command = self.SBEmployee, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 3, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "SALES BY MONTH", command = self.SBMonth, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 3,padx = 10, pady = 10, sticky = "we")
        
                
        but4 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 4,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but5 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 4,column = 2, padx = 10, pady = 15, sticky = "we")
        
    def SBEmployee(self):
        self.controller.destroy()
        show.SalesByEmployee(self.empid, self.cur)
    
    def SBMonth(self):
        self.controller.destroy()
        show.SalesByMonth(self.empid, self.cur)
  
        
class CustomerDetails(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "CUSTOMER DETAILS", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.configure(bg = "#7fff00")
        
        but1 = tk.Button(self, text = "VIEW ORDERS OF A CUSTOMER", command = lambda : controller.show_frame(OrderCustomer), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 1,columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(self, text = "VIEW DETAILS OF A CUSTOMER", command = lambda : controller.show_frame(DetailsCustomer), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 4,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but5 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 4,column = 1, padx = 10, pady = 15, sticky = "we")
        
class OrderCustomer(tk.Frame):
    
    def __init__(self,empid,cur, parent, controller):
        self.empid = empid
        self.cur = cur
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "ORDER'S CUSTOMER", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0,padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        l1 = tk.Label(self, text = "ENTER CUSTOMER MOBILE NUMBER", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, padx = 10, pady = 10, sticky = "we")
        
        self.custid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.custid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(self, text = "DISPLAY", command = self.displayOrder , fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3,padx = 10, pady = 15, sticky = "we")
        
                
        but2 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(CustomerDetails),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4,padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 5,padx = 10, pady = 15, sticky = "we")
        
    def displayOrder(self):
        self.cur.execute('select mobile from customers')
        res = self.cur.fetchall()
        chk = valid.validMobile(self.custid.get())
        if chk:
            chk2 = False
            for i in res:
                if str(i[0]) == self.custid.get():
                    chk2 = True
                    break
            if chk2:
                self.controller.destroy()
                show.CustomerDetailsOrder(self.empid, self.custid.get(), self.cur).mainloop()
            else:
                tk.messagebox.showerror(title = "INVALID MOBILE NUMBER", message = "CUSTOMER DOES NOT EXIST ! PLEASE TRY AGAIN !!")
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")
   
class DetailsCustomer(tk.Frame):
    
    def __init__(self,empid,cur, parent, controller):
        self.empid = empid
        self.cur = cur
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "DETAILS CUSTOMER", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0,padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        l1 = tk.Label(self, text = "ENTER CUSTOMER MOBILE NUMBER", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, padx = 10, pady = 10, sticky = "we")
        
        self.custid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.custid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(self, text = "DISPLAY", command = self.displayOrder, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold") )
        but1.grid(row = 3,padx = 10, pady = 15, sticky = "we")
        
                
        but2 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(CustomerDetails),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4,padx = 10, pady = 15, sticky = "we")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 5,padx = 10, pady = 15, sticky = "we")
        
    def displayOrder(self):
        self.cur.execute('select mobile from customers')
        res = self.cur.fetchall()
        chk = valid.validMobile(self.custid.get())
        if chk:
            chk2 = False
            for i in res:
                if str(i[0]) == self.custid.get():
                    chk2 = True
                    break
            if chk2:
                self.controller.destroy()
                show.CustomerDetails(self.empid, self.custid.get(), self.cur).mainloop()
            
            else:
                tk.messagebox.showerror(title = "INVALID MOBILE NUMBER", message = "CUSTOMER DOES NOT EXIST ! PLEASE TRY AGAIN !!")
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "INVALID MOBILE NUMBER ! PLEASE TRY AGAIN !!")   


class ViewProfile(tk.Frame):
    
    def __init__(self, empid,cur,parent, controller):
        tk.Frame.__init__(self,parent)
        container = self
        
        cur.execute('select * from employees where empid=:1',(empid,))
        res = cur.fetchall()
        res = res[0]
        self.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "           PROFILE        ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        lab1 = tk.Label(container, text = "EMPLOYEE ID :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab1.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab2 = tk.Label(container, text = res[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab2.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e" )
        
        lab3 = tk.Label(container, text = "NAME :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab3.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab4 = tk.Label(container, text = res[1], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab4.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab5 = tk.Label(container, text = "MOBILE :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab5.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab6 = tk.Label(container, text = res[2], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab6.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab7 = tk.Label(container, text = "ADDRESS :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab7.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab8 = tk.Label(container, text = res[3], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab8.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab9 = tk.Label(container, text = "GENDER :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab9.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab10 = tk.Label(container, text = res[4], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab10.grid(row = 5, column = 1, padx = 1, pady = 1, sticky = "e")
        
        
        lab9 = tk.Label(container, text = "DOB :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab9.grid(row = 6, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab10 = tk.Label(container, text = (str(res[5]).split())[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab10.grid(row = 6, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab11 = tk.Label(container, text = "DOJ :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab11.grid(row = 7, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab12 = tk.Label(container, text = (str(res[6]).split())[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab12.grid(row = 7, column = 1, padx = 1, pady = 1, sticky = "e")
        
        if res[8] == "INACTIVE":
            lab13 = tk.Label(container, text = "DOF :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
            lab13.grid(row = 8, column = 0, padx = 1, pady = 1, sticky = "w")
            
            lab14 = tk.Label(container, text = (str(res[7]).split())[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
            lab14.grid(row = 8, column = 1, padx = 1, pady = 1, sticky = "e")
            
        lab15 = tk.Label(container, text = "STATUS :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab15.grid(row = 9, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab16= tk.Label(container, text = res[8], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab16.grid(row = 9, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab17 = tk.Label(container, text = "PASSWORD :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab17.grid(row = 10, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab18= tk.Label(container, text = res[9], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab18.grid(row = 10 ,column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab19 = tk.Label(container, text = "SALARY :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab19.grid(row = 11, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab20= tk.Label(container, text = res[10], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab20.grid(row = 11, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab21 = tk.Label(container, text = "DESIGNATION :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab21.grid(row = 12, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab22= tk.Label(container, text = res[11], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab22.grid(row = 12, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab23 = tk.Label(container, text = "LOCK STATUS :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab23.grid(row = 13, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab24= tk.Label(container, text = res[12], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab24.grid(row = 13, column = 1, padx = 1, pady = 1, sticky = "e")
        
        but1 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 14,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but2 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 14,column = 1, padx = 10, pady = 15, sticky = "we")
        
class EditProfile(tk.Frame):
    
    def __init__(self, empid,cur,parent, controller):
        tk.Frame.__init__(self,parent)
        container = self
        self.cur = cur
        self.empid = empid
        cur.execute('select name,mobile,address,dob,gender from employees where empid=:1',(empid,))
        res = cur.fetchall()
        res = res[0]
        self.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "     EDIT  PROFILE    ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        lab1= tk.Label(container, text = "EMPID : ", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE)
        lab1.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab2= tk.Label(container, text = empid, font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE)
        lab2.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab3= tk.Label(container, text = "NAME : ", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE)
        lab3.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab4= tk.Label(container, text = res[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE)
        lab4.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        
        add = tk.StringVar()
        mob = tk.StringVar()
        gend = res[4]
        mob.set(res[1])
        add.set(res[2])
        
        lab5= tk.Label(container, text = "MOBILE : ", font = ("arial black",10, "bold"), bg = "black", fg = "white", relief = GROOVE)
        lab5.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e1= tk.Entry(container, textvariable = mob, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab6= tk.Label(container, text = "ADDRESS : ", font = ("arial black",10, "bold"), bg = "black", fg = "white", relief = GROOVE)
        lab6.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e2= tk.Entry(container, textvariable = add, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab7= tk.Label(container, text = "GENDER :", font = ("arial black",10, "bold"), bg = "black", fg = "white", relief = GROOVE)
        lab7.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")
        
        gender = ["MALE","FEMALE","OTHER"]
        self.gender = tk.StringVar()
        self.gender.set(gend)
        opt1 = tk.OptionMenu(container, self.gender, *gender)
        opt1.grid(row= 5, column = 1, padx = 10, pady  =10, sticky = "e")
        menu = opt1.nametowidget(opt1.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
      
            
   
         
        but3 = tk.Button(self, text = "CONFIRM", command = lambda: self.verify(mob.get(),add.get(),self.gender.get(),str(res[1])), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 8, columnspan = 2, padx = 10, pady = 10, sticky = "we")    
            
        but1 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 9,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but2 = tk.Button(self, text = "MAIN MENU", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 9,column = 1, padx = 10, pady = 15, sticky = "we")
        
        
    def verify(self, mobile, address, gender, oldmobile):
       
        chk1 = valid.validMobile(mobile)
        chk2 = True
        if chk1:
            
            self.cur.execute("select mobile from employees")
            res = self.cur.fetchall()
            if oldmobile == mobile:
                chk2 = True
            else:
                for i in res:
                    if str(i[0]) == mobile:
                        chk2 = False
                        break
            if chk2:
                self.cur.execute("update employees set mobile = :1,address = :2, gender = :3 where empid = :4",(mobile,address,gender,self.empid))
                self.cur.execute("commit")
                tk.messagebox.showinfo(title = "SUCCESS", message = "PROFILE UPDATED !")
            else:
                tk.messagebox.showerror(title = "FAILED", message = "MOBILE NUMBER ALREADY EXISTS !")
        else:
            tk.messagebox.showerror(title = "FAILED", message = "INVALID MOBILE NUMER !")
           
    def setGender(self, gender):
       
        self.gender = gender  
        
class ChangePassword(tk.Frame):
    
    def __init__(self, empid, cur, parent, controller):
        self.empid = empid
        self.cur = cur
       
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "CHANGE PASSWORD", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10, sticky = "we") 
        self.configure(bg = "#7fff00")
        self.l1 = tk.Label(self, text = "ENTER OLD PASSWORD", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        self.l1.grid(row = 1, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.oldpass = tk.StringVar()
        self.e1 = tk.Entry(self, textvariable = self.oldpass , font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        self.e1.grid(row = 2, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.but1 = tk.Button(self, text = "CONFIRM", command = self.verify, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        self.but1.grid(row = 3, columnspan = 2, padx = 10, pady = 10, sticky = "we")  
        
        but2 = tk.Button(self, text = "BACK", command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "we") 
        
        but3 = tk.Button(self, text = "MAIN MENU",command = controller.refresh,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "we") 
    def verify(self):
        self.cur.execute("select password from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        existing_password = res[0][0]
        if self.oldpass.get() == existing_password :
            self.l1.configure(text = "ENTER NEW PASSWORD")
            self.but1.configure(text = "UPDATE")
            self.but1.configure(command = self.changePassword)
            
            
        else:
            tk.messagebox.showwarning(title = "MATCH ERROR", message = "PASSWORD DOES NOT MATCH OLD PASSWORD !")
            
    def changePassword(self):
        chk = valid.validPassword(self.oldpass.get())
        if chk:
            self.cur.execute("update employees set password = :1 where empid = :2",(self.oldpass.get(),self.empid))
            self.cur.execute("commit")
            tk.messagebox.showinfo(title = "PASSWORD CHANGED", message = "PASSWORD CHANGED SUCCESSFULLY !")
        
        else:
            tk.messagebox.showerror(title = "INVALID PASSWORD", message = "PASSSWORD MUST BE OF ATLEAST 8 CHARACTERS !\n MUST CONTAIN ATLEAST 1 DIGIT!! \n MUST CONTAIN ATLEAST 1 SPECIAL CHARACTER!!! \n MUST CONTAIN ATLEAST 1 ALPHABET!!!! \n")
                        
        


          
def startManager(empid, cur): 
    Manager(empid,cur).mainloop()       

#-------------------------------------------------------------------------------------------------------------------