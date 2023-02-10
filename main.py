from application.salary import salary
from application.db.people import people
from datetime import datetime

print("Текущие дата и время:", datetime.today())
if __name__ == '__main__':
    salary()
    people()