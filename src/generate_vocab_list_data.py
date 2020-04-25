"""
Generate a .py file that defines a VocabList instance containing all the words.

This is faster than loading the words from a YAML file because the Python parser is faster than the
YAML parser, plus you don't have to convert from basic Python types into VocabWord instances.
"""
from chinesevocablist import VocabList

vocab_list = VocabList.load_from_yaml_file('chinese_vocab_list.yaml')

print('from chinesevocablist import VocabList, VocabWord, ExampleSentence, Classifier')
print('vocab_list = {}'.format(repr(vocab_list)))
