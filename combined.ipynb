# importing the module
import cv2
import numpy as np
import pickle
import sys
with open('C:/Users/raofe/GPS_Pics-1/pickles/gps_coords.pickle', 'rb') as file:
    gps_lst = pickle.load(file)
pickup_cnt = 0
dropoff_cnt = 0
pickup_dict = {}
dropoff_dict = {}
align_lst = []
align_lst1 = []




def click_event(event, x, y, flags, params):
    global pickup_cnt, dropoff_cnt, pickup_dict, dropoff_dict
    # checking for left mouse clicks
    

    if event == cv2.EVENT_LBUTTONDOWN:

        pickup_cnt += 1
        # displaying the coordinates
        # on the image window
        cv2.circle(img, (x,y), 10, (255,255,255), 2)
        cv2.circle(img, (x,y), 1, (0,0,255), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "{}".format(pickup_cnt), (x,y), font,
                    1, (0, 0, 255), 2)

        align_lst.append((x,y))
        print("{}, {}".format(x,y))

        cv2.imshow('image', img)
        cv2.waitKey(0)



# driver function
if __name__=="__main__":

    # reading the image
    img = cv2.imread("C:/Users/raofe/GPS_Pics-1/pictures/IMG_BASE.jpeg", 1)
    #scale_percent = 70
    #width = int(img.shape[1] * scale_percent / 100)
    #height = int(img.shape[0] * scale_percent / 100)
    #img = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)

    #cv2.imwrite("C:/Users/McIntosh Aeronautics/Documents/mppython/drone_images/image_2.jpeg", img)
    #img2 = cv2.imread('/Users/sparky/Documents/DroneOpencv/FayetteFlyers-mavic.png', 1)
    size = (len(img), len(img[0]))
    print(size)
    
    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()




# driver function
if __name__=="__main__":

    # reading the image
    img = cv2.imread("C:/Users/raofe/GPS_Pics-1/pictures/GPS_IMG.PNG", 1)
    
    #cv2.imwrite("C:/Users/McIntosh Aeronautics/Documents/mppython/drone_images/image_2.jpeg", img)
    #img2 = cv2.imread('/Users/sparky/Documents/DroneOpencv/FayetteFlyers-mavic.png', 1)
    size = (len(img), len(img[0]))
    print(size)
    
    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()



print(pickle.load(open('C:/Users/raofe/GPS_Pics-1/pickles/data.pickle', 'rb')))




solid_gps = align_lst


with open('C:/Users/raofe/GPS_Pics-1/pickles/actual_coords.pickle', 'wb') as file:
                pickle.dump(align_lst, file)


with open('C:/Users/raofe/GPS_Pics-1/pickles/GPS_coords.pickle', 'wb') as file:
                pickle.dump(align_lst, file)






#opening file from data.pickle
with open('C:/Users/raofe/GPS_Pics-1/pickles/data.pickle', 'rb') as file:
    data = pickle.load(file)
print(data)
zeroes_lst = [ [0]*data['shape'][1] for _ in range(data['shape'][0]) ]





#opening file from data.pickle
with open('C:/Users/raofe/GPS_Pics-1/pickles/data.pickle', 'rb') as file:
    data = pickle.load(file)
print(data)
zeroes_lst = [ [0]*data['shape'][1] for _ in range(data['shape'][0]) ]
 
img_coords = data['img']
#empty list for gps coords
gps_coords = []
#loop through the coord in data
for coord in data['gps']:# flip in the beginning
    #added into gps coords list
    gps_coords.append((coord[1],coord[0]))
#print the results 
print("Initial: {}".format(data['gps']))
print("Final: {}".format(gps_coords))

imgx = img_coords[1][0]-img_coords[0][0]
imgy = img_coords[1][1]-img_coords[0][1]
gpsx = gps_coords[1][0]-gps_coords[0][0]
gpsy = gps_coords[1][1]-gps_coords[0][1]

print("Img: {}, {}, \nGPS: {}, {}".format(imgx,imgy,gpsx,gpsy))

per_pix_x = gpsx/imgx
per_pix_y = gpsy/imgy
startx = gps_coords[0][0]-per_pix_x*img_coords[0][0]
starty = gps_coords[0][1]-per_pix_y*img_coords[0][1]
print("Start: {}, {}".format(starty,startx))

gps_lst = zeroes_lst.copy()
for y in range(len(gps_lst)):
    for x in range(len(gps_lst[0])):
        gps_lst[y][x] = (starty + per_pix_y*y, startx + per_pix_x*x)
print(gps_lst[0][0])
with open('C:/Users/raofe/GPS_Pics-1/pickles/gps_coords.pickle', 'wb') as file:
    pickle.dump(gps_lst, file)





#aligning the the 2 images
def alignImages(im1, im2):
    with open('C:/Users/raofe/GPS_Pics-1/pickles/actual_coords.pickle', 'rb') as file:
        points1 = np.array(pickle.load(file))
        print(len(points1))
    with open('C:/Users/raofe/GPS_Pics-1/pickles/gps_coords.pickle', 'rb') as file:
        points2 = np.array(pickle.load(file))
        print(len(points2))
    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    print(h)
    print(width)
    print(height)
    cv2.imshow('image', im1)
    cv2.waitKey(0)
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h






if __name__ == '__main__':

    # Read reference image
    refFilename = "C:/Users/raofe/GPS_Pics-1/pictures/GPS_IMG.PNG"
    print("Reading reference image : ", refFilename)
    imGPS = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    imFilename = 'C:/Users/raofe/GPS_Pics-1/pictures/IMG_BASE.jpeg'
    print("Reading image to align : ", imFilename)
    imActual = cv2.imread(imFilename, cv2.IMREAD_COLOR)

    print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, h = alignImages(imActual, imGPS)
    cv2.imshow('aligned', imReg)
    cv2.waitKey(0)
    # ONLY USE IN TESTING, FOR MAKING SURE IMAGES ALIGNED CORRECTLY
    added_image = cv2.addWeighted(imReg,0.5,imGPS,.5,0)
    # Write aligned image to disk.
    outFilename = "C:/Users/raofe/GPS_Pics-1/pictures/aligned.png"
    print("Saving aligned image : ", outFilename)
    cv2.imshow('aligned', added_image)
    cv2.waitKey(0)
    cv2.imwrite(outFilename, imReg)

    # Print estimated homography
    
    cv2.destroyAllWindows()
    print("Estimated homography : \n",  h)



#closes all windows
cv2.destroyAllWindows()




while 1:
    cv2.imshow('aligned', imReg)
    cv2.waitKey(0)
    cv2.imshow('aligned', imGPS)
    cv2.waitKey(0)
