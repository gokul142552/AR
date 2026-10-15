AR 🐍

Animated Terminal Text & Box Renderer for Python

AR is a small Python library created by Gokul Dahal, Nepal. It provides animated terminal text and dynamically sized text boxes to make command-line programs look more interesting.

Built while developing a text-based zombie RPG. ⚔️

✨ Features

- ⌨️ Character-by-character text animation
- 💬 Word-by-word text animation
- 📦 Dynamically sized text boxes
- 🎨 Custom box titles and multiple text lines
- ⚡ Lightweight — uses Python's standard library
- 🧩 Simple class-based interface with static methods

📥 Installation

AR is currently an early-development project.

1. Download "ar.py" from this repository.
2. Place it in your Python project's directory.
3. Import the "AR" class into your Python file.

from ar import AR

No external packages are required by the code shown in the current version.

⌨️ Animated Text

Use "AR.animation()" to display text with a typing effect.

Example

from ar import AR

AR.animation("Hello, world!")

Parameters

Parameter| Type| Default| Description
"text"| "str"| Required| The text to display
"delay"| "float"| "0.015"| Delay between characters or words, in seconds
"space"| "bool"| "True"| Prints a newline after the animation
"wbw"| "bool"| "False"| Enables word-by-word animation when "True"

Character-by-character animation

AR.animation("Loading the game...", delay=0.03)

Word-by-word animation

AR.animation(
    "Welcome to the game!",
    delay=0.2,
    wbw=True
)

Control the newline

AR.animation("Loading...", space=False)

Setting "space=False" prevents the function from printing a newline after the animation.

📦 Animated Text Box

Use "AR.draw()" to display multiple lines inside a box. Its width adjusts automatically to fit the longest line.

Example

from ar import AR

AR.draw(
    "COMBAT",
    "Zombie defeated!",
    "EXP +20",
    "HP: 75",
    "LEVEL UP!"
)

Output

COMBAT
---------------------
| Zombie defeated!  |
| EXP +20           |
| HP: 75            |
| LEVEL UP!         |
---------------------

Output shown for illustration; exact border length depends on the longest line.

Parameters

Parameter| Description
"title"| The title displayed above the box
"*texts"| One or more text lines displayed inside the box

Important: At least one text line must be supplied to "AR.draw()".

Another example

AR.draw(
    "PLAYER STATUS",
    "Name: Gokul",
    "Level: 5",
    "Health: 100",
    "EXP: 20/100"
)

Each line inside the box is displayed using "AR.animation()" with its default settings.

🧪 Requirements

- Python 3
- A terminal that supports the ANSI cursor-control sequences used by the animation function

🚧 Project Status

Early development — v0.1.0

AR is a learning project, and its features and API may change as development continues.

🛠️ Planned Improvements

- [ ] Custom animation settings for text boxes
- [ ] More box styles and border characters
- [ ] Additional terminal UI utilities
- [ ] Improved error handling and input validation

👨‍💻 Author

Gokul Dahal, Nepal

Created while learning Python and building a text-based RPG.

---

⭐ If you find this project interesting, consider starring the repository!
