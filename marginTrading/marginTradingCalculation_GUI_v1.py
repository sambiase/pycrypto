'''
    MarginTrading Calc GUI - Tkinter
'''
from tkinter import *
import tkinter as tk


class MarginTradingCalcGui:

    def __init__(self):
        """
            Window Builder
        """
        self.window = tk.Tk()
        self.window.title('MarginTrading Calc v1')
        self.window.configure(bg='black')
        self.window.geometry('350x500')
        self.window.resizable(FALSE, FALSE)

    def text_labels(self):
        """
            Text Labels
        :return:
        """
        frame_text_labels = tk.Frame(self.window)
        colateral = tk.Label(frame_text_labels, text='Valor Colateral', width=15, bg='black', fg='#F0B90B', font='Gotham 13 bold')
        alavancagem = tk.Label(frame_text_labels, text='Alavancagem (x)', width=15, bg='black', fg='#F0B90B',
                               font='Gotham 13 bold')
        alvo = tk.Label(frame_text_labels, text='Alvo (%)', width=15, bg='black', fg='#F0B90B', font='Gotham 13 bold')
        stop = tk.Label(frame_text_labels, text='Stop (%)', width=15, bg='black', fg='#F0B90B', font='Gotham 13 bold')
        frame_text_labels.pack(side=LEFT)
        colateral.pack()
        alavancagem.pack()
        alvo.pack()
        stop.pack()

    def entry_labels(self):
        """
            Entry Labels
        :return:
        """
        frame_entry_labels = tk.Frame(self.window)
        colateral = tk.Entry(frame_entry_labels,bg='white',font='Gotham 13 ')
        alavancagem = tk.Entry(frame_entry_labels,bg='white',font='Gotham 13 ')
        alvo = tk.Entry(frame_entry_labels,bg='white',font='Gotham 13 ')
        stop = tk.Entry(frame_entry_labels,bg='white',font='Gotham 13 ')
        frame_entry_labels.pack(side=RIGHT)
        colateral.pack()
        alavancagem.pack()
        alvo.pack()
        stop.pack()

mtc = MarginTradingCalcGui()
mtc.text_labels()
mtc.entry_labels()
mtc.window.mainloop()
