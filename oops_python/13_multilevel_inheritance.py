class Musical_instruments:
    number_of_major_keys=12
class StringInstruments(Musical_instruments):
    type_of_wood="Major Wood"

class Guitar(StringInstruments):
    def __init__(self):
         self.number_of_strings=6
         print(f"The guitar consists of {self.number_of_major_keys} keys and made of woodtype {self.type_of_wood} and has {self.number_of_strings} of strings")

guitar=Guitar()
