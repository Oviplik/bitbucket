from faker import Faker
import random

fake = Faker(locale="ru_RU")

# file = open('data.txt','w',encoding='utf-8')
# for i in range(1,98):
#     file.write(f"requisites{i}=Requisites.objects.create(type_paid='{random.choice(['карта', 'платежный счет'])}', type_card_account='{random.choice(['Банковский','Кредитный'])}', fio='{fake.name()}', phone='{fake.numerify(text='+7%%%%%%%%%%')}', limit='{random.randint(0, 1000)}')\n")
# file.close()

file = open('data.txt','w',encoding='utf-8')
for i in range(1,5000):
    file.write(f"order{i}=Order.objects.create(summa='{random.randint(100, 5000)}', status='{random.choice(['Ожидает оплаты', 'Оплачена', 'Отменена'])}')\norder{str(i)}.requisite.add(requisites{random.randint(1, 100)})\n\n")
file.close()
