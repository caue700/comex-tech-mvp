import unittest

from src.utils import formatar_moeda_brl, formatar_moeda_usd


class TestUtils(unittest.TestCase):

    def test_formatar_moeda_usd(self):
        """Valida a formatação de moedas estrangeiras no padrão brasileiro (USD)."""
        self.assertEqual(formatar_moeda_usd(1000.5), "US$ 1.000,50")
        self.assertEqual(formatar_moeda_usd(0.0), "US$ 0,00")
        self.assertEqual(formatar_moeda_usd(1234567.89), "US$ 1.234.567,89")
        self.assertEqual(formatar_moeda_usd(0.056), "US$ 0,06")  # Teste de arredondamento

    def test_formatar_moeda_brl(self):
        """Valida a formatação de moedas brasileiras no padrão brasileiro (BRL)."""
        self.assertEqual(formatar_moeda_brl(1000.5), "R$ 1.000,50")
        self.assertEqual(formatar_moeda_brl(0.0), "R$ 0,00")
        self.assertEqual(formatar_moeda_brl(1234567.89), "R$ 1.234.567,89")
        self.assertEqual(formatar_moeda_brl(0.056), "R$ 0,06")  # Teste de arredondamento


if __name__ == "__main__":
    unittest.main()
