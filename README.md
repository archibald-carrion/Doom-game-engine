# Doom game engine
Pseudo 3D basic game engine written in Python using Pygame to create Doom-like video games.
This project is a personal challenge to learn more about game development and 3D rendering, if you want to see my other projects, you can visit my [GitHub profile](https://github.com/archibald-carrion).

## Dependencies
This code was written in Python 3.10.6, and uses the following libraries:
-pygame 2.1.2

The program also use other python modules such as:
-os
-sys
-math
-time
-random

But these modules are included in the Python standard library, so you should not have to install them.

## Installation
You can install the required libraries using pip:
```bash
pip install pygame
```

## Usage
To run the program, you can use the following command:
```bash
python main.py
```
Or you can build th program using pyinstaller:
```bash
pyinstaller --onefile -w main.py
```
But you will need to install pyinstaller first:
```bash
pip install pyinstaller
```
The main.exe file will be created in the dist folder, to run the program you need to move the main.exe file to the root folder of the project where the resources folder is located, you can either move it manually or use the following command:
```bash
move dist\main.exe main.exe
```
Then you can run the program by double-clicking on the main.exe file, you no longer need the dist folder nor the build folder, you can delete them.

## Screenshots
![doom-like screenshot #0](https://github.com/archibald-carrion/Doom-game-engine/blob/main/resources/readme/screenshot0.png)
![doom-like screenshot #1](https://github.com/archibald-carrion/Doom-game-engine/blob/main/resources/readme/screenshot1.png)
