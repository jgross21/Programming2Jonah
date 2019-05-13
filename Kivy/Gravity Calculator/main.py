from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class GravitycalculatorApp(App):
    def build(self):
        return GravitycalculatorLayout()

class GravitycalculatorLayout(BoxLayout):
    # all of my functions will be here
    def calculate(self):
        try:
            f = 6.67e-11 * (int(self.m1.text) * int(self.m2.text)) / int(self.r.text) ** 2
            self.newtons.text = 'F(n)= {:.2e}'.format(f)

        except:
            self.newtons.text = 'That doesn\'t work'

if __name__ == '__main__':
    app = GravitycalculatorApp()
    app.run()
