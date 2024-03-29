Price=float(input("ราคาสินค้าทั้งหมด : "))
def VatCalculate(Price):
    TotalPrice=Price*107/100
    return TotalPrice
print(VatCalculate(Price))
