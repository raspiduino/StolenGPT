import requests
import time

class StolenGPT():
    # Init object
    def __init__(self):
        # API endpoint
        self.post_endpoint = "https://chat.mindtastik.com/test3/api.php"
        self.get_endpoint = "https://chat.mindtastik.com/test3/stream.php"

        # POST request header, or the API will return error "No conversation"
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        # Message buffer, for storing old message
        # Can be cleared using clear()
        self.buffer = []
        
        # Session ID
        self.session_id = ""
        
        # API message string
        self.success_str = '{"status":"success","msg":"Successfully sent request","reply":"event"}'
        self.done_str = 'data: [DONE]\n\n'
        
        # Max request retry when requests is not succeed
        self.retry = 5

    # Clear chat messages buffer
    def clear(self):
        self.buffer = []
    
    # Set max request retry
    
    # Get returned message
    def get(self):
        # Add session ID to cookies
        cookies = {'PHPSESSID': self.session_id}

        # Send request
        r = requests.get(self.get_endpoint, cookies=cookies)
        
        # Retry counter
        rc = 0
        
        # Repeat until response is done
        while r.text[-14::] != self.done_str:
            r = requests.get(self.get_endpoint, cookies=cookies)
            
            # Return None if retry exceeded
            if rc == self.retry:
                return None
            
            # Increase retry counter
            rc += 1

            # Delay 1 second
            time.sleep(1)

            # Debug message
            print("Get request failed: " + r.text[-14::])
        
        # Message placeholder
        msg = ""
        
        # Get message array
        a = [i.split("\n\n")[0] for i in r.text.split("data: ")[1:]]
        
        # Get message
        # Ignore first and last element of the array, since first element is
        # the returned status, and last element is just the string "[DONE]"
        for i in a[1:-1]:
            try:
                msg += i.split('"content":"')[1].split('"}')[0]
            except Exception as e:
                pass
        
        # Append message to chat buffer
        self.buffer[-1]["ai"] = msg
        
        return msg

    # Send message buffer
    def send(self):
        # Convert message buffer to data for request
        data = '{"conversation":"' + str(self.buffer).replace("None", "null").replace("'", "\\\"") + '"}'
        #print(data)

        # Send request
        r = requests.post(self.post_endpoint, headers=self.headers, data=data)
        
        # Retry counter
        rc = 0
        
        # Repeat until response is done
        while r.status_code != 200 or r.text != self.success_str:
            r = requests.post(self.post_endpoint, headers=self.headers, data=data)
            
            # Return None if retry exceeded
            if rc == self.retry:
                return None
            
            # Increase retry counter
            rc += 1

            # Delay 1 second
            time.sleep(1)

            # Debug message
            print("Send request failed:", str(r.status_code), r.text)

        # Set session id according to what the server returned
        self.session_id = r.headers["Set-Cookie"].split("; ")[0].split("PHPSESSID=")[1]

        # Get returned message
        return self.get()
    
    # Add user message to buffer
    def add(self, msg):
        self.buffer.append({"user":msg,"ai":None,"id":int(time.time() * 1000)})
    
    # Chat function (the one you are expected to use :))
    def chat(self, msg):
        # Add message to the messsage buffer
        self.add(msg)

        # Send buffer and return message
        return self.send()