
from PIL import Image
import random
import math

class RGBSplitter:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "image": ("IMAGE",),
                              }}
    RETURN_TYPES = ("IMAGE","IMAGE","IMAGE",)
    FUNCTION = "composite"
    CATEGORY = "image"

    def composite(self, image):
        print(type(image))
        print(image.size())
        R = image.clone()
        R[:, :, :, 1:3] = 0

        G = image.clone()
        G[:, :, :, [0, 2]] = 0

        B = image.clone()
        B[:, :, :, 0:2] = 0
        return (R,G,B,)

class RGBCombiner:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "r": ("IMAGE",),"g": ("IMAGE",),"b": ("IMAGE",),
                              }}
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "composite"
    CATEGORY = "image"

    def composite(self, r,g,b):
        recombined_tensor = r.clone()
        recombined_tensor[:, :, :, 1] = g[:, :, :, 1]
        recombined_tensor[:, :, :, 2] = b[:, :, :, 2]

        return (recombined_tensor,)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "MyRGBSplitter": RGBSplitter,
    "MyRGBCombiner": RGBCombiner,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "MyRGBSplitter": "RGB Splitter",
    "MyRGBCombiner": "RGB Combiner",
}