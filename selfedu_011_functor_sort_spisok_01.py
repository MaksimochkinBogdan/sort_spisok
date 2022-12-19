class Person:
    def __init__(self, surname, forename, old):
        self.__surname = surname
        self.__forename = forename
        self.__old = old
        
        
        
        
    @property
    def __data(self):
        return self.__surname, self.__forename, self.__old
    
    def __call__(self, *args, **kwargs):
        self.__data
    
    
    
    
    
    
class SortKey():
    def __init__(self, spisok):
        for i in spisok:
            if not isinstance(i,Person):
                raise ValueError("Принимается список только экземпляров класса Person")
        self.__spisok = [i() for i in spisok]
        
    def __call__(self, sorter):
        if sorter not in ['surname', 'old']:
            raise ValueError("Параметры сортировки либо surname, либо old")
        if sorter == 'surname':
            self.__spisok.sort()
            return self.__spisok
        else:
            self.__spisok.sort(key = lambda x: x[-1])
            return self.__spisok
    
    
p = [Person("Иванов", "Иван", 20), 
     Person("Петров", "Петр", 20), 
     Person("Федоров", "Федр", 20)
     ]

s = SortKey(p)
print(s('old'))
print(s('surname'))
