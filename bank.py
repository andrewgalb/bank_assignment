"""Man ska till exempel kunna ändra kundens namn samt hämta information
om kunden (personnummer, för- och efternamn samt hämta information
om kundens konton (kontonummer, saldo, kontotyp)).
Dessutom ska man kunna hantera kundens konto(n). Implementera
metoder som säkerställer ovanstående krav i klassen Bank nedan.
(Bank inkluderar förslag på metoder. Komplettera dessa med fler metoder
om det behövs)."""
class Bank:

    customers=[]

    def __init__(self,name):
        self.name=name

    """Läser in text filen och befolkar listan som ska innehålla kunderna."""
    def _load():
        raise NotImplementedError   
    
    """Returnerar bankens alla kunder (personnummer och namn)"""
    def get_customers():
        raise NotImplementedError

    """Skapar en ny kund med namn och personnummer. Kunden skapas endast om det inte
    finns någon kund med personnumret som angetts. Returnerar True om kunden skapades
    annars returneras False."""
    def add_customer(name, pnr):
        raise NotImplementedError

    """Returnerar information om kunden inklusive dennes konton. Första platsen i listan är
    #förslagsvis reserverad för kundens namn och personnummer sedan följer informationen
    #om kundens konton."""
    def get_customer(pnr):
        raise NotImplementedError

    """Byter namn på kund, returnerar True om namnet ändrades annars returnerar det False
    #(om kunden inte fanns)."""
    def change_customer_name(name, pnr):
        raise NotImplementedError

    """Tar bort kund med personnumret som angetts ur banken, alla kundens eventuella konton
    #tas också bort och resultatet returneras. Listan som returneras ska innehålla information
    #om alla konton som togs bort, saldot som kunden får tillbaka."""
    def remove_customer(pnr):
        raise NotImplementedError

    """Skapar ett konto till kunden med personnumret som angetts, returnerar kontonumret som
    #det skapade kontot fick alternativt returneras –1 om inget konto skapades."""
    def add_account(pnr):
        raise NotImplementedError

    """Returnerar Textuell presentation av kontot med kontonummer som tillhör
    #kunden (kontonummer, saldo, kontotyp)."""
    def get_account(pnr, account_id):
        raise NotImplementedError

    """Gör en insättning på kontot, returnerar True om det gick bra annars False."""
    def deposit(pnr, account_id, amount):
        raise NotImplementedError

    """Gör ett uttag på kontot, returnerar True om det gick bra annars False."""
    def withdraw(pnr, account_id, amount):
        raise NotImplementedError

    """Avslutar ett konto. Textuell presentation av kontots saldo ska genereras och
    #returneras."""
    def close_account(pnr, account_id):
        raise NotImplementedError

    """Returnerar alla transaktioner som en kund har gjort med ett specifikt
    konto eller -1 om kontot inte existerar"""
    def get_all_transactions_by_pnr_acc_nr( pnr, acc_nr ):
        raise NotImplementedError

