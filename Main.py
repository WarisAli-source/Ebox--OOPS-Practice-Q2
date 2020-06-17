from Item import Item
iid=input("\n")
itemname=input("\n")
companyname=input("\n")
price=int(input())

ob=Item(iid,itemname,companyname,price)
ob.display()