from document_managment.category import Category
from document_managment.document import Document
from document_managment.topic import Topic


class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def find_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_category_by_id(category_id)
        if category:
            category.owner = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_topic_by_id(topic_id)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def find_topic_by_id(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_document_by_id(document_id)
        if document:
            document.file_name = new_file_name

    def find_document_by_id(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document
        return

    def delete_category(self, category_id: int):
        category = self.find_category_by_id(category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_topic_by_id(topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.find_document_by_id(document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id: int):
        return self.find_document_by_id(document_id)

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += str(doc) + '\n'
        return result.strip('\n')