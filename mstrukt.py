

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
        if self.ist_gefullt and self.selbsuchen():
            self.eltern.kinder[self.selbsuchen() + 1](symbol)
        else:
            if symbol == ' ' and self.inhalt != '':
                self.gefullt_flag = True
                return

    '''
    Буду рекусивно по цепочке передавать символ, пока он не найдёт свободное место.
    '''



    def sicht(self):
        #Выводим содержимое.
        return self.inhalt

    def selbsuchen(self):
        if self.eltern:
            return next((i for i, c in enumerate(self.eltern.kinder) if c is self), None)
        return None


class Sum:
    def __init__(self, eltern = None):
        self.eltern = eltern
        self.kinder = list()
        self.binder = list()
        self.gefullt_flag = False

    def __call__(self, symbol):
        pass


    
    


