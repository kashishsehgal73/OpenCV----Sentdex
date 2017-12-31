/*
Copyright 2017 BIG VISION LLC ALL RIGHTS RESERVED

This code is made available to the students of 
the online course titled "OpenCV for Beginners" 
by Satya Mallick for personal non-commercial use. 

Sharing this code is strictly prohibited without written
permission from Big Vision LLC. 

For licensing and other inquiries, please email 
spmallick@bigvisionllc.com 
*/

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#include <cmath>
#include <vector>

using namespace cv;
using namespace std;

int main(void)
{
// Read image
Mat source = imread("sample.jpg",1);
source.at<Vec3b>(100,100)[0]=0;
source.at<Vec3b>(100,100)[1]=255;
source.at<Vec3b>(100,100)[2]=0;
source.at<Vec3b>(100,98)[0]=0;
source.at<Vec3b>(100,98)[1]=255;
source.at<Vec3b>(100,98)[2]=0;
source.at<Vec3b>(100,102)[0]=0;
source.at<Vec3b>(100,102)[1]=255;
source.at<Vec3b>(100,102)[2]=0;
source.at<Vec3b>(102,100)[0]=0;
source.at<Vec3b>(102,100)[1]=255;
source.at<Vec3b>(102,100)[2]=0;
source.at<Vec3b>(98,100)[0]=0;
source.at<Vec3b>(98,100)[1]=255;
source.at<Vec3b>(98,100)[2]=0;
source.at<Vec3b>(98,98)[0]=0;
source.at<Vec3b>(98,98)[1]=255;
source.at<Vec3b>(98,98)[2]=0;
source.at<Vec3b>(98,102)[0]=0;
source.at<Vec3b>(98,102)[1]=255;
source.at<Vec3b>(98,102)[2]=0;
source.at<Vec3b>(102,102)[0]=0;
source.at<Vec3b>(102,102)[1]=255;
source.at<Vec3b>(102,102)[2]=0;
source.at<Vec3b>(102,98)[0]=0;
source.at<Vec3b>(102,98)[1]=255;
source.at<Vec3b>(102,98)[2]=0;
source.at<Vec3b>(280,360)[0]=0;
source.at<Vec3b>(280,360)[1]=255;
source.at<Vec3b>(280,360)[2]=0;
source.at<Vec3b>(278,360)[0]=0;
source.at<Vec3b>(278,360)[1]=255;
source.at<Vec3b>(278,360)[2]=0;
source.at<Vec3b>(282,360)[0]=0;
source.at<Vec3b>(282,360)[1]=255;
source.at<Vec3b>(282,360)[2]=0;
source.at<Vec3b>(280,362)[0]=0;
source.at<Vec3b>(280,362)[1]=255;
source.at<Vec3b>(280,362)[2]=0;
source.at<Vec3b>(280,358)[0]=0;
source.at<Vec3b>(280,358)[1]=255;
source.at<Vec3b>(280,358)[2]=0;
source.at<Vec3b>(278,358)[0]=0;
source.at<Vec3b>(278,358)[1]=255;
source.at<Vec3b>(278,358)[2]=0;
source.at<Vec3b>(282,358)[0]=0;
source.at<Vec3b>(282,358)[1]=255;
source.at<Vec3b>(282,358)[2]=0;
source.at<Vec3b>(282,362)[0]=0;
source.at<Vec3b>(282,362)[1]=255;
source.at<Vec3b>(282,362)[2]=0;
source.at<Vec3b>(278,362)[0]=0;
source.at<Vec3b>(278,362)[1]=255;
source.at<Vec3b>(278,362)[2]=0;
source.at<Vec3b>(400,300)[0]=0;
source.at<Vec3b>(400,300)[1]=255;
source.at<Vec3b>(400,300)[2]=0;
source.at<Vec3b>(402,300)[0]=0;
source.at<Vec3b>(402,300)[1]=255;
source.at<Vec3b>(402,300)[2]=0;
source.at<Vec3b>(398,300)[0]=0;
source.at<Vec3b>(398,300)[1]=255;
source.at<Vec3b>(398,300)[2]=0;
source.at<Vec3b>(402,298)[0]=0;
source.at<Vec3b>(402,298)[1]=255;
source.at<Vec3b>(402,298)[2]=0;
source.at<Vec3b>(400,298)[0]=0;
source.at<Vec3b>(400,298)[1]=255;
source.at<Vec3b>(400,298)[2]=0;
source.at<Vec3b>(398,298)[0]=0;
source.at<Vec3b>(398,298)[1]=255;
source.at<Vec3b>(398,298)[2]=0;
source.at<Vec3b>(400,302)[0]=0;
source.at<Vec3b>(400,302)[1]=255;
source.at<Vec3b>(400,302)[2]=0;
source.at<Vec3b>(402,302)[0]=0;
source.at<Vec3b>(402,302)[1]=255;
source.at<Vec3b>(402,302)[2]=0;
source.at<Vec3b>(398,302)[0]=0;
source.at<Vec3b>(398,302)[1]=255;
source.at<Vec3b>(398,302)[2]=0;

line(source, Point2f(102,102), Point2f(358,278), Scalar(255,0,0), 1, 8,0);
line(source, Point2f(362,282), Point2f(298,398), Scalar(255,0,0), 1, 8,0);
line(source, Point2f(102,102), Point2f(298,402), Scalar(255,0,0), 1, 8,0);
imshow("points",source);

// Create mask/ warp matrix
Mat warpMat = (Mat_<double>(2,3) << 1.2, 0.2, 2, -0.3, 1.3, 1 );

// Another mask
Mat warpMat2 = (Mat_<double>(2,3) << 1.2, 0.3, 2, 0.2, 1.3, 1);

Mat result,result2;
// Use warp affine
cv::warpAffine(source, result, warpMat, Size(1.5*source.rows,1.4*source.cols), INTER_LINEAR, BORDER_REFLECT_101);
cv::warpAffine(source, result2, warpMat2, Size(1.5*source.rows, 1.4*source.cols), INTER_LINEAR, BORDER_REFLECT_101);
// Display images
imshow("Original", source);
imshow("Result", result);
imshow("Result2", result2);
waitKey(0);
destroyAllWindows();
}