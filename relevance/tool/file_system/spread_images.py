# mục đích: chia ảnh trong 1 folder thành các folder con với số lượng ảnh bằng nhau

import os, shutil

folderNames = [r'C:\Users\daoti\Downloads\hoa\Củ lan huệ', r'C:\Users\daoti\Downloads\hoa\Trà My', r'C:\Users\daoti\Downloads\hoa\Hoa hồng 30.3']
targets = [r'C:\Users\daoti\Downloads\hoa\converted\culanhue', r'C:\Users\daoti\Downloads\hoa\converted\tramy', r'C:\Users\daoti\Downloads\hoa\converted\hoahong']
numberOfImageEachFolder = 6

for folderName, target in zip(folderNames, targets): # zip() trả về iterator của tuples
  # get all images in a folder
  allImages = []
  for r, d, f in os.walk(folderName):
    for file in f:
      if file.endswith('.png') or file.endswith('.jpg'):
        allImages.append(os.path.join(r, file))
  totalFolder = int((len(allImages)-1)/numberOfImageEachFolder) + 1

  # copy image to folder
  print("totalFolder =", totalFolder)
    # create folder 
  if not os.path.exists(target): # checkk if target folder is not exists
    os.mkdir(target)
  for i in range(totalFolder):
    targetFolder = target + "\{}".format(i)
    # remove old
    if os.path.exists(targetFolder):
      shutil.rmtree(targetFolder)
    # create new
    os.mkdir(targetFolder)

  # copy image to folder
  for i in range(len(allImages)):
    origin = allImages[i]
    shutil.copy(origin, target+"\{}".format(int(i/numberOfImageEachFolder)))
