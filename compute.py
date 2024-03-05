from lxml import etree
f = open('orders.xml')
tree = etree.parse(f)

def tot(order_no):
    total = 0
    for element in tree.xpath(f"//order[@no='{order_no}']/entry/quantity"):
        total += int(element.text)
    return total

print(tot('o100'))