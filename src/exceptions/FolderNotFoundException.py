class FolderNotFoundException(Exception):
    '''Wrapper function for when a folder does not exist.'''
    def __init__(self, *args):
        super().__init__(*args)