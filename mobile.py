print("Hello! This is Mobile Budget App")
#print("Enter your Mobile Network Provider")
networkProvider = input("Enter your Mobile Network Provider:")
networkProvider1 = "MTN"
networkProvider2 = "Vodacom"
networkProvider3 = "Cell C"
networkProvider4 = "Virgin Mobile"
#mtn plans
MTN_Pay_Per_Second = {"Peak SMS Rates" : "R 0.50",
		                "Call Rates In Network" : "R 0.70",
		                "Call Rates Other Network" :"R 0.79",
		                "Data Per MB" :"R 0.99"}
MTN_Zone_Per_Second = {"Peak SMS Rates" : "R 0.75",
		                 "Call Rates In Network" : "R 2.50",
		                 "Call Rates Other Network" : "R 2.50",
		                 "Data Per MB" : "R 2.00"}
#vodacom plan
vodacom_Prepaid_79c = {  "Peak SMS Rates":"R 0.50",
                        "Call Rates In Other Network" : "R 0.79",
                        "Call Rates In Other Network" : "R 0.79",
                        "Data Per MB" : "null"}


vodacom4Less        = {  "Peak SMS Rates":"R 0.80",
                         "Call Rates In Network" : "R 2.60",
                         "Call Rates Other Network":"R 2.89",
                         "Data per MB" : "Null"}
#cell C plans                         
cellC_66C_Benefits  = {  "Peak SMS Rates":"R 0.50",
                         "Call Rates In Network" : "R 0.66",
                         "Call Rates Other Network":"R 0.66",
                         "Data per MB" : "R 2.00"}

easyChat  = {  "Peak SMS Rates":"R 0.50",
                         "Call Rates In Network" : "R 1.50",
                         "Call Rates Other Network":"R 1.50",
                         "Data per MB" : "R 0.79"}
#Virgin Mobile plans

virgin_Mobile_PrePaid  = {"Peak SMS Rates":"R 0.50",
                         "Call Rates In Network" : "R 0.99",
                         "Call Rates Other Network":"R 0.99",
                         "Data per MB" : "R 0.99"}




                     
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
        print("You have",round(callRatesInNetworks,1), 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.79
        print("You have",round(callRatesOtherNetworks,1), 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.99
        print('You have',round(dataPerMB,1) ,'data Per MB')

    if choosePlan == "MTN_Zone_Per_Second":
        print(MTN_Zone_Per_Second)
        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.75
        print('You can make',round(peakSMSrates,1) ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/2.50
        print("You have",round(callRatesInNetworks,1), 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/2.50
        print("You have",round(callRatesOtherNetworks,1), 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/2.00
        print('You have',round(dataPerMB,1),'data Per MB')


#   if guess == number:
        break

if networkProvider == networkProvider2:
    
    print('vodacom_Prepaid_79c')
    print("vodacom4Less") # There are four spaces in front of print.
    choosePlan = input("choosePlan:")
    


    if choosePlan == "vodacom_Prepaid_79c":
        print(vodacom_Prepaid_79c) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',round(peakSMSrates,1) ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.79
        print("You have",round(callRatesInNetworks,1), 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.79
        print("You have",round(callRatesOtherNetworks,1), 'calls to Networks')

        #Data Per MB
        #dataPerMB = currentAmount/null
        print('N/A')

    if choosePlan == "vodacom4Less":
        print(vodacom4Less)

        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.80
        print('You can make',round(peakSMSrates,1) ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/2.60
        print("You have",round(callRatesInNetworks,1), 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/2.89
        print("You have",round(callRatesOtherNetworks,1), 'calls to Networks')

        #Data Per MB
        #dataPerMB = currentAmount/2.00
        #print('You have',dataPerMB ,'data Per MB')
        print('N/A')


if networkProvider == networkProvider3 :
    
    print('cellC_66C_Benefits')
    print("easyChat") # There are four spaces in front of print.
    choosePlan = input("choosePlan:")
    


    if choosePlan == "cellC_66C_Benefits":
        print(cellC_66C_Benefits) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.66
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.66
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/2.00
        print('You have',dataPerMB ,'data Per MB')

    if choosePlan == "easyChat":
        print(easyChat)

        
         # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',peakSMSrates ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/1.50
        print("You have",callRatesInNetworks, 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/1.50
        print("You have",callRatesOtherNetworks, 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.79
        print('You have',dataPerMB ,'data Per MB')

if networkProvider == networkProvider4 :
    print('virgin_Mobile_PrePaid')
    
    choosePlan = input("choosePlan:")
    


    if choosePlan == "virgin_Mobile_PrePaid":
        print(virgin_Mobile_PrePaid) # There are eight spaces in front of print.
        currentAmount = input('EnterYourCurrentAmount:')
        currentAmount = int(currentAmount)
        #Number of sms you can make
        peakSMSrates = currentAmount/0.50
        print('You can make',round(peakSMSrates,0) ,'SMS')

        #Number of Call in Network
        callRatesInNetworks = currentAmount/0.99
        print("You have",round(callRatesInNetworks,1), 'calls in Networks')

        #Number of Calls to Other Networks
        callRatesOtherNetworks = currentAmount/0.99
        print("You have",round(callRatesOtherNetworks,1), 'calls to Networks')

        #Data Per MB
        dataPerMB = currentAmount/0.99
        print('You have',round(dataPerMB,1) ,'data Per MB')

    
else :
	print('Thanks for using our App')
