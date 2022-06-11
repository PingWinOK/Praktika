# Задача:
# написать класс vulnerability в котором можно будет:
# 1)Создать уязвимость
# 2)Создать описание уязвимости (при инициализации)
# 3)Сравнивать уязвимости
# 4)Повысить или понизить ранг уязвимости
class vulnerability:
    #Конструктор
    def __init__(self, name , description, rank):
        self.name = name
        self.description = description
        self.rank = rank

    #Вывод информации по объекту
    def stats(self):
        print("Название: " + self.name + "\n" + "Описание: " + self.description + "\n" + "Ранг: " + str(self.rank))

    #Редактирование объекта
    def edit_description(self,new_description):
        self.description = new_description

    def edit_rank(self,new_rank):
        self.rank = new_rank

    def edit_name(self,new_name):
        self.name = new_name

    #Понижение и понижение уязвимости
    def Up(self):
        self.rank += 1
    def Down(self):
        self.rank -= 1

    #Сравнение уязвимостей
    @staticmethod
    def comparison(rank1, rank2):
        if(rank1 < rank2):
            print("Эта уязвимость страшнее")
        else:
            print("Эта уязвимость страшна немного меньше")



Yiazvimost1 = vulnerability("Уязвимость очень опасная","Делает очень плохо файлам",1)
Yiazvimost2 = vulnerability("Уязвимость не очень опасная","Выводит смешную картинку на экран",5)
Yiazvimost1.stats()
Yiazvimost2.stats()
Yiazvimost1.edit_description("Делает файлам более-менее")
Yiazvimost1.stats()
Yiazvimost1.comparison(Yiazvimost1.rank,Yiazvimost2.rank)
Yiazvimost2.Down()
Yiazvimost2.stats()