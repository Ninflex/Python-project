from memory_profiler import profile

class Medkit:
    def __init__(self):
        #items is an empty dictionary
        self.items = {}
 
    def add(self, item, code):
        #Adding to the medkit function passing a key (item) and value (code)
        #Iterates through items in the dict and adds item else adds item anyways 
        if item in self.items:
            self.items[item] = code
        else:
            self.items[item] = code
 
    def display(self):
        #Prints Key and Value pair by iterating through the dict
        print("\n-----Your medkit-----")
        for item, code in self.items.items():
            print(f"{item}: with a unique code: {code}")
        print("---------------------")

    def compare(self, code):
        # Returns bool value depending on whether there is a code (passed value) equal to value in dict
        for value in self.items.values():
            if code == value:
                return True
        return False

    def remove(self, item):
        #Checks through items and selected item - by Value - is removed from medkit
        if item in self.items:
            del self.items[item]
            print(f"{item} removed from the medkit.")
        else:
            print(f"{item} not found in the medkit.")

class Order:
    def __init__(self):
        #orders is an empty list
        self.orders = []

    def add(self, medkit):
        #adds dictionary (medkit) to the list
        self.orders.append(medkit)

    def display(self):
        #iterates through a numbered version of orders list and prints the items dict value and key pair  
        print("\nOrder List contains:")
        for i, order in enumerate(self.orders, start = 1):
            print(f"-----Order {i}-----")
            for key, value in order.items.items():
                print(f"{key}: unique code {value}")

    def delete(self, order):
        #deletes order via index
        del self.orders[order - 1]

    def modify(self, order):
        #tries to declare order by index if index is valid
        try:
            order = self.orders[order - 1]
        except IndexError:
            print("Invalid order number")
            return

        print("\n----- Modify Order -----")
        order.display()

        while True:
            #Options to select from
            print("\n1. Add Item\n2. Remove Item\n3. Back")
            modifyOption = input("Eneter and option (1-3): ")
            #quantity is made so that a medkit can only have 5 items
            quantity = len(order.items)
            if modifyOption == "1":
                if quantity == 5:
                    #Cant have more than 5 items in a medkit
                    print("Medkit cannot contain more than 5 items!")
                else:
                    #adding items from a list of items 
                    itemList = ["Plasters","Painkillers","Anti-biotic Spray","Bandages","Splint","Iboprofen"]
                    print("\nPlease select an item:")
                    for i, item in enumerate(itemList):
                        print(f"{i}. {item}")
                    choice = input("\nEnter your choice: ")
                    #isdigit() validates if entered choice is a number
                    if choice.isdigit() and int(choice) <= 5 and int(choice) >= 0:
                        selected = itemList[int(choice)]
                        code = int(input("Please enter a unique 4 digit code: "))
                        if len(str(code)) == 4:
                            #checks if code is 4 digits and unique compared with the current medkit
                            if order.compare(code) == False:
                                #added using medkits add method to current medkit in the order list and is displayed with medkits method too
                                order.add(selected,code)
                                order.display()
                                
            elif modifyOption == "2":
                #Inputted value is passed into medkits remove method
                order.display()
                removeOption = input("Enter an item NAME to remove: ")
                order.remove(removeOption)
                order.display()

            elif modifyOption == "3":
                #makes sure that medkit has 5 items before returning to main menu
                if quantity < 5:
                    print("\nMedkit Must contain 5 items!")
                else:
                    break
                    


def main():
    #creates instance of Order class
    order = Order()
    #runs main menu while true and less than 20 orders are made
    while True and len(order.orders) < 20:
        print("----------Main Menu----------")
        print("\n1. Create Medkit\n2. Delete Medkit\n3. Modify Medkit\n4. Exit")
        option = input("\nEnter option (1-4): ")
        if option.isdigit() and int(option) == 4:
            #exits while loop (ends program)
            order.display()
            break
        elif option.isdigit() and int(option) == 1:
            itemList = ["Plasters","Painkillers","Anti-biotic Spray","Bandages","Splint","Iboprofen"]
            # creates instance of medkit inside elif so that new medkit is created everytime option equals 1
            medkit = Medkit()
            while len(medkit.items) < 5:
                print("\nPlease select an item:")
                for i, item in enumerate(itemList):
                    print(f"{i}. {item}")
                choice = input("\nEnter your choice: ")
         
                if choice.isdigit() and int(choice) <= 5 and int(choice) >= 0:
                    selected = itemList[int(choice)]
                    code = int(input("Please enter a unique 4 digit code: "))
                    if len(str(code)) == 4:
                        if medkit.compare(code) == False:
                            medkit.add(selected,code)
                            itemList.pop(int(choice))
                            medkit.display()
                        else:
                            print("\nCan't have the same code for more than one item")
                    else:
                        print("\nDid not enter a code that was 4 digits long")
                else:
                    print("Entered choice is out of range of list")
            print("\nSuccessfuly added 5 items to your medkit!")
            #displays order
            order.add(medkit)
            order.display()

        elif option.isdigit() and int(option) == 2:
            #deletes order via index
            order.display()
            deleteChoice = int(input("\nWhich Order number do you want to delete: "))
            order.delete(deleteChoice)
            print("New Order List:")
            order.display()

        elif option.isdigit() and int(option) == 3:
            #first checks if there is an order that can be modified else uses modify method in Order on the selected order
            if not order.orders:
                print("\nOrder List is Empty!\n")
            else:
                order.display()
                modifyChoice = int(input("\nWhich Order number do you want to modify: "))
                order.modify(modifyChoice)
                order.display()
    
 
#runs main when program starts 
if __name__ == "__main__":
    main()









