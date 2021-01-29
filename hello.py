#!/usr/bin/env python3

import os
import json
import secret
import cgi
import cgitb
cgitb.enable()

#FROM:
#END FROM

"""
print('Content-type: application/json')
# 'Content-type: application/octet-stream' download data
print()
print(json.dumps(dict(os.environ), indent=2))
"""

print('Content-Type: text/html')
print()
print("""
<!doctype html>
<html>
<body>
<h1>HELLO I AM HTML</h1>""")

print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print("<ul>")
for parameter in os.environ['QUERY_STRING'].split('&'):
    (name,value) = parameter.split('=')
    print(f"<li><em>{name}</em> = {value}</li>")

val1 = "hh"
print(f"""
</ul>

 <form method="GET" action="hello.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>

    """)

form = cgi.FieldStorage()
userINPUT = form.getvalue("username")
passwordINPUT = form.getvalue("password")


if secret.username == userINPUT and secret.password == passwordINPUT:
    #Use a http get or post I think Set-Cookie: usercookie=userINPUT
    #Set-Cookie: passwordcookie=passwordINPUT
    
    print(f"""
    
        <form method="POST" action="hello.py">
            Set-Cookie: usercookie={userINPUT}
            Set-Cookie: passwordcookie={passwordINPUT}
        </form>

            
            <h1> Welcome, {userINPUT}! </h1>
        <p> <small> Pst! I know your password is
            <span class="spoilers"> {passwordINPUT}</span>.
            </small>
        </p>
        """)


"""
{secret.username}
{secret.password}
{userINPUT}
{passwordINPUT}
"""
print(f"""
</body>
</html>
""")






