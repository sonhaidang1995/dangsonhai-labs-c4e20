from gmail import GMail, Message
from random import choice
from datetime import datetime
from threading import Timer
gmail = GMail("dangsonhai26061995@gmail.com","Theeternal0610")

html_content ="""
    <p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
    <p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
    <p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
    <p style="padding-left: 30px;"><em><strong>K&iacute;nh gửi:</strong></em> B&agrave; con c&ocirc; b&aacute;c</p>
    <p>Ch&aacute;u xin th&ocirc;ng b&aacute;o: <strong>{{sickness}}</strong></p>
    <p>Ch&aacute;u xin hứa sẽ chăm chỉ xem ti vi v&agrave; chơi điện tử.</p>
    <p>Ch&aacute;u xin ch&acirc;n th&agrave;nh cảm ơn!</p>
    <p style="text-align: right;"><em>H&agrave; Nội, ng&agrave;y 04 th&aacute;ng 08 năm 2018</em></p>
    <table style="width: 597px; float: right;" border="0">
    <tbody>
    <tr style="height: 17px;">
    <td style="width: 412.667px; height: 17px; text-align: right;">&nbsp;</td>
    <td style="width: 168.667px; text-align: center; height: 17px;">Học sinh</td>
    </tr>
    <tr style="height: 125px;">
    <td style="width: 412.667px; height: 125px;">&nbsp;</td>
    <td style="width: 168.667px; text-align: center; height: 125px;">Đặng Sơn Hải</td>
    </tr>
    </tbody>
    </table>
"""
reason = [
    "Cháu chán",
    "Cháu ốm",
    "Cháu ngủ dậy muộn",
    "Đang dở trận rank",
    "Đi tìm công lý"
]

html_new = html_content.replace("{{sickness}}",choice(reason))
msg = Message('Đơn xin nghỉ học',to = '20130075@student.hust.edu.vn',html = html_new)

def send_email():
    gmail.send(msg)

now = datetime.now()
off_day = now.replace(day= now.day+1,hour=7,minute=00,second=00,microsecond=0)
delta = off_day - now
secs = delta.seconds + 1
Timer(secs,send_email).start()
