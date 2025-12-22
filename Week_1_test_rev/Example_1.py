class Book:
    def __init__(self,title:str,pages:int):
        self.title=title
        self.__pages=pages
    def show_title(self):
        return self.title
    def get_pages(self):
        return self.__pages
book=Book("Wings of fire",210)
print(book.show_title())
print(book.get_pages())
