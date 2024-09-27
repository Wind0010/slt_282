#Question 1 Вопрос 1
git clone https://github.com/Alb1ngid/Ftest.git
cd Ftest

git remote remove origin
git remote add origin https://github.comhttps://github.com/Alb1ngid/oop46/.git
git push -u origin master

#Question 2 Вопрос 2
git checkout -b new-feature
python -m venv venv
venv\Scripts\activate
pip install -r reg.txt
pip freeze > requirements.txt
git rm reg.txt
git add requirements.txt
git commit -m "Создан requirements.txt, удалён reg.txt"
git push -u origin new-feature

#Question 3 Вопрос 3
python "seed_phrase_generator (2).py"
git checkout -b account-creation
git add .
git commit -m "Создание 50 аккаунтов"
git push -u origin account-creation
git checkout master
git pull origin master
git merge account-creation
git push origin main

#Quesiton 3
git checkout -b new-decorator-feature
touch decorator_house.py
git checkout -b new-decorator-feature

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("wassup")
        result = func(*args, **kwargs)
        print("what did u need to be a comfortable.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

git add decorator_house.py
git commit -m "Добавлен декоратор в decorator_house.py"
git push -u origin new-decorator-feature


say_hello("Peace")
