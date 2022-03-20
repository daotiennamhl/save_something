data: need_unfollow.txt, followed.txt 
	-> find list chưa follow 
		-> lọc list đó tìm ra những người cần follow
			-> sau khi follow thì thêm vào follow.txt

chạy follow:
	tìm ra list cần follow, filter qua các bước: xóa bỏ ẩn danh, xóa bỏ trùng lặp, xóa bỏ người đã follow(so sánh với followed.py)
		-> follow những user đó
			-> follow người nào thêm người đó vào need_unfollow.txt
chạy unfollow:
	cứ thế chạy :v