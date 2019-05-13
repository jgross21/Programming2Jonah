'''
Formatter (26pts)

Create a kivy app with the following rough layout

############
#  LABEL   #
#  SPINNER #
#  RADIOS  #
#  SLIDERS #
#  SWITCH  #
############

The label will be the formatting target for this application

- The spinner will change the font of the label (minimum 2 fonts) (6pts)
- The radios will be used to select the text for the label (3pts)
- Three sliders will be used to adjust the rgba values of the label background canvas color. (6pts)
- A switch will be used to change the font color from black to white. (3pts)

Each control will have an associated label. (8pts)

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class FormatterApp(App):
    def build(self):
        return FormatterLayout()

class FormatterLayout(BoxLayout):
    # all of my functions will be here
    def text_on(self, value):
        if value:
            self.label.color = 1, 1, 1, 1
        else:
            self.label.color = 0, 0, 0, 1
    def change_text(self, text):
        self.label.text = text

    def font_change(self, font):
        if font == 'Mexcellent':
            self.label.font_name = 'Mexcellent.ttf'
            self.spinner.font_name = 'Mexcellent.ttf'
        if font == 'Roboto':
            self.label.font_name = 'Roboto-BlackItalic.ttf'
            self.spinner.font_name = 'Roboto-BlackItalic.ttf'
    def change_window(self, r, g, b):
        Window.clearcolor = (r, g, b, 1)


if __name__ == '__main__':
    app = FormatterApp()
    app.run()

