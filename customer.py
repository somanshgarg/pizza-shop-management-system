import tkinter as tk
import show, logins
import time
from tkinter.constants import GROOVE


class Customer(tk.Tk):
    
    def __init__(self, custid, cur,*args, **kwargs):
     
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        #self.overrideredirect(True)
        container = tk.Frame()
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        
        self.cur = cur
        self.frames = {}
        
        
        self.cur.execute("select name from customers where mobile=:1",(custid,))
        res = self.cur.fetchall()
        res = res[0][0].upper().split()[0]
        st = "WELCOME "+res
        self.title(st)
        
        for F in (ViewProfile,MainMenu):
            x = F(custid, cur,container, self)
            self.frames[F] = x
            x.grid(row = 0, column = 0, sticky = "nswe")
        
        
        self.show_frame(MainMenu)
        
    def show_frame(self, F):
        frame = self.frames[F] 
        frame.tkraise()


class MainMenu(tk.Frame):
    
    def __init__(self, custid, cur,parent, controller):
     
        tk.Frame.__init__(self,parent)
        
        container = self
        self.cur = cur
        label = tk.Label(container, text = "    MAIN MENU    ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        self.custid = custid
       
        container.configure(bg = "#7fff00")
        self.controller = controller
        
        self.l1 = tk.Label(container, text = "DIGITAL CLOCK", fg = "red", bg = "white",width = 15, font = ("Courier", 20, "bold italic"), relief = GROOVE)
        self.l1.grid(row = 1, columnspan= 2,padx = 20, pady = 20, sticky = "news")
 
        but1 = tk.Button(container, text = "VIEW MENU", command = self.menu, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "LAST ORDER", command = self.lastOrder, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 3, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but3 = tk.Button(container, text = "ORDER HISTORY", command = self.orderHistory, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 4, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(container, text = "POINTS", command = self.points, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 5, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but5 = tk.Button(container, text = "ACCOUNT DETAILS", command = lambda : controller.show_frame(ViewProfile), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but5.grid(row = 6, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but6 = tk.Button(container, text = "EXIT", command = self.exit,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 7, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but7 = tk.Button(container, text = "LOGOUT", command = self.logout,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but7.grid(row = 7, column = 1, padx = 10, pady = 10, sticky = "we")
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
    
    def menu(self):
        self.controller.destroy()
        show.ShowAllPizza(self.custid, self.cur)
    
    def points(self):
        self.cur.execute("select points from customers where mobile=:1",(self.custid,))
        res = self.cur.fetchall()
        points = str(res[0][0])
        st = "YOU HAVE "+points+" POINTS IN YOUR ACCOUNT !"
        tk.messagebox.showinfo(title = "CUSTOMER POINTS ", message = st)
    
    def orderHistory(self):
        self.controller.destroy()
        show.CustomerDetailsOrder(0, self.custid, self.cur).mainloop()
    
    def lastOrder(self):
        self.controller.destroy()
        show.CustomerDetails(0,self.custid,self.cur).mainloop()
      
    def logout(self):
        
        yn = tk.messagebox.askyesno(title = "LOGOUT", message = "ARE YOU SURE ABOUT YOUR LOGGING OUT ?")
        if yn == True:
            self.controller.destroy()
            logins.logCustomer(self.cur).mainloop()  
      
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
            self.controller.destroy()
            
class ViewProfile(tk.Frame):
    
    def __init__(self, custid, cur,parent, controller):
        tk.Frame.__init__(self, parent)
        container = self
        
        
        cur.execute('select * from customers where mobile=:1',(custid,))
        res = cur.fetchall()
        res = res[0]
        self.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "        PROFILE     ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        lab1 = tk.Label(container, text = "NAME :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab1.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab2 = tk.Label(container, text = res[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab2.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e" )
        
        lab3 = tk.Label(container, text = "MOBILE : ", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab3.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab4 = tk.Label(container, text = res[1], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab4.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab5 = tk.Label(container, text = "GENDER : ", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab5.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab6 = tk.Label(container, text = res[2], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab6.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")

        
        lab9 = tk.Label(container, text = "DOF : ", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab9.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab10 = tk.Label(container, text = str(res[3]).split()[0], font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab10.grid(row = 5, column = 1, padx = 1, pady = 1, sticky = "e")
        
        
        lab9 = tk.Label(container, text = "POINTS :", font = ("arial black",10, "bold"), fg = "black", bg = "white", relief = GROOVE )
        lab9.grid(row = 6, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab10 = tk.Label(container, text = str(res[4]), font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE )
        lab10.grid(row = 6, column = 1, padx = 1, pady = 1, sticky = "e")
        
        
        but1 = tk.Button(self, text = "BACK", command = lambda : controller.show_frame(MainMenu),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 14,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but2 = tk.Button(self, text = "MAIN MENU", command = lambda : controller.show_frame(MainMenu),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 14,column = 1, padx = 10, pady = 15, sticky = "we")
            
def startCustomer(custid, cur):
    Customer(custid, cur).mainloop()
        
#-------------------------------------------------------------------------------------------------------------------