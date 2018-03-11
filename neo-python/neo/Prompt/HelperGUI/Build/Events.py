import hashlib
import json

from Config import ConfigOS, Memory

def save_to_memory(self):
    with open(Memory, 'r') as json_file:
        memory = json.load(json_file)
        memory['lines'] = self.line_buffers
        memory['document'] = self.document_window.document_line.toPlainText()
    with open(Memory, 'w') as json_file:
        json.dump(memory, json_file)
    print('gui> The commands and the document have been saved.')

def open_cryptography_workbench(self):
    if self.gui_on:
        self.document_window.show()
        self.document_window.raise_()

def hash_document(self):
    encoded_document = self.document_line.toPlainText().encode('utf-8')

    algorithm = self.hashAlgorithmBox.currentText()

    if algorithm==' sha256 ':
        document_hash = hashlib.sha256(encoded_document)
    elif algorithm==' sha512 ':
        document_hash = hashlib.sha512(encoded_document)
    else:
        document_hash = ''

    self.hash_line.setText(document_hash.hexdigest())
