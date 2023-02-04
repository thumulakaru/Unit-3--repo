# Quiz 39
## Code
### Python Code
```.py
from kivymd.app import MDApp


class Quiz_039(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return


    def add(self):
        self.count += 1
        self.root.ids.counter.text = f"Count {self.count}"

run = Quiz_039()
run.run()
```

### KV code
```.kv
Screen:
    size: 500, 500

    MDBoxLayout:
        id: main_box
        orientation: 'horizontal'
        size_hint: .7, .3
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: "blue"

        MDLabel:
            id: counter
            size_hint: .5, 1
            font_size: "34"
            text: "Click 'Add+1' to start"

        MDRaisedButton:
            id: add_button
            size_hint: .5, 1
            font_size: "34"
            text:"Add +1"
            color: "black"
            on_press: app.add()
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_039_result.png)

**Fig.1** Results after running the code
