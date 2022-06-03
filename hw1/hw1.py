import os
import csv

try:
    class CarBase:
        def __init__(self, brand, photo_file_name, carrying):
            if isinstance(brand, str):
                self.brand = brand
            else:
                raise TypeError(f"Значение {brand} не является строкой")
            if isinstance(photo_file_name, str):
                self.photo_file_name = photo_file_name
            else:
                raise TypeError(f"Значение {photo_file_name} не является строкой")
            try:
                float(carrying)
                self.carrying = carrying
            except ValueError:
                raise TypeError(f"Значение {carrying} должно быть числом")

        def get_photo_file_ext(self):
            print(os.path.splitext(self.photo_file_name)[-1])

    class Truck(CarBase):
        def __init__(self, brand, photo_file_name, carrying, body_whl):
            super().__init__(brand, photo_file_name, carrying)
            self.car_type = 'truck'
            if type(body_whl) == str:
                body_whl = body_whl.split('x')
                if len(body_whl) == 3:
                    try:
                        self.body_length = float(body_whl[0])
                        self.body_width = float(body_whl[1])
                        self.body_height = float(body_whl[2])
                    except ValueError:
                        raise ValueError("Габариты кузова дожны быть вещественными числами")
                elif len(body_whl) == 1 and body_whl[0] == '':
                    self.body_length = 0
                    self.body_width = 0
                    self.body_height = 0
                else:
                    raise ValueError("Неверные габариты кузова")
            else:
                raise TypeError(f"Значение {body_whl} не является строкой")

        def get_body_volume(self):
            return self.body_height * self.body_width * self.body_length

    class Car(CarBase):
        def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
            super().__init__(brand, photo_file_name, carrying)
            self.car_type = 'car'
            try:
                passenger_seats_count = int(passenger_seats_count)
                if passenger_seats_count <= 0:
                    raise ValueError(f"Значение {passenger_seats_count} не может быть меньше 1")
                else:
                    self.passenger_seats_count = passenger_seats_count
            except ValueError:
                raise TypeError(f"Значение {passenger_seats_count} не является целым числом")

    class SpecMachine(CarBase):
        def __init__(self, brand, photo_file_name, carrying, extra):
            super().__init__(brand, photo_file_name, carrying)
            self.car_type = 'spec_machine'
            if isinstance(carrying, str):
                self.extra = extra
            else:
                raise TypeError(f"Значение {extra} не является строкой")

except Exception as exp:
    print('Произошла какая-то ошибка')

def get_car_list(csv_filename):
    lst = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
        for elem in reader:
            if elem['car_type'] == 'car':
                if elem['brand'] != '' and elem['passenger_seats_count'] != '' \
                        and elem['photo_file_name'] != '' and elem['carrying'] != '':
                    lst.append(Car(elem['brand'], elem['photo_file_name'],
                                   elem['carrying'], elem['passenger_seats_count']))
            elif elem['car_type'] == 'truck':
                if elem['brand'] != '' and elem['body_whl'] != '' \
                        and elem['photo_file_name'] != '' and elem['carrying'] != '':
                    lst.append(Truck(elem['brand'], elem['photo_file_name'],
                                     elem['carrying'], elem['body_whl']))
            elif elem['car_type'] == 'spec_machine':
                if elem['brand'] != '' and elem['extra'] != '' \
                        and elem['photo_file_name'] != '' and elem['carrying'] != '':
                    lst.append(SpecMachine(elem['brand'], elem['photo_file_name'],
                                           elem['carrying'], elem['extra']))
    return lst






        
        
            
        


    
