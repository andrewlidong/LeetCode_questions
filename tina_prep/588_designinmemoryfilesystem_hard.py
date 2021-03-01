def Trie(): return collections.defaultdict(Trie)


class FileSystem:

    def __init__(self):
        self.fs = Trie()
        self.fileinfo = collections.defaultdict(str)

    def ls(self, path: str) -> List[str]:
        # if the path is in the file path, return the path
        if path in self.fileinfo:
            return path.split('/')[-1:]

        # set current to be the Trie
        cur = self.fs
        for token in path.split('/'):
            if token in cur:
                cur = cur[token]
            elif token:
                return []

        return sorted(cur.keys())

    def mkdir(self, path: str) -> None:
        cur = self.fs
        for token in path.split('/'):
            if token:
                cur = cur[token]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.fileinfo[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.fileinfo[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# Function inputs and outputs

# ls | input: string of the path -> output: if it is a file path, return a list that only contains this file's name.  If it is a directory path, return the list of file and directory names in this directory.  Output should be in lexicographic order.

# mkdir | input: string of the path -> output: given a diretory path does not exist, make a new directory according to the path.  If the middle directories don't exist either, create them. Return None.

# addContentToFile | input: string of file path and file content -> output: if the file doesn't exist, create that file containing given content.  If it already exists, append given content to original content.  Return None.

# returnContentFromFile | input: string of file path -> output: content in string format

# Notes

# Assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just '/'
# Assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
# Assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory

# Solution

# Keep two structures, self.fs being a Trie, and self.fileinfo being a dictionary mapping filepaths to the string content in their files.  For convenience, use a nested defaultdict strcture instead of a proper Trie object.  This means we should exercise caution as our call to TrieNode.__getitem__(child) has potential side effects if child is not in the node, but otherwise our code is very similar.
