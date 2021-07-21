'''interface for output to users'''
import cv2
import numpy
from calculate.calculator_normal import CalculatorNormal
from calculate.calculator_deriv import CalculatorDerivation
def deriv_plotting(func_string,x_range,y_range):
    func_pts = CalculatorDerivation(func_string, x_range[0], x_range[1], 500).get_points()
    x_pts = func_pts[0]
    y_pts = func_pts[1]
    new_func_pts = []
    for i in range(500):
        new_func_pts.insert(i, [x_pts[i], y_pts[i]])
    return plotter(new_func_pts, x_range, y_range, "Derivative of "+func_string)
def plotting(func_string,x_range,y_range):
    '''the plotting function'''
    func_pts = CalculatorNormal(func_string, x_range[0], x_range[1], 500).get_points()
    x_pts = func_pts[0]
    y_pts = func_pts[1]
    new_func_pts = []
    for i in range(500):
        new_func_pts.insert(i,[x_pts[i],y_pts[i]])
    return plotter(new_func_pts, x_range, y_range, func_string)
def shifter(point,x_range,y_range):
    '''shift to coordinate on interface'''
    x_start = x_range[0]
    x_end = x_range[1]
    y_start = y_range[0]
    y_end = y_range[1]
    shift_x = int(500*(point[0]-x_start)/(x_end-x_start))
    shift_y = 500-int(500*(point[1]-y_start)/(y_end-y_start))
    #origin_x = 250
    #origin_y = 250
    #shift_x=point[0]*25
    #shift_y=point[1]*25
    return [shift_x,shift_y]
def plotter(points,x_range,y_range,func_name):
    '''plotter function'''
    x_start = x_range[0]
    x_end = x_range[1]
    y_start = y_range[0]
    y_end = y_range[1]
    img = numpy.ones((500,500,1),numpy.uint8)*255
    #cv2.imshow('image',img)
    y_axis_pos = 500*(-x_start)/(x_end-x_start)
    x_axis_pos = 500*(y_end)/(y_end-y_start)
    x_axis_pos = int(x_axis_pos)
    y_axis_pos = int(y_axis_pos)
    if y_axis_pos < 500 and y_axis_pos >= 0:
        for i in range(500):
            img[500-y_axis_pos][i]=1
            img[500-y_axis_pos-1][int(i/25)*25]=1
    if x_axis_pos < 500 and x_axis_pos >= 0:
        for i in range(500):
            img[i][500-x_axis_pos]=1
            img[int(i/25)*25][500-x_axis_pos+1]=1
    in_plot_pts = []
    for index in range(len(points)):
        point = points[index];
        if point[1] != None and point[0] <= x_end and point[0] >= x_start and point[1] <= y_end and point[1]>= y_start:
            pos = shifter(point,x_range,y_range)
            in_plot_pts.append(point)
            if pos[0] < 500 and pos[0] >= 0:
                if pos[1] < 500 and pos[0]>=0:
                    img[pos[1]][pos[0]]=1
                    if point[0] == int(point[0]):
                        cv2.putText(img, "x="+str(point[0])+",y="+str(point[1]), (pos[0], pos[1]),
                                    cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), 1)
                    if index-1 >= 0 and point[1] is not None:
                        #print(points[index-1],points[index])
                        prev = shifter(points[index - 1],x_range,y_range)
                        img = cv2.line(img, (pos[0],pos[1]), (prev[0],prev[1]), (0,0,0), 1)
    #print(in_plot_pts[int(len(in_plot_pts) / 2)])
    if len(in_plot_pts) < 10:
        cv2.putText(img, "not enough points in this range",(25,250),cv2.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), 1);
    else:
        func_name_pts = shifter(in_plot_pts[int(len(in_plot_pts) / 2)+2],x_range,y_range)
        #print(func_name_pts)
        cv2.putText(img, "f(x)="+func_name, (func_name_pts[0],func_name_pts[1]), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), 1);
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

#plotting("x^2",[-0.5,10],[-0.5,10])
