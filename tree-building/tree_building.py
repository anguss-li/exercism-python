from typing import List
from unittest.case import expectedFailure


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records: List[Record]) -> List[Node]:
    if not records:
        return None

    records.sort(key=lambda r: r.record_id)

    if not all(r.record_id == i for i, r in enumerate(records)):
        raise ValueError('Record IDs must be unique and continuous starting from 0')
    if not all(r.parent_id == 0 or 0 <= r.parent_id < r.record_id for r in records):
        raise ValueError('Parent ID must be 0 or lower than child id')

    tree = [Node(0)]
    for r in records[1:]:
        tree.append(Node(r.record_id))
        tree[r.parent_id].children.append(tree[-1])

    return tree[0]
