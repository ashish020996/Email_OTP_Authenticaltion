# OTP generation and validation on Email

# Deployment Process

Step 1: Open settings.py from below address.
	<Your Drive>\Email Authentication via OTP\auproject --> settings.py

Step 2: Make following changes.
	EMAIL_HOST_USER = "<Enter Your Email>@gmail.com" ---> Enter your email address here. The OTP will be sent to reciever from this email address.
	EMAIL_HOST_PASSWORD = "<Authentication Key>"     ---> Generate Auth. key. 

Step 3: Open command prompt inside <Your drive>\Email Authentication via OTP\auproject.

Step 4: Type following command  --> python manage.py runserver

Step 5: Open browser and type http://127.0.0.1:8000/.

Step 6: Signup and you will receive OTP using the HOST_USER you entered in Step 2.


Thank you and Enjoy coding...!!!!!

Ashish Mulgaonkar 

Feel free to reach me on:
ashish020996@gmail.com