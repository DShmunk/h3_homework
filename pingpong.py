from multiprocessing import Process, Pipe
from time import sleep
from os import getpid

# receive a message
# print it as f"Process{getpid()} got message: {msg}"
# sleep before responding
# send response message back
def ponger(receiver, sender, response):
    while True:
        response = receiver.recv()
        print(f"{getpid()} got message: {response}")
        sleep(0.3)
        if response == "ping":
          response = "pong"
        else:
          response = "ping"
        sender.send(response)
        print(f"{getpid()} send message: {response}")


if __name__ == "__main__":
    receiver_1, sender_1 = Pipe()
    receiver_2, sender_2 = Pipe()
    response = "ping"
    p_1 = Process(target=ponger, args=(receiver_1, sender_2, response)).start()
    p_2 = Process(target=ponger, args=(receiver_2, sender_1, response)).start()
    sender_2.send(response)
# use pipe
# create 2 processes that will use ponger, give them different sides of pipes
# they also need a specific message (either ping or pong)
# start both processes
# initiate ping-pong by sending first message to one of the pipes