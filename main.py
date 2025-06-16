from livereload import Server, shell

def rebuild():
    print("test")

server = Server()
server.watch('index.html', rebuild)
server.serve(root='.')