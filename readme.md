1. Що таке лінійні трансформації?
Це перетворення простору при якому прямі лінії залишаються прямими

2. Як і в яких галузях застосовуються лінійні трансформації? 
За допомогою лінійних трансформацій можна перетворювати багатовимірні об'єкти в двовимірні об'єкти, 
або в об'єкти з іншими вимірами, що менші за ті, що були спочатку - це зветься Principal Component Analysis
і використовується в роботі з даними де є багато параметрів і їх треба зменшити до ключових,
Також можна змінювати цифрові зображення, як це було виконано в програмі - дзеркалити, обертати та ін.
Також під час навчання штучної нейронної мережі на етапі Forward PAss вхідні дані виглядають як вектори чи матриці, 
а тоді кожен наступний шар нейронної мережі бере Їх та множить на набір ваг і додає зсув(вектор) - що також є лінійними трансформаціями.

3. Що таке матриця лінійної трансформації та як її можна інтерпретувати?
Інтерпретація матриці лінійної трансформації в мому розумінні звучить так:
Коли матриця лінійної трансформації множиться на вектор, застосовуються елементи цієї матриці,
як коефіцієнти до х та у векторів, з суми яких складався початковий вектор.
Тоді відбувається додавання цих значеннь та утворюється новий вектор, що є сумою змінених базисних векторів.
(Для двовимірного простору)


4. Які особливості та властивості має матриця обертання?
Кожен елемент такої матриці міститься в межах від -1 до 1, детермінант дорівнює 1. Визначення матриці обертання, для
обернення фігури на довільний кут (в радіанах) реалізоване в функції rotate в main.py, транспонована матриця обертання дорівнює
оберненій иатриці.

5. Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2
Так, за результатами експериментів, якщо спочатку застосувати одну матрицю трансформації, а потім іншу -
результат двох трансформації не збігається з результатом, якщо це застосувати у зворотньому порядку.
Це через те, що множення матриць не комутативне.

6. Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду?
Для цього потрібно знайти обернену до цієї матриці лінійної трансформації.

Чи завжди можна здійснити обернену трансформацію? 
Це неможливо, якщо матриця трансформації не має до себе оберненої, тобто невироджена.

7. Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)?
За результатми моїх експериментів, простір стискається.

А якщо більше 1?
Простір збільшується.

Дорівнює 1? 
Всі відстані та кути залишаються такими як і до трансформації (приклад - матриці обертання)

Дорівнює 0?
об'ємна фігура проектується у пряму 