# Importing the necessary libraries
import cv2
import numpy as np
from operator import itemgetter

class draw: 
  def __init__(self,getBorderSize,getInput):
    self.getBorderSize=getBorderSize
    self.getInput= getInput

  def getImage(imagePath):
    print("image "+imagePath)
    
  def getInput():
    user_input = input('Do you like pizza (yes/no): ')
    if user_input.lower() == 'y':
      return True
    else:
      return False

  def getBorderSize(person):
    listPoint=[]
    for dimesion in person:
      width = int(dimesion[1])
      height = int(dimesion[0])
      listPoint.append((width,height))
      max_x = max(listPoint, key=itemgetter(0))
      min_x = min(listPoint, key=itemgetter(0))
      max_y = max(listPoint, key=itemgetter(1))
      min_y = min(listPoint, key=itemgetter(1))
    print("person :",person)
    print("listPoint :",listPoint)
    print("person :xy",min_x," ",min_y,",",max_x," ",max_y)
    value = max_y[1]-min_y[1]+max_x[0]-min_x[0]
    print("value ",value)
    return value

  def getImageFromImagePath(imagePath,arr,arr_define,arr_draw):
    imagePath = imagePath
    print("arr ",len(arr))
    print(arr)

    fileName = imagePath.split("/")[-1]
    # imagePath = './test2/yoga_pair_2.jpg'
    # getImage(imagePath)
    image = cv2.imread(imagePath)
    
    # Getting the height and width of the image
    height = image.shape[0]
    width = image.shape[1]
    print(width)
    print(height)

    #person i:
    personI = arr[0]
    list_size = []
    index_temp=0
    
    for person in arr: 
      dataaxx = draw.getBorderSize(person)
      list_size.append((dataaxx,index_temp))
      index_temp=index_temp+1
    print("list_size sort ",list_size)
    list_size = sorted(list_size , key=lambda k: [k[0], k[1]]).reverse
    print("list_size sort ",list_size)
    # print("Person ",personI)
    # for idx, dimesion in np.ndenumerate(personI):
    i=0
    for dimesion in personI:
        print("Data ")
        print(dimesion)
        # Drawing the lines
        # cv2.line(image, (0, 0), (width, height), (0, 0, 255), 5)
        # cv2.line(image, (width, 0), (0, height), (0, 0, 255), 5)


        # canvas = np.zeros((300, 300, 3), dtype="uint8")
        # x = list(('apple', 'banana', 'cherry'))
        # print(x)

        # (centerX, centerY) = (width // 2, height // 2)
        # font
        font = cv2.FONT_ITALIC
        # org
        org = (50, 50)
        # fontScale
        fontScale = 0.3
        # Blue color in BGR
        color = (0, 0, 0)
        # Line thickness of 2 px
        thickness = 1
        white = (0, 255, 0)

        text = arr_define[i]
        i=i+1
        if text in arr_draw:
            print(text)
            lineType = 2
            width = int(dimesion[1])
            height = int(dimesion[0])
            print("width,height:",width,height)
            pointX,pointY = width,height
            text_width, text_height = cv2.getTextSize(text, font, fontScale, lineType)[0]
            CenterCoordinates = (int(pointX)-int(text_width / 2), int(pointY) - int(text_height / 2))
            cv2.circle(image, (width, height), lineType, white,lineType)
            cv2.putText(image,text, CenterCoordinates,font, fontScale, color, thickness, cv2.LINE_AA)
      # break
    # confirm

    # Showing the image
    cv2.imshow('image', image)
    # input_check = draw.getInput()
    # print("input_check ",input_check)
    cv2.imwrite('./output/'+fileName, image)
    print('Done')
      # print('Done')
  

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    input_check = draw.getInput()
    print("input_check ",input_check)


  #main test
  # Reading the image
  # imagePath = './test2/yoga_pair_2.jpg'
  # getImage(imagePath)
  # image = cv2.imread(imagePath)
  
  # # Getting the height and width of the image
  # height = image.shape[0]
  # width = image.shape[1]
  # print(width)
  # print(height)
  
  # # Drawing the lines
  # cv2.line(image, (0, 0), (width, height), (0, 0, 255), 5)
  # cv2.line(image, (width, 0), (0, height), (0, 0, 255), 5)


  # # canvas = np.zeros((300, 300, 3), dtype="uint8")
  # x = list(('apple', 'banana', 'cherry'))
  # print(x)

  # (centerX, centerY) = (width // 2, height // 2)
  # # font
  # font = cv2.FONT_ITALIC
  # # org
  # org = (50, 50)
  # # fontScale
  # fontScale = 0.5
  # # Blue color in BGR
  # color = (255, 0, 0)
  # # Line thickness of 2 px
  # thickness = 1

  # white = (0, 0, 0)

  # text = "textImage"
  # lineType = 2
  # pointX,pointY = width,height
  # text_width, text_height = cv2.getTextSize(text, font, fontScale, lineType)[0]
  # CenterCoordinates = (int(pointX / 2)-int(text_width / 2), int(pointY / 2) - int(text_height / 2))
  # cv2.circle(image, (centerX, centerY), lineType, white,lineType)
  # cv2.putText(image,text, CenterCoordinates,font, fontScale, color, thickness, cv2.LINE_AA)
  
  # # Showing the image
  # cv2.imshow('image', image)
  # cv2.imwrite('./output/thuongnt.jpg', image)
  # print('Done')
  

  # # cv2.waitKey(0)
  # # cv2.destroyAllWindows()