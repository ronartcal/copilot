# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_BEDlHOdtbAEWSvPgI5Lp00ZydRk48QX
"""

! git clone

import cv2
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pickle
from pathlib import Path

class VIDEO :
  def __init__(self , save = False, save_path = "./", anotate=False )
  self.save  = save
  self.save_path  = save_path
  self.anotate  =  anotate
  self.fps

def calibrate(filename, silent = True):
    images_path = ''
    

    # setup object points
    

    # loop through provided images
    
    with open(filename, 'wb') as f:
        pickle.dump(calib_data, f)

    if not silent:
        for image_file in os.listdir(images_path):
            if image_file.endswith("jpg"):
                # show distorted images
                img = mpimg.imread(os.path.join(images_path, image_file))
                plt.imshow(cv2.undistort(img, mtx, dist))
                plt.show()

    return mtx, dist

if __name__ == '__main__':
    calibrate(CALIB_FILE_NAME, True)


class CAMERA :
  
  def __init__():
    self.callibrate  = False
    self.cam_matrix = None
    self.dist_coeffs= None
    self.img_size = None
    self.rvecs = None
    self.tvecs = None
    
  
  def callibrate(self , folder = 'camera_cal',n_x = 9, n_y = 6, verbose =   False):
    objp = np.zeros((n_y*n_x, 3), np.float32)
    objp[:, :2] = np.mgrid[0:n_x, 0:n_y].T.reshape(-1, 2)
    image_points = []
    object_points = []
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    for image_file in os.listdir(folder):
        if image_file.endswith("jpg"):
            # turn images to grayscale and find chessboard corners
            img = cv2.imread(os.path.join(images_path, image_file))
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            found, corners = cv2.findChessboardCorners(img_gray, (n_x, n_y))
            if found:
                self.callibrate = False
                corners2 = cv2.cornerSubPix(img_gray, corners, (11, 11), (-1, -1), criteria)
                image_points.append(corners2)
                object_points.append(objp)
                if verbose:
                    cv2.drawChessboardCorners(img, (n_x, n_y), corners, found)
                    plt.imshow(img)
                    plt.show()

    # pefrorm the calibration
    ret, self.cam_matrix, self.dist_coeffs, self.rvecs, self.tvecs = cv2.calibrateCamera(object_points, image_points, img_gray.shape[::-1], None, None)
    self.img_size  = img.shape
    
  def undistort(self, image)
    return image

class FRAME :
  def __init__(self,image):
    self.id =  id
    self.first = first
    self.speed =  self.getSpeed()
  
  def perspective_tfm():
    return
  
  def get_speed(self)
    return 30
  
  def detect_objects():
    return
  
  def find_distance() : 
    
    return
  
  def map_to_previous() : 
    return
  
  
  def vehicle_speed() :
    return

class DETECTION:
  def __init__(self , bbox, score, category,_id, image) :
    self.bbox = bbox
    self.score =  score
    self.category =  category
    self._id = _id
    self.image = image
    

class VEHICLE(DETECTION) :
  def __init__(self) :
    self.numplate=None
    self.rx = None
    self.ry = None
    self.vx = 0
    self.first = True
    
  def detect_number_plate(self):
    return None
  
  def detect_position(self) :
    return None
  
  def detect_velocity(self) :
    return None
    
  
    
    
class TRAFFIC_LIGHTS(DETECTION)
  def __init__(self) :
    return None
  
  def detect_status(self):
    return None
    
class TRAFFIC_SIGNS(DETECTION)
  def __init__(self) :
    return None
  
  def decipher(self):
    return None

class EVENT :
  def __init__():
    # TAILGAITING ,  FCAS WARNING , LANE CHANGING, TRAFFIC LIGHT JUMP
    self.time_stamp 
    self.image_path
    self.type
    self.speed
    self.coordinates