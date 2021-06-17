import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import stopwords
#text=input("ป้อนข้อความที่ต้องการ :")
text="กรุงเทพมหานคร เป็นเมืองหลวงและนครที่มีประชากรมากที่สุดของประเทศไทย เป็นศูนย์กลางการปกครอง การศึกษา การคมนาคมขนส่ง การเงินการธนาคาร การพาณิชย์ การสื่อสาร และความเจริญของประเทศ เป็นเมืองที่มีชื่อยาวที่สุดในโลก ตั้งอยู่บนสามเหลี่ยมปากแม่น้ำเจ้าพระยา มีแม่น้ำเจ้าพระยาไหลผ่านและแบ่งเมืองออกเป็น 2 ฝั่ง คือ ฝั่งพระนครและฝั่งธนบุรี กรุงเทพมหานครมีพื้นที่ทั้งหมด 1,568.737 ตร.กม. มีประชากรตามทะเบียนราษฎรกว่า 5 ล้านคน ทำให้กรุงเทพมหานครเป็นเอกนคร (Primate City) จัด มีผู้กล่าวว่า กรุงเทพมหานครเป็น เพราะมีประชากรมากกว่านครที่มีประชากรมากเป็นอันดับ 2 ถึง 40 เท่า"
cloud=WordCloud(background_color="white",
                font_path="Pridi-Bold.ttf",
                regexp=r"[\u0E00-\u0E7Fa-zA-Z']+",
                width=1024,
                height=768,
                stopwords = ' '.join(stopwords.words('thai'))
                ).generate(' '.join(word_tokenize(text)))
plt.imshow(cloud,cmap=plt.cm.gray,interpolation='bilinear')
plt.axis("off")
plt.show()
