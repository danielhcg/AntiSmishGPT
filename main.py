import openai 

#initializing personal key
openai.api_key = '[insert api key here]'

def detect(sender, body):
    try:
        detectionPrompt = f"""
I want you to act as a smishing detector to determine whether a given SMS message, including its sender and body, is a smishing message or a legitimate message. Your analysis should be thorough and evidence-based. Smishing SMS messages often impersonate legitimate brands and use social engineering techniques to deceive users. These techniques include, but are not limited to: fake rewards, fake warnings about account problems, and creating a sense of urgency or interest. Spoofing the sender address and embedding deceptive HTML links are also common tactics.

Analyze the SMS message by following these steps:
1. Identify any impersonation of well-known brands in the sender information and SMS body.
2. Examine the sender for spoofing signs, such as discrepancies in the sender name or email address.
3. Analyze the SMS body for social engineering tactics designed to induce clicks on hyperlinks. Inspect URLs to determine if they are misleading or lead to suspicious websites.
4. Provide a comprehensive evaluation of the SMS, highlighting specific elements that support your conclusion. Include a detailed explanation of any smishing or legitimacy indicators found in both the sender information and the SMS message.
5. Summarize your findings and provide your final verdict on the legitimacy of the SMS, supported by the evidence you gathered.

Sender: {sender}
SMS Body: {body}
"""

        #request to api 
        response = openai.Completion.create(
            engine="gpt-4",  
            prompt=detectionPrompt,
            max_tokens=100
        )

        # Parse the response
        output = response.choices[0].text.strip()
        print(output)

    except Exception as error:
        print("error:", str(error))

senderArg = "+1 (806) 224-7886"
bodyArg = "wel01.us/r/rest05WELLS FARGO(CS):Profilelocked because of unusual activities, kindly restore.Reply STOP to unsubscribe"

detect(senderArg, bodyArg)
