# Quiz 42

## Python code
```.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MysteryPageA(MDScreen):
    pass


class MysteryPageB(MDScreen):
    pass


class Quiz_042(MDApp):
    def build(self):
        return


my_app = Quiz_042()
my_app.run()
```

## KV file
```.kv
ScreenManager:
    id:scr_manager

    MysteryPageA:
        name:"MysteryPageA"

    MysteryPageB:
        name:"MysteryPageB"

<MysteryPageA>
    FitImage:
        source:"https://cdn.pixabay.com/photo/2018/05/12/17/41/forest-3394066_960_720.jpg"
    MDCard:
        size_hint: .7, .7
        pos_hint:{"center_x": .5,"center_y": .5 }
        md_bg_color: "#000000"
        orientation: "vertical"

        MDBoxLayout:
            size_hint: .5, .5
            pos_hint: {"center_x": .5,"center_y":.5}
            orientation: "vertical"

            MDLabel:
                id:label1
                text: "Mystery Page 1"
                font_style: "H5"
                halign: "center"
                size_hint: 1, .1
                color: "#FFFFFF"

        MDRaisedButton:
            text: "Mystery"
            on_press: root.parent.current = "MysteryPageB"

<MysteryPageB>
    FitImage:
        source:"https://cdn.pixabay.com/photo/2018/05/12/17/41/forest-3394066_960_720.jpg"
    MDCard:
        size_hint: .7, .7
        pos_hint:{"center_x": .5,"center_y": .5 }
        md_bg_color: "#000000"
        orientation: "vertical"

        MDBoxLayout:
            size_hint: .5, .5
            pos_hint: {"center_x": .5,"center_y":.5}
            orientation: "vertical"

            MDLabel:
                id:label2
                text: "You pressed the button now people will like Thor: Love and Thunder"
                font_style: "H5"
                halign: "center"
                size_hint: 1, .1
                color: "#FFFFFF"

        MDRaisedButton:
            text: "Back to home"
            on_press: root.parent.current = "MysteryPageA"
            pos_hint: {"center_x":.5}
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_042_result.png)

**Fig.1** Interface of the mystery page
