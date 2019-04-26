from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ScoreApp(App):
    def build(self):
        return ScoreLayout()

class ScoreLayout(BoxLayout):
    # my root widget which will contain all my functions
    def change_score(self, label, amount):
        new_score = int(label.text) + amount
        label.text = str(new_score)
    def reset(self):
        self.home.text = '0'
        self.away.text = '0'

if __name__ == '__main__':
    app = ScoreApp()
    app.run()