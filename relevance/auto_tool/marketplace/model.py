number_of_image_per_post = 5
def get_single_img_path(index):
    return fr'C:\Users\daotiennam\Desktop\New folder\img\{index}.jpg'

class Post:
    def __init__(self, title, price, description, img_path='', location=''):
        self.title = title
        self.price = price
        self.description = description
        self.img_path = img_path
        self.location = location
    def get_img_path(self):
        return self.img_path
    def set_img_path(self, id):
        self.img_path = "\n".join([get_single_img_path(id*number_of_image_per_post + i) for i in range(number_of_image_per_post)])

post = Post(
    'Tỏi, gừng nâng cao đề kháng',
    '55',
    'tỏi khô, hành khô, tỏi tía',
    '',
    ''
    )

post1 = Post(
    'Tỏi, gừng tăng cường sức khỏe',
    '55',
    'tỏi khô, hành khô, tỏi tía',
    '',
    ''
    )

post2 = Post(
    'Tỏi gừng, nâng cao sức khỏe',
    '55',
    'tỏi khô, hành khô, tỏi tía',
    '',
    ''
    )
list_post = [post, post1, post2]