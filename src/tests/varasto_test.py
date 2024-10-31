import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varastoneg = Varasto(-10,-2)
        self.varastoalku = Varasto(10,2)
        self.varastotäys = Varasto(10,12)
        self.varasto = Varasto("10")

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        

        self.assertAlmostEqual(self.varasto.saldo, 8)

        #testataan varstoon lisääminen negatiivinen ja kun varasto on melko täynnä
        self.varastoneg.lisaa_varastoon(-1)
        self.varastoalku.lisaa_varastoon(10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

        # testi varastosta otto negatiivinen luku
        self.varastoneg.ota_varastosta(-2)

        # testi ottetaan varastosta yli tilavuuden
        self.varastotäys.ota_varastosta(12)
    
    def test_str_printti(self):
        print(self.varasto)