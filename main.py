import smtplib

my_email = "mail009527@gmail.com"
password = "iamalex1992"

# my_email = "562937707@qq.com"
# password = "cxeaeccgiufybfjc"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="562937707@qq.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")

