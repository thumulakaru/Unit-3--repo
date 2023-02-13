# Quiz 41
## Python code
```.py
from kivymd.app import MDApp


class Quiz_041(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.current_player = "X"

    def build(self):
        return

    def button_press(self, button_id):
        print(button_id)
        current_player = self.current_player
        temp = "self.root.ids.button" + button_id
        current_button = eval(temp)

        # current_button.disabled = True
        if self.values[int(button_id) - 1] == 0:
            current_button.text = current_player
            if current_player == "X":
                self.current_player = "O"
                current_button.md_bg_color = "#FF0000"
                self.values[int(button_id) - 1] = 1
            else:
                self.current_player = "X"
                current_button.md_bg_color = "#0000FF"
                self.values[int(button_id) - 1] = 2

        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for indices in winning_combinations:
            if all(self.values[i] == self.values[indices[0]] and self.values[i] != 0 for i in indices):
                print(f"Winner is {current_player}")
                self.root.ids.label2.text = f"Winner is {current_player}"


                for i in range(1, 10):
                    temp = "self.root.ids.button" + str(i)
                    current_button = eval(temp)
                    current_button.disabled = True
                break


            else:
                print("No Winner Yet")
                self.root.ids.label2.text = f"Current Player: {self.current_player}"
                if 0 not in (self.values):
                    self.root.ids.label2.text = "No winner"

    def reset(self):
        self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.current_player = "X"
        for i in range(1, 10):
            temp = "self.root.ids.button" + str(i)
            current_button = eval(temp)
            current_button.text = ""
            current_button.md_bg_color = "grey"
            current_button.disabled = False

        self.root.ids.label2.text = f"Current Player: {self.current_player}"


quiz_41 = Quiz_041()
quiz_41.run()
```

## kv file
```.kv
Screen:
    id: screen
    size: 500, 500

    MDBoxLayout:
        id: prime_box
        orientation: "vertical"
        size_hint: .8, .8
        md_bg_color: "#00FF00"
        pos_hint: {'center_x': .5, 'center_y': .5}

        MDBoxLayout:
            id: text_box
            orientation: "vertical"
            size_hint: 1, .2

            MDLabel:
                id:label1
                text: "Tic Tac Toe by Thumula"
                halign: "center"
                font_style: "H3"

            MDLabel:
                id:label2
                text: "Current Player:" + app.current_player
                halign: "center"
                font_style: "H5"


        MDBoxLayout:
            id:Action_Box
            orientation: "vertical"
            md_bg_color: "#FF0000"
            size_hint: 1, .8
            pos_hint: {'center_x': 0.5, 'center_y':0.5}

            MDBoxLayout:
                id:layer_one
                orientation: "horizontal"
                md_bg_color: "#0000FF"
                size_hint: 1, .33

                MDRaisedButton:
                    id:button1
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("1")
                    size_hint: .33, 1
                    disabled: False

                MDRaisedButton:
                    id:button2
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("2")
                    size_hint: .33, 1
                    disabled: False

                MDRaisedButton:
                    id:button3
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("3")
                    size_hint: .33, 1
                    disabled: False

            MDBoxLayout:
                id:layer_one
                orientation: "horizontal"
                md_bg_color: "#0000FF"
                size_hint: 1, .33

                MDRaisedButton:
                    id:button4
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("4")
                    size_hint: .33, 1
                    disabled: False

                MDRaisedButton:
                    id:button5
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("5")
                    size_hint: .33, 1
                    disabled: False

                MDRaisedButton:
                    id:button6
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("6")
                    size_hint: .33, 1
                    disabled: False

            MDBoxLayout:
                id:layer_one
                orientation: "horizontal"
                md_bg_color: "#0000FF"
                size_hint: 1, .33

                MDRaisedButton:
                    id:button7
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("7")
                    size_hint: .33, 1
                    disabled: False

                MDRaisedButton:
                    id:button8
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("8")
                    size_hint: .33, 1
                    disabled: False

                MDRaisedButton:
                    id:button9
                    text: ""
                    md_bg_color: "grey"
                    on_release: app.button_press("9")
                    size_hint: .33, 1
                    disabled: False

            MDBoxLayout:
                id: reset_box
                size_hint: 1, .2
                orientation: 'vertical'
                md_bg_color:"#FFFFFF"

                MDRaisedButton:
                    id: reset_button
                    text: "Reset"
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.reset()
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_041_result.png)

**Fig.1** Interface of the tic tac toe
