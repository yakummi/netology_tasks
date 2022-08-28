from application.salary import calculate_salary
from application.db.people import get_employees
from application.date import get_time
from application.colorama_text import cm

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(get_time())
    print(cm())