# irregular_chars

irregular_chars is a library for cleaning text, such as removing zero-width characters or converting full-width characters to half-width.

## Installation

You can install the package via pip:
```bash
pip install irregular_chars
```

## Usage

Here is a simple example:
```py
from textcleaning import remove_zero_width_chars

text = "Hello\u200BWorld"
clean_text = remove_zero_width_chars(text)
print(clean_text)  # Outputs: HelloWorld
```
