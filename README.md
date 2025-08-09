# filmlab-cli

A simple command-line tool for film photographers.

This utility processes scanned film negatives or positives. It performs basic exposure and contrast adjustments using Python and Pillow. It’s designed for quick tweaks when digitising analog film.

## Features

- Adjust exposure of your scans on the fly
- Tweak contrast for a punchy or soft look
- Built with Pillow and Click
- Simple codebase—extend it for your own experiments

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python filmlab_cli.py input.jpg output.jpg --exposure 1.1 --contrast 0.9
```

This reads `input.jpg`, applies an exposure multiplier and a contrast factor, and writes the result to `output.jpg`.

## Contributing

Bug reports, ideas, and pull requests are welcome! See `CONTRIBUTING.md` for guidelines.
