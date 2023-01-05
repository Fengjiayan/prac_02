from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):

    output_km_text = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.handle_calculate()
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_km_text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
