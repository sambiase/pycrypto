from marginTrading import marginTradingCalculation_GUI_v1 as mtc
import tkinter as tk


def test_init():
    mtc.MarginTradingCalcGui.__init__(tk)


def test_mt_calculation():
    mtc.MarginTradingCalcGui.mt_calculation(None,50,3,5,10)


def test_input_data():
    mtc.MarginTradingCalcGui.input_data(tk)


def test_res_window():
    mtc.MarginTradingCalcGui.res_window(None, 100, 3, 5, 10)