class MenuOption:
    """ Menu option, including option, help text, and function"""

    def __init__(self, option, text, function=None):
        self.option = option
        self.text = text
        self.fn = function


class Menu:
    """ CLI Menu Options """

    def __init__(self, menu_name):
        self._stale_text = True
        self._text = ""
        self.name = menu_name
        self.options = {"x": MenuOption("x", "Exit")}

    def new_option(self, option, text, function=None):
        """
        Add a new option to the menu.
        """
        self._stale_text = True
        self.options[option] = MenuOption(
            option=option,
            text=text,
            function=function
        )

    def edit_option(self, option: str, text: str = None, function=None):
        """
        Change the text or function of an existing option, or create new
          if not already an option
        """
        if option not in self.options:
            return self.new_option(option, text, function)
        opt = self.options[option]
        opt.text = text if text is not None else opt.text
        opt.fn = function if function is not None else opt.fn

    @property
    def menu_text(self):
        """
        Generate menu text.
        """
        if self._stale_text:
            self.text = f"\n{self.name}\n"
            for opt in self.options.values():
                if opt.option == "x":
                    continue
                self.text += f"  {opt.option} - {opt.text}\n"
            self.text += "  x - Exit"
            self._stale_text = False
        return self.text


    def get_action(self, option: str):
        """
        Get the action associated with the menu option
        """
        if option == "x":
            return "x"
        elif option in self.options:
            return self.options[option].fn

    def prompt(self):
        while True:
            print(self.menu_text)
            selection = input("Enter Option:").strip().lower()
            action = self.get_action(selection)
            if isinstance(action, str) and action == "x":
                return
            elif action is None:
                continue
            action()
