Для выполнения программы запустите:

sudo docker-compose up


Затем, в другом терминале:

sudo docker build -t producer ./Producer

sudo docker run -it --network=hw1_network1 producer


Чтобы проверить запись в БД:

sudo docker build -t tester ./Tester

sudo docker run -it --network=hw1_network1 tester


Тестер будет выводить всё, что записывается в БД, в момент добавления.
