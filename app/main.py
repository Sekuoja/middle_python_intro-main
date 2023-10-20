"""Генератор приветствий."""
import pprint

def Greeting(name: str) -> str:
      """Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Returns:
          int: Текст приветствия
      """
      # pprint.pprint(name.lower())
      return f'Привет, {name.title()}'
