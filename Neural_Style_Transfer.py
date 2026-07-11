import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# -----------------------------
# Function to load image
# -----------------------------
def load_image(image_path, image_size=(512, 512)):
    img = Image.open(image_path)
    img = img.resize(image_size)
    img = np.array(img).astype(np.float32) / 255.0

    # Keep only RGB channels
    if img.shape[-1] == 4:
        img = img[..., :3]

    img = img[np.newaxis, :]
    return tf.convert_to_tensor(img)

# -----------------------------
# Load images
# -----------------------------
content_image = load_image("content.jpg")
style_image = load_image("style.jpg")

# -----------------------------
# Load pretrained model
# -----------------------------
print("Loading TensorFlow Hub model...")

model = hub.load(
    "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
)

print("Model loaded successfully!")

# -----------------------------
# Apply style transfer
# -----------------------------
stylized_image = model(content_image, style_image)[0]

# -----------------------------
# Save output
# -----------------------------
output = tf.squeeze(stylized_image)
output = tf.clip_by_value(output, 0.0, 1.0)
output = Image.fromarray((output.numpy() * 255).astype(np.uint8))
output.save("output.jpg")

print("Style transfer completed successfully!")
print("Output saved as output.jpg")

# -----------------------------
# Display images
# -----------------------------
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(tf.squeeze(content_image))
plt.title("Content Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(tf.squeeze(style_image))
plt.title("Style Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(output)
plt.title("Stylized Image")
plt.axis("off")

plt.show()
