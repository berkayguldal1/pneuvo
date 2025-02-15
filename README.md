# Quntal

**Quntal** is a fun, interactive and lightweight terminal simulation environment designed to simulate a Linux-like experience with a playful and custom shell. It includes features like user authentication, package simulation, system info commands, and an extensible framework for running Python-based scripts.

## Features

- **User Authentication**: Allows users to create accounts and securely log in using a username and password stored in `login.dll`.
- **System Info**: Commands like `nelfetch` display mock system information similar to `neofetch`, providing details about the simulated OS, Kernel, and hardware.
- **Package Simulation**: Users can install and manage fictional packages with the `pakage install` command.
- **Python Script Execution**: Execute Python scripts directly from the terminal by typing their name (as long as they exist in the current directory).
- **Customizable Shell**: The default shell is `yash`, but you can extend the functionality by adding more commands.
  
## Installation

To get started with **Quntal**, clone the repository and run the Python script:

```bash
git clone https://github.com/yourusername/quntal.git
cd quntal
python3 quntal.py
