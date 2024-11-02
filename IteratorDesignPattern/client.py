from listcollection import ListColleciton
if __name__=="__main__":
    colc1=ListColleciton()
    colc1.add__item(10)
    colc1.add__item(20)
    colc1.add__item(30)
    itr1=colc1.create_iterator()
    print(itr1.next())
    print(itr1.next())