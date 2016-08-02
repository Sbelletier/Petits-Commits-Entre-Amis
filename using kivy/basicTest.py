#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout#How a widget is created
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2 
		#size_hint works with proportions
        self.add_widget(Label(text='User Name',size_hint=[1.0,0.3]))
        self.username = TextInput(multiline=False,size_hint=[0.2,0.3])
        self.add_widget(self.username)
        self.add_widget(Label(text='password',size_hint=[1.0,1.0]))
        self.password = TextInput(password=True, multiline=False,size_hint=[0.2,1.0])
        self.add_widget(self.password)

class BigWidget(GridLayout):
	def __init__(self, **kwargs):
		super(BigWidget, self).__init__(**kwargs)
		self.rows = 3
		self.add_widget(LoginScreen())
		self.add_widget(Button(text='Compute'))
		
		
class MyApp(App):

    def build(self):
        return BigWidget()#Has to return the root widget


if __name__ == '__main__':
    MyApp().run()