## Слияние веток

### 1. Как получить ветку с сервера

1. После того, как друг создал ветку, проверить изменения во всех ветках командой ```git fetch```.
2. Переключиться в удаленную (remote) ветку друга, чтобы создать ее локально командой  ```git checkout <branch-name>```.
3. Просмотреть все ветки командой ```git branch --all```, ветка друга должна быть зеленой.

### 2. Как слиять одну ветку с другой

1. Переключиться в основную ветку командой ```git checkout main```.
2. Обьединить ветку друга с основной веткой командой ```git merge <branch-name>```.
3. Отправить изменения на сервер командой ```git push```.

### 3. После слияния веток

Посмотреть историю репозиория с помощью команды ```git log```.