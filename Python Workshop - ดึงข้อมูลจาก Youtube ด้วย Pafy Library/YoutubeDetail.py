import pafy
url=input("ป้อน URL วิดีโอที่ต้องการดูรายละเอียด :")
video=pafy.new(url)
print(video.title)
print(video.rating)
print("จำนวนการดู = "+"{:,d}".format(video.viewcount))
print(video.author)
print(video.length)
print("ชอบ = "+"{:,d}".format(video.likes))
print("ไม่ชอบ = "+"{:,d}".format(video.dislikes))
print(video.description)
