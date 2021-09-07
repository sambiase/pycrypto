"""
    MarginTrading Calc v1.0

    EN - Program used to calculate Margin Trading
    BR - Programa para calcular Margin Trading

"""
import os


class MarginTradingCalculation:

    def __init__(self, colateral, leverage, target, stop_loss):
        self.colateral = colateral
        self.leverage = leverage
        self.target = target
        self.stop_loss = stop_loss

    def calculation(self):
        borrowed_value = self.colateral * (self.leverage - 1)
        trading_total_value = self.colateral + borrowed_value
        liquidation_percentage = (100 / self.leverage) / 100
        liquidation_value = (self.colateral * liquidation_percentage)
        profit = trading_total_value * (self.target / 100)
        loss = trading_total_value * (self.stop_loss / 100)
        return borrowed_value, trading_total_value, liquidation_percentage, liquidation_value, profit, loss


class MarginTradingCalculationBR:

    def __init__(self):
        self.colateral = float(input('\nValor Colateral: '))
        self.leverage = float(input('Alavancagem (x): '))
        self.target = float(input('Alvo (%): '))
        self.stop_loss = float(input('Stop (%): '))

    def calc_results_br(self, res):
        os.system('clear')
        print(f'\nValor Colateral: {self.colateral}')
        print(f'Alavancagem (x): {self.leverage}')
        print(f'\nValor do Empréstimo: {res[0]}')
        print(f'Valor Total do Trade: {res[1]}')
        print(f'Liquidação (%): {round(res[2] * 100, 2)}')
        print(f'Valor de Liquidação: {round(res[3], 2)}')
        print(f'Lucro: {round(res[4], 2)}')
        print(f'Prejuízo: {round(res[5], 2)}')


class MarginTradingCalculationEN:

    def __init__(self):
        self.colateral = float(input('\nColateral Value: '))
        self.leverage = float(input('Leverage (x): '))
        self.target = float(input('Target (%): '))
        self.stop_loss = float(input('Stop Loss (%): '))

    def calc_results_en(self, res):
        os.system('clear')
        print(f'\nColateral Value: {self.colateral}')
        print(f'Leverage: {self.leverage}')
        print(f'Borrowed Value: {res[0]}')
        print(f'Trading Total Value: {res[1]}')
        print(f'Liquidation (%): {round(res[2] * 100, 2)}')
        print(f'Liquidation Value: {round(res[3], 2)}')
        print(f'Profit: {round(res[4], 2)}')
        print(f'Loss: {round(res[5], 2)}')


if __name__ == '__main__':

    os.system('clear')
    choice = 'S'

    while choice == 'S' or choice == 'Y':
        try:
            language = int(input('(1) - Portugues\n(2) - English\n(3) - Exit\n --> '))
            if language == 3:
                exit()
            else:
                if language == 1 or language == 2:
                    if language == 1:  # Portuguese
                        choice = 'S'
                        while choice.upper() == 'S':
                            mt_br = MarginTradingCalculationBR()
                            mtcalc = MarginTradingCalculation(mt_br.colateral, mt_br.leverage, mt_br.target,
                                                              mt_br.stop_loss)
                            res = mtcalc.calculation()
                            mt_br.calc_results_br(res)
                            choice = str(input('\nCalcular novamente? (S) (N)\n--> '))
                            os.system('clear')

                            if choice.upper() == 'S':
                                pass
                            elif choice.upper() == 'N':
                                print('\nObrigado por usar o software MarginTrading :)')
                            else:
                                print('\nOpcao Inválida :(')

                    elif language == 2:
                        choice = 'Y'
                        while choice.upper() == 'Y':
                            mt_en = MarginTradingCalculationEN()
                            mtcalc = MarginTradingCalculation(mt_en.colateral, mt_en.leverage, mt_en.target,
                                                              mt_en.stop_loss)
                            res = mtcalc.calculation()
                            mt_en.calc_results_en(res)
                            choice = str(input('\nCalculate again? (Y) (N)\n--> '))
                            os.system('clear')

                            if choice.upper() == 'Y':
                                pass
                            elif choice.upper() == 'N':
                                print('\nThanks for using MarginTrading :)')
                            else:
                                print('Invalid option :(')
                else:
                    os.system('clear')
                    print('Opcao Invalida (Invalid option)\n')

        except ValueError:
            os.system('clear')
            print('Opcao invalida. Por favor tente novamente.\n Invalid option. Please try again.\n')
