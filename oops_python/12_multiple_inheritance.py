class Operating_System:
    multitask=True
class Apple:
    website="www.appleinc.com"
class Macbook(Operating_System,Apple):
    def __init__(self):
        if self.multitask==True:
            print("This is a multitasking website" , self.website)
macbook=Macbook()
