**Automated Web Interaction & Game Navigation Script – Documentation**

---

## Table of Contents

1. Project Overview
2. Key Features
3. Technology Stack & Dependencies
4. Environment Setup
5. Directory & Configuration Files
6. Script Structure & Main Workflow
7. Function Descriptions

   * 7.1 `scrldown(driver)`
   * 7.2 `scrlup(driver)`
   * 7.3 `darrow(driver)`
   * 7.4 `moregame(driver)`
   * 7.5 `notmoreg(driver)`
   * 7.6 `gamec(driver)`
   * 7.7 `do_task(browser_num, url)`
8. Multi-Threading & Concurrency
9. GoLogin Profile Management
10. Error Handling & Retry Logic
11. Security Considerations
12. Customization Guide
13. Troubleshooting
14. Keywords & Index
15. License & Author

---

## 1. Project Overview

This Python script automates web browsing tasks across multiple Chrome profiles via the **GoLogin** API. It:

* Launches multiple Chrome instances in parallel (threads).
* Logs in using randomized GoLogin profile IDs.
* Navigates to YouTube, plays videos, and interacts with a series of game portals.
* Simulates keyboard and mouse actions via **PyAutoGUI** (typing, scrolling).
* Randomizes timings to mimic human behavior.

It is ideal for automated testing, session isolation, and large-scale interaction with web content.

---

## 2. Key Features

* **Browser Profile Isolation**: Each thread uses a unique GoLogin profile.
* **Parallel Execution**: Multiple threads perform tasks concurrently.
* **Dynamic Interaction**: Functions to scroll, click “more games,” and handle in-frame elements.
* **Randomized Delays**: Introduces random sleep intervals to avoid detection.
* **Error Recovery**: Basic retry logic on failures during interactions.

---

## 3. Technology Stack & Dependencies

* **Python 3.8+**
* **Selenium**: Browser automation
* **GoLogin SDK**: Profile management
* **PyAutoGUI**: Simulated user input (keyboard/mouse)
* **threading**: Concurrency
* **subprocess**: Launching Chrome headlessly

Install dependencies via pip:

```bash
pip install selenium pyautogui gologin
```

Additionally, download the appropriate **chromedriver** binary and ensure it is in your `PATH`.

---

## 4. Environment Setup

1. **GoLogin Account**: Obtain your API token and profile IDs.
2. **path.txt**: Contains the path to your Chrome or Chromium executable for GoLogin.
3. **ids.txt**: One GoLogin profile ID per line.
4. **links.txt**: List of URLs to visit (e.g., game portals).
5. **Python Script**: Save as `automation.py` alongside the above files.

---

## 5. Directory & Configuration Files

```
/automation_project/
├── automation.py     # Main script
├── path.txt          # Chrome executable path
├── ids.txt           # GoLogin profile IDs
├── links.txt         # URLs to automate
├── chromedriver      # Selenium driver (executable)
└── README.md         # This documentation
```

---

## 6. Script Structure & Main Workflow

1. **Load Configuration**: Read `path.txt`, `ids.txt`, and `links.txt`.
2. **Define Interaction Functions**: Scroll, arrow keys, click game elements.
3. **`do_task()`**: For each thread:

   * Pick a random GoLogin profile.
   * Start profile, connect Selenium to its debugger address.
   * Navigate to YouTube, perform search and login actions via PyAutoGUI.
   * Iterate through `links.txt`, visiting each URL.
   * For each link, scroll randomly, call interaction functions (`moregame`, `gamec`, etc.).
   * Close browser and stop GoLogin session.
4. **Thread Management**: Create and start a thread for each target URL.
5. **Synchronization**: `join()` all threads before exiting.

---

## 7. Function Descriptions

### 7.1 `scrldown(driver)`

Sends a `PAGE_DOWN` keypress to the `<html>` element, scrolling the page.

### 7.2 `scrlup(driver)`

Sends a `PAGE_UP` keypress to scroll up.

### 7.3 `darrow(driver)`

Sends a `ARROW_DOWN` keypress with a random delay (2–10s) to mimic slow scroll.

### 7.4 `moregame(driver)`

Clicks the “more games” image button (`//img[@alt="more games"]`), then selects one of the resulting game icons.

### 7.5 `notmoreg(driver)`

Selects a random game category link (`//span[@style="text-transform: capitalize;"]`).

### 7.6 `gamec(driver)`

* Scrolls down 20 lines.
* Chooses a random game card (`.game-card undefined`) and clicks.
* If an in-frame “play” button (`#pluto-splash-button`) exists, switches to frame and clicks it.

### 7.7 `do_task(browser_num, url)`

Main thread function:

1. Randomly select a GoLogin profile ID.
2. Start GoLogin session and attach Selenium via `Options.experimental_option("debuggerAddress")`.
3. Navigate to YouTube, enter credentials via PyAutoGUI.
4. Loop through each URL from `links.txt`, visiting and calling interaction functions in random order and count.
5. Clean up: close WebDriver and stop GoLogin.

---

## 8. Multi-Threading & Concurrency

* Uses Python’s `threading.Thread` to run `do_task()` concurrently for each URL in `urls` list.
* Threads are started with a small delay (2s) to stagger profile launches.

---

## 9. GoLogin Profile Management

* **GoLogin** API initiates a profile with `profile_id` and `executable_path`.
* `start()` returns a `debugger_address` for remote debugging.
* Selenium attaches to this address, isolating cookies and localStorage per session.

---

## 10. Error Handling & Retry Logic

* Wrapped key interaction calls in `try/except` loops.
* On exception, script reloads the URL and retries typing steps.
* Consider enhancing with exponential backoff and logging in production.

---

## 11. Security Considerations

* **Profile IDs & Tokens** should be kept secret and not committed to source control.
* **Delay Randomization**: Reduces risk of bot detection.
* **Headless Mode**: Not used here; browsers are visible. For stealth, enable `--headless`.

---

## 12. Customization Guide

* **Game URLs**: Edit `links.txt` to include desired portals.
* **Profile Pool**: Add or remove IDs in `ids.txt`.
* **Chrome Path**: Update `path.txt` with the correct executable path per OS.
* **Interaction Steps**: Modify or extend functions in `automation.py`.

---

## 13. Troubleshooting

* **Chromedriver Version Mismatch**: Ensure `chromedriver` matches Chrome version.
* **GoLogin Errors**: Verify token validity and active profile subscription.
* **PyAutoGUI Failures**: Confirm window focus and correct screen resolution.

---

## 14. Keywords & Index

```
Selenium parallel threads
goLogin automation
dynamic profile debugging
pyautogui web interaction
game portal navigation
random delay automation
multithreaded Selenium Python
evade bot detection
automated game clicks
browser profile isolation
```

---

## 15. License & Author

**Author:** Smaron Biswas
**Date:** 2025
**License:** MIT License

This documentation is released under the MIT License. Feel free to adapt and extend the script for your own projects.
