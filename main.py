import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Line, Ellipse, Rectangle, InstructionGroup
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
from datetime import datetime
import math

kivy.require('2.0.0')


class ClockWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
        
    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1)
            self.draw_clock_face()
            now = datetime.now()
            second = now.second
            self.draw_seconds_hand(second)
    
    def draw_clock_face(self):
        self.canvas.clear()
        with self.canvas:
            # Draw the white background
            Color(1, 1, 1)
            Rectangle(pos=self.pos, size=self.size)
            # Draw the clock face
            Color(0, 0, 0)
            radius = min(self.width, self.height) / 2
            center_x = self.center_x
            center_y = self.center_y

            # Draw the clock numbers
            for hour in range(1, 13):
                angle = math.radians(30 * hour)
                #angle = math.radians(30 * hour - 90)
                x = center_x + 0.8 * radius * math.sin (angle)
                y = center_y + 0.8 * radius * math.cos (angle)
                label = CoreLabel(text=str(hour), font_size=40)
                label.refresh()
                text = label.texture
                text_pos = (x - text.width / 2, y - text.height / 2)
                self.canvas.add(Rectangle(texture=text, pos=text_pos, size=text.size))
            
    def draw_seconds_hand(self, second):
        with self.canvas:
            radius = min(self.width, self.height) / 2
            # Angles for the four hands
            angles = [
                math.radians(360 / 60 * second - 90),
                math.radians(360 / 60 * second + 0),
                math.radians(360 / 60 * second + 90),
                math.radians(360 / 60 * second + 180),
            ]
            colors = [(0, 1, 0, 1), (1, 0, 0, 1), (1, 1, 0, 1), (0, 0, 0, 1)]
            
            for angle, color in zip(angles, colors):
                #x = self.center_x + self.width / 2 * math.sin(angle)
                #y = self.center_y + self.height / 2 * math.cos(angle)
                x = self.center_x + 0.7 * radius * math.sin(angle)
                y = self.center_y + 0.7 * radius * math.cos(angle)
                Color(*color)
                Line(points=[self.center_x, self.center_y, x, y], width=3)


class ClockApp(App):
    def build(self):
        self.title = "Four Hands Clock"
        return ClockWidget()


if __name__ == '__main__':
    ClockApp().run()
