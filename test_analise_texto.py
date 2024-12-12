import unittest
from analise_texto import contador_de_palavras, contador_de_caracteres, contador_linha

class TestTextAnalyzer(unittest.TestCase):
  def teste_contador_de_palavras(self):
    text = "Um exemplo de texto."
    self.assertEqual(contador_de_palavras(text), 4)

  def teste_contador_de_caracteres(self):
    text = "Outro exemplo."
    self.assertEqual(contador_de_caracteres(text), 14)

  def teste_contador_linha(self):
    text = "Linha 1\nLinha 2\nLinha 3"
    self.assertEqual(contador_linha(text), 3)

if __name__ == "__main__":
  unittest.main()
  