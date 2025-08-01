# Crossword Puzzle Game

A simple crossword puzzle game built with [Kivy](https://kivy.org), a Python framework for cross-platform app development. This project targets Android deployment, featuring a 5x5 grid with interactive letter input and answer validation. It’s designed for minimal graphics overhead, ideal for Python developers creating lightweight puzzle games.

## Project Management
The project will be managed using HacknPlan here: https://app.hacknplan.com/p/225329/dashboards/project

## Features
- 5x5 crossword grid with active (white) and inactive (black) cells.
- Single-letter input via `TextInput` widgets, restricted to alphabetic characters.
- "Check Answers" button with color feedback (green for correct, red for incorrect).
- Cross-platform development with easy Android packaging using Buildozer.
- Extensible for clues, larger grids, or dynamic puzzle generation.

## Prerequisites
- **macOS**: Ventura, Sonoma, or later.
- **Python**: 3.7–3.10 (3.10 recommended). Verify with:
  ```bash
  python3 --version
  ```
  Install via Homebrew if needed:
  ```bash
  brew install python@3.10
  ```
- **VS Code**: For coding and debugging (optional but recommended).
- **Terminal**: For setup and deployment.
- **Android Device/Emulator**: For testing APKs.

## Setup Instructions (macOS)

### 1. Create Project Directory and Virtual Environment
1. Open Terminal (or VS Code’s integrated Terminal).
2. Create and navigate to the project directory:
   ```bash
   mkdir crossword_game
   cd crossword_game
   ```
3. Create a virtual environment (`venv`):
   ```bash
   python3 -m venv .venv
   ```
4. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
   Deactivate later with:
   ```bash
   deactivate
   ```

### 2. Install Kivy and Dependencies
1. Upgrade pip:
   ```bash
   pip install --upgrade pip
   ```
2. Install Kivy:
   ```bash
   pip install kivy[base]
   ```
   If errors occur (e.g., SDL2 issues), install dependencies:
   ```bash
   brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer
   ```
   Retry Kivy installation.
3. Verify Kivy with `test_kivy.py`:
   ```python
   from kivy.app import App
   from kivy.uix.label import Label

   class TestApp(App):
       def build(self):
           return Label(text="Kivy is working!")

   if __name__ == '__main__':
       TestApp().run()
   ```
   Save as `test_kivy.py` and run:
   ```bash
   python test_kivy.py
   ```
   A window should display “Kivy is working!”.

### 3. Install Buildozer for Android Packaging
1. Install Homebrew (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Buildozer dependencies:
   ```bash
   brew install pkg-config autoconf automake
   pip install cython==0.29.36
   pip install buildozer
   ```
3. Install Android SDK:
   ```bash
   brew install android-sdk
   ```
   Set the SDK path:
   ```bash
   export ANDROID_HOME=/usr/local/share/android-sdk
   echo 'export ANDROID_HOME=/usr/local/share/android-sdk' >> ~/.zshrc
   source ~/.zshrc
   ```
4. Accept SDK licenses:
   ```bash
   $ANDROID_HOME/tools/bin/sdkmanager --licenses
   ```
   Press `y` for all prompts.
5. Initialize Buildozer:
   ```bash
   buildozer init
   ```
   Edit `buildozer.spec` with settings like `title=Crossword Puzzle`, `package.name=crossword`, `requirements=python3,kivy`, and `android.api=33`.

### 4. Configure VS Code
1. Open the project in VS Code:
   ```bash
   code .
   ```
2. Select the `venv` interpreter:
   - Press `Cmd+Shift+P`, type “Python: Select Interpreter,” choose `./.venv/bin/python`.
3. Install extensions:
   - **Python** (ms-python.python): Linting, debugging.
   - **Pylance** (ms-python.vscode-pylance): Code completion.
   - **Kivy Language**: For `.kv` file support (optional).
4. Create `.vscode/launch.json` for debugging:
   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Run Kivy App",
               "type": "python",
               "request": "launch",
               "program": "${file}",
               "console": "integratedTerminal",
               "python": "${workspaceFolder}/.venv/bin/python"
           }
       ]
   }
   ```

### 5. Test Android Deployment
1. Connect an Android device (enable Developer Mode, USB Debugging) or set up an emulator via Android Studio.
2. Build and deploy the APK:
   ```bash
   buildozer android debug deploy run
   ```
   For emulators, use:
   ```bash
   buildozer android debug deploy run --device emulator-5554
   ```
   (Replace `emulator-5554` with your emulator’s ID from `adb devices`.)
3. Check the `bin` folder for the APK.

### 6. Run the Crossword App
1. Use the provided `crossword_app.py` (a 5x5 crossword grid with input and validation).
2. Run locally:
   ```bash
   python crossword_app.py
   ```
   Or press `F5` in VS Code.
3. Test on Android after building the APK.

### 7. Prepare for Google Play
1. Build a release APK:
   ```bash
   buildozer android release
   ```
2. Sign the APK with `jarsigner` (see Kivy/Buildozer docs).
3. Create a Google Play Developer account ($25 one-time fee).
4. Upload the signed APK with a privacy policy.

## Development Workflow
- **Code**: Extend `crossword_app.py` for clues, larger grids, or puzzle generation.
- **AI Assistance**: Use **GPT-4o Mini** (~$0.15/$0.60 per million tokens, https://openai.com/api/pricing) for:
  - Generating Kivy code (e.g., “Add a ScrollView for crossword clues”).
  - Debugging (e.g., “Fix Buildozer error: [specific error]”).
  - Puzzle logic (e.g., “Write a Python crossword generator”).
  - Free alternatives: **Qwen 2.5 Coder** (local) or **HuggingChat** (web-based).
- **Version Control**: Initialize Git:
  ```bash
  git init
  echo ".venv/" >> .gitignore
  echo "bin/" >> .gitignore
  git add .
  git commit -m "Initial project setup"
  ```
- **Backup Dependencies**:
  ```bash
  pip freeze > requirements.txt
  ```

## Project Structure
```
crossword_game/
├── .venv/              # Virtual environment
├── bin/                # APKs generated by Buildozer
├── .buildozer/         # Buildozer cache
├── .vscode/            # VS Code settings
│   └── launch.json
├── crossword_app.py    # Main Kivy app
├── buildozer.spec      # Buildozer configuration
├── requirements.txt    # Dependencies
└── .gitignore          # Git ignore file
```

## Next Steps
- Add clues using a `ScrollView` with `Label` widgets.
- Implement a crossword generator in Python.
- Style the UI with colors or minimal PNGs.
- Test on multiple Android devices (API 21+).

## Resources
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Real Python Kivy Tutorial](https://realpython.com/mobile-app-kivy-python/)
- [Google Play Developer Console](https://play.google.com/console/)

For issues or enhancements, consult GPT-4o Mini or open an issue on this repository.