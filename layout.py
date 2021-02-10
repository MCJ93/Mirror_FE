import PySimpleGUI as gui

elementKeys = {
  "currentTime": "_currentTime_",
  "currentDate": "_currentDate",
  "currentDayOfWeek": "_currentDayOfWeek_"
}

layout = [
  [
    gui.Text("00:00:00", key=elementKeys["currentTime"]),
    gui.Text("00/00/00", key=elementKeys["currentDate"]),
    gui.Text("_", key=elementKeys["currentDayOfWeek"])
  ], [
    gui.Button("OK")
  ]
]
