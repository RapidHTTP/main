from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # 默认请求路径为 index.html

        try:
            # 尝试打开请求的文件
            file_path = '.' + self.path
            with open(file_path, 'rb') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        except IOError:
            # 文件未找到，发送自定义的 404 页面
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.send_404_page()

    def send_404_page(self):
        with open('404.html', 'rb') as file:
            content = file.read()
            self.wfile.write(content)

    def log_message(self, format, *args):
        # 禁用请求日志输出
        return


def run_server(port):
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'RapidHTTP已经运行在 {port}端口上了！')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server(8000)
