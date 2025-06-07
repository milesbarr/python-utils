# Python Utils

A collection of handy Python utility scripts for everyday development tasks.
These utilities are designed to save time and reduce boilerplate for common
programming needs.

## Features

- **Image Cropping**: Crop images to specific aspect ratios with
  [`crop.py`](crop.py).
- **Function Debouncing**: Debounce function calls to limit execution frequency
  with [`debounce.py`](debounce.py).
- **File Modification Comparison**: Check if one file is newer than another with
  [`file.py`](file.py).
- **Stripping Markdown**: Remove Markdown formatting from text with
  [`markdown.py`](pyutils/markdown.py).
- **MD5 Hash Validation**: Check if a string is a valid MD5 hash with
  [`md5.py`](md5.py).
- **Slugify Strings**: Convert any string into a URL-friendly slug with
  [`slugify.py`](slugify.py).

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/milesbarr/python-utils@main
```

Or clone the repository and install locally:

```bash
git clone https://github.com/milesbarr/python-utils.git
cd python-utils
pip install .
```

## Usage

You can use these utilities by copying the desired script(s) into your project
or by importing them directly if installed as a package:

```python
from pyutils import (
    crop_image_to_aspect_ratio,
    crop_image_to_aspect_ratio_and_shrink,
    debounce,
    is_file_newer,
    strip_markdown,
    is_md5,
    slugify,
)
```

Crop an image to an aspect ratio:

```python
from pyutils import crop_image_to_aspect_ratio

crop_image_to_aspect_ratio("input.jpg", "output.jpg", (16, 9))
```

Crop an image to an aspect ratio and shrink it to the specified size:

```python
from pyutils import crop_image_to_aspect_ratio_and_shrink

crop_image_to_aspect_ratio_and_shrink("input.jpg", "output.jpg", (1920, 1080))
```

Debounce a function:

```python
from pyutils import debounce

@debounce(0.5)
def my_function():
    print("Called!")
```

Check if one file is newer than another:

```python
from pyutils import is_file_newer

if not is_file_newer("output.html", "input.md"):
  print("Changed!")
```

Strip Markdown formatting from a string:

```python
from pyutils import strip_markdown

print(strip_markdown("**Bold** and *italic* text"))
# Output: Bold and italic text
```

Validate an MD5 hash:

```python
from pyutils import is_md5

print(is_md5("098f6bcd4621d373cade4e832627b4f6"))  # Output: True
```

Slugify a string:

```python
from pyutils import slugify

print(slugify("Hello, World!"))  # Output: hello-world
```

Refer to each script for function documentation and usage examples.

## License

This project is licensed under the [MIT License](LICENSE).
