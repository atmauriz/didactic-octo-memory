class NoTestFolderExeption(FileNotFoundError):
    """
    Custom exception
    """
    def __init__(self):
        super().__init__("No 'test' or 'tests' folder found")
