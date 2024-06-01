"""
Модуль tree_store содержит класс TreeStore для работы с древовидными структурами данных.

Примеры использования:

    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        # ... другие элементы ...
    ]
    tree_store = TreeStore(items)
    all_items = tree_store.get_all()
    item = tree_store.get_item(2)
    children = tree_store.get_children(1)
    parents = tree_store.get_all_parents(3)
"""

from typing import List, Dict, Any


class TreeStore:
    """
    Класс для хранения и работы с древовидными структурами данных.
    """

    def __init__(self, items: List[Dict[str, Any]]):
        """
        Инициализирует объект TreeStore.

        :arg
            items (List[Dict[str, Any]]): Исходный массив объектов с полями 'id' и 'parent'.
        :return
            None
        """
        self.items = items
        # решение в тупую (по памяти не очень)
        self.item_map = {item['id']: item for item in items}
        self.child_map = {item['id']: [] for item in items}
        for item in items:
            if item['parent'] != 'root':
                self.child_map[item['parent']].append(item)

    def getAll(self) -> List[Dict[str, Any]]:
        """
        Метод для получения исходного массива элементов.

        :return
            List[Dict[str, Any]]: Исходный массив объектов.
        """
        return self.items

    def getItem(self, id: int) -> Dict[str, Any]:
        """
        Метод для получения объекта элемента по его ID.

        :arg
            id (int): ID элемента.

        :return
            Dict[str, Any]: Объект элемента, соответствующий ID, или None, если элемента с таким ID нет.
        """
        return self.item_map.get(id)

    def getChildren(self, id: int) -> List[Dict[str, Any]]:
        """
        Возвращает список дочерних элементов для заданного элемента по его ID.

        :arg
            id (int): ID элемента.

        :return
            List[Dict[str, Any]]: Список дочерних элементов, или пустой список, если у элемента нет дочерних.
        """
        return self.child_map.get(id, [])

    def getAllParents(self, id: int) -> List[Dict[str, Any]] or None:
        """
        Возвращает список всех родительских элементов от заданного элемента до корневого.

        :arg
            id (int): ID элемента.

        :return
            List[Dict[str, Any]]: Список родительских элементов, от самого элемента до корня дерева.
        """
        current_item = self.item_map.get(id, None)
        if current_item is None:
            return None
        else:
            parents = [current_item]
        while current_item:
            current_item = self.item_map.get(current_item['parent'])
            if current_item:
                parents.append(current_item)
        return parents[::-1]
