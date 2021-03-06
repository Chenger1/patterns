import copy


class Document:
    def __init__(self, name, doc_format):
        self.name = name 
        self.format = doc_format


class Prototype:
    def __init__(self):
        self._objects = {}

    def add_obj(self, name, obj):
        self._objects[name] = obj

    def remove_obj(self, name):
        del self._objects[name]

    def clone(self, name):
        new_object = copy.deepcopy(self._objects[name])
        return new_object


if __name__ == '__main__':
    doc1 = Document('File1', 'docx')
    doc2 = Document('File2', 'txt')
    prototype = Prototype()
    prototype.add_obj('File1', doc1)
    prototype.add_obj('File2', doc2)

    new_obj = prototype.clone('File1')
    prototype.remove_obj('File2')
    print(type(new_obj))
    
    new_obj.name = 'New file'
    print(f'New: {new_obj.name}. Old: {doc1.name}')
    print(f'Old id - {id(doc1)} ---- New id - {id(new_obj)}')

