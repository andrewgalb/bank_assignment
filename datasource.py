"""DataSource klassen kräver konkreta implementationer. Ett krav är att
implementationen ska använda en textfil som datasource"""
class DataSource:

    """Denna metod implementerar kopplingen till en generisk datasource. Returnerar
    en <class ‘tuple’> med en <class ‘bool’> och en <class ‘str’> t.ex., (True,
    "“Connection successful” [, datasource namn])"""
    def datasource_conn(self):
        raise NotImplementedError

    """Returnerar alla kunder i banken."""
    def get_all(self):
        raise NotImplementedError

        