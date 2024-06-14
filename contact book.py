book={}
def display_contact():
    print("Name\t\tContact number")
    for key in book:
      print("{}\t\t{}".format(key,book.get(key)))
while True:
    print("1.Add new contact \n2.Search contact \n3.Display contact \n4.Edit contact \n5.Delete contact \n6.Exit")
    c=int(input("\nEnter your choice:"))
    if(c==1):
        name=input("Enter the name:")
        num=int(input("Enter the phone number:"))
        book[name]=num
    elif(c==2):
        sname=input("Enter the contact name:")
        if sname in book:
            print(sname,"'s phone number is ",book[sname])
        else:
            print("The contact name is not found in the book")
    elif(c==3):
        if not book:
            print("Empty contact book")
        else:
            display_contact()
    elif(c==4):
        ebook=input("Enter the contact to be edited:")
        if ebook in book:
            p=input("Enter phone number:")
            book[ebook]=p
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif(c==5):
        dbook=input("Enter the contact the contact to be deleted:")
        if dbook in book:
            con=input("Do you want to delete the contact(y/n):")
            if con=="y" or con=="Y":
                book.pop(dbook)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break
        
            
