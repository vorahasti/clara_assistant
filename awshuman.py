import pyttsx3 as sp
import speech_recognition as sr
import os

print("I am Clara your personal assistant 24x7 to help you.")
sp.speak("I am Claraa your personal assistant 24 into 7 to help you.")

while True:
    r=sr.Recognizer()

    print("\nWhat may I do for you Hasti?\n")
    sp.speak("What may I do for you Hasti?")

    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)
        print("Listening Done! \n")  
  
    o=r.recognize_google(audio)
    print("\nYou said ----> "+o)
    
    o=o.lower()
    if("start"in o or "run" in o):
        print("\nYes Hasti. Instance Available in stopped state are:\n")
        sp.speak("Yes Hasti. Instance Available in stopped state are:")
        os.system("aws ec2 describe-instances --query \"Reservations[*].Instances[*].{Instance:InstanceId,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}\" --filters Name=instance-state-name,Values=stopped --output yaml")
        print("\n Enter Instance Id of Instance you wish to start",end=' ')
        sp.speak("Enter Instance Id of Instance you wish to start")
        i=input()
        os.system("aws ec2 start-instances --instance-ids "+i)
        sp.speak("Yes,Hasti Your Instance will take few time to Start.")
        print("You could check your AWS Console")
        sp.speak("You can check your AWS Console")
    elif("state" in o or "status" in o):
        print("All the instances in running state are as follows:\n")
        sp.speak("All the instances in running state are as follows:\n")
        os.system("aws ec2 describe-instances --query \"Reservations[*].Instances[*].{Instance:InstanceId,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}\" --filters Name=instance-state-name,Values=running,terminated --output yaml")
        print("All the instances in stop state are as follows:\n")
        sp.speak("All the instances in stop state are as follows:\n")
        os.system("aws ec2 describe-instances --query \"Reservations[*].Instances[*].{Instance:InstanceId,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}\" --filters Name=instance-state-name,Values=stopped --output yaml")
    elif("stop"in o):
        print("\nYes Hasti. Instance Available in start state are:\n")
        sp.speak("Yes Hasti. Instance Available in start state are:")
        os.system("aws ec2 describe-instances --query \"Reservations[*].Instances[*].{Instance:InstanceId,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}\" --filters Name=instance-state-name,Values=running --output yaml")
        print("\n Enter Instance Id of Instance you wish to stop",end=' ')
        sp.speak("Enter Instance Id of Instance you wish to stop")
        i=input()
        os.system("aws ec2 stop-instances --instance-ids "+i)
        sp.speak("Yes,Hasti Your Instance will take few time to stop.")
        print("You could check your AWS Console")
        sp.speak("You can check your AWS Console")
        
    elif("list"in o or "detail" in o or "details" in o):
        print("Detail about all the instances:\n")
        sp.speak("Detail about all the instances:")
        os.system("aws ec2 describe-instances --instance-ids --query \"Reservations[*].Instances[*].{LaunchTime:LaunchTime,Instance:InstanceId,ImageId:ImageId,VolumeInfo:BlockDeviceMappings,SubnetId:SubnetId,AvailabilityZone:Placement.AvailabilityZone,PublicIP:PublicIpAddress Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}\" --filters Name=instance-state-name,Values=stopped,running --output yaml")
       
        
    elif("key" in o or "pair" in o or "keypair" in o):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("What name would you like to give your keypair?\n")
            sp.speak("What name would you like to give your keypair?")
            print("Speak...")
            audio=r.listen(source)
        o=r.recognize_google(audio)
        print("Creating key pair "+o)
        os.system("aws ec2 create-key-pair --key-name "+o)
        sp.speak("Your Keypair"+o+" has been created.")
        
    elif("security" in o or "group" in o or "security group" in o):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("What name would you like to give security group?")
            sp.speak("What name would you like to give security group?")
            print("Speak...")
            audio=r.listen(source)
        o=r.recognize_google(audio)
        print("Creating seurity group "+o)
        os.system("aws ec2 create-security-group --group-name "+o+" --description firewall")
        sp.speak("Your Security Group"+o+" has been created.")
        
        s=sr.Recognizer()
        with sr.Microphone() as source:
            print("What Inbound rule you would like to apply?")
            sp.speak("What Inbound rule you would like to apply?")
            print("Speak...")
            audio=s.listen(source)
        p=r.recognize_google(audio)
        print("Creating Inbound Rule "+p)
        os.system("aws ec2 authorize-security-group-ingress --group-name "+o+" --protocol all --cidr 0.0.0.0/0")
     
    elif("launch" in o):
        print("Yes,Hasti. Select among following AMI:\n")
        sp.speak("Yes,Hasti. Select among following A M I")
        
        print("1. Amazon Linux 2 AMI (HVM), SSD Volume Type - ami-0e306788ff2473ccb (64-bit x86)\n2. Microsoft Windows Server 2019 Base - ami-0b2f6494ff0b07a0e (64-bit x86) \n3. Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-03cfb5e1fb4fac428 \n4. Red Hat Enterprise Linux 8 (HVM), SSD Volume Type - ami-052c08d70def0ac62 (64-bit x86) \n5. Red Hat Enterprise Linux 8 (HVM), SSD Volume Type - ami-0ad289a92ed067259 (64-bit Arm)\n6. SUSE Linux Enterprise Server 15 SP2 (HVM), SSD Volume Type - ami-0d0522ed4db1debd6 (64-bit x86) \n7. Ubuntu Server 20.04 LTS (HVM), SSD Volume Type - ami-0cda377a1b884a1bc (64-bit x86) \n9. Ubuntu Server 20.04 LTS (HVM), SSD Volume Type - ami-086c142842468ba9d (64-bit Arm)")
        
        print("\n\nYour Choice:",end=' ')
        a=input()
        if(a==1):
            aid="ami-0e306788ff2473ccb"
        elif(a==2):
            aid="ami-0b2f6494ff0b07a0e"
        
        print("You selected "+a+" as your AMI. \n")
        sp.speak("You selected "+a+" as your A M I.")
           
        print ("t2.micro is your default instance type \n")
        sp.speak("t2.micro is your default instance type")
        
        print ("default subnet in any availability-zone selected \n")
        sp.speak("default subnet in any availability-zone selected")
        
        print ("Creating Volume of 8GB \n")
        sp.speak("Creating Volume of 8GB \n")
        
        print ("Enter number of instance:",end=' ')
        sp.speak("Enter number of instance")
        n=input()
        print ("You selected "+n)
        sp.speak("You selected "+n)
        
        
        
        s=sr.Recognizer()
        with sr.Microphone() as source:
            print("\nWhat name would you like to give your Instance?")
            sp.speak("What name would you like to give your Instance?")
            print("\nSpeak...")
            audio=s.listen(source)
        a=r.recognize_google(audio)
        print("Your Instance name is "+a)
        sp.speak("Your Instance name is"+a)
        
        with sr.Microphone() as source:
            print("\nYour Security Group Name")
            sp.speak("Your Security Group Name")
            print("Speak")
            audio=s.listen(source)
        p=r.recognize_google(audio)
        print("Security Group Name is "+p)
        sp.speak("Security Group Name is "+p)
        
        with sr.Microphone() as source:
            print("\nYour Key Pair")
            sp.speak("Your Key Pair")
            print("Speak...")
            audio2=s.listen(source)
        q=r.recognize_google(audio2)
        print("Your Key Pair is "+q)
        sp.speak("Your Key Pair is "+q)
        
        print("\n Launching instance \n")
        print("\nInstance has been launched successfully\n")
        sp.speak("Instance has been launched successfully")
        
        os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --key-name "+q+" --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value="+a+"}] --security-groups "+p+" --instance-type t2.micro --placement AvailabilityZone=ap-south-1a --count "+n)
        print("\n Instance Launched Successfully \n")      
    elif("create" in o and "volume" in o):
            s=sr.Recognizer()
            with sr.Microphone() as source:
                print("\nWhat name would you like to give to Volume? ")
                sp.speak("What name would you like to give to Volume? ")
                print("\nSpeak...")
                audio=s.listen(source)
            a=r.recognize_google(audio)
                
            print("Okay, Please enter Size of Volume in GB: ",end=' ')
            sp.speak("Okay, Please enter Size of Volume in GB")
            v=input()
            os.system("aws ec2 create-volume --availability-zone ap-south-1a --size "+v+" --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value="+a.lower()+"}]")  
            print("\nYour Volume "+a+" of size "+v+" GB is sucessfully Created.\n")
            sp.speak("Your Volume "+a+" of size "+v+" GB is sucessfully Created.") 
        
    elif("attach" in o and "volume" in o):
            sp.speak("Yes, Wait for a while")
            print("VOLUME DETAILS:\n")
            os.system("aws ec2 describe-volumes --filters --query \"Volumes[*].{ID:VolumeId,Tag:Tags}")
            print("\n Enter Volume Id using above details",end=' ')
            sp.speak("Enter Volume Id using above details")
            vi=input()
            print("\nINSTANCE DETAILS:\n")
            os.system("aws ec2 describe-instances --output yaml-stream --filters Name=instance-type,Values=t2.micro --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" ")
            print("\n Enter Instance Id using above details",end=' ')
            sp.speak("Enter Instance Id using above details")
            iv=input()
            os.system("aws ec2 attach-volume --volume-id "+vi+" --instance-id "+iv+" --device /dev/sdf")
            print("\nVolume Attached Sucessfully.\n")
            sp.speak("\nVolume Attached Sucessfully.")
    elif("terminate"in o):
            print("\nINSTANCE DETAILS:\n")
            os.system("aws ec2 describe-instances --filters Name=instance-type,Values=t2.micro --query \"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}\" --output yaml")
            print("\n Enter Instance Id of Instance you wish to terminate",end=' ')
            sp.speak("Enter Instance Id of Instance you wish to terminate")
            i=input()
            os.system("aws ec2 terminate-instances --instance-ids "+i)
            sp.speak("Your Instance has terminated.")
            sp.speak("You can check your AWS Console")
            
    elif("wait"in o or "hold" in o): 
        print("Okay Waiting")
        sp.speak("Okay Waiting")
        print("Would you like to continue? (yes=y)", end='')
        a=input()
        if(a=="y"):
            print("Okay Continuing")
            sp.speak("Okay Continuing")        
        else:
            os.system("cls")
            break
    else:
        sp.speak("Have a good day Hasti. You can call me anytime for help later.")
        os.system("cls")
        break
        
    
    
