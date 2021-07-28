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
        self.window.geometry('350x440')
        self.window.resizable(FALSE, FALSE)
        self.window.iconbitmap('CryptoTech_Logo.ico')

    def input_data(self):
        """
            Text & Entry Labels
        :return:
        """
        top_frame = tk.Frame(self.window)
        colateral_frame = tk.Frame(self.window)
        alavancagem_frame = tk.Frame(self.window)
        alvo_frame = tk.Frame(self.window)
        stop_frame = tk.Frame(self.window)

        colateral_text = tk.Label(colateral_frame, text='Valor Colateral', width=18, height=2, fg='black', bg='#F0B90B',
                                  font='Gotham 15 bold')
        colateral_input = tk.Entry(colateral_frame, bg='white', font='Gotham 13 ')

        alavancagem_text = tk.Label(alavancagem_frame, text='Alavancagem (x)', width=18, height=2, fg='black',
                                    bg='#F0B90B', font='Gotham 15 bold')
        alavancagem_input = tk.Entry(alavancagem_frame, bg='white', font='Gotham 13 ')

        alvo_text = tk.Label(alvo_frame, text='Alvo (%)', width=18, height=2, fg='black', bg='#F0B90B',
                             font='Gotham 15 bold')
        alvo_input = tk.Entry(alvo_frame, bg='white', font='Gotham 13 ')

        stop_text = tk.Label(stop_frame, text='Stop (%)', width=18, height=2, fg='black', bg='#F0B90B',
                             font='Gotham 15 bold')
        stop_input = tk.Entry(stop_frame, bg='white', font='Gotham 13 ')

        top_frame.pack(pady=25)

        colateral_frame.pack(side=TOP, pady=10)
        colateral_text.pack(side=LEFT)
        colateral_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        alavancagem_frame.pack(side=TOP, pady=10)
        alavancagem_text.pack(side=LEFT)
        alavancagem_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        alvo_frame.pack(side=TOP, pady=10)
        alvo_text.pack(side=LEFT)
        alvo_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        stop_frame.pack(side=TOP, pady=10)
        stop_text.pack(side=LEFT)
        stop_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        return colateral_input

    def res_window(self):
        """
            Window that shows the results of the Margin Calculation
        :return:
        """

        res_window = tk.Tk()
        res_window.title('MarginTrading Calc v1 - Results')
        res_window.configure(bg='#F0B90B')
        res_window.geometry('350x440')
        res_window.resizable(FALSE, FALSE)
        res_window.iconbitmap('CryptoTech_Logo.ico')

        top_frame = tk.Frame(res_window)
        colateral_frame = tk.Frame(res_window)
        alavancagem_frame = tk.Frame(res_window)
        alvo_frame = tk.Frame(res_window)
        stop_frame = tk.Frame(res_window)

        colateral_text = tk.Label(colateral_frame, text='Valor Colateral', width=18, height=2, fg='white', bg='black',
                                  font='Gotham 15 bold')

        colateral_res = tk.Label(colateral_frame, text='', width=18, height=2,bg='white', font='Gotham 13 ')

        top_frame.pack(pady=25)

        colateral_frame.pack(side=TOP, pady=10)
        colateral_text.pack(side=LEFT)
        colateral_res.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        alavancagem_frame.pack(side=TOP, pady=10)
        #alavancagem_text.pack(side=LEFT)
        #alavancagem_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        alvo_frame.pack(side=TOP, pady=10)
        #alvo_text.pack(side=LEFT)
        #alvo_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        stop_frame.pack(side=TOP, pady=10)
        #stop_text.pack(side=LEFT)
        #stop_input.pack(side=RIGHT, padx=35, pady=15, ipady=3)

        res_window.mainloop()

    def calc_btn(self):
        """
            Calc Button
        :return:
        """

        calc_btn_frame = tk.Frame(self.window)
        calc_btn = tk.Button(calc_btn_frame, text='Calcular', width=10, height=1, fg='black', bg='#F0B90B',
                             font='Gotham 15 bold')

        calc_btn_frame.pack(pady=18)
        calc_btn.bind("<Button>", MarginTradingCalcGui.res_window)
        calc_btn.pack()


mtc = MarginTradingCalcGui()
mtc.input_data()
mtc.calc_btn()
mtc.window.mainloop()
