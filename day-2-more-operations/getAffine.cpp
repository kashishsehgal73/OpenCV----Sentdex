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
// Input triangle
vector <Point2f> tri1;
tri1.push_back(Point2f(50, 50));
tri1.push_back(Point2f(180, 140));
tri1.push_back(Point2f(150, 200));
     
// Output triangle
vector <Point2f> tri2;
tri2.push_back(Point2f(72, 51));
tri2.push_back(Point2f(246, 129));
tri2.push_back(Point2f(222, 216));

// Another output triangle
vector <Point2f> tri3;
tri3.push_back(Point2f(77, 76));
tri3.push_back(Point2f(260, 219));
tri3.push_back(Point2f(242, 291));

// Get the transformation matrices
Mat warp = cv::getAffineTransform(tri1,tri2);
Mat warp2 = cv::getAffineTransform(tri1,tri3);
// Display the matrices
cout << "Warp Matrix 1 : \n\n " << warp << "\n\n" << "Warp Matrix 2 : \n" << warp2<< endl;
}
