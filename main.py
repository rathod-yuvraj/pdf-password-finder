import pikepdf
import time

pdf_file=input("PDF:")
password_list=input("PASSWORD LIST:")
passwords=open(password_list)

i=0
start_time=time.time()
for password in passwords:
    password=password.strip("\n")

    i+=1
    print("\r {}  Password Tested!" .format(i),end="")
    try:
        pikepdf.open(pdf_file,password=password)

        print("\n" + " *" * 20 )

        end_time =time.time()
        print("PASSWORD FOUND" )
        print("PASSWORD : {}" .format(password))
        print("[{}]PASSWORD TESTED in {} SECOND !".format(i,str(end_time=start_time)  [:4]))

        print("* " *20)

        passwords.close()
        break
    except:
        pass    
