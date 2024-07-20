<p align="center">
  <img width="100" height="100" src="https://yt3.googleusercontent.com/EZoeNy2GvU7ITiH2-SMTjlsKC_CdPv0j35bv1mCiI113ITBf2axxdZBvHVrOMPHfD6OJ469jrA=s900-c-k-c0x00ffffff-no-rj">
  <h1 align="center">🎧 Яндекс Музыка — Discord RPC</h1>
</p>

# 🤓 Получение API токена

Есть несколько вариантов получения API токена Яндекс Музыки

## Колхозским путем (нужен установленный клиент на компьютере):

- Качаем [Process Hacker](https://processhacker.sourceforge.io/)
- Ищем процесс Яндекс Музыки (В UWP Версии он называется ``Y.Music.exe``)
- ПКМ по процессу/Properties/Memory/Strings/OK
![Пример](https://i.imgur.com/idMDzas.png)
- В открывшимся окне нажимаем Filter/Contains, и вводим ``y0_AgAAAA``
![Пример](https://i.imgur.com/GWidvYh.png)
- Копируем первую найденную строку. Это и есть наш API ключ
![Пример](https://i.imgur.com/7kvXISq.png)

## Ещё более колхозский путь
- Способ описан [тут](https://github.com/MarshalX/yandex-music-api/discussions/513#discussioncomment-2729781)

# 🧠 Использование скрипта

- Качаем все содержимое репозитория, и открываем это папку с только что скачанными файлами в командной строке.
Поочередно вводим:
```
pip install -r requirements.txt
python main.py
```


- При первоначальном запуске скрипта, в директории где лежит скрипт будет создан файл **access_token**
Копируем туда наш API ключ, и перезапускаем.
```
python main.py
```

- Смотрим на наш профиль и видим:

![Результат](https://i.imgur.com/bjz9PED.png)
