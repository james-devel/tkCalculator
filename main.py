#!/usr/bin/env python3

import tkinter as tk


class Calculator(tk.Frame):
    
    
    def __init__(self, master=None):
    
        super().__init__(master)
        self.master = master
        self.entryvar = tk.StringVar()
        self.master.bind('<Return>', self.calculate)
        self.master.bind('<KP_Enter>', self.calculate)
        self.pack()
        self.createlayout()
        self.charwhitelist = ['*', '/', '+', '-',
                              '.', '(', ')', '0',
                              '1', '2', '3', '4',
                              '5', '6', '7', '8',
                              '9'
                              ]


    def clearentry(self):
        # Clears out the entry box
        self.entryvar.set('')


    def addcharacter(self, text):
        # Called by a button. addes its own text to the entry
        if self.entryvar.get() == 'ERROR':
            self.clearentry()
        self.entryvar.set(self.entryvar.get() + text)
    

    def calculate(self, event=None):
        # Calculates what ever is in the entry box and/or throws an error
        self.entrystr = self.entryvar.get()
        
        for self.char in self.entrystr:
            if self.char not in self.charwhitelist:
                self.entryvar.set('ERROR')
                break
        else:
            try:
                self.entryvar.set(eval(self.entrystr))
            except:
                self.entryvar.set('ERROR')


    def createlayout(self):
        # Creates all the buttons and what not
        self.entry = tk.Entry(self, justify=tk.RIGHT,
            textvariable=self.entryvar)
        self.entry.grid(row=0, column=0, columnspan=5)
        
        self.key0 = tk.Button(self, text='0',
            command=lambda:self.addcharacter('0'))
        self.key0.grid(row=4, column=0,
            columnspan=2, sticky='nesw')
        
        self.key1 = tk.Button(self, text='1',
            command=lambda:self.addcharacter('1'))
        self.key1.grid(row=3, column=0, sticky='nesw')
        
        self.key2 = tk.Button(self, text='2',
            command=lambda:self.addcharacter('2'))
        self.key2.grid(row=3, column=1, sticky='nesw')
        
        self.key3 = tk.Button(self, text='3',
            command=lambda:self.addcharacter('3'))
        self.key3.grid(row=3, column=2, sticky='nesw')
        
        self.key4 = tk.Button(self, text='4',
            command=lambda:self.addcharacter('4'))
        self.key4.grid(row=2, column=0, sticky='nesw')
        
        self.key5 = tk.Button(self, text='5',
            command=lambda:self.addcharacter('5'))
        self.key5.grid(row=2, column=1, sticky='nesw')
        
        self.key6 = tk.Button(self, text='6',
            command=lambda:self.addcharacter('6'))
        self.key6.grid(row=2, column=2, sticky='nesw')
        
        self.key7 = tk.Button(self, text='7',
            command=lambda:self.addcharacter('7'))
        self.key7.grid(row=1, column=0, sticky='nesw')
        
        self.key8 = tk.Button(self, text='8',
            command=lambda:self.addcharacter('8'))
        self.key8.grid(row=1, column=1, sticky='nesw')
        
        self.key9 = tk.Button(self, text='9',
            command=lambda:self.addcharacter('9'))
        self.key9.grid(row=1, column=2, sticky='nesw')
        
        self.keydec = tk.Button(self, text='.',
            command=lambda:self.addcharacter('.'))
        self.keydec.grid(row=4, column=2, sticky='nesw')
        
        self.keyadd = tk.Button(self, text='+',
            command=lambda:self.addcharacter('+'))
        self.keyadd.grid(row=1, column=3, sticky='nesw')
        
        self.keysub = tk.Button(self, text='-',
            command=lambda:self.addcharacter('-'))
        self.keysub.grid(row=2, column=3, sticky='nesw')
        
        self.keymul = tk.Button(self, text='*',
            command=lambda:self.addcharacter('*'))
        self.keymul.grid(row=3, column=3, sticky='nesw')
        
        self.keydiv = tk.Button(self, text='/',
            command=lambda:self.addcharacter('/'))
        self.keydiv.grid(row=4, column=3, sticky='nesw')
        
        self.keycalc = tk.Button(self, text='=',
            command=self.calculate)
        self.keycalc.grid(row=4, column=4, sticky='nesw')
        
        self.keyclear = tk.Button(self, text='C',
            command=self.clearentry)
        self.keyclear.grid(row=1, column=4, sticky='nesw')
        
        self.keylpar = tk.Button(self, text='(',
            command=lambda:self.addcharacter('('))
        self.keylpar.grid(row=2, column=4, sticky='nesw')
        
        self.keyrpar = tk.Button(self, text=')',
            command=lambda:self.addcharacter(')'))
        self.keyrpar.grid(row=3, column=4, sticky='nesw')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('tkCalculator')
    calculator = Calculator(root)
    root.mainloop()
