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
        print(self.api_key)


        self.temp_label = QLabel(self)
        self.icon = QLabel(self)
        self.weather_label = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(500,300,300,500)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.button)

        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.icon)
        vbox.addWidget(self.weather_label)

        self.setLayout(vbox)
        self.city.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.icon.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)

        self.button.clicked.connect(self.get_weather)

        self.setStyleSheet('''
            QLabel {
                font-size: 30px;
            }
            QLineEdit {
                padding: 10;
                font-size: 20px;
            }
            QPushButton {
                padding: 10;
                font-size: 20px;
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
            weather_data = response_json["weather"][0]
            temp_data = response_json["main"]
            self.temp_label.setText(f"{int((temp_data["temp"])- 273.15):.0f} °C") # Kelvin to Celsius
            self.weather_label.setText(weather_data["description"])

            icon_url = f"https://openweathermap.org/payload/api/media/file/{weather_data["icon"]}.png"
            image = QPixmap()
            image.loadFromData(requests.get(icon_url).content)
            self.icon.setPixmap(image)

        else:
            self.reset()

    def reset(self):
        self.temp_label.clear()
        self.weather_label.clear()
        self.icon.clear()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())