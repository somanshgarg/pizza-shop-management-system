import tkinter as tk
import validation as valid, cashier, manager, admin, creates
from tkinter.constants import GROOVE,DISABLED, NORMAL, INSERT
import datetime
from PIL import ImageTk, Image


orders = []
cust = []
current_order = 0


def getCustomers(cur):#TESTED
    #GET ALL CURRENT CUSTOMERS
    global cust
    cur.execute('select mobile from customers')
    res = cur.fetchall()
    for tup in res:
        cust.append(str(tup[0]))

class TakeOrder(tk.Tk):
    
    def __init__(self, empid, cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.empid = empid
        self.cur = cur
        self.custid = ''
        self.title("TAKE ORDER @ PSMS")
        
        self.frames = {} #DICTIONARY OF FRAMES
        for F in (EnterEmployee,ProcessOrder, ViewHalfMenu):
            x= F(empid, cur, container, self)
            self.frames[F] = x
            x.grid(row = 0, column = 0, sticky = "nswe")
       
            
        self.show_frame(EnterEmployee)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def mainmenu(self):
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
      
        if des == "CASHIER":
            self.destroy()
            cashier.startCashier(self.empid, self.cur)
        elif des == "MANAGER":
            self.destroy()
            manager.startManager(self.empid, self.cur)
        elif des == "ADMIN":
            self.destroy()
            admin.startAdmin(self.empid, self.cur)
        
class EnterEmployee(tk.Frame):
    
    def __init__(self,empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.cur = cur
        self.empid = empid
        label = tk.Label(self, text = "        ODRER CREATION       ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        l1 = tk.Label(self, text = "ENTER CUSTOMER MOBILE NUMBER : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        self.custid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.custid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "e")
        
        but1 = tk.Button(self, text = "GO", command = self.verify, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(self, text = "CREATE CUSTOMER", command = self.create, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 3, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.img = ImageTk.PhotoImage(Image.open("dom.png"))
        limage = tk.Label(self, image = self.img,bg = "#7fff00")
        limage.grid(row = 4, columnspan = 2,padx = 10, pady = 10,sticky = "nwe")
        
        but3 = tk.Button(self, text = "MAIN MENU", command = self.controller.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but3.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(self, text = "BACK", command = self.controller.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but4.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "we")
     
    def create(self):
        self.controller.destroy()
        creates.CreateCustomer(self.empid, self.cur).mainloop()
       
    def verify(self):
        chk = valid.validMobile(self.custid.get())
        chk2 = False
        if chk:
            self.cur.execute("select mobile from customers")
            res = self.cur.fetchall()
            for i in res:
                if str(i[0]) == self.custid.get():
                    self.controller.custid = self.custid.get()
                    chk2 = True
                    break
            if chk2:
                self.controller.show_frame(ProcessOrder)
                self.cur.execute("select name from customers where mobile=:1",(self.controller.custid,))
                res = self.cur.fetchall()
                name = "WELCOME CUSTOMER : "+res[0][0]
                x = self.controller.frames[ProcessOrder].disp
                x.configure(state = NORMAL)
                x.delete("1.0", tk.END)
                x.insert("1.0", name)
                x.configure(state = DISABLED)
            else:
                tk.messagebox.showerror(title = "INVALID ID", message = "CUSTOMER DOES NOT EXIST !")
            
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "INVALID MOBILE NUMBER")
            
    
            
class ProcessOrder(tk.Frame):

    def __init__(self,empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bill = ''
        self.controller = controller
        self.parent = parent
        self.cur = cur
        self.empid = empid
        self.configure(bg = "#7fff00")
        label = tk.Label(self, text = "    PROCESS CREATION    ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10, sticky = "we")
        
        l1 = tk.Label(self, text = "ID/NAME/SHORTUCT", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 10)
        
        l2 = tk.Label(self, text = "SIZE", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        l3 = tk.Label(self, text = "QUANTITY", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l3.grid(row = 1, column = 2, sticky = "e", padx = 10, pady = 10)
        
        self.orderid = tk.StringVar()
        e1 = tk.Entry(self, textvariable = self.orderid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 10)
        
        self.size = tk.StringVar()
        self.size.set("SMALL")
        sizes = ["SMALL","MEDIUM","LARGE"]
        sizemenu = tk.OptionMenu(self, self.size, *sizes)
        sizemenu.grid(row = 2, column = 1, padx = 10, pady = 10)
        menu = sizemenu.nametowidget(sizemenu.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        
        self.quant = tk.StringVar()
        e2 = tk.Entry(self, textvariable = self.quant, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 2, column = 2, sticky = "w", padx = 10, pady = 10)
        
        but1 = tk.Button(self, text = "GENERATE", command = self.generate, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 3, columnspan = 3, sticky = "we", padx = 10, pady = 10 )
        
        but5 = tk.Button(self, text = "VIEW MENU", command = lambda : controller.show_frame(ViewHalfMenu), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but5.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = 10 )
        
        but2 = tk.Button(self, text = "VIEW ORDER", command = self.viewOrder, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 4, column = 1, sticky = "we", padx = 10, pady = 10 )
        
        but3 = tk.Button(self, text = "REMOVE LAST", command = self.removeLast, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 4, column = 2, sticky = "e", padx = 10, pady = 10 )
        
        self.but6 = tk.Button(self, text = "CANCEL", command = self.cancel, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        self.but6.grid(row = 5, column = 0, sticky = "w", padx = 10, pady = 10 )
        
        self.but7 = tk.Button(self, text = "PRINT",command = self.printBill, state = DISABLED, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        self.but7.grid(row = 5, column = 1, sticky = "we", padx = 10, pady = 10 )
        
        self.but8 = tk.Button(self, text = "DONE", command = self.done, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        self.but8.grid(row = 5, column = 2, sticky = "e", padx = 10, pady = 10 )
        
        but9 = tk.Button(self, text = "BACK", command = lambda : self.controller.show_frame(EnterEmployee),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but9.grid(row = 6, columnspan = 3, sticky = "we", padx = 10, pady = 10 )
        
        st = "WELCOME TO SCREEN"
        self.disp = tk.Text(self, height = 10, width = 50)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 7, columnspan = 3, padx = 10, pady = 10)
  
        
    def generate(self):
        self.but7.configure(state = DISABLED)
        self.cur.execute('select prid,name,shortcut from menu')
        res = self.cur.fetchall()
        lotup = []#LOTUP TO CHECK FOR NAME INPRID,SHORTCUT,NAME
        for tup in res:
            a,b,c = tup[0],tup[1],tup[2]
            lotup.append((str(a),str(b).upper(),str(c).upper()))
        name = self.orderid.get() 
        prid = 0  
        chk = False
        name = name.upper()
        for i in lotup:
            if name in i:
                chk = True
                name = i[1]
                prid = i[0]
        if chk:
            chkquant = valid.validNumber(self.quant.get())
            if chkquant:
                size = self.size.get()
                size = size[0].lower()
                tup = (name,size,int(self.quant.get()))
                orders.append(tup)
                txt = tup[0]+" "+tup[1].upper()+" "+str(tup[2])+" ADDED"
                
                self.disp.configure(state = NORMAL)
                self.disp.delete("1.0", tk.END)
                self.disp.insert("1.0", txt)
                self.disp.configure(state = DISABLED)
            else:
                tk.messagebox.showerror(title = "INVALID INPUT", message= "INVALID QUANTITY! SHOULD BE NUMERIC !!")
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH ID/NAME/SHORTCUT EXISTS !")
    
    def viewOrder(self):#TESTED
    #VIEW THE ORDERS IN THE 'ORDERS' LIST
        self.but7.configure(state = DISABLED)
        global orders
        st = '\n'
        if len(orders)!=0:
            for i in orders:
                st = st+"NAME : "+str(i[0])+" SIZE : "+i[1].upper() + " QUANTITY : "+str(i[2])+"\n"  
        else:
            st = "NO ORDER TO DISPLAY "
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)  
    
    def removeLast(self):#TESTED
        #REMOVE LAST ORDER FROM THE 'ORDERS' LIST
        self.but7.configure(state = DISABLED)
        global orders
        st = ''
        if len(orders) == 0:
            st = "EMPTY ORDER BASKET ! CANNOT REMOVE ANYTHING !"
        else:
            i = orders.pop()
            st = "REMOVED : \n NAME :"+i[0]+" SIZE : "+i[1].upper()+" QUANTITY :"+str(i[2])
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)  
    
    def cancel(self):
        self.but7.configure(state = DISABLED)
        global orders
        chk = tk.messagebox.askyesno(title = "CANCEL ORDER", message = "DO YOU WANT TO CANCEL THE WHOLE ORDER ?")
        if chk == True:
        
            orders = []
            text = "WHOLE ORDER CANCELLED !"
            self.disp.configure(state = NORMAL)
            self.disp.delete("1.0", tk.END)
            self.disp.insert("1.0", text)
            self.disp.configure(state = DISABLED)    
            
    def done(self):
        global orders, print_list
        st = ''
        if len(orders) == 0:
            st = "ORDER BASKET IS EMPTY"
        else:
            
            chk = tk.messagebox.askyesno(title = "CONFIRM ORDER ", message = "CONFIRM ORDER ? \n NOTE : ONCE CONFIRMED CANOT BE CANCELLED")
            if chk:
                custid = self.controller.custid
                self.cur.execute("select points from customers where mobile=:1",(int(custid),))
                res = self.cur.fetchall()
                point = int(res[0][0])
                redeem = False
                if point>0:
                    txt = "REDEEM CUSTOMER'S "+str(point)+" POINTS ?"
                    yesno = tk.messagebox.askyesno(title = "REDEEM POINTS", message  = txt)
                    if yesno:
                        redeem = True
                bill = self.generateBillandSave(custid, self.empid, redeem, self.cur)
                self.bill = bill
                chk_disbill = tk.messagebox.askyesno(title = "BILL", message = "DISPLAY BILL ?")
                if chk_disbill:
                    tk.messagebox.showinfo(title = "BILL", message = bill)
                st = "ORDER DONE SUCCESSFULLY \n BASKET IS NOW EMPTY"
                self.but7.configure(state = NORMAL)
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)   
        
        
        
    def generateBillandSave(self,custid, empid, redeem, cur):#TESTED
    #GENERATE BILL, SAVE ORDER INTO DATABASE, UPDATE CUSTOMERS POINTS
    #REDEEM TRUE FLASE
        global current_order
        time = datetime.datetime.now()
        manual = """
        ---------------------------------------------------------------------------------------------
                                        PIZZA SHOP MANAGEMENT SYSTEM
        ---------------------------------------------------------------------------------------------
        Order id : """
        cur.execute('select max(ordid) from orders')
        res = cur.fetchall()
        ordid = res[0][0] + 1
        manual += str(ordid)
        cur.execute('select name from customers where mobile = :1',(custid,))
        res = cur.fetchall()
        custnm = res[0][0]
        current_order = ordid
        manual += "\t CUSTOMER NAME : "+ custnm
        manual += """
        ---------------------------------------------------------------------------------------------
        TIMINGS :
        
        """   
        tm = time
        tm = str(tm)
        tm = tm.split('.')
        tm = tm[0]
        manual += str(tm)
        manual += """
        ---------------------------------------------------------------------------------------------
        NAME \t\t TYPE \t\t SIZE \t\t QUANTITY \t\t PRICE \t\t TOTAL
        ---------------------------------------------------------------------------------------------
        """
        
        bill = 0
        for i in orders:
            name = i[0].upper()
            size = i[1].upper()
            sz = ''
            if size == 'S':
                sz = 'select price_s,type from menu where name=:1'
            if size == 'M':
                sz = 'select price_m,type from menu where name=:1'
            if size == 'L':
                sz = 'select price_l,type from menu where name=:1'
            quan = int(i[2])
            cur.execute(sz,(name,))
            res = cur.fetchall()
            res = res[0]
            
            price = res[0]
            type = res[1]
            b = quan * int(price) 
            st = "\n"
            st = st+name+"\t\t"+type+"\t\t"+size+"\t\t"+str(quan)+"\t\t"+str(price)+"\t\t"+str(b)
            st += "\n ("+type+")"
            manual +=st
            bill = bill + int(b)
        manual += "\n"
        manual += """
        ---------------------------------------------------------------------------------------------
        SUB TOTAL = RS """
        manual += str(bill)
        
        cur.execute('select points from customers where mobile=:1',(custid,))
        res = cur.fetchall()
        points = res[0][0]
        gtotal = 0
        #REDEEMING POINTS
        if redeem:
            if points>bill:
                points -= bill
            else:
                
                gtotal = bill - points
                points = 0
        else:
            gtotal = bill
        manual += """\n
        ---------------------------------------------------------------------------------------------
        POINTS REDEEMED = """
        pointE = int(gtotal/100)
        points += pointE
        manual += str(bill-gtotal)
        manual += """\n
        ---------------------------------------------------------------------------------------------
        GRAND TOTAL  = RS """
        manual += str(gtotal)
        gst = round((0.05)*gtotal,2)
        manual += """\n
        ---------------------------------------------------------------------------------------------
        GST @ 5 % = RS """
        manual += str(gst)
        manual += """\n
        ---------------------------------------------------------------------------------------------
        AMOUNT PAYABLE = RS """
        amount = gtotal+round(gst)
        manual += str(amount)
        
        manual += """\n
        ---------------------------------------------------------------------------------------------
        POINTS EARNED  = """
        manual += str(pointE)
        manual +="""\n
        ---------------------------------------------------------------------------------------------
                        THANK YOU ! FOR SHOPPING WITH US!! KEEP COMING !!!
        ---------------------------------------------------------------------------------------------
                                            HAVE A NICE DAY!!
        ---------------------------------------------------------------------------------------------
        """
        
        
        cur.execute("insert into orders(ordid,custid,empid,time,bill,details) values(:1,:2,:3,:4,:5,:6)",(ordid,custid,empid,time,amount,manual))
        cur.execute('update customers set points=:1 where mobile=:2 ',(points,custid))
        cur.execute('commit')
        return manual
    
    def printBill(self):#TESTED
        #WRITES THE BILL IN A FILE TO BE PRINTED
        global current_order, orders
        filename = "bill_"+str(current_order)+".txt"
        order = open(filename,"w")
        order.write(self.bill)
        order.close()
        txt = " ORDER : "+str(current_order)+" PRINTED AS : "+filename
        orders = []
        st = txt + "\n\n ORDER BASKET IS NOW EMPTY"
        self.but7.configure(state = DISABLED)
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
     
            
class ViewHalfMenu(tk.Frame):

    def __init__(self,empid, cur, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.cur = cur
        label = tk.Label(self, text = "             MENU   ORDER          ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10, sticky = "we")
        self.configure(bg = "#7fff00")
        
        labelmsg = tk.Text(self, width = 50, height = 20)
        labelmsg.grid(row = 1,columnspan = 3,padx = 10, pady = 10, sticky = "we")
        
        cur.execute('select prid,name,price_s,price_m,price_l,type,shortcut from menu order by prid')
        res = cur.fetchall()
        txt = "ID    NAME    S/M/L    TYPE    SHORTCUT\n"
        for tup in res:
            txt += str(tup[0])+" "+tup[1]+"\t"+str(tup[2])+"/"+str(tup[3])+"/"+str(tup[4])+"\t"+tup[5]+" "+tup[6]+"\n"
        labelmsg.insert(INSERT, txt)
        labelmsg.configure(state = DISABLED)
        
        but1 = tk.Button(self, text = "BACK", command = lambda : self.controller.show_frame(ProcessOrder),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 2,column = 0, padx = 10, pady = 15, sticky = "we")
        
        but2 = tk.Button(self, text = "TAKE ORDER", command = lambda : controller.show_frame(EnterEmployee),fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 2,column = 2, padx = 10, pady = 15, sticky = "we")
        
        
      
def startOrder(empid, cur):  
    TakeOrder(empid,cur).mainloop()

#-------------------------------------------------------------------------------------------------------------------