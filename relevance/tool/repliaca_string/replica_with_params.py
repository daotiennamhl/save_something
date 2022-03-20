### mục đích: nhân nội dung theo số thứ tự được truyền vào
# các biến cần sửa
string = r"""<FacePost>
    <Id>{id}</Id>
    <PostContent />
    <TypeId>8</TypeId>
    <TypeName>Mặt hàng</TypeName>
    <DateCreated>2021-04-03T15:36:43.4752275+07:00</DateCreated>
    <ImageFolder>C:\Users\daoti\Downloads\hoa\converted\hoahong\{folderIndex}</ImageFolder>
    <ImageFolderCount>6</ImageFolderCount>
    <GLSellImage />
    <GLSellName>Gốc Hoa Hồng Ngoại</GLSellName>
    <GLSellLocation />
    <GLSellPrice>8</GLSellPrice>
    <GLSellCate>Vườn</GLSellCate>
    <GLSellFolderCount>0</GLSellFolderCount>
    <GLSellTags />
    <GLSellCustomObj>{{"Year":"","Make":"","Model":"","KM":"","BodyStyle":"","Condition":"","FuelType":"","Transmission":"","RentType":"","NumberOfBedRooms":"","NumberOfBathRooms":"","Feet":"","LaundryType":"","ParkingType":"","AirConditioningType":"","HeatingType":"","CatFriendly":false,"DogFriendly":false}}</GLSellCustomObj>
    <JobType>0</JobType>
    <JobPriceFrom>0</JobPriceFrom>
    <JobPriceTo>0</JobPriceTo>
    <JobPriceType>0</JobPriceType>
  </FacePost>"""
numberOfPost = 29
startId = 30
res = ''

for i in range(startId, startId + numberOfPost):
  res += string.format(id=i, folderIndex=i-startId+1) + "\n"
f = open('res.txt', "wb")
f.write(res.encode("utf8"))
f.close()
