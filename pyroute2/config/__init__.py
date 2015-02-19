import socket
import multiprocessing

# classes that one can to substitute if needed
SocketBase = socket.socket
MpPipe = multiprocessing.Pipe
MpProcess = multiprocessing.Process
