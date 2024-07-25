from typing import List

class FileSystemComponent:
    def __init__(self, name: str):
        self.name = name

    def show_details(self):
        raise NotImplementedError("Subclasses must implement this method")


class File(FileSystemComponent):
    def show_details(self):
        print(f"File: {self.name}")


class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.show_details()


# Exemplo de uso
file1 = File("file1.txt")
file2 = File("file2.txt")
dir1 = Directory("dir1")
dir2 = Directory("dir2")

dir1.add(file1)
dir2.add(dir1)
dir2.add(file2)

dir2.show_details()
