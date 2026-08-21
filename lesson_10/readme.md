# ДЗ №10 — Allure в проекте PageObject

Автотесты из домашнего задания №7 (паттерн PageObject)
с подключённой отчётностью Allure:

- калькулятор с задержкой (Google Chrome);
- интернет-магазин Saucedemo (Firefox).

## Установка

```bash
pip install selenium pytest allure-pytest
scoop install allure
```

`scoop install allure` ставит утилиту Allure Report —
без неё терминал не распознает команду `allure`.

## Запуск тестов и формирование отчёта

```bash
pytest tests --alluredir allure-result
```

В папке `allure-result` появятся результаты прогона тестов.

## Просмотр отчёта

```bash
allure serve allure-result
```

Команда соберёт HTML-отчёт и откроет его на локальном сервере
в браузере. Альтернатива — сохранить отчёт в папку и открыть файл:

```bash
allure generate allure-result -o allure-report
allure open allure-report
```
