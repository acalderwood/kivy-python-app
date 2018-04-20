# ---------- KIVY TUTORIAL PT 4  ----------

# In this part of my Kivy tutorial I'll show how to use
# the ListView, ListAdapter and how to create a toolbar

# ---------- personoffersdb.py  ----------

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class PersonOffersListButton(ListItemButton):
    pass


class PersonOffersDB(BoxLayout):

    # Connects the value in the TextInput widget to these
    # fields
    business_name_text_input = ObjectProperty()
    points_numeric_input = ObjectProperty()
    price_numeric_input = ObjectProperty()
    person_offers_list = ObjectProperty()

    def submit_offer(self):

        # Get the student name from the TextInputs
        business_name = self.business_name_text_input.text
        points = self.points_numeric_input.text
        price = self.price_numeric_input.text

        # Add the student to the ListView
        self.person_offers_list.adapter.data.extend([business_name + "                " + points + " points               $" + price])

        # Reset the ListView
        self.person_offers_list._trigger_reset_populate()

    def delete_offer(self, *args):

        # If a list item is selected
        if self.person_offers_list.adapter.selection:

            # Get the text from the item selected
            selection = self.person_offers_list.adapter.selection[0].text

            # Remove the matching item
            self.person_offers_list.adapter.data.remove(selection)

            # Reset the ListView
            self.person_offers_list._trigger_reset_populate()

    def replace_offer(self, *args):

        # If a list item is selected
        if self.person_offers_list.adapter.selection:

            # Get the text from the item selected
            selection = self.person_offers_list.adapter.selection[0].text

            # Remove the matching item
            self.person_offers_list.adapter.data.remove(selection)

            # Get the student name from the TextInputs
            business_name = self.business_name_text_input.text

            # Add the updated data to the list
            self.person_offers_list.adapter.data.extend([business_name])

            # Reset the ListView
            self.person_offers_list._trigger_reset_populate()


class PersonOffersDBApp(App):
    def build(self):
        return PersonOffersDB()

#class OfferBoard(BoxLayout):
#    offers = ListProperty()
#    print self.person_offers_list

dbApp = PersonOffersDBApp()

dbApp.run()
