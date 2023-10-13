"""
*Задание 2. *

• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным
 командой crc32.
"""
import os.path

import pytest
import subprocess

def test_list_files():
    output = subprocess.check_output(['./my_program', 'l'])

    assert 'file.text' in output.decode()

def test_exstract_files_with_paths():
    subprocess.call(['./my_program', 'c', '-p', 'path/to/archive', 'file1.txt', 'file2.txt'])

    output = subprocess.check_output(['./my_program', 'x', '-p','path/to/archive'])

    assert os.path.exists('path/to/archive'/'file1.txt')
    assert os.path.exists('path/to/archive'/'file2.txt')

def test_hash_calculation():
    with open('file.txt', 'w') as f:
        f.write('Im student')

    output = subprocess.check_output(['./my_program', 'h', 'file.txt'])

    expected_hash = subprocess.check_output(['crc32', 'file.txt']).decode().rstrip()
    assert output.decode().rstrip() == expected_hash


    if __name__ == '__main__':
            pytest.main
