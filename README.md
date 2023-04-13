# ChatGPT-Discord-Bot-Custom-Role
Простой чат-бот на основе ChatGPT для Discord с кастомной системной ролью.

# Установка
## Пакеты и репозиторий
- Установка необходимых пакетов
<pre>pip install -r requirements.txt</pre>
- Клонирование репозитория
<pre>git clone https://github.com/klimsat/ChatGPT-Discord-Bot-Custom-Role
cd ChatGPT-Discord-Bot-Custom-Role</pre>

## Шаг 1. Создание Discord бота
1. Перейти на https://discord.com/developers/applications и создать новое приложение

   ![Screenshot_28](https://user-images.githubusercontent.com/25348662/231749979-83d8abe1-b7ad-4022-8031-5ce32dd40b3b.png)

2. Перейти на вкладку **Bot** и создать нового бота
3. Скопировать токен бота

   ![Screenshot_29](https://user-images.githubusercontent.com/25348662/231752961-f44735bf-e667-4964-a134-e69cd9f438a2.png)
4. Вставить полученный токен в файл **main.py** в поле `TOKEN`, заменив текст `DISCORD-TOKEN` токеном вашего бота

   ![Screenshot_31](https://user-images.githubusercontent.com/25348662/231754526-33ef64b1-7e84-44fa-8a3d-23b511d5ffb1.png)

5. Включить MESSAGE CONTENT INTENT и сохранить изменения

   ![Screenshot_30](https://user-images.githubusercontent.com/25348662/231755259-fe37aad9-26e2-4577-9997-2868666a1698.png)

## Шаг 2. Получить OpenAI API токен
### Генерация OpenAI API токена
1. Необходимо зарегистрироваться на платформе https://platform.openai.com
2. Перейти на https://beta.openai.com/account/api-keys
3. Создать новый токен

   ![Screenshot_33](https://user-images.githubusercontent.com/25348662/231757544-9a1ec710-35ab-49fe-b24a-da6f9c2834a0.png)

4. Вставить полученный токен в файл **main.py** в поле `openai.api_key`, заменив текст `OPENAI-TOKEN` OpenAI токеном

   ![Screenshot_32](https://user-images.githubusercontent.com/25348662/231757923-acc42956-c8fd-48d9-bee3-e17ae1a5bb4f.png)


## Запуск
<pre>python main.py</pre>
