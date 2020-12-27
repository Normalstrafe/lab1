###Lab_4: Робота з Docker

2. Перевіряю чи встановлений докер і запускаю перевірку версії, ви виводжу тестовий імедж
    ```bash
    docker -v
    docker -h
    docker run docker/whalesay cowsay Docker is fun
    ```
    перенаправляю вивід цих команд у файл 'my_work.log' та повинен був зробити коміт, але виникли проблеми з віртуальною машиною
3. Як можна бачити Docker працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи Docker дещо схожа на віртуальні машини. Перш за все створила імедж з якого буде запускатись контейнер. Для цього існує Dockerfile який описує контент імеджу.
4. Для знайомства з Docker створюю імедж із Django сайтом зробленим у попередній роботі.
    - Використовую команду щоб завантажити базовий імедж з репозиторію (спочатку цього не зробив, але згодом дійшов до того, що по іншому не працює):
    ```
    docker pull python:3.8-slim
    docker images
    docker inspect python:3.8-slim
    ```
    - Створюю  файл з іменем `Dockerfile` та копіюю туди файл з репозиторію;
    - Редактую dockerfile свої потреби
5. Логінюсь в docker hub [DockerHUB](hhttps://hub.docker.com/repository/docker/normalstrafer/lab4).
6. виконую білд (build) Docker імеджа та завантажую його до репозиторію: 
    ```
    docker build -t normalstrafer/lab4:django .
    docker images
    docker push normalstrafer:test
    ```
    [Image](https://hub.docker.com/layers/normalstrafer/lab4/django/images/sha256-f6d394378dfc87c35e3990b0ef02279b1ac0971f9810f822f9b4771cfbe2f6e6?context=repo)
    
7. Запускаю веб сайт
    ```
    docker run -it --name=django --rm -p 8000:8000 normalstrafer/lab4:django
    ``` 
    - Переконуюсь, що сайт працює;
8. Створюю Dockerfile.site
    ```
        sudo docker build -t normalstrafer:monitoring --file Dockerfile.site . 
        sudo docker images
        sudo docker push normalstrafer:monitoring
   відповідно зміннюю dockerfile.site для моніторингу
    ``` 
   Запускаю обидва імеджі.
   ```bash
        sudo docker run -it --rm -p 8000:8000 normalstrafer/lab4:django
        sudo docker run --net=host --rm -it --volume /home/lab1/lab_4:/app normalstrafer/lab4:monitoring
   ``` 
   В  ході дуже довгого вирішення проблем з запуском одночасно двох імеджів,  використав ще дуже багато команд,
    зокрема "python3 -m venv env", "python3 manage.py migrate", І ще багато інших, які важко згадати(юзав по кілька разів,в різних комбінаціях)
    Найбільші труднощі викликали шляхи, та плутанина з різними версіями Python, також кілька разів не бачило файл manage.py, який був коректним 
    та працював у lab3(можливо вказував неправильний шлях)