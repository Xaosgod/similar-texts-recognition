# Веб-сервис image-text-recognition на базе OCR фреймворка easyocr
## Работа с difflib
### Для использования difflib необходимо: 
- Установить difflib
```
pip install difflib
```
- Нужно привести текст к нижнему регитру
```
normalized1 = text1.lower()
normalized2 = text2.lower()
```
-Запускае функцию сравнения
```
matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
```
## Создание REST API с помощью FastApi
- Устанавливаем необходимые компоненты
```
pip install wheel -U
pip install uvicorn fastapi pydantic 
```
- Создаем основу приложения с расширением .py
```
from fastapi import FastAPI, File, UploadFile
app = FastAPI()
```
- Проверим работу приложение для этого открывает терминал и прописываепм команду:
```
uvicorn <имя_вашего_файла>:app

```
- В браузере открываем страницу по адресу http://127.0.0.1:8000/docs
- Если запуск происходил через вируальную машину, то узнаем связанный через сетевой мост IP для этого прописываем в терминале команду
```
ifconfig

```
- Далее прописываем команду
```
uvicorn <имя_вашего_файла>:app --host <ваше_IP>

```
- Добавляем эндпоинт POST, на входе подается 2 текста
```
@app.post("/similar-recognition")
async def create_upload_files(files: List[UploadFile] = File(...)):

```
- Далее считываем файл и обрабатываем его с помощью difflib и на выходе имеем метрику схожести 2 текстов

```
@app.post("/similar-recognition")
async def create_upload_files(files: List[UploadFile] = File(...)):
  text1 = await files[0].read()
  text2 = await files[1].read()
  normalized1 = text1.lower()
  normalized2 = text2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

```
- Полный код:
```
from fastapi import FastAPI, File, UploadFile
from typing import List
import difflib
app = FastAPI()

@app.post("/similar-recognition")
async def create_upload_files(files: List[UploadFile] = File(...)):
  text1 = await files[0].read()
  text2 = await files[1].read()
  normalized1 = text1.lower()
  normalized2 = text2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()

```

 
