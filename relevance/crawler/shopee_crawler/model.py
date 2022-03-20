class Post:
  def __init__(self, link, title, price, quantity_sold, district):
    self.link = link or ""
    self.title = title or ""
    self.price = price or ""
    self.quantity_sold = quantity_sold or ""
    self.district = district or ""