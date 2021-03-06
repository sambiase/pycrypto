'''
    MarginTrading Calc GUI - ttkbootstrap
'''
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MarginTradingCalcGui:

    def __init__(self):
        """
            Main Window
        """
        self.window = ttk.Window(themename='superhero')
        self.window.title('MarginTrading Calc v1')
        self.window.geometry('340x430')
        self.window.resizable(FALSE, FALSE)

    def input_data(self):
        """
            Text & Entry Labels
        :return:
        """

        INPUT_MSG = 'WARNING'
        FONT = 'Gotham 13 bold'
        TEXT_WIDTH = 15
        top_frame = ttk.Frame(self.window)
        collateral_frame = ttk.Frame(self.window)
        calc_btn_frame = ttk.Frame(self.window)
        leverage_frame = ttk.Frame(self.window)
        target_frame = ttk.Frame(self.window)
        stop_frame = ttk.Frame(self.window)
        calc_btn_frame = ttk.Frame(self.window)

        collateral_text = ttk.Label(collateral_frame, text='Collateral Value', width=TEXT_WIDTH, anchor='c',
                                    foreground='black',
                                    background='#F0B90B', font=FONT)

        collateral_input = ttk.Entry(collateral_frame, bootstyle=INPUT_MSG)

        leverage_text = ttk.Label(leverage_frame, text='Leverage (x)', width=TEXT_WIDTH, anchor='c', foreground='black',
                                  background='#F0B90B', font=FONT)
        leverage_input = ttk.Entry(leverage_frame, bootstyle=INPUT_MSG)

        target_text = ttk.Label(target_frame, text='Target (%)', width=TEXT_WIDTH, anchor='c', foreground='black',
                                background='#F0B90B', font=FONT)
        target_input = ttk.Entry(target_frame, bootstyle=INPUT_MSG)

        stop_text = ttk.Label(stop_frame, text='Stop (%)', width=TEXT_WIDTH, anchor='c', foreground='black',
                              background='#F0B90B', font=FONT)
        stop_input = ttk.Entry(stop_frame, bootstyle=INPUT_MSG)

        calc_btn = ttk.Button(calc_btn_frame, text='Calculate', bootstyle=SUCCESS, width=13,
                              command=lambda: MarginTradingCalcGui.res_window(collateral=int(collateral_input.get()),
                                                                              leverage=int(leverage_input.get()),
                                                                              target=int(target_input.get()),
                                                                              stop=int(stop_input.get())))

        top_frame.pack(pady=15)

        collateral_frame.pack(side=TOP, pady=15)
        collateral_text.pack(side=LEFT, ipadx=25, ipady=10)

        collateral_input.pack(side=RIGHT, padx=30, ipady=3)

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

        mtc.window.mainloop()

    def res_window(**kwargs):
        """
            Window that shows the results of the Margin Calculation
        :return:
        """

        FONT = 'Gotham 13'
        TEXT_WIDTH = 20
        res_window = ttk.Window(themename='superhero')
        res_window.title('MarginTrading Calc v1 - Results')
        res_window.geometry('340x430')
        res_window.resizable(FALSE, FALSE)

        top_frame = ttk.Frame(res_window)
        collateral_frame = ttk.Frame(res_window)
        leverage_frame = ttk.Frame(res_window)
        loan_frame = ttk.Frame(res_window)
        trade_total_value_frame = ttk.Frame(res_window)
        liquidation_percent_frame = ttk.Frame(res_window)
        liquidation_value_frame = ttk.Frame(res_window)
        profit_frame = ttk.Frame(res_window)
        loss_frame = ttk.Frame(res_window)

        loan_value = kwargs.get('collateral') * (kwargs.get('leverage') - 1)
        trading_total_value = kwargs.get('collateral') + loan_value
        liquidation_percentage = (100 / kwargs.get('leverage')) / 100
        liquidation_value = (kwargs.get('collateral') * liquidation_percentage)
        profit = trading_total_value * (kwargs.get('target') / 100)
        loss = trading_total_value * (kwargs.get('stop') / 100)

        collateral_text = ttk.Label(collateral_frame, text='Collateral Value', width=TEXT_WIDTH, anchor='c',
                                    foreground='black',
                                    background='#F0B90B', font=FONT)

        collateral_res = ttk.Label(collateral_frame, text=kwargs.get('collateral'), width=18, font='Gotham 13')

        leverage_text = ttk.Label(leverage_frame, text='Leverage (x)', width=TEXT_WIDTH, anchor='c', foreground='black',
                                  background='#F0B90B', font=FONT)

        leverage_res = ttk.Label(leverage_frame, text=kwargs.get('leverage'), width=18, font='Gotham 13')

        loan_text = ttk.Label(loan_frame, text='Loan Value', width=TEXT_WIDTH, anchor='c', foreground='black',
                              background='#F0B90B', font=FONT)

        loan_res = ttk.Label(loan_frame, text=loan_value, width=18, font='Gotham 13')

        trade_total_value_text = ttk.Label(trade_total_value_frame, text='Trade Total Value', width=TEXT_WIDTH,
                                           anchor='c',
                                           foreground='black',
                                           background='#F0B90B', font=FONT)

        trade_total_value_res = ttk.Label(trade_total_value_frame, text=trading_total_value, width=18,
                                          font='Gotham 13')

        liquidation_percent_text = ttk.Label(liquidation_percent_frame, text='Liquidation (%)', width=TEXT_WIDTH,
                                             anchor='c',
                                             foreground='black',
                                             background='#F0B90B', font=FONT)

        liquidation_percent_res = ttk.Label(liquidation_percent_frame, text=liquidation_percentage,
                                            width=18, font='Gotham 13')

        liquidation_value_text = ttk.Label(liquidation_value_frame, text='Liquidation Value', width=TEXT_WIDTH,
                                           anchor='c',
                                           foreground='black',
                                           background='#F0B90B', font=FONT)

        liquidation_value_res = ttk.Label(liquidation_value_frame, text=liquidation_value, width=18,
                                          font='Gotham 13')

        profit_text = ttk.Label(profit_frame, text='Profit', width=TEXT_WIDTH, anchor='c', foreground='black',
                                background='#F0B90B', font=FONT)

        profit_res = ttk.Label(profit_frame, text=profit, width=18, font='Gotham 13')

        loss_text = ttk.Label(loss_frame, text='Loss', width=TEXT_WIDTH, anchor='c', foreground='black',
                              background='#F0B90B', font=FONT)

        loss_res = ttk.Label(loss_frame, text=loss, width=18, font='Gotham 13')

        top_frame.pack(pady=15)

        collateral_frame.pack(side=TOP, pady=10)
        collateral_text.pack(side=LEFT)
        collateral_res.pack(side=RIGHT, padx=35, ipady=1)

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

