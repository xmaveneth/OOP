import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = [None, None, None]

    def add_filter(self, slot_num, filter):
        if self.filters[slot_num - 1] is None and slot_num == 1 and isinstance(filter, Mechanical) or slot_num == 2 and isinstance(filter, Aragon) or slot_num == 3 and isinstance(filter, Calcium):
            self.filters[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.filters[slot_num - 1] = None

    def get_filters(self):
        result = []
        for el in self.filters:
            if el is not None:
                result.append(el)
        return tuple(result)

    def water_on(self):
        for el in self.filters:
            if el is None or not(0 <= (time.time() - el.date) <= self.MAX_DATE_FILTER):
                return False
        return True


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if getattr(self, key, False) is False:
            object.__setattr__(self, key, value)

class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if getattr(self, key, False) is False:
            object.__setattr__(self, key, value)

class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if getattr(self, key, False) is False:
            object.__setattr__(self, key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
print(f1, f2, f3)
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно