'''
    MarginTrading v1.0

    EN - Program used to calculate Margin Trading
    BR - Programa para calcular Margin Trading
'''
import os


class Margin_Trading_Calculation:

    def __init__(self):
        pass

    def calculation(self, colateral, leverage, target, stop_loss):
        borrowed_value = colateral * (leverage - 1)
        trading_total_value = colateral + borrowed_value
        liquidation_percentage = (100 / leverage) / 100
        liquidation_value = (colateral * liquidation_percentage)
        profit = trading_total_value * (target / 100)
        loss = trading_total_value * (stop_loss / 100)
        return borrowed_value, trading_total_value, liquidation_percentage, liquidation_value, profit, loss


class Margin_Trading_Calculation_BR:

    def __init__(self):
        self.colateral = float(input('\nValor Colateral: '))
        self.leverage = float(input('Alavancagem (x): '))
        self.target = float(input('Alvo (%): '))
        self.stop_loss = float(input('Stop (%): '))

    def print_calculation_results_br(self, res):
        os.system('cls')
        print(f'\nValor Colateral: {self.colateral}')
        print(f'Alavancagem (x): {self.leverage}')
        print(f'\nValor do Emprestimo: {res[0]}')
        print(f'Valor Total do Trade: {res[1]}')
        print(f'Liquidacao (%): {round(res[2] * 100, 2)}')
        print(f'Valor de Liquidacao: {round(res[3], 2)}')
        print(f'Lucro: {round(res[4], 2)}')
        print(f'Perda: {round(res[5], 2)}')


class Margin_Trading_Calculation_EN:

    def __init__(self):
        self.colateral = float(input('\nColateral Value: '))
        self.leverage = float(input('Leverage (x): '))
        self.target = float(input('Target (%): '))
        self.stop_loss = float(input('Stop Loss (%): '))

    def print_calculation_results_en(self, res):
        os.system('cls')
        print(f'\nColateral Value: {self.colateral}')
        print(f'Leverage: {self.leverage}')
        print(f'Borrowed Value: {res[0]}')
        print(f'Trading Total Value: {res[1]}')
        print(f'Liquidation (%): {round(res[2] * 100, 2)}')
        print(f'Liquidation Value: {round(res[3], 2)}')
        print(f'Profit: {round(res[4], 2)}')
        print(f'Loss: {round(res[5], 2)}')


if __name__ == '__main__':

    os.system('cls')
    choice = 'S'

    while choice == 'S' or choice == 'Y':

        language = int(input('(1) - Portugues\n(2) - English\n--> '))

        if language == 1 or language == 2:
            if language == 1:           # Portugues
                choice = 'S'
                while choice.upper() == 'S':
                    mt_br = Margin_Trading_Calculation_BR()
                    res = Margin_Trading_Calculation.calculation(None, mt_br.colateral, mt_br.leverage, mt_br.target,
                                                                 mt_br.stop_loss)
                    mt_br.print_calculation_results_br(res)
                    choice = str(input('\nCalcular novamente? (S) (N)\n--> '))
                    os.system('cls')

                    if choice.upper() == 'N':
                        print('\nObrigado por usar o soft MarginTrading :)')
                    elif choice.upper() == 'S':
                        pass
                    else:
                        print('\nOpcao Invalida :(')

            elif language == 2:
                choice = 'Y'
                while choice.upper() == 'Y':
                    mt_en = Margin_Trading_Calculation_EN()
                    res = Margin_Trading_Calculation.calculation(None, mt_en.colateral, mt_en.leverage, mt_en.target,
                                                                 mt_en.stop_loss)
                    mt_en.print_calculation_results_en(res)
                    choice = str(input('\nCalculate again? (Y) (N)\n--> '))
                    os.system('cls')

                    if choice.upper() == 'N':
                        print('\nThanks for using MarginTrading :)')
                    elif choice.upper() == 'Y':
                        pass
                    else:
                        print('Invalid option :(')
        else:
            os.system('cls')
            print('Opcao Invalida (Invalid option)\n')


