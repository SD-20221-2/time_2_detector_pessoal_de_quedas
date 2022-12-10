import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    swimmer_age = input("Enter your age: ")
    remote_result = proxy.verify_swimmer_category(swimmer_age)
    print(remote_result)