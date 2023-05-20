from http .server import ThreadingHTTPServer ,BaseHTTPRequestHandler #line:1
class SimpleHTTPRequestHandler (BaseHTTPRequestHandler ):#line:4
    def do_GET (O0O000OO000OO0000 ):#line:5
        if O0O000OO000OO0000 .path =='/':#line:6
            O0O000OO000OO0000 .path ='/index.html'#line:7
        try :#line:9
            OOOOO00OOO00OO0OO ='.'+O0O000OO000OO0000 .path #line:11
            with open (OOOOO00OOO00OO0OO ,'rb')as OO00000OOO00OOOO0 :#line:12
                O0OO00000O0OOOOO0 =OO00000OOO00OOOO0 .read ()#line:13
                O0O000OO000OO0000 .send_response (200 )#line:14
                O0O000OO000OO0000 .send_header ('Content-type','text/html')#line:15
                O0O000OO000OO0000 .end_headers ()#line:16
                O0O000OO000OO0000 .wfile .write (O0OO00000O0OOOOO0 )#line:17
        except IOError :#line:18
            O0O000OO000OO0000 .send_response (404 )#line:20
            O0O000OO000OO0000 .send_header ('Content-type','text/html')#line:21
            O0O000OO000OO0000 .end_headers ()#line:22
            O0O000OO000OO0000 .send_404_page ()#line:23
    def send_404_page (O00O0O00OO000OO00 ):#line:25
        with open ('404.html','rb')as O00O0O0O000O0O000 :#line:26
            OO0OO0OOOOO00OO0O =O00O0O0O000O0O000 .read ()#line:27
            O00O0O00OO000OO00 .wfile .write (OO0OO0OOOOO00OO0O )#line:28
    def log_message (OO0000O0O0OO00OO0 ,O0OOOO0O00O00O0O0 ,*O00O0000000000O0O ):#line:30
        return #line:32
def run_server (OO0OO0O00000O00OO ):#line:35
    OO00O000O00O0O00O =('',OO0OO0O00000O00OO )#line:36
    O00O0O000OOOO000O =ThreadingHTTPServer (OO00O000O00O0O00O ,SimpleHTTPRequestHandler )#line:37
    print (f'RapidHTTP已经运行在 {OO0OO0O00000O00OO}端口上了！')#line:38
    O00O0O000OOOO000O .serve_forever ()#line:39
if __name__ =='__main__':#line:42
    run_server (8000 )#line:43
