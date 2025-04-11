
def add_inventory(dictionary, widget_name, quantity):
    if widget_name in dictionary:
        dictionary[widget_name]= dictionary[widget_name] + quantity
    if widget_name not in dictionary:
        dictionary[widget_name]= quantity

def remove_inventory_widget(dictionary, widget_name):
    if widget_name in dictionary:
        dictionary.pop(widget_name)
        return "Record deleted"
    else:
        return "Item not found"
