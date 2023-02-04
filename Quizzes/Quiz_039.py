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