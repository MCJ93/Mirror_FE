import PySimpleGUI as gui

elementKeys = {
  "currentTime": "_currentTime_",
  "currentDate": "_currentDate",
  "currentDayOfWeek": "_currentDayOfWeek_",
  "currentTemperature": "_currentTemperature_"
}

leftColumn = [
  [
    gui.Text(
      "",
      size=(0, 32),
      background_color="#000"
    ),
  ],
  [
    gui.Text(
      "00:00:00",
      font=("Bebas Neue", 60),
      key=elementKeys["currentTime"],
      background_color="#000"
    ),
  ],
  [
    gui.Text(
      "---------------",
      key=elementKeys["currentDayOfWeek"],
      font=("Bebas Neue", 25),
      background_color="#000"
    ),
    gui.Text(
      "00/00/00",
      key=elementKeys["currentDate"],
      font=("Bebas Neue", 25),
      background_color="#000"
    ),
    gui.Button("OK")
  ]
]

rightColumn = [
  [
    gui.Text(
      "",
      size=(0, 32),
      background_color="#000"
    ),
  ],
  [
    gui.Text(
      "00--",
      font=("Bebas Neue", 60),
      key=elementKeys["currentTemperature"],
      background_color="#000"
    ),
  ]
]

layout = [
  [
    gui.Column(
      leftColumn,
      size=(800, 800),
      background_color="#000"
    ),
    gui.Column(
      rightColumn,
      size=(400, 800),
      background_color="#000"
    )
  ]
]
