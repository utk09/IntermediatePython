# pip install kivy
# pip install docutils pygments pypiwin32 kivy.deps.sdl2
# pip install kivy.deps.glew


import kivy

kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))  # eval() evaluates the passed string as a Python expression
                # and returns the result.
                # For example, eval("1 + 1") interprets and executes the expression "1 + 1"
                # and returns the result (2)
            except Exception:
                self.display.text = "Error !"


class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
