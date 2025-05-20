import json
import numpy as np

# Load meta info
with open("meta.json") as f:
    meta = json.load(f)

sample_rate = meta["capture"]["samples_per_second"]
print(f"Sample rate: {sample_rate} Hz")

# === CONFIGURE THESE ===
baud_rate = 115200          # Try common ones: 9600, 19200, 57600, 115200
channel_file = "digital-0.bin"  # Try digital-1.bin if needed

# Load digital signal (each bit is 0 or 1)
data = np.fromfile(channel_file, dtype=np.uint8)

samples_per_bit = int(sample_rate / baud_rate)
print(f"Samples per bit: {samples_per_bit}")

decoded_bytes = []
i = 0
while i < len(data) - samples_per_bit * 10:
    if data[i] == 0:  # Start bit detected
        # Sample in the middle of each bit
        byte = 0
        for bit in range(8):
            sample_index = i + (bit + 1) * samples_per_bit
            if data[sample_index] == 1:
                byte |= (1 << bit)
        decoded_bytes.append(byte)
        i += samples_per_bit * 10  # Move to the next byte frame
    else:
        i += 1

# Print result
text = ''.join([chr(b) if 32 <= b < 127 else '.' for b in decoded_bytes])
print("\nDecoded UART output:")
print(text)
