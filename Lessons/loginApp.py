from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    def try_login(self):
        print("User tried to login")
        # Get the input username and password and print it
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text


class RegistrationScreen(MDScreen):
    def try_register(self):
        print("User tried to register")
        # Get the registration details and print it
        uname = self.ids.uname.text
        passwd1 = self.ids.passwd1.text
        passwd2 = self.ids.passwd2.text
        if passwd1 == passwd2:
            self.ids.passwd2.error = True
            self.ids.passwd1.error = True



class loginApp(MDApp):
    def build(self):
        return


# Create an object

test = loginApp()
test.run()