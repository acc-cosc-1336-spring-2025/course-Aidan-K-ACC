
def add_inventory(dictionary, widget_name, quantity):
    if widget_name in dictionary:
        dictionary[widget_name]= dictionary[widget_name] + quantity
    if widget_name not in dictionary:
        dictionary[widget_name]= quantity

def remove_inventory_widget(dictionary, widget_name):
    if widget_name in dictionary:
        dictionary.pop(widget_name)
        return("Record deleted")
    else:
        return "Item not found"


dictionary= {}

add_inventory(dictionary, 'Widget1', 10)
add_inventory(dictionary, 'Widget1', 25)
print(dictionary)
remove_inventory_widget(dictionary, 'Widget1')
print(remove_inventory_widget(dictionary, 'Widget1'))
print(dictionary)