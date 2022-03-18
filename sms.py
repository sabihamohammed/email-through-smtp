from twilio.rest import Client 
 
account_sid = 'ACbd5550086464c3b546af5b33eb30b540' 
auth_token = 'd0d12c1c1dc703a5aea9a5c60c2d7445' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              from_ ='+13193186124', 
                              body='hey handsome',      
                              to='+919791788409' 
                          ) 
 
print(message.sid)