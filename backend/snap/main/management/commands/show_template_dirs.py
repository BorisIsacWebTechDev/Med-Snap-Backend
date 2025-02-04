from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Shows the directories where Django searches for templates'

    def handle(self, *args, **kwargs):
        # Получаем настройки шаблонов
        template_settings = settings.TEMPLATES[0]

        # Печатаем директории, в которых Django ищет шаблоны
        if template_settings.get('DIRS'):
            self.stdout.write("Django будет искать шаблоны в этих директориях (DIRS):")
            for dir_path in template_settings['DIRS']:
                self.stdout.write(f"- {dir_path}")
        else:
            self.stdout.write("Django не использует дополнительные директории для поиска шаблонов (DIRS пуст).")

        # Проверка, включен ли APP_DIRS
        if template_settings.get('APP_DIRS', False):
            self.stdout.write("\nDjango также будет искать шаблоны в директориях 'templates' каждого установленного приложения.")
        else:
            self.stdout.write("\nDjango не будет искать шаблоны в директориях 'templates' приложений (APP_DIRS = False).")
