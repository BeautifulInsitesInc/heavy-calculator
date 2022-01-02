import kivy
from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window # Set size of app
from kivy.uix.image import Image #not needed if only placing image in design file .kv
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

#Window.size = (500,700)
#os.environ["fullscreen"] = 'auto'
Config.set('graphics', 'window_state', 'minimized')

Builder.load_file('heavy_calculator.kv')

class MyLayout(Widget):
    def clear(self):
        print('clearing')
        self.ids.calc_input.text="0"
        self.ids.display_image.size_hint = (1,.0001)
        self.ids.display_image.opacity = 0
        self.ids.calc_input.size_hint = (1,.2)

    def button_press(self, button):
        # create a variable that contains what ever is in the box 
        prior = self.ids.calc_input.text

        if prior=='0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def plus_minus(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'
    
    def equals(self):
        prior = self.ids.calc_input.text
        #error handling
        try:
            answer = eval(prior)
            if answer == 666:
                self.ids.calc_input.size_hint = (1,.0001)
                self.ids.display_image.size_hint = (1,1)
                self.ids.display_image.opacity = 1
                self.ids.calc_input.text = "The Number Of The Beast!"
            else:
                self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "You're Going To Hell In A Handbasket"

        '''
        if "+" in prior:
            num_list = prior.split("+")
            answer=0.0
            # loop through list
            for number in num_list:
                answer = answer + float(number)
            self.ids.calc_input.text = str(answer)
        '''

class Calculator(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Calculator().run()

