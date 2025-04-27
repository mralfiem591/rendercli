from colorama import Fore, Style, init
from rich.console import Console
from rich.tree import Tree

# Initialize Colorama for cross-platform compatibility
init(autoreset=True)

# Initialize Rich console
console = Console()

class _CliUtils:
    """
    Utilities used by RenderCli.
    Not intended for direct use outside of this class.
    """
    def __init__(self):
        self.console = Console()

    def clear_screen(self):
        """
        Clears the console screen.
        """
        self.console.clear()

class RenderCli:
    """
    A class to render a CLI menu with options and handle user input.
    `__init__` method initializes the console and CLI utilities.
    Use `render_menu` method to display the menu and get user input plus handle everything else.
    Use `validate_input` to check if the input is valid.
    Use `get_hotkey` to prompt for a hotkey and return a valid one.

    """
    def __init__(self):
        self.cli_utils = _CliUtils()
        self.console = Console()

    def render_menu(self, title: str, options: dict, clear: bool = True) -> str | None:
        """
        Renders the CLI menu with a title, options, and waits for user input.
        :param title: str - Title of the menu
        :param options: dict - Dictionary with hotkeys as keys and option descriptions as values
        :param clear: bool - Whether to clear the screen before rendering
        :return: `str.lower()` - Valid hotkey or `None` if invalid
        """
        # Clear the screen if specified
        if clear:
            self.cli_utils.clear_screen()

        # Print the title using Rich markup
        self.console.print(f"[bright_cyan]{title}[/bright_cyan]")
        
        # Generate the tree structure for the menu
        tree = Tree("[bold yellow]Options:[/bold yellow]")
        for hotkey, description in options.items():
            tree.add(f"[green]{hotkey}[/green] - {description}")
        self.console.print(tree)

        # Get and validate user input
        self.console.print()
        user_input = self.get_hotkey("Choose an option: ", options)
        Style.RESET_ALL # Reset the style after user input due to bugs in color rendering
        return user_input.lower() if user_input else None


    def validate_input(self, user_input: str, options: dict) -> bool:
        """
        Validates the user's input.
        :param user_input: str - User input to validate
        :param options: dict - Dictionary with hotkeys
        :return: bool - `True` if valid, `False` otherwise
        """
        return user_input.lower() in {key.lower() for key in options.keys()}



    def get_hotkey(self, prompt: str, options: dict) -> str | None:
        """
        Prompts the user for a hotkey and returns a valid one.
        :param prompt: str - Prompt to display
        :param options: dict - Dictionary with hotkeys
        :return: `str.lower()` - Valid hotkey or `None` if invalid
        """
        user_input = input(f"{Fore.YELLOW}{prompt}")
        if self.validate_input(user_input, options):
            return user_input.lower()
        else:
            return None