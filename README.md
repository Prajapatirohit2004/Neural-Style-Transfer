# Neural-Style-Transfer

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: ROHIT KUMAR PRAJAPATI

*INTERN ID*: CITS218

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTOSH


# Neural Style Transfer

## Overview

The **Neural Style Transfer** project is an Artificial Intelligence (AI) and Deep Learning application that applies the artistic style of one image to another while preserving the original content. This project uses a pre-trained Neural Style Transfer model built with TensorFlow and TensorFlow Hub to generate visually appealing stylized images. By combining the content of a photograph with the artistic characteristics of a painting, the model creates a unique output that resembles digital artwork.

Neural Style Transfer is one of the most popular applications of Convolutional Neural Networks (CNNs) in computer vision. It demonstrates how deep learning techniques can separate the content and style of an image and intelligently merge them into a new image. This project is designed as a beginner-friendly AI application that showcases the practical use of pre-trained deep learning models without requiring users to train a model from scratch.

## Features

- Applies artistic styles to photographs using a pre-trained AI model.
- Preserves the original content while transferring artistic features.
- Supports custom content and style images.
- Automatically generates and saves the stylized output image.
- Displays the content, style, and generated images for comparison.
- Simple Python implementation with minimal code.
- Beginner-friendly and easy to customize.

## Technologies Used

- Python 3
- TensorFlow
- TensorFlow Hub
- NumPy
- Pillow (PIL)
- Matplotlib
- Deep Learning
- Convolutional Neural Networks (CNN)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Prajapatirohit2004/Neural-Style-Transfer.git
```

2. Navigate to the project directory:

```bash
cd Neural-Style-Transfer
```

3. Install the required dependencies:

```bash
pip install tensorflow
pip install tensorflow-hub
pip install pillow
pip install matplotlib
pip install numpy
```

4. Add your images:

- `content.jpg` – The original photograph.
- `style.jpg` – The artistic style image.

5. Run the project:

```bash
python style_transfer.py
```

## How It Works

The application first loads the content image and the style image, resizing them to a suitable resolution for processing. A pre-trained Neural Style Transfer model from TensorFlow Hub is then loaded. The model extracts the structural content from the content image and the artistic patterns, colors, and textures from the style image. These features are combined to generate a new stylized image that retains the scene of the original photograph while adopting the artistic appearance of the style image. Finally, the generated image is displayed on the screen and saved as **output.jpg** in the project directory.

## Applications

Neural Style Transfer has numerous real-world applications, including:

- Digital art creation
- Photo editing and enhancement
- Social media filters
- Graphic design
- Content creation
- Animation and gaming
- Advertising and marketing
- Educational AI demonstrations

## Future Enhancements

This project can be extended with several advanced features, such as:

- Support for multiple artistic styles.
- Real-time style transfer using webcam input.
- Batch processing of multiple images.
- Web application using Streamlit or Flask.
- Graphical User Interface (GUI) using Tkinter.
- Adjustable style intensity.
- High-resolution image generation.
- GPU acceleration for faster processing.

## Learning Outcomes

This project provided practical experience in Artificial Intelligence, Deep Learning, Computer Vision, and image processing using TensorFlow. It helped in understanding how pre-trained neural networks perform feature extraction, how convolutional neural networks process visual information, and how transfer learning can be applied to solve creative image transformation tasks efficiently. Additionally, the project strengthened Python programming skills and familiarity with popular AI libraries.

## Conclusion

The Neural Style Transfer project demonstrates the power of Artificial Intelligence in transforming ordinary photographs into artistic creations. By leveraging a pre-trained TensorFlow model, the application performs high-quality style transfer efficiently without requiring extensive computational resources or model training. This project serves as an excellent introduction to Deep Learning and Computer Vision while showcasing the practical applications of neural networks in creative image generation. It also provides a strong foundation for exploring more advanced AI techniques and developing intelligent image processing applications in the future.

<img width="1500" height="500" alt="Neural_style_Transfer_Output" src="https://github.com/user-attachments/assets/9ed485b9-a21b-48ae-a773-145c75a02d1b" />
