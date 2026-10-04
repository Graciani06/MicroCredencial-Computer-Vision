#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <vector>

// Gris como la media plana de los tres canales: (B + G + R) / 3.
// No usar cvtColor.
// Devuelve una imagen de 1 canal y tipo CV_8U.
static cv::Mat meanBGR(const cv::Mat& img) {
    std::vector<cv::Mat> bgr;
    cv::split(img, bgr);  // OJO: devuelve b, g, r
    cv::Mat b32, g32, r32;
    bgr[0].convertTo(b32, CV_32F);
    bgr[1].convertTo(g32, CV_32F);
    bgr[2].convertTo(r32, CV_32F);
    cv::Mat gray32 = (b32 + g32 + r32) / 3.0;
    cv::Mat gray;
    gray32.convertTo(gray, CV_8U);  // redondea
    return gray;
}

// Gris segun la norma BT.601:  gray = 0.299*R + 0.587*G + 0.114*B.
// No usar cvtColor.
// Devuelve una imagen de 1 canal y tipo CV_8U.
static cv::Mat bt601BGR(const cv::Mat& img) {
    std::vector<cv::Mat> bgr;
    cv::split(img, bgr);  // bgr[0]=B, bgr[1]=G, bgr[2]=R
    cv::Mat b32, g32, r32;
    bgr[0].convertTo(b32, CV_32F);
    bgr[1].convertTo(g32, CV_32F);
    bgr[2].convertTo(r32, CV_32F);
    cv::Mat gray32 = 0.299 * r32 + 0.587 * g32 + 0.114 * b32;
    cv::Mat gray;
    gray32.convertTo(gray, CV_8U);
    return gray;
}

// Diferencia absoluta entre dos imágenes.
static cv::Mat diff(const cv::Mat& img_a, const cv::Mat& img_b) {
    cv::Mat img_diff;
    cv::absdiff(img_a, img_b, img_diff);  // gray_diff = |gray_1 - gray_2|
    return img_diff;
}

int main(int argc, char** argv) {
    cv::Mat img = cv::imread("../data/knights.png", cv::IMREAD_COLOR);
    if (img.empty()) {
        std::cerr << "Error: no se pudo leer la imagen." << std::endl;
        return 1;
    }
    // Convertir la imagen a escala de grises usando las funciones definidas
    cv::Mat gray_1 = meanBGR(img);
    cv::Mat gray_2 = bt601BGR(img);

    // Calcular la diferencia entre las dos imágenes en escala de grises
    // Multiplicar la diferencia por 5 para hacerla más visible
    cv::Mat gray_diff;
    cv::multiply(diff(gray_1, gray_2), 5, gray_diff);

    cv::imwrite("gray_mean.png", gray_1);
    cv::imwrite("gray_bt601.png", gray_2);
    cv::imwrite("gray_diff.png", gray_diff);
    cv::imshow("gray rgb", gray_1);
    cv::imshow("gray bt601", gray_2);
    cv::imshow("gray diff", gray_diff);
    cv::waitKey(0);
    cv::destroyAllWindows();
    return 0;
}
