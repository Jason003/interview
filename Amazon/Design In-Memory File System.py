class Trie:
    def __init__(self):
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = Trie()
        self.content = {}

    def ls(self, path: str) -> List[str]:
        if path in self.content: return [path.split('/')[-1]]
        if path == '/': return sorted(list(self.root.children.keys()))
        curr = self.root
        for s in path.split('/')[1:]:
            if s not in curr.children: return []
            curr = curr.children[s]
        return sorted(list(curr.children.keys()))

    def mkdir(self, path: str) -> None:
        if path == '/': return
        curr = self.root
        for s in path.split('/')[1:]:
            if s not in curr.children:
                curr.children[s] = Trie()
            curr = curr.children[s]

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath == '/': return
        curr = self.root
        for s in filePath.split('/')[1:]:
            if s not in curr.children:
                curr.children[s] = Trie()
            curr = curr.children[s]
        if filePath not in self.content:
            self.content[filePath] = content
        else:
            self.content[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.content[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)