import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BoykoKulish1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# TODO
# 1) Сделать автоматическую транскрипцию названия категории в латиницу. Убрать поле URL-адреса в форме создания категории
# 2) Добавить стили на формы редактирования, создания новых объектов
# 3) Добавить в вкладку товары (на каждый товар) изображение. Реализовать одиночное хранение файла для каждого товара