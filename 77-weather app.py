import sys
import requests
import os
from dotenv import load_dotenv
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt # alignment
from PyQt5.QtGui import QPixmap

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        load_dotenv() 
        self.city = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.button = QPushButton("Get Weather", self)
        self.api_key = os.getenv("API_KEY")

        self.temp_label = QLabel(self)
        self.icon = QLabel(self)
        self.weather_label = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(500,300,300,400)

        vbox = QVBoxLayout()
        input_layout = QVBoxLayout()

        input_layout.addWidget(self.city)
        input_layout.addWidget(self.city_input, alignment=Qt.AlignHCenter)

        self.city.setFixedHeight(self.city.height()+3)

        vbox.addLayout(input_layout)
        vbox.addWidget(self.button, alignment=Qt.AlignHCenter)
        self.button.setFixedWidth(200)
        self.city_input.setFixedWidth(200)
    
        # create display layout
        display_layout = QVBoxLayout()

        display_layout.addWidget(self.temp_label)
        display_layout.addWidget(self.icon)
        display_layout.addWidget(self.weather_label)

        vbox.addLayout(display_layout)
        self.setLayout(vbox)

        self.city.setAlignment(Qt.AlignHCenter)
        self.city_input.setAlignment(Qt.AlignHCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.icon.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)

        self.button.clicked.connect(self.get_weather)


        self.city.setObjectName("title")
        self.temp_label.setObjectName("temp")
        self.weather_label.setObjectName("desc")
        self.icon.setObjectName("icon")


        self.setStyleSheet('''
            QWidget {
                font-family: Arial;
                font-size: 20px;
            }
            QLabel#title {
                font-size: 20px;
                font-weight: 600;
                color: #222;
            }
            QLabel#temp {
                font-size: 20px;
                font-weight: 600;
                color: #222;
            }
            QLineEdit {
                font-size: 20px;
                padding: 10px;
                border: 2px solid black;
                border-radius: 6px;
                background: white;
            }
            QPushButton {
                padding: 5;
                font-size: 13px;
                border: 2px solid grey;
            }
            QPushButton:hover {
                background-color: pink;
            }
        ''')
    
    def get_weather(self):
        city_name = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
        response = requests.get(url) # object
        response_json = response.json()

        if response.status_code == 200:
            print("Data retrieved!")
            self.display(response_json)
        else:
            self.reset()
            self.error(f"{response.status_code}: Failed to get data")
    
    def display(self, data):
        weather_data = data["weather"][0]
        temp_data = data["main"]
        self.temp_label.setText(f"{int((temp_data["temp"])- 273.15):.0f} °C") # Kelvin to Celsius
        self.temp_label.setStyleSheet("font-size: 30px;" "color: black;")
        self.weather_label.setText(weather_data["description"])

        icon_url = f"https://openweathermap.org/payload/api/media/file/{weather_data["icon"]}.png"
        image = QPixmap()
        image.loadFromData(requests.get(icon_url).content)
        image.scaled(70,70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.icon.setPixmap(image)
    

    def error(self, message):
        self.temp_label.setText(message)
        self.temp_label.setStyleSheet("font-size: 18px;" "color: red;")

    def reset(self):
        self.temp_label.clear()
        self.weather_label.clear()
        self.icon.clear()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())