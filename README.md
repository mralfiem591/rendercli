# RenderCli

> A Python library for creating and rendering visually appealing Command-Line Interface (CLI) menus.

RenderCli is a Python class designed to create and render visually appealing Command-Line Interface (CLI) menus. It uses the `rich` library for styled output and provides utilities for handling user input and validation.

## Features

- **Dynamic Menus**: Render customizable CLI menus with titles and options.
- **Rich Styling**: Leverages the `rich` library for colorful and structured output.
- **Input Validation**: Ensures user input matches predefined hotkeys.
- **Cross-Platform Compatibility**: Uses `colorama` for consistent behavior across platforms.
- **Reusable Utilities**: Includes helper methods for clearing the screen and validating input.

## Installation

To use RenderCli, ensure the following Python libraries are installed:

```bash
pip install rich colorama
```

## Usage

### Example Code

```python
from clirender import RenderCli

# Initialize RenderCli
cli = RenderCli()

# Define menu options
menu_title = "Main Menu"
menu_options = {
    "1": "Option 1",
    "2": "Option 2",
    "q": "Quit"
}

# Render the menu and get user input
selected_hotkey = cli.render_menu(menu_title, menu_options)

# Handle user input
if selected_hotkey == "1":
    print("You selected Option 1!")
elif selected_hotkey == "2":
    print("You selected Option 2!")
elif selected_hotkey == "q":
    print("Exiting...")
else:
    print("Invalid selection.")
```

### Methods

#### `render_menu(title: str, options: dict, clear: bool = True) -> str | None`

Renders a CLI menu with a title and options, waits for user input, and validates it.

- **Parameters**:
  - `title` (str): The title of the menu.
  - `options` (dict): A dictionary of hotkeys and their corresponding descriptions.
  - `clear` (bool): Whether to clear the screen before rendering (default: `True`).
- **Returns**: A valid hotkey as a lowercase string, or `None` if invalid.

#### `validate_input(user_input: str, options: dict) -> bool`

Validates if the user's input matches one of the provided hotkeys.

- **Parameters**:
  - `user_input` (str): The input to validate.
  - `options` (dict): A dictionary of hotkeys.
- **Returns**: `True` if valid, `False` otherwise.

#### `get_hotkey(prompt: str, options: dict) -> str | None`

Prompts the user for a hotkey and validates the input.

- **Parameters**:
  - `prompt` (str): The prompt to display.
  - `options` (dict): A dictionary of hotkeys.
- **Returns**: A valid hotkey as a lowercase string, or `None` if invalid.

**For normal usage, `render_menu` is the main method to call, as it handles rendering the menu, capturing user input, and validating user input.**

## Dependencies

- [rich](https://pypi.org/project/rich): For styled CLI output.
- [colorama](https://pypi.org/project/colorama): For cross-platform console color support.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Author

Created by [@mralfiem591](https://github.com/mralfiem591). Contributions and feedback are welcome!
