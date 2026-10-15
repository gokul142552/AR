AR 🐍

AR is a small Python library for animated terminal text and text-based user interface (TUI) components.

Built by Gokul Dahal, Nepal 🇳🇵

✨ Features

- Animated character-by-character text
- Word-by-word text animation
- Dynamic-width text boxes
- Customizable animation speed
- Reusable class-based methods

📦 Installation

Download "ar.py" and place it in your Python project's directory.

Import the library:

from ar import AR

🎬 Animation

AR.animation(text, delay=0.015, space=True, wbw=False)

Parameters

Parameter| Type| Default| Description
"text"| "str"| Required| The text to display.
"delay"| "float"| "0.015"| Time delay in seconds between characters or words.
"space"| "bool"| "True"| Prints a newline after the animation if enabled.
"wbw"| "bool"| "False"| Enables word-by-word animation when "True"; otherwise, animates character by character.

Example

AR.animation("Hello, world!")
AR.animation("Loading...", delay=0.1)
AR.animation("A zombie approaches!", wbw=True)
AR.animation("Done!", space=False)

🖥️ Draw a Text Box

AR.draw(title, *texts)

Draws a bordered text box whose width adjusts automatically to the longest text line.

Parameters

Parameter| Type| Description
"title"| "str"| The heading displayed above the box.
"*texts"| "str" arguments| One or more text lines displayed inside the box. The box width is determined by the longest line.

Example

AR.draw(
    "INFO",
    "KILLED THE ZOMBIE!",
    "EXP +20",
    "HP: 75",
    "LEVEL UP!"
)

Output:

INFO
----------------------
| KILLED THE ZOMBIE! |
| EXP +20            |
| HP: 75             |
| LEVEL UP!          |
----------------------

You can pass as many text lines as needed without adding more parameters to the function.

Note: At least one text line is required by the current implementation.

🚧 Project Status

AR is currently in early development. Features, parameters, and usage may change as the project evolves.

👨‍💻 Author

Gokul Dahal, Nepal 🇳🇵
