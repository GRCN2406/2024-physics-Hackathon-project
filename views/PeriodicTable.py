import arcade
import json

from widgets.ElementBox import ElementBox
from model.Element import Element
from views import IsotopeSelection

"""
    JSON found in ressources/PeriodicTable/TableauPeriodiqueInfo.json
    Element.py = is the class that contains the data and any methode that directly affects the data of the element.
    ElementBox.py = is the visual representation of each element using python arcade.
    PeriodicTable.py = is the view. It draws the table and allows the user to click an element which will be stored in the selected_element variable.
    for now theres a print statement that will print the name and symbol of the element clicked for debugging purposes.
"""

class PeriodicTableView(arcade.View):
    def __init__(self):
        super().__init__()
        
        # array of all elements
        self.elements = []
        
        # var containing last clicked element
        self.selected_element = None
        
        # draw elements from json
        self.create_elements(load_json_data("ressources/PeriodicTable/TableauPeriodiqueInfo.json"))

    def create_elements(self, json_data):
        for element_data in json_data["elements"]:
            element = Element(
                element_data['symbol'],
                element_data['name'],
                element_data['number'],
                element_data['atomic_mass'],
                element_data['category']
            )
            # spacing between elements
            xpos = element_data['xpos'] * (self.window.get_size()[0] / 20) + self.window.get_size()[0] / 20
            ypos = element_data['ypos'] * -(self.window.get_size()[1] / 12) + self.window.get_size()[1]

            element_box = ElementBox(element, xpos, ypos, self.window.get_size()[1] / 15)
            self.elements.append(element_box)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        for element in self.elements:
            element.draw()
            
        arcade.draw_text("Please select an element", 250, self.window.get_size()[1]/10 * 9, arcade.color.BLACK, 20)



    def on_mouse_press(self, x, y, button, modifiers):
        for element in self.elements:
            if element.is_clicked(x, y):
                # self.selected_element = element
                # print(f"Element clicked: {element.element.name} ({element.element.symbol})")
                isotope_view = IsotopeSelection.IsotopeSelectionView(selected_element=element)
                isotope_view.setup()
                arcade.get_window().show_view(isotope_view)

def load_json_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    json_data = load_json_data("ressources/PeriodicTable/TableauPeriodiqueInfo.json")
    window = PeriodicTableView(800, 600, "Periodic Table", json_data)
    arcade.run()
