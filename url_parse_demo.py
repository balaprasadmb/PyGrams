import urlparse

url = 'https://uat49.auruspay.com/storeservices/orderreview.jsp?cart_id=123456789&session_id=200000000000000000000000147908&wallet_id=2&oauth_token=4b0bcd189ad947e922f5ab4fa5c40a43d7e93a27&oauth_verifier=4b0bcd189ad947e922f5ab4fa5c40a43d7e93a27&checkoutId=3468471081307195529&checkout_resource_url=https%3A%2F%2Fsandbox.api.mastercard.com%2Fmasterpass%2Fpaymentdata%2F4b0bcd189ad947e922f5ab4fa5c40a43d7e93a27&mpstatus=success'

r = urlparse.urlparse(url)

print r

print dir(r)

print 'params: ',r.params

print r.query

s = str(r.query)

qr = s.split('&')

for i in qr:
    if i.find('checkoutId') != -1:
        print i.split('=')[1]