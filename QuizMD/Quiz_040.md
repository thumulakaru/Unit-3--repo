# Quiz 40
## Code
### Python code
```.py
from kivymd.app import MDApp


class Quiz_040(MDApp):
    def __init__(self, **kwargs):
        dark_msg = "Dark mode"
        light_msg = "Light mode"
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"

    def touch(self):
        dark = "#000000"
        light = "#FFFFFF"
        dark_msg = "Dark mode"
        light_msg = "Light mode"

        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.root.ids.mode_chip.text = light_msg
            self.root.ids.mode_chip.md_bg_color = "white"
            self.root.ids.mode_chip.text_color = "black"

        else:
            self.theme_cls.theme_style = "Light"
            self.root.ids.mode_chip.text = dark_msg
            self.root.ids.mode_chip.md_bg_color = "black"
            self.root.ids.mode_chip.text_color = "white"


test = Quiz_040()
test.run()
```

### KV code
```.py
Screen:
    size: 500, 500

    MDScreen:
        id:"screen"
        theme_style: "Light"


        MDLabel:
            id:name
            text: "Thumula"
            text_color: "#000000"
            halign: "center"
            font_size: "34pt"

        MDRaisedButton:
            id: mode_chip
            text: "Dark Mode"
            md_bg_color:"#000000"
            text_color: "#FFFFFF"
            pos_hint: {"left": 1}
            icon_right: "close-circle-outline"
            theme_style: self.theme_style
            on_press:app.touch()
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_040_result.png)

**Fig.1** Results after running the code
