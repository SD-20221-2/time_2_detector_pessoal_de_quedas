import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    average_balance = input("Enter last year's average balance: $")
    remote_result = proxy.credit(average_balance)
    print(remote_result)