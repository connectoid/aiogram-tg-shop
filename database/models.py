from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    categories = relationship('Category', backref='menu', lazy=True) 
    
    def __repr__(self):
        return self.title


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
    meals = relationship('Meal', backref='category', lazy=True)

    def __repr__(self):
        return self.title


class Meal(Base):
    __tablename__ = 'meal'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    composition = Column(String(200), nullable=True)
    weight = Column(Integer)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return self.title


engine = create_engine('postgresql://postgres:postgres@localhost:5432/tgshop', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(Menu(title='Японское меню'))
session.add(Menu(title='Европейское меню'))
session.add(Category(title='Гункан', menu_id=1))
session.add(Category(title='Роллы', menu_id=2))
session.add(Meal(title='Спайс магуро', composition='Тунец, соус', weight=25, price=50, category_id=1))
session.add(Meal(title='Авокадо куриму', composition='Угорь, авокадо', weight=20, price=55, category_id=2))
session.commit()