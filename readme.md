# Python Pomodoro Application

<!-- ![Pomodoro App](pomodoro_app_screenshot.png) -->

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction

The Python Pomodoro Application is a simple and efficient time management tool based on the Pomodoro Technique. It helps you stay focused and productive by breaking work into intervals separated by short breaks.


## Features

- Set custom work and break intervals.
- Visual and audible notifications for work and break intervals.
- Pause and resume the timer.
- Track the number of completed Pomodoros.
- Configurable notification sounds.
- Simple and intuitive command-line interface.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine or download the ZIP file and extract it.

```bash
git clone https://github.com/SheikhMizan/Pomodoro.git
```

3. Navigate to the project directory.

```bash
cd Pomodoro
```

4. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

To start the Pomodoro timer, run the following command:

```bash
python pomodoro.py start
```

The application will prompt you to enter the duration of the work interval and the break interval in minutes. After setting the intervals, the Pomodoro timer will begin, and you'll receive visual and audible notifications at the end of each interval.

To pause the timer, press `Ctrl + C` in the terminal. To resume the timer, run the `start` command again.

To reset the number of completed Pomodoros, run:

```bash
python pomodoro.py reset
```

To display the help message and see all available commands, run:

```bash
python pomodoro.py --help
```

## Configuration

You can customize the application's behavior by modifying the `pomodoro.py` file. Here, you can change notification sounds, notification intervals, and other settings.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.

---

Happy Pomodoro-ing! If you have any questions or suggestions, feel free to open an issue or submit a pull request. Thanks for using the Python Pomodoro Application!
