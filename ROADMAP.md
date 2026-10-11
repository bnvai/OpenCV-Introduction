# Roadmap

Auto-generated from [syllabus.json](syllabus.json) and notebook status by `python tools/cvtool.py sync`.
Legend: ✅ done · 🚧 in progress · ⬜ todo

<!-- mindmap:start -->
```mermaid
mindmap
  root((OpenCV Intro))
    Part 1: Classical 2D Image Processing
      🚧 01 Images as Arrays
      ⬜ 02 Image Arithmetic
      ⬜ 03 Thresholding, Erosion, and Dilation
      ⬜ 04 Flood Fill and Connected Components
      ⬜ 05 Image Moments
      ⬜ 06 Eigenvectors and Eigenvalues of the Moment Covariance Matrix
      ⬜ 07 Distance Measures
      ⬜ 08 Geometric Transformations
      ⬜ 09 Image Warping, Inverse Mapping, and Bilinear Interpolation
      ⬜ 10 Convolution
      ⬜ 11 Smoothing and Gaussian Pyramids
      ⬜ 12 Differentiation and Edge Detection
      ⬜ 13 Second Derivatives and the Laplacian
      ⬜ 14 Nonlinear Filters
      ⬜ 15 The Fourier Transform and Frequency-Domain Filtering
      ⬜ 16 Wavelets and Gabor Filters
      ⬜ 17 Image Compression - Lossless and Lossy
      ⬜ 18 Color Spaces
      ⬜ 19 Clustering - k-Means, GMMs, and DBSCAN
    Part 2: Classical 3D Computer Vision
      ⬜ 20 Feature Detection and Matching
      ⬜ 21 Optical Flow and Motion Estimation
      ⬜ 22 Stereo Matching
      ⬜ 23 Model Fitting, Robust Estimation, and RANSAC
      ⬜ 24 Projective Geometry
      ⬜ 25 Image Stitching and Mosaicking
      ⬜ 26 Image Formation
      ⬜ 27 Camera Calibration
      ⬜ 28 Epipolar Geometry
      ⬜ 29 Structure from Motion
    Part 3: Deep Learning for Computer Vision
      ⬜ 30 Projection - The Central Idea
      ⬜ 31 Neural Network Fundamentals
      ⬜ 32 Multi-Layer Perceptrons
      ⬜ 33 Optimization
      ⬜ 34 Convolutional Neural Networks
      ⬜ 35 Training a CNN
      ⬜ 36 Image Classification in Practice
      ⬜ 37 Classic Architectures
      ⬜ 38 Transfer Learning
      ⬜ 39 Visualizing and Understanding CNNs
      ⬜ 40 Object Detection from Sliding Windows
      ⬜ 41 Object Detection as Regression
      ⬜ 42 Semantic Segmentation
      ⬜ 43 Instance Segmentation
      ⬜ 44 Precision and Parallel Training
```
<!-- mindmap:end -->

## Learning arc

| Part | Theme | Why it matters |
|---|---|---|
| I | Pixels, filters, features of a single image | Foundation for every later step; the OpenCV everyday toolkit |
| II | Geometry across views: matching, stereo, calibration, SfM | Robotics, AR, 3D reconstruction |
| III | Learned representations: CNNs, detection, segmentation | Modern production CV |
