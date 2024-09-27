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
