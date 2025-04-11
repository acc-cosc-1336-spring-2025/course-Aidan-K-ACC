import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        dictionary= {}
        add_inventory(dictionary, 'Widget1', 10)
        self.assertEquals(dictionary, {'Widget1':10})
        add_inventory(dictionary, 'Widget1', 25)
        self.assertEquals(dictionary, {'Widget1':35})
        add_inventory(dictionary, 'Widget1', -10)
        self.assertEquals(dictionary, {'Widget1':25})
    
    def test_remove_inventory_widget(self):
        dictionary= {'Widget1':1,'Widget2':2}
        remove_inventory_widget(dictionary, 'Widget1')
        self.assertEquals(len(dictionary)==1, True)
        self.assertEquals('Widget2' in dictionary.keys(), True)
    