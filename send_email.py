import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ankocamillus@gmail.com"
    password = "hzrlaywutaxrdlzo"

    receiver = "ankocamillus@gmail.com"
    context = ssl.create_default_context()

    # message = """\
    # Subject: Hi!
    # Hi!
    # How are you?
    # Bye!
    # """


    with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)