from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text="Hello", font_size=30)
        button = Button(text="Click Me", size_hint=(1, 0.3))

        button.bind(on_press=self.say_hello)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def say_hello(self, instance):
        self.label.text = "Hello!"

MyApp().run()