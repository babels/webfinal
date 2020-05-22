from flask import Flask, render_template, request

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY='yourkeyhere'

app = Flask(__name__)


def sndmsg( sndr, rcvr, subj, cont ):
  ml = str("<strong>%s</strong>" % cont)
  message = Mail(
    from_email    =  sndr,
    to_emails     =  rcvr,
    subject       =  subj,
    html_content  =  ml)

  try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    rsp = sg.send(message)
    rc = rsp.status_code

    print(rc)
    print(rsp.body)
    print(rsp.headers)

    return rc

  except Exception as e:
    print(e)

    return 500


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/quote', methods=['POST'])
def qut():

  fnme = None
  lnme = None
  ceml = None
  cpne = None
  cmsg = None

  ner = request.json.items()

  for ky, val in ner:
     ky  = str( ky )
     val = str( val )

     if ( ky == "fnme" ):
       fnme = val
     if ( ky == "lnme" ):
       lnme = val
     if ( ky == "ceml" ):
       ceml = val
     if ( ky == "cpne" ):
       cpne = val
     if ( ky == "cmsg" ):
       cmsg = val

  lg = str( "Got %s %s %s %s %s" % ( fnme,lnme,ceml,cpne,cmsg) )

  rcv = "iamthe42spiral@gmail.com@gmail.com"

  cnt = str("RECIEVED REQUEST FOR QUOTE<br><br> From:<br>%s %s<br>Phone: %s<br> Email: %s<br><br>MESSAGE:<br>%s" % (fnme, lnme, cpne, ceml, cmsg) )
  cn2 = str("Thank you for your interest in Nachorny Landscaping and Design.<br>  This automated message is to inform you that your request for a quote has been recieved and that one of our qualified specialists witll be in touch with you within twenty four hours.<br><br>&emsp;Sincerely<br>&emsp;&emsp;<i>-Nachorny Design</i>")
  sndmsg( "god@nachorny.design", rcv, "New Quote", cnt)
  sndmsg( "NOREPLY@nachorny.design", ceml, "Request Recieved!", cn2)
  print(lg)

  return "Your Request Has Been Recieved!"


@app.errorhandler(500)
def server_error(e):

  try:
    e = str(e).encode('utf-8')
  except:
      return "200"

  exc = str("[!] Bad Request:  %s" % e)
  print(exc)
  return """
  Why yes of course
  """.format(e), 200

@app.errorhandler(404)
def server_error(e):
  try:
    e = str(e).encode('utf-8')
  except:
      return "200"

  exc = str("[!] Bad Request:  %s" % e)
  print(exc)
  return """
  I'll get right on that boss
  """.format(e), 202



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=443, debug=False)
# [END gae_python37_app]


