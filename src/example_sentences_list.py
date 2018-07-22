import yaml

from models import ExampleSentence


def load_tatoeba_example_sentences_file(fpath):
  """
  Load data from Tatoeba example sentences YAML file.

  This file is generated by this GitHub project: https://github.com/kerrickstaley/tatoeba_rank

  :param str fpath: path to file
  :return list[ExampleSentence]:
  """
  rv = []

  with open(fpath) as f:
    data = yaml.load(f)
    for item in data:
      rv.append(ExampleSentence(trad=item['trad'], simp=item['simp'], pinyin=item['pinyin'], eng=item['eng']))

  return rv


class ExampleSentenceList:
  @classmethod
  def load(cls):
    return cls(load_tatoeba_example_sentences_file('reference_files/tatoeba_sentences.yaml'))

  def __init__(self, sents):
    self.sents = sents
    self.trad_to_sents = {}
    self.simp_to_sents = {}
    for sent in self.sents:
      if sent.trad:
        self._add_sent_to_dict(sent, sent.trad, self.trad_to_sents)
      if sent.simp:
        self._add_sent_to_dict(sent, sent.simp, self.simp_to_sents)

  @staticmethod
  def _add_sent_to_dict(sent, chars, dict_):
    """
    :param ExampleSentence sent:
    :param str chars: Either sent.trad or sent.simp.
    :param dict dict_:
    """
    max_word_length = 4
    processed_words = {''}
    for start in range(len(chars)):
      for end in range(start + 1, start + 1 + max_word_length):
        word = chars[start:end]
        if word in processed_words:
          continue
        processed_words.add(word)
        dict_.setdefault(word, [])
        dict_[word].append(sent)

