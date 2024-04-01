import math


class PhotoAlbum:
    PAGE_PHOTO_CONTAIN = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.make_pages(pages)

    @staticmethod
    def make_pages(value):
        photos = list()
        for page_number in range(value):
            photos.append(list())
        return photos
    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_count = math.ceil(photos_count / cls.PAGE_PHOTO_CONTAIN)
        album = cls(pages_count)
        return album

    def add_photo(self, label: str):
        for page_number in range(self.pages):
            if len(self.photos[page_number]) < 4:
                self.photos[page_number].append(label)
                return f"{label} photo added successfully on page {page_number + 1} slot {len(self.photos[page_number])}"
        return "No more free slots"
    def display(self):
        result = 11 * '-' + '\n'
        for page in self.photos:
            result += f"{len(page) * '[] '}".strip() + '\n'
            result += 11 * '-' + '\n'
        return result
