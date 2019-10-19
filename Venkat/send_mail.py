# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("venkateswaramalepati@gmail.com", "ammananna@143") 
  
# message to be sent 
message = "Test Mail from Python"
  
# sending the mail 
s.sendmail("venkateswaramalepati@gmail.com", "venkateswaramalepati@gmail.com", message) 
  
# terminating the session 
s.quit()