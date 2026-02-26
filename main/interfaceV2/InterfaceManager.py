from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.widgets import Label, TextArea, Frame
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

from interfaceV2.LibraryFacade import LibraryFacade
from helper.Membership import Membership


class CLI:

    def __init__(self):
        self.facade = LibraryFacade()

        # Form fields
        self.username_field = TextArea(height=1)
        self.password_field = TextArea(height=1, password=True)
        self.message = Label(text="Welcome to University Library")

        # Key bindings
        self.kb = KeyBindings()
        self._bind_keys()

        # Build UI
        self.application = self._create_application()

    # ----------------------------------
    # Key Bindings (F Keys)
    # ----------------------------------
    def _bind_keys(self):

        @self.kb.add("f1")
        def _(event):
            self.handle_sign_in()

        @self.kb.add("f2")
        def _(event):
            self.handle_join()

        @self.kb.add("f3")
        def _(event):
            event.app.exit()

    # ----------------------------------
    # Layout
    # ----------------------------------
    def _create_application(self):

        body = HSplit([
            Label(text="📚 UNIVERSITY LIBRARY SYSTEM", style="class:title"),
            Window(height=1, char="═"),

            Frame(self.username_field, title="Username"),
            Frame(self.password_field, title="Password"),

            Window(height=1),
            self.message,
            Window(height=1),

            Label(
                text="F1 Sign In    F2 Join    F3 Exit",
                style="class:footer"
            ),
        ])

        style = Style.from_dict({
            "class:title": "bold underline",
            "class:footer": "reverse",
            "class:frame.label": "bold",
        })

        return Application(
            layout=Layout(body),
            key_bindings=self.kb,
            style=style,
            full_screen=True,
        )

    # ----------------------------------
    # Logic
    # ----------------------------------
    def handle_sign_in(self):
        username = self.username_field.text.strip()
        password = self.password_field.text.strip()

        if not Membership.username_exists(username):
            self.message.text = "User does not exist."
            return

        if not self.facade.sign_in(username, password):
            self.message.text = "Incorrect password."
            return

        # Successful login
        self.application.exit()
        self.facade.run_member_ui()

    def handle_join(self):
        username = self.username_field.text.strip()
        password = self.password_field.text.strip()

        if not username:
            self.message.text = "Invalid username."
            return

        if Membership.username_exists(username):
            self.message.text = "Username already exists."
            return

        if len(password) < 6:
            self.message.text = "Password must be at least 6 characters."
            return

        if self.facade.join(username, password, "a"):
            self.message.text = "Welcome to our library community!"
        else:
            self.message.text = "Registration failed."

    # ----------------------------------
    def run(self):
        self.application.run()


# --------------------------------------
# Entry Point
# --------------------------------------
if __name__ == "__main__":
    CLI().run()