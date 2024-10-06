from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RiyaltoDirham(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Enter amount in SAR", font_size=24)
        layout.add_widget(self.label)

        self.input_sar = TextInput(hint_text="Enter Saudi Riyals (SAR)", multiline=False, input_type='number', font_size=20)
        layout.add_widget(self.input_sar)

        convert_button = Button(text="Convert to MAD", size_hint=(1, 0.5), font_size=20)
        convert_button.bind(on_press=self.convert_currency)
        layout.add_widget(convert_button)

        self.result_label = Label(text="", font_size=24)
        layout.add_widget(self.result_label)

        return layout

    def convert_currency(self, _):
        try:
            sar_amount = float(self.input_sar.text)

            conversion_rate = 1 / 20

            mad_amount = sar_amount * conversion_rate

            self.result_label.text = f"{sar_amount} SAR = {mad_amount:.2f} MAD"
        except ValueError:
            self.result_label.text = "Please enter a valid number!"

if __name__ == "__main__":
    RiyaltoDirham().run()
