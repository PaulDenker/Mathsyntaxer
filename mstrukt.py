

'''
Задача этого модуля в том чтобы перехватывая символы формировать из них разметку latex.
Так, чтобы это было возможно быстрее.

Мне нравится немецкий, а ещё есть желание сопротивляться экспансии английского языка.
Обозначение переменных будет компромиссном между желанием и здравым смыслом.
'''

class Sack:
    '''
    Объекты этого класса - слова. Тупиковые ветки синтаксического графа.
    '''
    def __init__(self, eltern = None):
        self.eltern = eltern
        self.inhalt = str()
        self.gefullt_flag = False

    @property
    def ist_gefullt(self):
        #Проверка наполненности.
        return self.gefullt_flag

    def __call__(self, symbol):
        #Кушаем символы и реагируем на стоп-символы.
        if self.ist_gefullt:
            idx = self.eltern.kindidx(self)
            self.eltern.kinder[idx+1](symbol)
            return
        if not self.ist_gefullt:
            if symbol == ' ':
                if self.inhalt != '':
                    self.gefullt_flag = True
                    return
            if symbol in '+-':
                if self.inhalt != '':
                    self.gefullt_flag = True
                    self.eltern.neukind()
                    self.eltern.neubind(symbol)
                    return
            else:
                self.inhalt += symbol
                return
                

    '''
    Буду рекусивно по цепочке передавать символ, пока он не найдёт свободное место.
    '''

    def sicht(self):
        #Выводим содержимое.
        return self.inhalt



class Sum:
    def __init__(self, eltern = None):
        self.eltern = eltern
        self.kinder = [Sack(self)]
        self.binder = list()
        self.gefullt_flag = False

    def __call__(self, symbol):
        self.kinder[0](symbol)
        print(self.kinder)

    def neukind(self):
        self.kinder.append(Sack(self))

    def neubind(self, bindsymbol):
        self.binder.append(bindsymbol)

    def kindidx(self, kind):
        return next((i for i, c in enumerate(self.kinder) if c is kind), None)



    
sum = Sum()
while True:
    x = input()
    sum(x)


