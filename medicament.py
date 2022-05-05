import pandas as pd


class Medicament:
    def __init__(self, nume, afectiuni, cod_producator, producator, administrare, reactii, substante, pret):
        self.nume = nume
        self.afectiuni_medicale = afectiuni
        self.cod_producator = cod_producator
        self.producator = producator
        self.administrare = administrare
        self.substante_active = self.substante_active_(substante)
        self.reactii_adverse = reactii
        self.pret = pret

    def substante_active_(self, substante) -> str:
        """Contruirea unui sablon de afisare pentru substantele active impreuna cu gramajul lor
        :params substante: substante active
        :type substante: list
        :returns: dataframe pentru a creea tabel
        """
        total = ''
        for s in substante:
            total += s[0] + '(' + s[1]['gramaj'] + ') '
        return total

    @staticmethod
    def meds_to_df(meds_lst) -> pd.DataFrame:
        """
        :params meds_lst: medicamente
        :type meds_lst: list
        :returns: dataframe pentru a creea tabel
        """
        return pd.DataFrame([m.__dict__ for m in meds_lst])

    def __str__(self):
        return self.nume
