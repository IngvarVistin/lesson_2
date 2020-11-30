product_list = []
analytics_name = []
analytics_price = []
analytics_quantity = []
analytics_unit = []
analytics_dict = {
    'Наименование': analytics_name, 'Цена': analytics_price, 'количество': analytics_quantity, 'Еденица измерения': analytics_unit
}
for i in range(int(input('Сколько товаров необходимо ввести?  '))):
    name_product = input('Введите наименование товара: ')
    analytics_name.append(name_product)
    price = float(input('Введите цену товара: '))
    analytics_price.append(price)
    quantity = float(input('Введите количество товара: '))
    analytics_quantity.append(quantity)
    unit = input('Введите еденицу измерения: ')
    analytics_unit.append(unit)
    product_dict = {'Наименование': name_product, 'Цена': price, 'Количество': quantity, 'Еденица изм': unit}
    nom_product = (len(product_list)+1)
    merch = (nom_product, product_dict)
    product_list.append(merch)
print(product_list)
print(analytics_dict)