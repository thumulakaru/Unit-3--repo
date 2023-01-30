# GUI Task
## Example 1
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Lessons/example1.png)

**Fig.1** Example 1 output

## Example 2
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Lessons/example2.png)

**Fig.2** Example 2 output

## Example 3
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Lessons/example3.png)

**Fig.3** Example 3 output

## Currency Converter

### Code
```.py
from kivymd.app import MDApp


class Task_1_1(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = ""

    def build(self):
        return

    def set_value(self):
        user_start = self.root.ids.user_start_x.text
        self.count = user_start


    def convert_JPY(self):
        if self.count.isdigit():
            self.count = int(self.count)
            jpy_amount = self.count * 0.36
            self.root.ids.counter_label.text = f"LKR {self.count} is JPY {jpy_amount}."
            self.root.ids.error_label.text = ""
        else:
            self.root.ids.error_label.text = "Invalid Input"
            self.root.ids.counter_label.text = ""


    def convert_USD(self):
        if self.count.isdigit():
            self.count = int(self.count)
            usd_amount = self.count * .0027
            self.root.ids.counter_label.text = f"LKR {self.count} is USD {usd_amount}."
            self.root.ids.error_label.text = ""
        else:
            self.root.ids.error_label.text = "Invalid Input"
            self.root.ids.counter_label.text = ""


test = Task_1_1()
test.run()
```

### KV file
```.kv
Screen:
    size: 500, 500

    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDLabel:
            text:"Currency Converter"
            halign: 'center'
            font_style: 'H3'
            text_color: "#000000"
            size_hint: 1, .2
            pos_hint: {'center_x':0.5}

        MDBoxLayout:
            id: first_box
            orientation: 'vertical'
            size_hint: 1, .3
            pos_hint: {'center_x': .5, 'center_y': .5}

            MDTextField:
                id: user_start_x
                hint_text: 'Enter a number'
                mode: 'rectangle'
                on_text: app.set_value()
                size_hint: 1, .025
                pos_hint: {'center_x': .5}

            MDLabel:
                id: error_label
                font_style : 'Body1'
                text_color : "#FF0000"
                size_hint: 1, 0.005

            MDChip:
                text: "JPY"
                pos_hint: {"right": 1}
                icon_right: "close-circle-outline"
                md_bg_color: "#FFFF00"
                on_press:app.convert_JPY()

            MDChip:
                text: "USD"
                pos_hint: {"right":1}
                icon_right: "close-circle-outline"
                md_bg_color: "#FF0000"
                on_press:app.convert_USD()

        MDBoxLayout:
            id: second_box
            orientation: 'horizontal'
            size_hint: 1, .3

            MDLabel:
                id: counter_label
                font_style: "Body1"
                text_color: "#00FF00"
```

### Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Tasks/Task_1_1.png)

**Fig.4** Interface of the currency converter


## Bit to byte Converter

### Code
```.py
from kivymd.app import MDApp

class Task_1_2(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = ""

    def build(self):
        return

    def set_value(self):
        user_start = self.root.ids.user_start_x.text
        self.count = user_start


    def convert(self):
        if self.count.isdigit():
            self.count = int(self.count)
            self.root.ids.error_label.text = ""
            multiples = [" Kilo", " Mega", " Giga", " Tera", " Peta", " Exa"]
            byte_val = self.count/8
            mult = ""
            num_val = byte_val
            for i in range(6, 0, -1):
                temp_val = byte_val/(1024**i)
                if temp_val >= 1:
                    num_val = temp_val
                    mult = multiples[i-1]
                    break
                else:
                    mult = ""
            value = f"{round(num_val, 2)}{mult}"
            self.root.ids.final_label.text = f"{value} bytes"

        else:
            self.root.ids.error_label.text = "Invalid Input"
            self.root.ids.final_label.text = ""


test = Task_1_2()
test.run()
```

### KV file
```.kv
Screen:
    size: 500, 500

    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDLabel:
            text:"Bit to Byte Converter"
            halign: 'center'
            font_style: 'H3'
            text_color: "#000000"
            size_hint: 1, .2
            pos_hint: {'center_x':0.5}

        MDBoxLayout:
            id: first_box
            orientation: 'vertical'
            size_hint: 1, .15
            pos_hint: {'center_x': .5, 'center_y': .5}

            MDTextField:
                id: user_start_x
                hint_text: 'Enter a number'
                mode: 'rectangle'
                on_text: app.set_value()
                size_hint: 1, .025
                pos_hint: {'center_x': .5}

            MDLabel:
                id: error_label
                font_style : 'Body1'
                text_color : "#FF0000"
                size_hint: 1, 0.005

            MDChip:
                text: "Convert"
                pos_hint: {"right": 1}
                icon_right: "close-circle-outline"
                md_bg_color: "#FFFF00"
                on_press:app.convert()

        MDBoxLayout:
            id: second_box
            orientation: 'horizontal'
            size_hint: 1, .3

            MDLabel:
                id: final_label
                font_style: "Body1"
                text_color: "#00FF00"
```

### Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Tasks/Task_1_2.png)

**Fig.5** Interface of the bit to byte converter
