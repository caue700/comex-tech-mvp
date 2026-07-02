import unittest

import pandas as pd

from src.calculations import calcular_cif_dataframe_estimado, calcular_cif_estimado


class TestCalculations(unittest.TestCase):

    def test_calcular_cif_estimado(self):
        """Valida a soma simples estimada do CIF (FOB + Frete + Seguro)."""
        self.assertEqual(calcular_cif_estimado(100.0, 20.0, 5.0), 125.0)
        self.assertEqual(calcular_cif_estimado(0.0, 0.0, 0.0), 0.0)
        self.assertEqual(calcular_cif_estimado(50000.5, 4500.25, 350.1), 54850.85)

    def test_calcular_cif_dataframe_estimado(self):
        """Valida se a coluna 'valor_cif_usd_estimado' é injetada corretamente no DataFrame."""
        df = pd.DataFrame(
            {
                "valor_fob_usd_estimado": [100.0, 200.0],
                "frete_usd_estimado": [10.0, 20.0],
                "seguro_usd_estimado": [5.0, 10.0],
            }
        )
        df_resultado = calcular_cif_dataframe_estimado(df)
        self.assertIn("valor_cif_usd_estimado", df_resultado.columns)
        self.assertEqual(df_resultado["valor_cif_usd_estimado"].iloc[0], 115.0)
        self.assertEqual(df_resultado["valor_cif_usd_estimado"].iloc[1], 230.0)


if __name__ == "__main__":
    unittest.main()
