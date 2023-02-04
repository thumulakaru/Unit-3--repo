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
