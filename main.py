from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.textfield import MDTextFieldLeadingIcon, MDTextFieldHintText, MDTextFieldTrailingIcon

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class ConverterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        self.input_riyals = MDTextField(
            MDTextFieldLeadingIcon(icon="bank"),
            MDTextFieldHintText(text="Hint text",),
            MDTextFieldTrailingIcon(icon="currency-usd",),
            mode="outlined",
            size_hint_x=None,
            width="240dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            hint_text="Enter amount in Riyals",
            halign="center",
        )

        self.result_label = MDLabel(
            text="Converted amount in Dirhams: 0",
            font_size=30,
            halign="center",
            text_color=(0.8, 0.8, 0.8, 1)
        )

        convert_button = MDButton(
            MDButtonIcon(icon="bank-transfer",),
            MDButtonText(
            text="Convert",),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_press=self.convert
        )

        layout.add_widget(self.input_riyals)
        layout.add_widget(self.result_label)
        layout.add_widget(convert_button)

        return layout

    def convert(self, *_):
        try:
            riyals = float(self.input_riyals.text)
            dirhams = riyals / 20
            self.result_label.text = f"Converted amount in Dirhams: {dirhams:.2f}"
            self.animate_result()
        except ValueError:
            self.result_label.text = "Please enter a valid number."

    def animate_result(self):
        anim = Animation(text_color=(1, 1, 0, 1), duration=0.2)
        anim += Animation(text_color=(0.8, 0.8, 0.8, 1), duration=0.2)
        anim.start(self.result_label)

if __name__ == "__main__":
    ConverterApp().run()
