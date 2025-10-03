import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_pass(self):
        pass

    def test_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_retourne_monnaie_apres_une_piece(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        pieces = coinBox.retourne_monnaie()
        # Après une seule pièce, on doit récupérer exactement 1 pièce
        self.assertEqual(pieces, 1)
        self.assertEqual(coinBox.get_monnaie_courante(), 0)
        self.assertEqual(coinBox.get_vente_permise(), False)

    def test_permet_une_double_vente(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        coinBox.vente()
        self.assertEqual(coinBox.get_vente_permise(), True)

        # Après retour, la boîte doit être vide
        self.assertEqual(coinBox.get_monnaie_courante(), 0)
        self.assertEqual(coinBox.get_vente_permise(), False)
