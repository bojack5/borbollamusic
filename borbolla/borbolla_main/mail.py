import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





# me == my email address
# you == recipient's email address
class Email(object):
    #me = "luis.borbolla@udem.edu"
    def __init__(self , to ,subject, msg , nombre = '' , email = '' , mensaje = ''):
    	
    	
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = subject
        self.msg['From'] = 'luis@4suredesign.com'
        self.msg['To'] = to
        self.text = msg
        self.html = """\
<html>
  <head></head>
  <body>
    
    <p>Se recibio un mensaje nuevo en la pagina web de Borbolla Music Store!<br>
       Nombre : %s<br>
       Email  : %s<br>
       Mensaje: %s<br>
       .
    </p>
    <p> Alternativamente puedes checarlo en la pagina de administracion <a href = '/admin/'>pulsando aqui</a>
    <img src="http://cdn.gq.com.mx/uploads/images/thumbs/mx/gq/2/s/2016/22/las_mejores_fotos_de_megan_fox_135912044_900x1345.jpg" alt="Mountain View" style="width:304px;height:228px;">
  </body>
</html>
"""





        part1 = MIMEText(self.text, 'plain')
        part2 = MIMEText(self.html%(nombre,email,mensaje), 'html')

        self.msg.attach(part1)
        self.msg.attach(part2)

        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login('luis@4suredesign.com', 'borbollaSP123')
        mail.sendmail(self.msg['From'],to , self.msg.as_string())
        mail.quit()

if __name__ == '__main__':
    a = Email('luis@4suredesign.com','Hola como estas','ujfdhiusdhisudhfiusdhfself.')        