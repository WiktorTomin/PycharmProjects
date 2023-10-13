"""
Задание 1.

Условие:
Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt
 строку вида: время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора
  из файла /proc/loadavg (можно писать просто всё содержимое этого файла).
"""
import time


class StatFixture:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.stat_file_path = "stat.txt"

    def _get_file_stats(self):
        return 10, 1024

    def _get_cpu_load_stats(self):

        with open("/proc/loadavg", "r") as file:
            cpu_load_stats = file.read()
        return cpu_load_stats

    def after_step(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        files_count, file_size = self._get_file_stats()
        cpu_load_stats = self._get_cpu_load_stats()

        with open(self.stat_file_path, "a") as file:
            file.write(f"{timestamp}, {files_count}, {file_size}, {cpu_load_stats}\n")


# Пример использования фикстуры после каждого шага теста
stat_fixture = StatFixture("config.txt")
stat_fixture.after_step()
