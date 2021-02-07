import PySimpleGUI as gui

elementKeys = {
  "currentTime": "_currentTime_"
}

layout = [
  [
    gui.Text("00:00:00", key=elementKeys["currentTime"])
  ], [
    gui.Button("OK")
  ]
]
