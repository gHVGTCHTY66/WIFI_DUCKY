🦆 WiFi Ducky (Modified Atom Ducky for Pico W)

🚨 Important This is a modified version of Atom Ducky, tailored for easy setup and smooth usability, specifically for Raspberry Pi Pico W. If you're a beginner or just want a plug-and-play HID tool without deep technical errors and complications—this is for you.

💡 What is WiFi Ducky? WiFi Ducky is a custom version of the Atom Ducky project, built to run on Raspberry Pi Pico W. It acts like a BadUSB Rubber Ducky device with a web interface, allowing you to inject keystroke payloads wirelessly.

This version was created after I tried the original and faced multiple setup errors. So I modified and cleaned up the project to ensure:

✅ Smoother setup process

✅ Works without BLE (Bluetooth Low Energy)

✅ Tested on Raspberry Pi Pico W

✅ Beginner-friendly usability

⚠️ For educational and ethical hacking purposes only. Do not misuse this tool.

📌 What’s Modified?

Removed unnecessary features to make it lightweight and fast

Cleaned and simplified configuration files

Removed BLE dependencies for better compatibility with Pico W

Improved the web interface experience

Ensured stable HID injection over WiFi

Added troubleshooting fixes for CircuitPython and Pico compatibility

✅ Supported Hardware This version is made and tested on:

Raspberry Pi Pico W (⚠️ Pico W has WiFi but no BLE – this version does NOT require BLE.)

Make sure your board supports:

✅ HID (Keyboard emulation)

✅ WiFi

❌ No BLE required

🔥 Features

Web-based GUI (Access via browser over WiFi)

Rubber Ducky-like HID keystroke injection

Create and edit payloads directly from browser

Live keyboard simulation

Switch between Normal and Rubber mode

USB drive hiding option (optional)

WiFi Access Point mode support

🧠 Why This Version?

The original Atom Ducky is powerful, but:

It can be overwhelming for beginners

It throws errors on boards like Raspberry Pi Pico W

BLE-related code isn’t needed for most use-cases

Setup steps are complex and spread out

So I built WiFi Ducky to be:

💻 Easy to install 📱 Easy to use ⚙️ Easy to configure

⚠️ Disclaimer This project is meant for educational and ethical hacking demonstrations only. Do not use it on systems you do not own or have explicit permission to test. I am not responsible for any misuse or damage caused by this tool.

❤️ Credits Original Project: Atom Ducky by FLOCK4H || Modified and simplified by: panic-malware
