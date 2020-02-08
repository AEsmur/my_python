class Client:
    def __init__(self, name = "anonymous", addr = "homeless",
                 num = "8(800)5553535"):
        self.name = name
        self.addr = addr
        self.num = num        

class Car:
    def __init__(self, client = "name1", brand = "Lada",
                 model = "Sedan", year = "2007"):
        self.client = client
        self.brand = brand
        self.model = model
        self.year = year

    def price(self):
        if self.brand == "BMW":
            if self.model == "3-series":
                if self.year >= 1975:
                    print('Цена обслуживания', self.brand,
                          self.model, self.year, 'года составит',
                          round(self.year * 0.5, 2))
                else:
                    print("Вы ошиблись! " +
                          "BMW 3 серии не выпускался раньше 1975 года!")
            elif self.model == "5-series":
                if self.year >= 1972:
                    print('Цена обслуживания', self.brand,
                          self.model, self.year, 'года составит',
                          round(self.year * 0.6, 2))
                else:
                    print("Вы ошиблись! " +
                          "BMW 5 серии не выпускался раньше 1972 года!")
            elif self.model == "i8":
                if self.year >= 2015:
                    print('Цена обслуживания', self.brand,
                          self.model, self.year, 'года составит',
                          round(self.year * 0.8, 2))
                else:
                    print("Вы ошиблись! " +
                          "BMW i8 не выпускался раньше 2015 года!")
            else:
                print('Мы не обслуживаем модель', self.model,
                      'марки', self.brand)
                
        elif self.brand == "Mercedes":
            if self.model == "S-class":
                if self.year >= 1954:
                    print('Цена обслуживания', self.brand,
                          self.model, self.year, 'года составит',
                          round(self.year * 0.65, 2))
                else:
                    print("Вы ошиблись! " +
                          "Mercedes S-класса не выпускался раньше 1954 года!")
            else:
                print('Мы не обслуживаем модель', self.model,
                      'марки', self.brand)
                
        elif self.brand == "Porsche":
            if self.model == "911":
                if self.year >= 1963:
                    print('Цена обслуживания', self.brand,
                          self.model, self.year, 'года составит',
                          round(self.year * 0.7, 2))
                else:
                    print("Вы ошиблись! " +
                          "Porsche 911 не выпускался раньше 1963 года!")
            else:
                print('Мы не обслуживаем модель', self.model,
                      'марки', self.brand)
        else:
            print("Это центр обслуживания " +
                  "BMW, Mercedes и Porsche, а не " +
                  self.brand)

Car("Oleg", "BMW", "3-series", 2013).price()
Car("Igor", "BMW", "i8", 1675).price()
Car("Daniel", "Audi", "A4", 2010).price()
Car("Michael", "Porsche", "911", 2019).price()
Car("Ivan", "Mercedes", "E-class", 2007).price()
