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
