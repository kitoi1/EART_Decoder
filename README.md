# UART Signal Decoder

This Python script decodes UART signals from a digital binary file using metadata from a JSON file.

## Overview

The script reads a digital signal (binary file) sampled at a given rate, then decodes UART serial data based on a specified baud rate. The decoded ASCII output is printed to the console.

## Features

- Loads capture metadata (sample rate) from `meta.json`.
- Reads digital samples from a binary file (e.g., `digital-0.bin`).
- Supports configurable baud rates.
- Decodes UART data assuming 1 start bit, 8 data bits, and no parity or stop bits.
- Prints the decoded text, replacing non-printable characters with dots (`.`).

## Requirements

- Python 3.6+
- NumPy

## Installation

Install dependencies via pip:

```bash
pip install -r requirements.txt
