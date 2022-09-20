import unittest
from unittest.mock import patch
from h1 import documents, directories
from h1 import document_owner, documents_in_shelf, general_docs, add_documents, delete_documents


class TestFunc(unittest.TestCase):
    def test_doc_owner(self):
        with patch('builtins.input', return_value='11-2'):
            assert input() == '11-2'
            result = f'Владелец документа - Геннадий Покемонов'
            self.assertMultiLineEqual(document_owner(documents), result)

        with patch('builtins.input', return_value=''):
            assert input() == ''
            result = f"Документ отсутствует."
            self.assertMultiLineEqual(document_owner(documents), result)

    def test_doc_in_shelf(self):
        with patch('builtins.input', return_value='11-2'):
            assert input() == '11-2'
            result = f"Документ хранится на полке - 1"
            self.assertMultiLineEqual(documents_in_shelf(directories), result)

        with patch('builtins.input', return_value=''):
            assert input() == ''
            result = f"Документ отсутствует."
            self.assertMultiLineEqual(documents_in_shelf(directories), result)

    def test_share_docs(self):
        self.assertIsInstance(general_docs(documents), list)

    def test_add_docs(self):
        with patch('builtins.input', return_value='1'):
            assert input() == '1'
            result = f'Документ уже существует.'
            new_document = {
                'type': 'passport',
                'number': '11-2',
                'name': 'Максим Некрасов'
            }
            self.assertMultiLineEqual(add_documents(documents, directories, new_document), result)

    def test_del_doc(self):
        with patch('builtins.input', return_value='11-2'):
            assert input() == '11-2'
            result = f'Удаление прошло успешно.'
            self.assertMultiLineEqual(delete_documents(documents, directories), result)