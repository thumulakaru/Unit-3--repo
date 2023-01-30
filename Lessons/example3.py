from kivymd.app import MDApp


class example3(MDApp):
    def build(self):
        return


    def change_author(self, name):
        self.root.ids.title.text = f"Author {name}"


test = example3()
test.run()
