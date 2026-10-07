#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/photo.hpp>
#include <string>
#include <utility>
#include <vector>

const std::string IMAGE = "../data/dog.jpg";

/**
 * Convierte img en una imagen con estilo propio...
 *
 * @param img  imagen de entrada, en color (BGR)
 * @return la imagen con el efecto, en BGR (CV_8UC3) y del mismo tamaño que img
 */
cv::Mat cartoonize(const cv::Mat& img) {
    //// TODO: CODE HERE
    cv::Mat result = img.clone();
    //// END TODO
    return result;
}

/**
 * Los efectos que ya trae OpenCV en el módulo photo, para compararlos con el propio.
 *
 * @param img  imagen de entrada, en color (BGR)
 * @return lista de pares {nombre de ventana, imagen} con cada efecto
 */
std::vector<std::pair<std::string, cv::Mat>> photoEffects(const cv::Mat& img) {
    cv::Mat stylized, preserved, sketchGray, sketchColor, detailed;
    cv::stylization(img, stylized, 60, 0.45f);
    cv::edgePreservingFilter(img, preserved, cv::RECURS_FILTER, 60, 0.4f);
    cv::pencilSketch(img, sketchGray, sketchColor, 60, 0.07f, 0.02f);  // dos resultados
    cv::detailEnhance(img, detailed, 10, 0.15f);
    return {
        {"stylization", stylized},
        {"edgePreservingFilter", preserved},
        {"pencilSketch (gray)", sketchGray},
        {"pencilSketch (colour)", sketchColor},
        {"detailEnhance", detailed},
    };
}

int main() {
    //// Cargar la imagen en color
    cv::Mat img = cv::imread(IMAGE);
    if (img.empty()) {
        std::cerr << "Error: could not read the image" << std::endl;
        return 1;
    }

    cv::Mat cartoon = cartoonize(img);
    cv::imshow("cartoon", cartoon);
    for (const auto& [name, effect] : photoEffects(img)) {
        cv::imshow(name, effect);
    }
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}
