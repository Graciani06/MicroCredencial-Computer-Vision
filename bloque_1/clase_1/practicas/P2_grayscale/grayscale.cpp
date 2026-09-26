#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <vector>


// Gris como la media plana de los tres canales: (B + G + R) / 3.
// No usar cvtColor.
// Devuelve una imagen de 1 canal y tipo CV_8U.
static cv::Mat meanBGR(const cv::Mat& img) {
    // TODO: codificar la conversion
    return cv::Mat::zeros(img.size(), CV_8UC1);
}


// Gris segun la norma BT.601:  gray = 0.299*R + 0.587*G + 0.114*B.
// No usar cvtColor.
// Devuelve una imagen de 1 canal y tipo CV_8U.
static cv::Mat bt601BGR(const cv::Mat& img) {
    // TODO: codificar la conversion
    return cv::Mat::zeros(img.size(), CV_8UC1);
}


// Diferencia absoluta entre dos imágenes.
static cv::Mat diff(const cv::Mat& img_a, const cv::Mat& img_b) {
    // TODO: calcular la diferencia absoluta entre las dos imágenes
    return cv::Mat::zeros(img_a.size(), img_a.type());
}


int main(int argc, char** argv) {
    // TODO: cargar la imagen
    cv::Mat img = cv::Mat::zeros(400, 400, CV_8UC3);   // Borrar esta linea

    // Convertir la imagen a escala de grises usando las funciones definidas
    cv::Mat gray_1 = meanBGR(img);
    cv::Mat gray_2 = bt601BGR(img);

    // Calcular la diferencia entre las dos imágenes en escala de grises
    // Multiplicar la diferencia por 5 para hacerla más visible
    cv::Mat gray_diff;
    cv::multiply(diff(gray_1, gray_2), 5, gray_diff);

    // TODO: Salvar las imágenes en escala de grises y la diferencia
    // TODO: mostrar las imágenes en escala de grises y la diferencia


    cv::destroyAllWindows();
    return 0;
}
