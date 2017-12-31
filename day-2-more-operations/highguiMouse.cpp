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

#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <vector>
#include <iostream>
#include <math.h>

using namespace cv;
using namespace std;

// Points to store the center of the circle and a point on the circumference
Point center, circumference;
// Source image
Mat source;

// function which will be called on mouse input
void drawCircle(int action, int x, int y, int flags, void *userdata)
{
  // Action to be taken when left mouse button is pressed
  if( action == EVENT_LBUTTONDOWN )
  {
  	center = Point(x,y);
  	// Mark the center
  	circle(source, center, 1, Scalar(255,255,0), 2, CV_AA );
  }
  // Action to be taken when left mouse button is released
  else if( action == EVENT_LBUTTONUP)
  {
  	circumference = Point(x,y);
  	// Calculate radius of the circle
  	float radius = sqrt(pow(center.x-circumference.x,2)+pow(center.y-circumference.y,2));
  	// Draw the circle
  	circle(source, center, radius, Scalar(0,255,0), 2, CV_AA );
  	imshow("Window", source);
  }
  
}
int main()
{
  source = imread("sample.jpg",1);
  // Make a dummy image, will be useful to clear the drawing
  Mat dummy = source.clone();
  namedWindow("Window");
  // highgui function called when mouse events occur
  setMouseCallback("Window", drawCircle);
  int k=0;
  // loop until escape character is pressed
  while(k!=27)
  {
  	imshow("Window", source );
  	putText(source,"Choose center, and drag, Press ESC to exit and c to clear" ,Point(10,30), FONT_HERSHEY_SIMPLEX, 0.7,Scalar(255,255,255), 2 );
  	k= waitKey(20) & 0xFF;
  	if(k== 99)
  		// Another way of cloning
  		dummy.copyTo(source);
  }
  return 0;
}
