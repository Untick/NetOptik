Программа проекта стажировки "Система определения параметров очков по номенклатуре. НетОптик":

1. Парсинг сайта с очками https://www.netoptik.ru/yandexmarket.yml.
   Задача стажера: написать скрипт, который будет автоматически получать изображения очков и информацию о предложении из оффера. Данные должны быть структурированными и готовыми к дальнейшей обработке и анализу. (Из офферов получаем изображения очков и таблицу информации о оффере.)

2. Создание модели нейросети для распознавания очков по материалу.
   Задача стажера: разработка модели нейросети, которая сможет классифицировать очки по материалам - комбинированные, металл, пластик. Получение необходимых данных с сайта и их размещение в соответствующих директориях для последующего обучения модели. (По заданным категориям качаем с сайта изображения и размещаем по 3 папкам, потом запускаем модель.)

3. Создание модели нейросети для распознавания очков по виду дужек.
   Задача стажера: разработка модели нейросети, способной классифицировать очки по видам дужек - ободковые, безободковые, леска. Получение изображений с сайта и распределение по требуемым категориям для дальнейшего обучения модели.
(По заданным категориям качаем с сайта изображения и размещаем по 3 папкам, потом запускаем модель.)

4. Модель нейросети по распознаванию атрибутов очков с дужки:
    Задача стажера: создание модели, которая будет распознавать символы кода с дужки очков и сопоставлять эти коды с записями в таблице атрибутов для определения модели очков. В качестве данных используются предоставленные Заказчиком фотографии символьного кода на дужках и таблица атрибутов к ним.

Все разработанные модели должны обладать высоким качеством предсказаний, проходить тестирование и валидацию. 
