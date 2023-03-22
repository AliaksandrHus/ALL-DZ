# 1 Создать Flask приложение для регистрации на мероприятие
# 2 Подключить БД
# 3 Использовать SQLAlchemy

from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
engine = create_engine('sqlite:///party.db')


class Base(DeclarativeBase): pass


class Person(Base):

    __tablename__ = "Person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)


Base.metadata.create_all(bind=engine)


@app.route('/')
def main():
    return render_template('main.htm')


@app.route('/people')
def people():

    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).all()

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        tm = env.get_template('people.htm')
        return tm.render(users=people)


@app.route('/registration', methods=['POST', 'GET'])
def registration():

    if request.method == 'POST':
        if request.form['name'] and request.form['email']:
            with Session(autoflush=False, bind=engine) as db:
                new = Person(name=request.form['name'], email=request.form['email'])
                db.add(new)
                db.commit()

                return render_template('message.htm')

    return render_template('registration.htm')


if __name__ == '__main__':

    with Session(autoflush=False, bind=engine) as db:
        people = db.query(Person).all()

        if not people:

            print('Список пуст - добавляем пользователей.')

            with Session(autoflush=False, bind=engine) as db:
                for pers in [('Петя Шмыг', 'petya@mail.ru'),
                             ('Вася Клык', 'vasa@gmail.com'),
                             ('Даша Март', 'dasha@yandex.ru'),
                             ('Саня Крот', 'sania@mail.ru'),
                             ('Катя Смог', 'kat@gmail.com'),
                             ('Таня Корд', 'tanya@mail.ru')]:

                    x = Person(name=pers[0], email=pers[1])
                    db.add(x)
                    db.commit()

    app.run()
