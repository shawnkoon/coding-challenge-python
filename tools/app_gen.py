import click
import os


@click.command()
@click.argument('folder_name')
@click.argument('class_name')
@click.option('--typed', '-t', is_flag=True)
def generate(folder_name, class_name, typed):
    path = generate_folder(folder_name)
    click.echo('\n>>> Created folder at {}'.format(path))
    generate_app_file(path, class_name, typed)
    click.echo('>>> Created app file.')
    generate_test_file(path, class_name)
    click.echo('>>> Created test file.\n')


def generate_folder(folder_name: str) -> str:
    path = '../src/algorithms/{}'.format(folder_name)
    os.mkdir(path)
    with open(f'{path}/__init__.py', 'w+') as f:
        f.write('')
    return path


def generate_app_file(path: str, class_name: str, typed: bool) -> None:
    with open(f'{path}/app.py', 'w+') as f:
        if typed:
            f.write('from typing import List\n'
                    '\n'
                    '\n'
                    '')
        f.write('class {class_name}:\n'
                '    \"\"\"\n'
                '    Source : <URL>\n'
                '\n'
                '    <Description>\n'
                '    \"\"\"\n'
                '\n'
                '    def function(self):\n'
                '        pass\n'
                ''.format(class_name=class_name))


def generate_test_file(path: str, class_name: str) -> None:
    with open(f'{path}/test_app.py', 'w+') as f:
        f.write('import unittest\n'
                'from .app import {class_name}\n'
                '\n'
                '\n'
                'class {class_name}Test(unittest.TestCase):\n'
                '    def setUp(self):\n'
                '        self.tester = {class_name}()\n'
                '\n'
                '    def test_case_1(self):\n'
                '        pass\n'
                ''.format(class_name=class_name))


if __name__ == '__main__':
    generate()
