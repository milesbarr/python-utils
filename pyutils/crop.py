from PIL import Image


def crop_image_to_aspect_ratio(
    im: Image, aspect_ratio: tuple[int, int]
) -> Image:
    """Crop an image to match a specified aspect ratio.

    Args:
        im (Image): The image to be cropped.
        aspect_ratio (tuple[int, int]): The target aspect ratio in the
            form (width, height).

    Returns:
        Image: The cropped image with the specified aspect ratio.
    """
    w, h = im.size
    rw, rh = aspect_ratio
    if w * rh > h * rw:
        new_width = h * rw // rh
        left = (w - new_width) // 2
        box = (left, 0, w - left, h)
    else:
        new_height = w * rh // rw
        top = (h - new_height) // 2
        box = (0, top, w, h - top)
    return im.crop(box)


def crop_image_to_aspect_ratio_and_shrink(
    im: Image, size: tuple[int, int]
) -> Image:
    """Crop and shrink an image to a specified size.

    Args:
        im (Image): The image to be processed.
        size (tuple[int, int]): The target size in the form (width,
            height).

    Returns:
        Image: The processed image resized to the target size.
    """
    im = crop_image_to_aspect_ratio(im, size)
    if im.size > size:
        im = im.resize(size)
    return im
