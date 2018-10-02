import tkinter as tk
from tkinter.constants import DISABLED, INSERT, NORMAL,GROOVE
from datetime import datetime
import admin, manager,validation as valid, cashier


class ChangeMenu(tk.Tk):
    
    def __init__(self, empid, prid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.prid = prid
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.frames = {} #DICTIONARY OF FRAMES
        self.title("CHANGE MENU @ PSMS")
        container.configure(bg = "#7fff00")
        self.cur.execute("select name,price_s,price_m,price_l,shortcut,type,details from menu where prid=:1",(prid,))
        res = self.cur.fetchall()
        res = res[0]
        label = tk.Label(container, text = "    CHANGE PIZZA    ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        
        l1 = tk.Label(container, text ="PRODUCT ID : " , font = ("arial black",12, "bold"), fg = "black", bg = "white", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        
        l2 = tk.Label(container, text = str(prid), font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE)
        l2.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "e")
        
        self.name  = tk.StringVar()
        self.name.set(res[0])
        self.oldname = res[0]
        self.price_s = tk.StringVar()
        self.price_s.set(res[1])
        self.price_m = tk.StringVar()
        self.price_m.set(res[2])
        self.price_l = tk.StringVar()
        self.price_l.set(res[3])
        self.shortcut = tk.StringVar()
        self.shortcut.set(res[4])
        self.oldshortuct = res[4]
        self.type = tk.StringVar()
        self.type.set(res[5])
        self.details = tk.StringVar()
        self.details.set(res[6])
        
        l3 = tk.Label(container, text = "NAME : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l3.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e1 = tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l4 = tk.Label(container, text = "PRICE SMALL : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l4.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e2 = tk.Entry(container, textvariable = self.price_s, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l5 = tk.Label(container, text = "PRICE MEDIUM : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l5.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e3 = tk.Entry(container, textvariable = self.price_m, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l6 = tk.Label(container, text = "PRICE LARGE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l6.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e4 = tk.Entry(container, textvariable = self.price_l, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e4.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l7 = tk.Label(container, text = "SHORTCUT : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l7.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = "w")
        
        e5 = tk.Entry(container, textvariable = self.shortcut, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e5.grid(row = 6, column = 1, padx = 10, pady = 10, sticky = "e")
        
        l8 = tk.Label(container, text = "TYPE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l8.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = "w")
        
        types = ["VEG","NON-VEG"]
        sm= tk.OptionMenu(container, self.type, *types)
        sm.grid(row = 7, column = 1, padx = 10, pady = 10)
        menu = sm.nametowidget(sm.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
     
    
        
        l9 = tk.Label(container, text = "DETAILS : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l9.grid(row = 8, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.disp = tk.Text(container, height = 5, width = 18, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        self.disp.insert(INSERT, self.details.get())
        self.disp.grid(row = 9, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but3 = tk.Button(container, text = "UPDATE", command = self.update, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 10, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 11, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 11, column = 1, padx = 10, pady = 10, sticky = "we")
        
        
    def mainmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
  
      
        if des == "MANAGER" :
            manager.startManager(self.empid, self.cur)
            
        elif des == "ADMIN" :
            admin.startAdmin(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
     
        if des == "MANAGER":
            x = manager.Manager(self.empid, self.cur)
            x.back("ChangeMenu")
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ChangeMenu")
        
    def update(self):
        self.cur.execute("select name,shortcut from menu where prid=:1",(self.prid))
        res = self.cur.fetchall()
        res = res[0]
        self.oldname = res[0].upper()
        self.oldshortuct = res[1].upper()
        
        
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
            if self.oldname.upper() == name:
                chk_name  = True
            else:
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
                            if self.oldshortuct.upper() == shortcut:
                                chk_shrt  = True
                            else:
                                for i in loshrt:
                                    if shortcut == i:
                                        chk_shrt = False
                                        break
                                    chk_shrt = True
                            if chk_shrt:
                                if len(shortcut)<9:
                                    self.cur.execute("update menu set name=:1 ,price_s=:2, price_m=:3, price_l=:4, type=:5, shortcut=:6, details=:7 where prid=:8",(name,prices,pricem,pricel,self.type.get(),shortcut.upper(),details,self.prid))
                                    self.cur.execute("commit")
                                    tk.messagebox.showinfo(title = "SUCCESSFULLY CHANGED", message = "PIZZA SUCCESSFULLY CHANGED !")
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
        
        
class ChangeShortcut(tk.Tk):
    
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
        self.title("CHANGE SHORTCUT @ PSMS")
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "    CHANGE SHORTCUT    ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        
        l1 = tk.Label(container, text =" ENTER PIZZA ID/NAME/SHORTCUT: " , font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(container, text = "CONFIRM", command = self.confirm, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 3, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        self.name = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e1.grid(row = 2, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
      
        l2 = tk.Label(container, text =" ENTER NEW SHORTCUT" , font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 4, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        self.shortcut = tk.StringVar()
        e2 = tk.Entry(container, textvariable = self.shortcut, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e2.grid(row = 5, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        
        self.but3 = tk.Button(container, text = "UPDATE", command = self.update, state = DISABLED, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        self.but3.grid(row = 6, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 7, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row = 7, column = 1, padx = 10, pady = 10, sticky = "we")
        
        self.prid = ''
        
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
    
    def confirm(self):
        
        
        self.cur.execute('select prid,name,shortcut from menu')
        res = self.cur.fetchall()
        lotup = []#LOTUP TO CHECK FOR NAME INPRID,SHORTCUT,NAME
        for tup in res:
            a,b,c = tup[0],tup[1],tup[2]
            lotup.append((str(a),str(b).upper(),str(c).upper()))
        name = self.name.get()
        prid = 0  
        shrt = ''
        chk = False
        name = name.upper()
        for i in lotup:
            if name in i:
                chk = True
                name = i[1]
                prid = i[0]
                shrt = i[2]
        if not chk:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH PIZZA ID/NAME/SHORTUCT EXISTS ! PLEASE TRY AGAIN !!")
        else:
            self.shortcut.set(shrt)
            self.but3.configure(state = NORMAL)
            self.prid = prid
            
    def update(self):
        prid = self.prid
        current_shortcut = ''
        self.cur.execute("select shortcut from menu where prid=:1",(prid,))
        res = self.cur.fetchall()
        current_shortcut = res[0][0].upper()
        
        loshrt = []
        self.cur.execute("select shortcut from menu ")
        res = self.cur.fetchall()
        for i in res:
            loshrt.append(i[0].upper())
        chk_shrt = False
        if current_shortcut == self.shortcut.get().upper():
            chk_shrt = True
        else:
            for i in loshrt:
                if self.shortcut.get().upper() == i.upper():
                    chk_shrt = False
                chk_shrt = True
                
        if chk_shrt:
            self.cur.execute("update menu set shortcut=:1 where prid=:2",(self.shortcut.get().upper(),prid))
            self.cur.execute("commit")
            tk.messagebox.showinfo(title = "CHANGED SUCCESSFULLY", message = "SHORTUCT CHANGED SUCESSFULLY")
        else:
            tk.messagebox.showerror(title = "INVALD SHORTCUT", message = "SHORTCUT ALREADY EXISTS !")
            
            
            
class ApplyOfferSingle(tk.Tk):
    
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
        self.title("SINGLE PIZZA OFFER @ PSMS")
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "          SINGLE  PIZZA  OFFER          ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        
        l1 = tk.Label(container, text =" ENTER PIZZA ID/NAME/SHORTCUT " , font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        
        l2 = tk.Label(container, text =" ENTER DISCOUNT % " , font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "e")
        
        self.name = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        
        self.offer = tk.StringVar()
        e2 = tk.Entry(container, textvariable = self.offer, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "e")
        
 
        
        but0 = tk.Button(container, text = "UPDATE", command = self.update, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but0.grid(row = 3, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 6, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row= 6, column = 1, padx = 10, pady = 10, sticky = "we")
  
        st = "WELCOME TO APPLY OFERS"
        self.disp = tk.Text(container, height = 10)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 5, columnspan = 2, padx = 10, pady = 10)
        self.screen()
        
        
        
    def update(self):
        chk = valid.validNumber(self.offer.get())
        if chk:
            self.cur.execute('select prid,name,shortcut from menu')
            res = self.cur.fetchall()
            lotup = []#LOTUP TO CHECK FOR NAME INPRID,SHORTCUT,NAME
            for tup in res:
                a,b,c = tup[0],tup[1],tup[2]
                lotup.append((str(a),str(b).upper(),str(c).upper()))
            name = self.name.get()
            prid = 0  
            shrt = ''
            chk = False
            name = name.upper()
            for i in lotup:
                if name in i:
                    chk = True
                    name = i[1]
                    prid = i[0]
                    shrt = i[2]
            if not chk:
                tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH PIZZA ID/NAME/SHORTUCT EXISTS ! PLEASE TRY AGAIN !!")
            else:
                dis = int(self.offer.get())
                dis = dis/100
                self.cur.execute('select price_s,price_m,price_l from menu where prid=:1',(prid,))
                res = self.cur.fetchall()
                res = res[0]
                s,m,l = res
                s = int(s)
                m = int(m)
                l = int(l)
                dis1 = int(s - s*dis)
                dis2 = int(m - m*dis)
                dis3 = int(l - l*dis)
                self.cur.execute('update menu set price_s=:1,price_m=:2,price_l=:3 where prid=:4',(dis1,dis2,dis3,prid))
                self.cur.execute('commit')
                tk.messagebox.showinfo(title = "OFFER APPLIED", message = "OFFER APPLIED SUCCESSSFULLY !")
                self.display(prid)
            
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message  = "DISCOUNT SHOULD BE NUMERIC ONLY !")   
        
      
        
    def screen(self):
        self.cur.execute("select * from menu order by prid")
        i = self.cur.fetchall()
        st = "\n"
        for res in i:
            
            st += "PRODUCT ID : "+str(res[0])
            st += "\nPRODUCT NAME : "+str(res[1])
            st += "\nPRICE-    SMALL: "+str(res[2])+"    MEDIUM: "+str(res[3])+"    LARGE: "+str(res[4])
            st += "\nSHORTCUT : "+str(res[5])
            st += "\nTYPE : "+str(res[6])
            st += "\nDETAILS : "+str(res[7])+"\n\n"
            st += "--------------------------------------------------------------------------------"
        self.disp.configure(state = NORMAL)
        
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
    
    def display(self,prid):
        self.cur.execute("select * from menu where prid=:1",(prid,))
        res = self.cur.fetchall()
        res = res[0]
        st = "\n"
     
        
        st += "PRODUCT ID : "+str(res[0])
        st += "\nPRODUCT NAME : "+str(res[1])
        st += "\nPRICE-    SMALL: "+str(res[2])+"    MEDIUM: "+str(res[3])+"    LARGE: "+str(res[4])
        st += "\nSHORTCUT : "+str(res[5])
        st += "\nTYPE : "+str(res[6])
        st += "\nDETAILS : "+str(res[7])+"\n\n"
        st += "--------------------------------------------------------------------------------"
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
            x.back("ApplyOffers")
        
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ApplyOffers")
            
class ApplyOfferAll(tk.Tk):
    
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
        self.title("ALL PIZZA OFFER @ PSMS")
        container.configure(bg = "#7fff00")
        label = tk.Label(container, text = "            All    PIZZA    OFFER            ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
        
        l2 = tk.Label(container, text =" ENTER DISCOUNT % " , font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l2.grid(row = 1, columnspan = 2, padx = 10, pady = 10, sticky = "we")

        self.offer = tk.StringVar()
        e2 = tk.Entry(container, textvariable = self.offer, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e2.grid(row = 2, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
 
        
        but0 = tk.Button(container, text = "UPDATE", command = self.update, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but0.grid(row = 3, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 6, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row= 6, column = 1, padx = 10, pady = 10, sticky = "we")
  
        st = "WELCOME TO APPLY OFFERS"
        self.disp = tk.Text(container, height = 10)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 5, columnspan = 2, padx = 10, pady = 10)
        self.screen()
        
        
        
    def update(self):
        chk = valid.validNumber(self.offer.get())
        if chk:
            dis = int(self.offer.get())
            dis = dis/100
            self.cur.execute("select prid from menu order by prid")
            res = self.cur.fetchall()
            for prid in res:
                prid = prid[0]
                self.cur.execute('select price_s,price_m,price_l from menu where prid=:1',(prid,))
                res = self.cur.fetchall()
                res = res[0]
                s,m,l = res
                s = int(s)
                m = int(m)
                l = int(l)
                dis1 = int(s - s*dis)
                dis2 = int(m - m*dis)
                dis3 = int(l - l*dis)
                self.cur.execute('update menu set price_s=:1,price_m=:2,price_l=:3 where prid=:4',(dis1,dis2,dis3,prid))
            self.cur.execute('commit')
            tk.messagebox.showinfo(title = "OFFER APPLIED", message = "OFFER APPLIED SUCCESSSFULLY !")
            self.screen()
           
        
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message  = "DISCOUNT SHOULD BE NUMERIC ONLY !")   
        
      
        
    def screen(self):
        self.cur.execute("select * from menu order by prid")
        i = self.cur.fetchall()
        st = "\n"
        for res in i:
            
            st += "PRODUCT ID : "+str(res[0])
            st += "\nPRODUCT NAME : "+str(res[1])
            st += "\nPRICE-    SMALL: "+str(res[2])+"    MEDIUM: "+str(res[3])+"    LARGE: "+str(res[4])
            st += "\nSHORTCUT : "+str(res[5])
            st += "\nTYPE : "+str(res[6])
            st += "\nDETAILS : "+str(res[7])+"\n\n"
            st += "--------------------------------------------------------------------------------"
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0",tk.END)
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
            x.back("ApplyOffers")
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ApplyOffers")
            

class ChangeEmployeeByManager(tk.Tk):
    
    def __init__(self, empid, employeeid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.employeeid = employeeid
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.title("CHANGE EMPLOYEE DETAILS @ PSMS")
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "CHANGE EMPLOYEE DETAILS", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
      
        self.cur.execute("select name,address,dob,gender,doj,mobile from employees where empid=:1",(int(self.employeeid),))
        res = self.cur.fetchall()
        res = res[0]
        
        self.name  = tk.StringVar()
        self.name.set(res[0])
        self.address= tk.StringVar()
        self.address.set(res[1])
        self.dob = tk.StringVar()
        
        a,b,c = ((str(res[2]).split())[0]).split('-')
        x = c+"/"+b+"/"+a
        self.dob.set(x)
        
        self.gender = tk.StringVar()
        self.gender.set(res[3])
        
        self.doj = tk.StringVar()
        a,b,c = ((str(res[4]).split())[0]).split('-')
        x = c+"/"+b+"/"+a
        self.doj.set(x)

        self.mobile = tk.StringVar()
        self.mobile.set(res[5])
   
        
        lab1= tk.Label(container, text = "EMPID : ", font = ("arial black",12, "bold"), fg = "black", bg = "white", relief = GROOVE)
        lab1.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab2= tk.Label(container, text = str(employeeid), font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE)
        lab2.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab3= tk.Label(container, text = "NAME : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab3.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e1= tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab4= tk.Label(container, text = "MOBILE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab4.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e2= tk.Entry(container, textvariable = self.mobile, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab5= tk.Label(container, text = "ADDRESS : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab5.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e3= tk.Entry(container, textvariable = self.address, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab6= tk.Label(container, text = "DATE OF BIRTH dd/mm/yyyy : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab6.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e4= tk.Entry(container, textvariable = self.dob, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e4.grid(row = 5, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab7= tk.Label(container, text = "GENDER :", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab7.grid(row = 6, column = 0, padx = 1, pady = 1, sticky = "w")
        
        genders = ["MALE","FEMALE","OTHER"]
        opt1= tk.OptionMenu(container, self.gender, *genders)
        opt1.grid(row = 6, column = 1, padx = 10, pady = 10)
        menu = opt1.nametowidget(opt1.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        
        lab8= tk.Label(container, text = "DATE OF JOINING dd/mm/yyyy : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab8.grid(row = 7, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e5= tk.Entry(container, textvariable = self.doj, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e5.grid(row = 7, column = 1, padx = 1, pady = 1, sticky = "e")
        
        but0 = tk.Button(container, text = "UPDATE", command = self.update, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but0.grid(row = 8, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 9, column = 0, padx = 10, pady = 10,sticky = "w")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row= 9,column = 1, padx = 10, pady = 10, sticky = "e")
        
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
            x.back("ChangeEmployeeDetails")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ChangeEmployeeDetails")
    
    def update(self):
        name = self.name.get()
        mobile = self.mobile.get()
        dob = self.dob.get()
        doj = self.doj.get()
        gender = self.gender.get()
        address = self.address.get()
        
        chk_name = valid.validName(name)
        chk_dob = valid.validDate(dob)
        chk_doj = valid.validDate(doj)
        chk_mobile = valid.validMobile(mobile)
        current_mobile = ''
        self.cur.execute("select mobile from employees where empid=:1",(int(self.employeeid),))
        res = self.cur.fetchall()
        current_mobile = str(res[0][0])
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
                    if mobile == current_mobile:
                        chk2 = True
                    else:
                        for i in res:
                            if str(i[0]) == mobile:
                                chk2 = False
                                break
                            chk2 = True
                            
                    if chk2:
                        self.cur.execute("update employees set mobile = :1,address = :2, gender = :3,dob = :4,doj = :5,name = :6 where empid = :7",(mobile,address,gender,dob,doj,name,self.employeeid))
                        self.cur.execute("commit")
                        tk.messagebox.showinfo(title = "SUCCESS", message = "PROFILE UPDATED !")
                    else:
                        tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE NUMBER ALREADY EXISTS !")
        
                else:
                    tk.messagebox.showerror(title = "INVALID MOBILE", message = "MOBILE SHOULD BE NUMERIC AND OF 10 DIGITS ONLY !")
        
            else:
                tk.messagebox.showerror(title = "INVALID DATE", message = "DATE SHOULD BE VALID AND FORMAT - dd/mm/yyyy !")
        
                
        else:
            tk.messagebox.showerror(title = "INVALID NAME", message = "NAME SHOULD BE ONLY OF CHARACTERS !")
            
class LockUnlockAccount(tk.Tk):
    
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
        self.title("LOCK UNLOCK ACCOUNT @ PSMS")
        self.cur.execute("select designation from employees where empid=:1",(empid,))
        res = self.cur.fetchall()
        self.des = res[0][0]
        container.configure(bg = "#7fff00")
       
        
        label = tk.Label(container, text = "LOCK-UNLOCK ACCOUNT", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        l1 = tk.Label(container, text = "ENTER EMPLOYEE ID", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.employeeid = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.employeeid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE    )
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(container, text = "LOCK", command =  lambda : self.verify("LOCKED"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(container, text = "UNLOCK", command = lambda : self.verify("UNLOCKED"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = "we")
        
        st = "WELCOME TO LOCK UNLOCK ACCOUNT"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
        
        but3 = tk.Button(container, text = "LOCK ALL", command = self.lockAll, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but3.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "we")
        
        but4 = tk.Button(container, text = "UNLOCK ALL", command = self.unLockAll, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but4.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "we")
   
        
        but5 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but6 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "we")
     
    def verify(self, par): 
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
                self.lockUnlock(par)
            else:
                tk.messagebox.showerror(title = "INVALID EMPLOYEE ID", message = "EMPLOYEE ID DOES NOT EXIST !")
                
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NOT A VALID EMPLOYEE ID ! SHOULD BE ONLY NUMERIC !!")
        
    def lockUnlock(self, par):
        self.cur.execute("select designation from employees where empid=:1",(int(self.employeeid.get()),))
        res = self.cur.fetchall()
        emp_des = res[0][0]
        if self.des == "MANAGER":
            if emp_des == "CASHIER":
                self.cur.execute("update employees set locks=:1 where empid=:2",(par,int(self.employeeid.get())))
                self.cur.execute("commit")
                msg = "EMPLOYEE SUCCESSSFULLY "+par
                tk.messagebox.showinfo(title = "SUCCESSFULLY DONE", message = msg)
                msg = "DO YOU WANT TO VIEW "+par+" ACCOUNT ?"
                ch = tk.messagebox.askyesno(title = "VIEW ACCOUNT", message = msg)
                if ch:
                    self.cur.execute("select * from employees where empid=:1",(int(self.employeeid.get()),))
                    res = self.cur.fetchall()
                    res = res[0]
                    st = ''
                   
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
                    self.disp.configure(state = NORMAL)
                    self.disp.delete("1.0", tk.END)
                    self.disp.insert("1.0", st)
                    self.disp.configure(state = DISABLED)
                
            else:
                tk.messagebox.showerror(title = "ACCESS DENIED", message = "YOU ARE NOT AUTHORIZED TO LOCK/UNLOCK THIS ACCOUNT !")
        else:
            if emp_des == "CASHIER" or emp_des == "MANAGER":
                self.cur.execute("update employees set locks=:1 where empid=:2",(par,int(self.employeeid.get())))
                self.cur.execute("commit")
                msg = "EMPLOYEE SUCCESSSFULLY "+par
                tk.messagebox.showinfo(title = "SUCCESSFULLY DONE", message = msg)
                msg = "DO YOU WANT TO VIEW "+par+" ACCOUNT ?"
                ch = tk.messagebox.askyesno(title = "VIEW ACCOUNT", message = msg)
                if ch:
                    self.cur.execute("select * from employees where empid=:1",(int(self.employeeid.get()),))
                    res = self.cur.fetchall()
                    res = res[0]
                    st = ''
                   
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
                    self.disp.configure(state = NORMAL)
                    self.disp.delete("1.0", tk.END)
                    self.disp.insert("1.0", st)
                    self.disp.configure(state = DISABLED)
                
            else:
                tk.messagebox.showerror(title = "ACCESS DENIED", message = "YOU ARE NOT AUTHORIZED TO LOCK/UNLOCK THIS ACCOUNT !")
        
    def lockAll(self):
        if self.des == "MANAGER":
            self.cur.execute("update employees set locks='LOCKED' where designation='CASHIER'")
            self.cur.execute("commit")
            tk.messagebox.showinfo(title = "LOCKED SUCCESSFULL", message = "ALL CASHIER HAS BEEN LOCKED SUCCESSFULLY !")
            ch = tk.messagebox.askyesno(title = "VIEW LOCKED ACCOUNT", message = "DO YOU WANT TO VIEW ALL LOCKED ACCOUNTS ~ CASHIER ?")
            if ch:
                self.cur.execute("select * from employees where designation='CASHIER'")
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
                self.disp.configure(state = NORMAL)
                self.disp.delete("1.0", tk.END)
                self.disp.insert("1.0", st)
                self.disp.configure(state = DISABLED)
        else:
            self.cur.execute("update employees set locks='LOCKED' where designation='CASHIER' or designation='MANAGER'")
            self.cur.execute("commit")
            tk.messagebox.showinfo(title = "LOCKED SUCCESSFULL", message = "ALL CASHIER AND MANAGER HAS BEEN LOCKED SUCCESSFULLY !")
            ch = tk.messagebox.askyesno(title = "VIEW LOCKED ACCOUNT", message = "DO YOU WANT TO VIEW ALL LOCKED ACCOUNTS ~ CASHIER AND MANAGER ?")
            if ch:
                self.cur.execute("select * from employees where designation='CASHIER' or designation='MANAGER'")
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
                self.disp.configure(state = NORMAL)
                self.disp.delete("1.0", tk.END)
                self.disp.insert("1.0", st)
                self.disp.configure(state = DISABLED)
                
    def unLockAll(self):
        if self.des == "MANAGER":
            self.cur.execute("update employees set locks='UNLOCKED' where designation='CASHIER'")
            self.cur.execute("commit")
            tk.messagebox.showinfo(title = "UNLOCKED SUCCESSFULL", message = "ALL CASHIER HAS BEEN UNLOCKED SUCCESSFULLY !")
            ch = tk.messagebox.askyesno(title = "VIEW UNLOCKED ACCOUNT", message = "DO YOU WANT TO VIEW ALL UNLOCKED ACCOUNTS ~ CASHIER ?")
            if ch:
                self.cur.execute("select * from employees where designation='CASHIER'")
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
                self.disp.configure(state = NORMAL)
                self.disp.delete("1.0", tk.END)
                self.disp.insert("1.0", st)
                self.disp.configure(state = DISABLED)
        else:
            self.cur.execute("update employees set locks='UNLOCKED' where designation='CASHIER' or designation='MANAGER'")
            self.cur.execute("commit")
            tk.messagebox.showinfo(title = "UNLOCKED SUCCESSFULL", message = "ALL CASHIER AND MANAGER HAS BEEN UNLOCKED SUCCESSFULLY !")
            ch = tk.messagebox.askyesno(title = "VIEW UNLOCKED ACCOUNT", message = "DO YOU WANT TO VIEW ALL UNLOCKED ACCOUNTS ~ CASHIER AND MANAGER ?")
            if ch:
                self.cur.execute("select * from employees where designation='CASHIER' or designation='MANAGER'")
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
            x.back("EmployeeDetails")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("EmployeeDetails")
            
    def show(self, par):
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des= res[0][0]
        
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)
        query = ''
        if des == "MANAGER":
            if par == "ACTIVE":
                query = "select * from employees where designation = 'CASHIER' and STATUS = 'ACTIVE' "
            
            elif par == "INACTIVE":
                query = "select * from employees where designation = 'CASHIER' and STATUS = 'INACTIVE' "
                
            else:
                query = "select * from employees where designation = 'CASHIER' "
                
        else:
            if par == "ACTIVE":
                query = "select * from employees where STATUS = 'ACTIVE' "
            
            elif par == "INACTIVE":
                query = "select * from employees where STATUS = 'INACTIVE' "
                
            else:
                query = "select * from employees "
        
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
        
class DeletePizza(tk.Tk):
    
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
        self.title("DELETE PIZZA @ PSMS")
        self.frames = {} #DICTIONARY OF FRAMES
        container.configure(bg = "#7fff00")
       
        
        label = tk.Label(container, text = "            DELETE   PIZZA         ", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        l1 = tk.Label(container, text = "ENTER PIZZA ID/NAME/SHORTCUT", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.pizza = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.pizza, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but1 = tk.Button(container, text = "VERIFY", command = self.verify, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 2,columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        st = "WELCOME TO DELETE PIZZA"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
        
        but2 = tk.Button(container, text = "DELETE PIZZA", command = self.delPizza, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 4, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        
        but5 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = "we")
        
        self.prid = ''
        but6 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "we")
    
    def verify(self):
        self.cur.execute('select prid,name,shortcut from menu')
        res = self.cur.fetchall()
        lop = []
        for tup in res:
            x = [str(tup[0]),tup[1].upper(),tup[2].upper()]
            lop.append(x)
        prid = self.pizza.get().upper()
        chk = False
        for li in lop:
            if prid in li:
                chk = True
                self.prid = int(li[0])
                break
        if chk:
            self.cur.execute("select * from menu where prid=:1",(self.prid,))
            res = self.cur.fetchall()
            res = res[0]
            st = "\n"
            st += "PRODUCT ID : "+str(res[0])
            st += "\nPRODUCT NAME : "+str(res[1])
            st += "\nPRICE-    SMALL: "+str(res[2])+"    MEDIUM: "+str(res[3])+"    LARGE: "+str(res[4])
            st += "\nSHORTCUT : "+str(res[5])
            st += "\nTYPE : "+str(res[6])
            st += "\nDETAILS : "+str(res[7])
            
            self.disp.configure(state = NORMAL)
            self.disp.delete("1.0", tk.END)   
            self.disp.insert("1.0", st)
            self.disp.configure(state = DISABLED)
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH PIZZA ID/NAME/SHORTCUT EXISTS !")
    
    def delPizza(self):
        if valid.validNumber(self.prid):
            ch = tk.messagebox.askyesno(title = "CONFIRM DELETION", message = "ARE YOU SURE TO REMOVE PIZZA ?")
            if ch:
                self.cur.execute("select max(prid) from menu")
                res = self.cur.fetchall()
                res = res[0][0]
                prid = int(self.prid)
                if self.prid == res:
                    self.cur.execute("delete from menu where prid=:1",(prid,))
                else:
                    self.cur.execute("delete from menu where prid=:1",(prid,))
                    self.cur.execute("update menu set prid=:1 where prid=:2",(prid,res))
                self.cur.execute("commit")
                tk.messagebox.showinfo(title = "SUCCESSFULL", message = "PIZZA REMOVED SUCCESSFULLY")
                self.disp.configure(state = NORMAL)
                st = "PIZZA REMOVED SUCCESFULLY "
                self.disp.delete("1.0", tk.END)   
                self.disp.insert("1.0", st)
                self.disp.configure(state = DISABLED)
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NO SUCH PIZZA ID/NAME/SHORTCUT EXISTS !")
        
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
            x.back("Menu")
            
class ChangeEmployeeByAdmin(tk.Tk):
    
    def __init__(self, empid, employeeid,cur,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.employeeid = employeeid
        #self.overrideredirect(True)
        container = tk.Frame()
        self.empid = empid
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.cur = cur
        self.title("CHANGE EMPLOYEE DETAILS @ PSMS")
        container.configure(bg = "#7fff00")
        
        label = tk.Label(container, text = "CHANGE EMPLOYEE DETAILS", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 2, padx = 10, pady = 10)
      
        self.cur.execute("select name,address,dob,gender,doj,mobile,password,salary,designation from employees where empid=:1",(int(self.employeeid),))
        res = self.cur.fetchall()
        res = res[0]
        
        self.name  = tk.StringVar()
        self.name.set(res[0])
        self.address= tk.StringVar()
        self.address.set(res[1])
        self.dob = tk.StringVar()
        
        a,b,c = ((str(res[2]).split())[0]).split('-')
        x = c+"/"+b+"/"+a
        self.dob.set(x)
        
        self.gender = tk.StringVar()
        self.gender.set(res[3])
        
        self.doj = tk.StringVar()
        a,b,c = ((str(res[4]).split())[0]).split('-')
        x = c+"/"+b+"/"+a
        self.doj.set(x)

        self.mobile = tk.StringVar()
        self.mobile.set(res[5])
   
        self.password = tk.StringVar()
        self.password.set(res[6])
        
        self.salary = tk.StringVar()
        self.salary.set(res[7])
        
        self.designation = tk.StringVar()
        self.designation.set(res[8])
        
        lab1= tk.Label(container, text = "EMPID : ", font = ("arial black",12, "bold"), fg = "black", bg = "white", relief = GROOVE)
        lab1.grid(row = 1, column = 0, padx = 1, pady = 1, sticky = "w")
        
        lab2= tk.Label(container, text = str(employeeid), font = ("arial black",10, "bold"), fg = "red", bg = "white", relief = GROOVE)
        lab2.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab3= tk.Label(container, text = "NAME : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab3.grid(row = 2, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e1= tk.Entry(container, textvariable = self.name, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 2, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab4= tk.Label(container, text = "MOBILE : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab4.grid(row = 3, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e2= tk.Entry(container, textvariable = self.mobile, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e2.grid(row = 3, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab5= tk.Label(container, text = "ADDRESS : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab5.grid(row = 4, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e3= tk.Entry(container, textvariable = self.address, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e3.grid(row = 4, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab6= tk.Label(container, text = "DATE OF BIRTH dd/mm/yyyy : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab6.grid(row = 5, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e4= tk.Entry(container, textvariable = self.dob, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e4.grid(row = 5, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab7= tk.Label(container, text = "GENDER :", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab7.grid(row = 6, column = 0, padx = 1, pady = 1, sticky = "w")
        
        genders = ["MALE","FEMALE","OTHER"]
        opt1= tk.OptionMenu(container, self.gender, *genders)
        opt1.grid(row = 6, column = 1, padx = 10, pady = 10)
        menu = opt1.nametowidget(opt1.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        
        lab8= tk.Label(container, text = "DATE OF JOINING dd/mm/yyyy : ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab8.grid(row = 7, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e5= tk.Entry(container, textvariable = self.doj, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e5.grid(row = 7, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab9= tk.Label(container, text = "  PASSWORD ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab9.grid(row = 8, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e6= tk.Entry(container, textvariable = self.password, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e6.grid(row = 8, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab10= tk.Label(container, text = "  SALARY ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab10.grid(row = 9, column = 0, padx = 1, pady = 1, sticky = "w")
        
        e7= tk.Entry(container, textvariable = self.salary, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e7.grid(row = 9, column = 1, padx = 1, pady = 1, sticky = "e")
        
        lab11= tk.Label(container, text = "DESIGNATION ", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        lab11.grid(row = 10, column = 0, padx = 1, pady = 1, sticky = "w")
        
        des = ["CASHIER","MANAGER","ADMIN"]
        opt2= tk.OptionMenu(container, self.designation, *des)
        opt2.grid(row = 10, column = 1, padx = 10, pady = 10)
        menu = opt2.nametowidget(opt2.menuname)
        menu.configure(font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)

        but0 = tk.Button(container, text = "UPDATE", command = self.update, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but0.grid(row = 11, columnspan = 2, padx = 10, pady = 10,sticky = "we")
        
        but1 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but1.grid(row = 12, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but2 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but2.grid(row= 12,column = 1, padx = 10, pady = 10, sticky = "we")
        
    def mainmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
  
      
        if des == "MANAGER" :
            manager.startManager(self.empid, self.cur)
            
        elif des == "ADMIN":
            admin.startAdmin(self.empid, self.cur)
            
        elif des == "CASHIER":#PREVENTIVE MEASURE IF ADMIN DEMOTES HIMSELF TO CASHIER
            cashier.startCashier(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
     
        if des == "MANAGER":
            x = manager.Manager(self.empid, self.cur)
            x.back("ChangeEmployeeDetails")
            
        elif des == "ADMIN":
            x = admin.Admin(self.empid, self.cur)
            x.back("ChangeEmployeeDetails")
            
        elif des == "CASHIER":#PREVENTIVE MEASURE IF ADMIN DEMOTES HIMSELF TO CASHIER
            cashier.startCashier(self.empid, self.cur)
    
    def update(self):
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
        current_mobile = ''
        self.cur.execute("select mobile from employees where empid=:1",(int(self.employeeid),))
        res = self.cur.fetchall()
        current_mobile = str(res[0][0])
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
                    if mobile == current_mobile:
                        chk2 = True
                    else:
                        for i in res:
                            if str(i[0]) == mobile:
                                chk2 = False
                                break
                            chk2 = True
                            
                    if chk2:
                        if chk_sal:
                            if chk_pass:
                                self.cur.execute("update employees set mobile = :1,address = :2, gender = :3,dob = :4,doj = :5,name = :6,password = :7,salary = :8, designation = :9 where empid = :10",(mobile,address,gender,dob,doj,name,passd,int(sal),self.designation.get(),self.employeeid))
                                self.cur.execute("commit")
                                tk.messagebox.showinfo(title = "SUCCESS", message = "PROFILE UPDATED !")
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
            
class FireRehireEmployee(tk.Tk):
    
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
        self.cur.execute("select designation from employees where empid=:1",(empid,))
        res = self.cur.fetchall()
        self.des = res[0][0]
        self.title("FIRE-REHIRE EMPLOYEE @ PSMS")
        container.configure(bg = "#7fff00")
       
        
        label = tk.Label(container, text = "FIRE-REHIRE EMPLOYEE", font = ("Verdana",25, "bold italic underline"), fg = "blue", bg = "white", relief = GROOVE)
        label.grid(row = 0, columnspan = 3, padx = 10, pady = 10)
        
        l1 = tk.Label(container, text = "ENTER EMPLOYEE ID", font = ("arial black",12, "bold"), fg = "white", bg = "black", relief = GROOVE)
        l1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "we")
        
        self.employeeid = tk.StringVar()
        e1 = tk.Entry(container, textvariable = self.employeeid, font = ("arial black",10, "bold"), fg = "blue", bg = "white", relief = GROOVE)
        e1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but0 = tk.Button(container, text = "DISPLAY", command =  self.verify, fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but0.grid(row = 2, columnspan = 2, padx = 10, pady = 10, sticky = "we")
        
        st = "WELCOME TO FIRE REHIRE ACCOUNT"
        self.disp = tk.Text(container, width = 50, height = 20)
        self.disp.insert(INSERT, st)
        self.disp.configure(state = DISABLED)
        self.disp.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
        
        but1 = tk.Button(container, text = "FIRE", command =  lambda : self.verify("INACTIVE"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but1.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "we")
        
        but2 = tk.Button(container, text = "REHIRE", command = lambda : self.verify("ACTIVE"), fg = "white", bg = "#0000cd", font = ("arial black",11, "bold"))
        but2.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "we")
        
        but5 = tk.Button(container, text = "BACK", command = self.backmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but5.grid(row = 5, column = 0, padx = 10, pady = 10,sticky = "we")
        
        but6 = tk.Button(container, text = "MAIN MENU", command = self.mainmenu,fg = "white", bg = "red", font = ("arial black",12,"bold"))
        but6.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = "we")
     
    def verify(self, par = 1): 
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
                if par == 1:
                    self.show()
                else:
                    self.fireRehire(par)
            else:
                tk.messagebox.showerror(title = "INVALID EMPLOYEE ID", message = "EMPLOYEE ID DOES NOT EXIST !")
                
        else:
            tk.messagebox.showerror(title = "INVALID INPUT", message = "NOT A VALID EMPLOYEE ID ! SHOULD BE ONLY NUMERIC !!")
            
    def fireRehire(self, par):
        employeeid =  int(self.employeeid.get())
        st = ''
        if par == "INACTIVE":
            x= datetime.now().date()
            mon = ['','January','February','March','April','May','June','July','August','September','October','November','December']
            a,b,c = str(x).split('-')
            x = c+"-"+mon[int(b)]+"-"+a
            self.cur.execute("update employees set status=:1,doin=:2 where empid=:3",(par,str(x),employeeid))
            self.cur.execute("commit")
            st = "EMPLOYEE ID "+str(employeeid)+" SUCCESSFULLY FIRED"
        else:
            self.cur.execute("update employees set status=:1,doin=NULL where empid=:3",(par,employeeid))
            self.cur.execute("commit")
            st = "EMPLOYEE ID "+str(employeeid)+" SUCCESSFULLY REHIRED"
            
           
            
        
        tk.messagebox.showinfo(title = "SUCCESSFULLY CHANGED", message = st)
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
    def show(self):
        employeeid =  int(self.employeeid.get())
        self.cur.execute('select * from employees where empid=:1',(int(employeeid),))
        res = self.cur.fetchall()
        res = res[0]
        st = ''
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
        self.disp.configure(state = NORMAL)
        self.disp.delete("1.0", tk.END)   
        self.disp.insert("1.0", st)
        self.disp.configure(state = DISABLED)
        
    def mainmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
        admin.startAdmin(self.empid, self.cur)
            
    def backmenu(self):
        self.destroy()
        self.cur.execute("select designation from employees where empid = :1",(self.empid,))
        res = self.cur.fetchall()
        des = res[0][0]
 
        x = admin.Admin(self.empid, self.cur)
        x.back("HireFireRehire")
        
def changeEmployeeLockLogin(empid, cur):#TESTED
    #LOCKS THE EMPID SENT BY LOGIN AND CHEKS FOR NOT OF 'ADMIN'
    cur.execute('select designation from employees where empid=:1',(empid,))
    res = cur.fetchall()
    des = res[0][0]
    if des == 'ADMIN':
        #"SYSTEM ERROR! CANNOT LOCK ADMIN !!"
        pass
    else:
        cur.execute("update employees set locks='LOCKED' where empid=:1",(empid,))
        cur.execute('commit')
        #"YOUR ACCOUNT HAS BEEN LOCKED !!"
        #"CONTACT YOUR ADMIN OR MANAGER !!"
        
#-------------------------------------------------------------------------------------------------------------------