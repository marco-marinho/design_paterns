"""
Single responsibility / separation of concerns.

Log class has a single responsibility, managing its entries. The function to manage its persistence is placed outside
the class, to avoid the god object anti-pattern.
"""


class Log:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        self.count += 1
        self.entries.append(entry)

    def remove_entry(self, index):
        self.count -= 1
        del self.entries[index]

    def __str__(self):
        return "\n".join([f"{idx + 1}: {entry}" for idx, entry in enumerate(self.entries)])


def save_log(log: Log, path: str):
    with open(path, mode='w') as ofile:
        ofile.write(str(log))
