# Translator

A simple PyQt5 application for converting between Simplified Chinese and Traditional Chinese characters.

## Getting Started

### Prerequisites

Before running the application, ensure you have the required dependencies installed by running:

```bash
pip install -r requirements.txt
```

### Installation

You can build and package the application using PyInstaller. Here are the steps to package it for macOS:

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Build the application using PyInstaller:

   ```bash
   pyinstaller --name "translator" --windowed app.py
   ```

   This command will create a `dist` directory containing the standalone application.

4. To create a macOS DMG (Disk Image) for distribution, you can use a tool like Image2icon to create a custom application icon and replace the default icon in the `dist` directory.

5. Run the application from the `dist` directory:

   ```bash
   cd dist
   ./translator
   ```
