git clone https://github.com/Alb1ngid/Ftest.git
cd Ftest

git remote remove origin
git remote add origin https://github.comhttps://github.com/Alb1ngid/oop46/.git
git push -u origin master



git checkout -b new-feature
python -m venv venv
venv\Scripts\activate
pip install -r reg.txt
pip freeze > requirements.txt
git rm reg.txt
git add requirements.txt
git commit -m "Создан requirements.txt, удалён reg.txt"
git push -u origin new-feature
