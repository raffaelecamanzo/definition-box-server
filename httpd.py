import http.server

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
HttpServer = http.server.HTTPServer

if __name__ == '__main__':
    httpd = HttpServer(('', PORT), Handler)
    print('Starting server at port', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server stopped')
