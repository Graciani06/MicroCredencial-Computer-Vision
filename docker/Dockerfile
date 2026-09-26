# =============================================================================
# Imagen de desarrollo para curso de Computer Vision
#   - Ubuntu 24.04 + OpenCV 5.0.0 (compilado desde fuente, C++ y Python)
#   - Toolchain C++ (g++, cmake, ninja, gdb) y Python 3 (numpy, matplotlib, jupyter)
#   - GUI (imshow via GTK) usando el X11 del host, vídeo (FFmpeg) y webcam (V4L2)
#   - Soporte oficial: Linux. Sin servidor X en el host, imshow no abre ventanas.
# Build multi-stage: la etapa "builder" compila OpenCV y se descarta;
# la imagen final solo lleva los binarios y las librerías de runtime.
# =============================================================================

# ----------------------------- Etapa 1: builder ------------------------------
FROM ubuntu:24.04 AS builder

ARG OPENCV_VERSION=5.0.0

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake ninja-build git wget ca-certificates unzip \
    python3-dev python3-numpy \
    libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libavutil-dev \
    libv4l-dev \
    libjpeg-turbo8-dev libpng-dev libtiff-dev libwebp-dev \
    zlib1g-dev libtbb-dev \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O /tmp/opencv.tar.gz \
        https://github.com/opencv/opencv/archive/refs/tags/${OPENCV_VERSION}.tar.gz \
    && tar -xzf /tmp/opencv.tar.gz -C /tmp \
    && rm /tmp/opencv.tar.gz

RUN cmake -S /tmp/opencv-${OPENCV_VERSION} -B /tmp/build -G Ninja \
        -D CMAKE_BUILD_TYPE=Release \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D OPENCV_GENERATE_PKGCONFIG=ON \
        -D WITH_GTK=ON \
        -D WITH_FFMPEG=ON \
        -D WITH_V4L=ON \
        -D WITH_TBB=ON \
        -D BUILD_opencv_python3=ON \
        -D PYTHON3_PACKAGES_PATH=/usr/local/lib/python3.12/dist-packages \
        -D BUILD_TESTS=OFF \
        -D BUILD_PERF_TESTS=OFF \
        -D BUILD_EXAMPLES=OFF \
        -D BUILD_opencv_apps=OFF \
    && cmake --build /tmp/build \
    && cmake --install /tmp/build

# ------------------------- Etapa 2: imagen final ------------------------------
FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake ninja-build gdb pkg-config git nano \
    python3 python3-pip \
    libgtk-3-0 \
    libavcodec60 libavformat60 libswscale7 libavutil58 \
    libv4l-0 \
    libjpeg-turbo8 libpng16-16 libtiff6 libwebp7 libwebpdemux2 \
    libtbb12 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local
RUN ldconfig

RUN pip3 install --no-cache-dir --break-system-packages \
    numpy==1.26.4 \
    matplotlib==3.11.1 \
    jupyterlab==4.6.2


ARG USER_UID=1000
ARG USER_GID=1000
RUN groupmod -o -g ${USER_GID} ubuntu \
    && usermod -o -u ${USER_UID} -g ${USER_GID} ubuntu \
    && mkdir -p /workspace \
    && chown -R ${USER_UID}:${USER_GID} /workspace /home/ubuntu

USER ubuntu
WORKDIR /workspace

# Puerto de Jupyter
EXPOSE 8888

CMD ["/bin/bash"]
