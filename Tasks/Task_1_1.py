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