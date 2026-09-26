// Comprobación del entorno: imprime la versión de OpenCV y muestra una imagen.
#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    std::cout << "OpenCV (C++): " << cv::getVersionString() << std::endl;

    cv::Mat img(240, 640, CV_8UC3, cv::Scalar(40, 40, 40));
    cv::putText(img, "Entorno OK - OpenCV " CV_VERSION, {20, 130},
                cv::FONT_HERSHEY_SIMPLEX, 0.9, {0, 255, 0}, 2);

    if (std::getenv("DISPLAY")) {
        cv::imshow("check", img);
        cv::waitKey(0);
    } else {
        cv::imwrite("check.png", img);
        std::cout << "Sin DISPLAY: imagen guardada en check.png" << std::endl;
    }
    return 0;
}
