'''
    MarginTrading Calc GUI - ttkinter ttk
'''
from tkinter import FALSE, TOP, LEFT, RIGHT
import tkinter as ttk
from ttkbootstrap import Style
from tkinter import ttk


class MarginTradingCalcGui:

    def __init__(self):
        """
            Main Window
        """
        style = Style(theme='superhero')
        self.window = style.master
        style.configure('TButton', font=('Gotham', 14))
        style.configure('TEntry', fieldbackground='white')
        self.window.title('MarginTrading Calc v1')
        self.window.geometry('340x430')
        self.window.resizable(FALSE, FALSE)
        self.window.iconbitmap('cryptotech_logo.ico')

    def mt_calculation(self, colateral, leverage, target, stop_loss):
        """
            MarginTrading Calc Function

        :param self: None
        :param colateral: int
        :param leverage: int
        :param target: int
        :param stop_loss: int
        :return:
        """
        loan_value = colateral * (leverage - 1)
        trading_total_value = colateral + loan_value
        liquidation_percentage = (100 / leverage) / 100
        liquidation_value = (colateral * liquidation_percentage)
        profit = trading_total_value * (target / 100)
        loss = trading_total_value * (stop_loss / 100)
        return loan_value, trading_total_value, liquidation_percentage, liquidation_value, profit, loss

    def input_data(self):
        """
            Text & Entry Labels
        :return:
        """

        top_frame = ttk.Frame(self.window)
        colateral_frame = ttk.Frame(self.window)
        leverage_frame = ttk.Frame(self.window)
        target_frame = ttk.Frame(self.window)
        stop_frame = ttk.Frame(self.window)
        calc_btn_frame = ttk.Frame(self.window)

        colateral_text = ttk.Label(colateral_frame, text='Valor Colateral', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')
        colateral_input = ttk.Entry(colateral_frame)

        leverage_text = ttk.Label(leverage_frame, text='Alavancagem (x)', width=15, anchor='c', foreground='black',
                                  background='#F0B90B', font='Gotham 14 bold')
        leverage_input = ttk.Entry(leverage_frame)

        target_text = ttk.Label(target_frame, text='Alvo (%)', width=15, anchor='c', foreground='black',
                                background='#F0B90B', font='Gotham 14 bold')
        target_input = ttk.Entry(target_frame)

        stop_text = ttk.Label(stop_frame, text='Stop (%)', width=15, anchor='c', foreground='black',
                              background='#F0B90B', font='Gotham 14 bold')
        stop_input = ttk.Entry(stop_frame)

        calc_btn = ttk.Button(calc_btn_frame, text='Calcular', style='secondary.TButton', width=10,
                              command=lambda: MarginTradingCalcGui.res_window(None, int(colateral_input.get()),
                                                                              int(leverage_input.get()),
                                                                              int(target_input.get()),
                                                                              int(stop_input.get())))

        top_frame.pack(pady=15)

        colateral_frame.pack(side=TOP, pady=15)
        colateral_text.pack(side=LEFT, ipadx=25, ipady=10)
        colateral_input.pack(side=RIGHT, padx=30, ipady=3)

        leverage_frame.pack(side=TOP, pady=15)
        leverage_text.pack(side=LEFT, ipadx=25, ipady=10)
        leverage_input.pack(side=RIGHT, padx=30, ipady=3)

        target_frame.pack(side=TOP, pady=15)
        target_text.pack(side=LEFT, ipadx=25, ipady=10)
        target_input.pack(side=RIGHT, padx=30, ipady=3)

        stop_frame.pack(side=TOP, pady=15)
        stop_text.pack(side=LEFT, ipadx=25, ipady=10)
        stop_input.pack(side=RIGHT, padx=30, ipady=3)

        calc_btn_frame.pack(pady=30)

        calc_btn.pack()

    def res_window(self, colateral_input, alavancagem_input, target_input, stop_input):
        """
            Window that shows the results of the Margin Calculation
        :return:
        """
        style = Style(theme='cyborg')
        res_window = style.master
        res_window.title('MarginTrading Calc v2 - Results')
        res_window.geometry('350x440')
        res_window.resizable(FALSE, FALSE)
        res_window.iconbitmap('cryptotech_logo.ico')

        calc_results = MarginTradingCalcGui.mt_calculation(None, colateral_input, alavancagem_input, target_input,
                                                           stop_input)

        top_frame = ttk.Frame(res_window)
        colateral_frame = ttk.Frame(res_window)
        leverage_frame = ttk.Frame(res_window)
        loan_frame = ttk.Frame(res_window)
        trade_total_value_frame = ttk.Frame(res_window)
        liquidation_percent_frame = ttk.Frame(res_window)
        liquidation_value_frame = ttk.Frame(res_window)
        profit_frame = ttk.Frame(res_window)
        loss_frame = ttk.Frame(res_window)

        colateral_text = ttk.Label(colateral_frame, text='Valor Colateral', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        colateral_res = ttk.Label(colateral_frame, text=f'{colateral_input}', width=18, font='Gotham 13')

        leverage_text = ttk.Label(leverage_frame, text='Alavancagem (x)', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        leverage_res = ttk.Label(leverage_frame, text=f'{alavancagem_input}', width=18, font='Gotham 13')

        loan_text = ttk.Label(loan_frame, text='Valor do Empréstimo', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        loan_res = ttk.Label(loan_frame, text=f'{calc_results[0]}', width=18, font='Gotham 13')

        trade_total_value_text = ttk.Label(trade_total_value_frame, text='Valor Total do Trade', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        trade_total_value_res = ttk.Label(trade_total_value_frame, text=f'{calc_results[1]}', width=18, font='Gotham 13')

        liquidation_percent_text = ttk.Label(liquidation_percent_frame, text='Liquidação (%)', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        liquidation_percent_res = ttk.Label(liquidation_percent_frame, text=f'{round(calc_results[2] * 100, 2)}',
                                            width=18, font='Gotham 13')

        liquidation_value_text = ttk.Label(liquidation_value_frame, text='Valor de Liquidação', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        liquidation_value_res = ttk.Label(liquidation_value_frame, text=f'{round(calc_results[3], 2)}', width=18,
                                          font='Gotham 13')

        profit_text = ttk.Label(profit_frame, text='Lucro', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        profit_res = ttk.Label(profit_frame, text=f'{round(calc_results[4], 2)}', width=18, font='Gotham 13')

        loss_text = ttk.Label(loss_frame, text='Prejuízo', width=15, anchor='c', foreground='black',
                                   background='#F0B90B', font='Gotham 14 bold')

        loss_res = ttk.Label(loss_frame, text=f'{round(calc_results[5], 2)}', width=18, font='Gotham 13')

        top_frame.pack(pady=15)

        colateral_frame.pack(side=TOP, pady=10)
        colateral_text.pack(side=LEFT)
        colateral_res.pack(side=RIGHT, padx=35, ipady=1)

        leverage_frame.pack(side=TOP, pady=10)
        leverage_text.pack(side=LEFT)
        leverage_res.pack(side=RIGHT, padx=35, ipady=1)

        loan_frame.pack(side=TOP, pady=10)
        loan_text.pack(side=LEFT)
        loan_res.pack(side=RIGHT, padx=35, ipady=1)

        trade_total_value_frame.pack(side=TOP, pady=10)
        trade_total_value_text.pack(side=LEFT)
        trade_total_value_res.pack(side=RIGHT, padx=35, ipady=1)

        liquidation_percent_frame.pack(side=TOP, pady=10)
        liquidation_percent_text.pack(side=LEFT)
        liquidation_percent_res.pack(side=RIGHT, padx=35, ipady=1)

        liquidation_value_frame.pack(side=TOP, pady=10)
        liquidation_value_text.pack(side=LEFT)
        liquidation_value_res.pack(side=RIGHT, padx=35, ipady=1)

        profit_frame.pack(side=TOP, pady=10)
        profit_text.pack(side=LEFT)
        profit_res.pack(side=RIGHT, padx=35, ipady=1)

        loss_frame.pack(side=TOP, pady=10)
        loss_text.pack(side=LEFT)
        loss_res.pack(side=RIGHT, padx=35, ipady=1)

        res_window.mainloop()


if __name__ == '__main__':
    mtc = MarginTradingCalcGui()
    mtc.input_data()
    mtc.window.mainloop()
