'''
    MarginTrading Calc GUI - Tkinter
'''
from tkinter import FALSE, TOP, LEFT, RIGHT
import tkinter as tk


class MarginTradingCalcGui:

    def __init__(self):
        """
            Main Window
        """
        self.window = tk.Tk()
        self.window.title('MarginTrading Calc v1')
        self.window.configure(bg='black')
        self.window.geometry('350x440')
        self.window.resizable(FALSE, FALSE)
        # self.window.iconbitmap('cryptotechlogo.ico')

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

        top_frame = tk.Frame(self.window)
        colateral_frame = tk.Frame(self.window)
        leverage_frame = tk.Frame(self.window)
        target_frame = tk.Frame(self.window)
        stop_frame = tk.Frame(self.window)
        calc_btn_frame = tk.Frame(self.window)

        colateral_text = tk.Label(colateral_frame, text='Valor Colateral', width=18, height=2, fg='black', bg='#F0B90B',
                                  font='Gotham 15 bold')
        colateral_input = tk.Entry(colateral_frame, bg='white', font='Gotham 13 ')

        leverage_text = tk.Label(leverage_frame, text='Alavancagem (x)', width=18, height=2, fg='black',
                                 bg='#F0B90B', font='Gotham 15 bold')
        leverage_input = tk.Entry(leverage_frame, bg='white', font='Gotham 13 ')

        target_text = tk.Label(target_frame, text='Alvo (%)', width=18, height=2, fg='black', bg='#F0B90B',
                               font='Gotham 15 bold')
        target_input = tk.Entry(target_frame, bg='white', font='Gotham 13 ')

        stop_text = tk.Label(stop_frame, text='Stop (%)', width=18, height=2, fg='black', bg='#F0B90B',
                             font='Gotham 15 bold')
        stop_input = tk.Entry(stop_frame, bg='white', font='Gotham 13 ')

        calc_btn = tk.Button(calc_btn_frame, text='Calcular', width=10, height=1, fg='black', bg='#F0B90B',
                             font='Gotham 15 bold',
                             command=lambda: MarginTradingCalcGui.verify_input(None, int(colateral_input.get()),
                                                                               int(leverage_input.get()),
                                                                               int(target_input.get()),
                                                                               int(stop_input.get())))

        top_frame.pack(pady=15)

        colateral_frame.pack(side=TOP, pady=15)
        colateral_text.pack(side=LEFT)
        colateral_input.pack(side=RIGHT, padx=35, ipady=3)

        leverage_frame.pack(side=TOP, pady=15)
        leverage_text.pack(side=LEFT)
        leverage_input.pack(side=RIGHT, padx=35, ipady=3)

        target_frame.pack(side=TOP, pady=15)
        target_text.pack(side=LEFT)
        target_input.pack(side=RIGHT, padx=35, ipady=3)

        stop_frame.pack(side=TOP, pady=15)
        stop_text.pack(side=LEFT)
        stop_input.pack(side=RIGHT, padx=35, ipady=3)

        calc_btn_frame.pack(pady=20)

        calc_btn.pack()

    @classmethod
    def verify_input(self, colateral_input, leverage_input, target_input, stop_input):
        print(colateral_input)

    def res_window(self, colateral_input, leverage_input, target_input, stop_input):
        """
            Window that shows the results of the Margin Calculation
        :return:
        """

        res_window = tk.Tk()
        res_window.title('MarginTrading Calc v1 - Results')
        res_window.configure(bg='black')
        res_window.geometry('350x440')
        res_window.resizable(FALSE, FALSE)
        # res_window.iconbitmap('cryptotechlogo.ico')

        calc_results = MarginTradingCalcGui.mt_calculation(None, colateral_input, leverage_input, target_input,
                                                           stop_input)

        top_frame = tk.Frame(res_window)
        colateral_frame = tk.Frame(res_window, bg='black')
        leverage_frame = tk.Frame(res_window, bg='black')
        loan_frame = tk.Frame(res_window, bg='black')
        trade_total_value_frame = tk.Frame(res_window, bg='black')
        liquidation_percent_frame = tk.Frame(res_window, bg='black')
        liquidation_value_frame = tk.Frame(res_window, bg='black')
        profit_frame = tk.Frame(res_window, bg='black')
        loss_frame = tk.Frame(res_window, bg='black')

        colateral_text = tk.Label(colateral_frame, text='Valor Colateral', width=18, fg='black', bg='#F0B90B',
                                  font='Gotham 14 bold')

        colateral_res = tk.Label(colateral_frame, text=f'{colateral_input}', width=18, bg='white', font='Gotham 13')

        leverage_text = tk.Label(leverage_frame, text='Alavancagem (x)', width=18, fg='black', bg='#F0B90B',
                                 font='Gotham 14 bold')

        leverage_res = tk.Label(leverage_frame, text=f'{leverage_input}', width=18, bg='white', font='Gotham 13')

        loan_text = tk.Label(loan_frame, text='Valor do Empr??stimo', width=18, fg='black', bg='#F0B90B',
                             font='Gotham 14 bold')

        loan_res = tk.Label(loan_frame, text=f'{calc_results[0]}', width=18, bg='white', font='Gotham 13')

        trade_total_value_text = tk.Label(trade_total_value_frame, text='Valor Total do Trade', width=18, fg='black',
                                          bg='#F0B90B',
                                          font='Gotham 14 bold')

        trade_total_value_res = tk.Label(trade_total_value_frame, text=f'{calc_results[1]}', width=18, bg='white',
                                         font='Gotham 13')

        liquidation_percent_text = tk.Label(liquidation_percent_frame, text='Liquida????o (%)', width=18, fg='black',
                                            bg='#F0B90B', font='Gotham 14 bold')

        liquidation_percent_res = tk.Label(liquidation_percent_frame, text=f'{round(calc_results[2] * 100, 2)}',
                                           width=18, bg='white', font='Gotham 13')

        liquidation_value_text = tk.Label(liquidation_value_frame, text='Valor de Liquida????o', width=18, fg='black',
                                          bg='#F0B90B', font='Gotham 14 bold')

        liquidation_value_res = tk.Label(liquidation_value_frame, text=f'{round(calc_results[3], 2)}', width=18,
                                         bg='white', font='Gotham 13')

        profit_text = tk.Label(profit_frame, text='Lucro', width=18, fg='black', bg='#F0B90B', font='Gotham 14 bold')

        profit_res = tk.Label(profit_frame, text=f'{round(calc_results[4], 2)}', width=18, bg='white', font='Gotham 13')

        loss_text = tk.Label(loss_frame, text='Preju??zo', width=18, fg='black', bg='#F0B90B', font='Gotham 14 bold')

        loss_res = tk.Label(loss_frame, text=f'{round(calc_results[5], 2)}', width=18, bg='white', font='Gotham 13')

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
