class apple:
    manufacturer="Apple inc."
    contact_website="www.appleinc.com"
    def contact_details(self):
        print("Please contact us " , self.contact_website)   

class Macbook(apple):
    print("This is a child class of class apple")
    def printdetails(self,name):
        print("This is " , self.name)
macbook=Macbook()
macbook.contact_details()      