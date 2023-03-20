# Call a Secured API Using JSON Web Token (JWT) Profile 

## ToC
1. [Create a Service User and Private/Public Keys in ZITADEL](#1)
2. [Generate a Token](#2)
3. [Invoke the API](#3)


## 1. Create a Service User and Private/Public Keys in ZITADEL <a name="1"></a>

1. Go to the **Users** tab in your organization as shown below and click on the **Service User** tab : 

2. To add a service user, click on the **New** button. 

3. Next, add the details of the service user and select either **Bearer** or **JWT** for Access Token Type and click on **Create**. For this example, we will select **JWT**. 

4. Now you will see the saved details. 

5. Next,  we need to generate a private-public key pair in ZITADEL and you must get the private key to sign your JWT.  Go to **Keys** and click on **New**. 

6. Select type **JSON** and click **Add**
7. Download the key by clicking **Download**. After the download, click **Close**. 

8. You will see the following screen afterwards. 

9. The downloaded key will be of the following format: 


<img
    src="screenshots/1.png"
    width="75%"
    alt="Register the API"
/>
