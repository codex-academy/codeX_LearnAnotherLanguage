print("Hello! This is Mobile Budget App")
#print("Enter your Mobile Network Provider")
networkProvider = input("Enter your Mobile Network Provider:")
networkProvider1 = "MTN"
networkProvider2 = "Vodacom"
networkProvider3 = "Cell C"
networkProvider4 = "Virgin Mobile"

MTN_Pay_Per_Second = {"Peak SMS Rates" : "R 0.50",
		                "Call Rates In Network" : "R 0.70",
		                "Call Rates Other Network" :"R 0.79",
		                "Data Per MB" :"R 0.99"}
MTN_Zone_Per_Second = {"Peak SMS Rates" : "R 0.75",
		                 "Call Rates In Network" : "R 2.50",
		                 "Call Rates Other Network" : "R 2.50",
		                 "Data Per MB" : "R 2.00"}
while networkProvider == networkProvider1:
    print('MTN_Pay_Per_Second Plan.')
    print("MTN_Zone_Per_Second Plan") # There are four spaces in front of print.
    choosePlan = input("choosePlan:")
    


    if choosePlan == "MTN_Pay_Per_Second":
        print(MTN_Pay_Per_Second) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.7
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.79
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.99
        print('You have',dataPerMB ,'data Per MB')

    if choosePlan == "MTN_Zone_Per_Second":
        print(MTN_Zone_Per_Second)
        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.75
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/2.50
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/2.50
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/2.00
        print('You have',dataPerMB ,'data Per MB')


#   if guess == number:
        break

if networkProvider == networkProvider2:
    
    print('Vodacom_Pay_Per_Second Plan.')
    print("Vodacom_Zone_Per_Second Plan") # There are four spaces in front of print.
    choosePlan = input("choosePlan:")
    


    if choosePlan == "Vodacome_Pay_Per_Second":
        print(MTN_Pay_Per_Second) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.7
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.79
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.99
        print('You have',dataPerMB ,'data Per MB')

    if choosePlan == "Vodacom_Zone_Per_Second":
        print(Vodacom_Zone_Per_Second)

        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.75
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/2.50
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/2.50
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/2.00
        print('You have',dataPerMB ,'data Per MB')


if networkProvider == networkProvider3 :
    
    print('Vodacom_Pay_Per_Second Plan.')
    print("Vodacom_Zone_Per_Second Plan") # There are four spaces in front of print.
    choosePlan = input("choosePlan:")
    


    if choosePlan == "Vodacome_Pay_Per_Second":
        print(MTN_Pay_Per_Second) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.7
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.79
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.99
        print('You have',dataPerMB ,'data Per MB')

    if choosePlan == "Vodacom_Zone_Per_Second":
        print(Vodacom_Zone_Per_Second)

        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.75
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/2.50
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/2.50
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/2.00
        print('You have',dataPerMB ,'data Per MB')

if networkProvider == networkProvider4 :
    print('Vodacom_Pay_Per_Second Plan.')
    print("Vodacom_Zone_Per_Second Plan") # There are four spaces in front of print.
    choosePlan = input("choosePlan:")
    


    if choosePlan == "Vodacome_Pay_Per_Second":
        print(MTN_Pay_Per_Second) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.7
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.79
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.99
        print('You have',dataPerMB ,'data Per MB')

    if choosePlan == "Vodacom_Zone_Per_Second":
        print(Vodacom_Zone_Per_Second)

        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.75
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/2.50
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/2.50
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/2.00
        print('You have',dataPerMB ,'data Per MB')


else :
	print('Thanks for using our App')
