# ProjectsHandler

ProjectsHandler - Это ваш помощник в управлении проектами

Он позволит:
- Создавать проекты
- Хранить метаданные о проекте 
- Управлять TODO-списками, документациями (WIP)
- Управлять множеством проектов (WIP)

## Установка
1. Установите Python 3.12 и выше
    - Для Linux: `sudo apt install python3`
    - Для Windows 10/11: [Python 3.12](https://www.python.org/downloads/release/python-3120/) (не забудьте добавить в PATH!)

2. Обновите pip (опционально)
    - `python -m pip install --upgrade pip`
    - или `pip install --upgrade pip`

3. Установите пакет
    ```bash
    pip install git+https://github.com/wandderq/ProjectsHandler.git
    ```

4. Готово! Проверьте установку:
    ```bash
    projectshandler --help
    ```

## Использование
```
usage: projectshandler [-h] [-v] {init,info} ...

Handler, Helper, Manager for all your's awesome projects

positional arguments:
  {init,info}    Handle commands
    init         Initialize new project
    info         Get project info

options:
  -h, --help     show this help message and exit
  -v, --verbose  Verbose mode
```

## Лицензия
Данный проект использует [лицензию MIT](LICENSE)