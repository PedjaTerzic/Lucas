'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python lucas.py
    or if it doesn't work use this one:
        python3 lucas.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from mpmath import *
from sympy import *
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry, Radiobutton, Button, Style

mp.dps = 50000; mp.pretty = True

class Lucas(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("LUCAS")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global v
        v = IntVar()
        v.set(1)
        global coeff
        coeff = StringVar()
        global base
        base = StringVar()
        global exp
        exp = StringVar()
        global const
        const = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)
		
        
        rb1 = Radiobutton(frame1, text = "k*b^n-c", variable = v, value = 1,style='My.TRadiobutton')
        rb1.pack( anchor = W )
		
        rb2 = Radiobutton(frame1, text = "k*b^n+c", variable = v, value = 2,style='My.TRadiobutton')
        rb2.pack( anchor = W )
		
        
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Enter the coefficient :", width=18,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=coeff,style='My.TEntry')
        entry2.pack(fill=X, padx=5, expand=True)
		
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text="Enter the base :", width=18,background='orange')
        lbl3.pack(side=LEFT, padx=5, pady=5)

        entry3 = Entry(frame3,textvariable=base,style='My.TEntry')
        entry3.pack(fill=X, padx=5, expand=True)
		
        frame4 = Frame(self,style='My.TFrame')
        frame4.pack(fill=X)

        lbl4 = Label(frame4, text="Enter the exponent :", width=18,background='orange')
        lbl4.pack(side=LEFT, padx=5, pady=5)

        entry4 = Entry(frame4,textvariable=exp,style='My.TEntry')
        entry4.pack(fill=X, padx=5, expand=True)
		
        frame5 = Frame(self,style='My.TFrame')
        frame5.pack(fill=X)
		
        lbl5 = Label(frame5, text="Enter the constant :", width=18,background='orange')
        lbl5.pack(side=LEFT, padx=5, pady=5)
		
        entry5 = Entry(frame5,textvariable=const,style='My.TEntry')
        entry5.pack(fill=X, padx=5, expand=True)

        
        frame6 = Frame(self,style='My.TFrame')
        frame6.pack(fill=X)

        result = Label(frame6, textvariable=res, width=32,background='orange')
        result.pack(side=LEFT, padx=103, pady=5)

		
        frame7 = Frame(self,style='My.TFrame')
        frame7.pack(fill=X)

        btntest = Button(frame7, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame7, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame7, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        elif msg == 'errc':
            tkinter.messagebox.showerror('Error!', 'Coefficient must be positive integer')
        elif msg == 'errb':
            tkinter.messagebox.showerror('Error!', 'Base must be an even number')
        elif msg == 'erre':
            tkinter.messagebox.showerror('Error!', 'Exponent must be greater than double constant')
			
    
        
    

    def test(self):
        try:
            k = int(coeff.get())
            b = int(base.get())
            n = int(exp.get())
            c = int(const.get())
			
            if k<0:
                self.errorMsg('errc')
            elif b%2 != 0:
                self.errorMsg('errb')
            elif n<=2*c:
                self.errorMsg('erre')
            else:
				
                def polynomial(m,x):
                    if m==1:
                        return x
                    else:
                        p0=2
                        p1=x
                        l=2
                        while l<=m:
                            p=x*p1-p0
                            p0=p1
                            p1=p
                            l=l+1
                        return p
               
            
                if v.get()==1:
                    M=k*b**n-c
                    d=3
                    while not(jacobi_symbol(d-2,M)==-1 and jacobi_symbol(d+2,M)==1):
                        d=d+1
                    s=polynomial(k*b,d)%M
                    ctr=1
                    while ctr<=n-1:
                        s=polynomial(b,s)%M
                        ctr=ctr+1
                    if int(s)==polynomial(c-1,d):
                        value="probably prime"
                        res.set(self.makeAsItIs(value))
                    else:
                        value="composite"
                        res.set(self.makeAsItIs(value))
					
                else:
                    N=k*b**n+c
                    d=3
                    while not(jacobi_symbol(d-2,N)==1 and jacobi_symbol(d+2,N)==1):
                        d=d+1
                    s=polynomial(k*b,d)%N
                    ctr=1
                    while ctr<=n-1:
                        s=polynomial(b,s)%N
                        ctr=ctr+1
                    if int(s)==polynomial(c-1,d):
                        value="probably prime"
                        res.set(self.makeAsItIs(value))
                    else:
                        value="composite"
                        res.set(self.makeAsItIs(value))

          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            coeff.set('')
            base.set('')
            exp.set('')
            const.set('')
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    s.configure('My.TRadiobutton', background='orange')
    s.map('My.TRadiobutton', background=[('active', '#FFC133')])
    root.geometry("300x204")
    lucas = Lucas(root)
    root.mainloop()

if __name__ == '__main__':
    main()