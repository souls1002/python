class pointofsale:

    def __init__(self, a=0, r=0,recieve=0,change=0,temp=0):

        print("\n\nWELCOME TO ENRHIC'S KARENDERYA\n")

        self.a = a
        self.r = r
        self.receive = recieve
        self.change = change
        self.temp = temp

    def foods(self):

        print("ENRHIC'S KARENDERYA")

        print("1.Adobo-30", "\n2.Nilaga-35", "\n3.Pork Chop-50", "\n4.Dinuguan-40","\n5.Cash Out", "\n6.Exit")

        while (1):

            c = int(input("Choose:\n"))

            if (c == 1):

                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 30 * d

            elif (c == 2):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 35 * d

            elif (c == 3):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 50 * d

            elif (c == 4):
                d = int(input("Enter the quantity:\n"))
                self.r = self.r + 40 * d

            elif (c == 5):
                print("total:", self.r)
                if (self.r > 0):
                    recieve = int(input("Input Money Recieve:\n"))
                    print("Change:",recieve - self.r)
                    print("THANK YOU FOR EATING")
                    quit()
            elif (c == 6):
                quit()
            else:
                print("Invalid option")





def main():
    a = pointofsale()

    while (1):

            a.foods()





main()
