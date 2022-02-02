import os
from pathlib import Path
from datetime import datetime

# global variable to see if user is signed-in
signedIn = False
# get the name of current user
current_Name = ""
firstName = ""
lastName = ""
userName = ""
password = ""
emailOpt = ""
smsOpt = ""
advOpt = ""
languageOpt = ""
titleOpt = "None"
majorOpt = "None"
UniOpt = "None"
aboutOpt = "None"
expOpt1Title = "Title: None"
expOpt1Emp = "Employer: None"
expOpt1Start = "Start Date: None"
expOpt1End = "End Date: None"
expOpt1Loc = "Job Location: None"
expOpt1Des = "Description: None"
expOpt2Title = "Title: None"
expOpt2Emp = "Employer: None"
expOpt2Start = "Start Date: None"
expOpt2End = "End Date: None"
expOpt2Loc = "Job Location: None"
expOpt2Des = "Description: None"
expOpt3Title = "Title: None"
expOpt3Emp = "Employer: None"
expOpt3Start = "Start Date: None"
expOpt3End = "End Date: None"
expOpt3Des = "Description: None"
expOpt3Loc = "Job Location: None"
eduOptSchool = "School: None"
eduOptDegree = "Degree: None"
eduOptYears = "Years: None"
subscription = ""
variable = 0
placeholder = "Placeholder"


# display menu that lets user select options
def menu():
    if not signedIn:
        print("\nWant to hear what students have to say about InCollege?")
        print("\nRead about how InCollege helped Ethan Timor:")
        print('\t "I was never able to land an interview or internship in college. ')
        print("\t Thankfully, I discovered InCollege and I couldn't be more thankful! ")
        print("\t Within days, I had interviews, and offers from companies like:")
        print("\t Tesla, Microsoft, Google, and Apple")
        print("\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.")
        print('\t It would not be possible without InCollege."')

    if signedIn:
        number_of_requests = countRequests()
        if number_of_requests == 1:
            print("You have 1 pending friend request!\n")
        if number_of_requests > 1:
            print(f"You have {number_of_requests} pending friends requests!")

        number_of_messages = countMessages(userName)
        if number_of_messages == 1:
            print("You have 1 new message in your inbox!\n")
        if number_of_messages > 1:
            print(f"You have {number_of_messages} new messages in your inbox!")

        jobTimeNotification()

    print("\nMenu")
    print("[1] Log In")
    print("[2] Create an Account")
    print("[3] Search for a Job")
    print("[4] Find Someone You Know")
    print("[5] Learn a New Skill")
    print("[6] Not Sure About InCollege? Watch this Video!")
    print("[7] Useful Links")
    print("[8] InCollege Important Links")
    print("[9] Personal Profile")
    print("[10] Show My Network")
    print("[11] See Friend Requests")
    print("[12] Messages")
    print("[13] Training")
    print("[14] Exit the Program")

    option = int(input("Enter your option: "))

    if option == 1:
        login()
    elif option == 2:
        create(accountCount())
    elif option == 3:
        searchJob()
    elif option == 4:
        findSomeone()
    elif option == 5:
        learnSkill()
    elif option == 6:
        print("Video is now playing")
        menu()
    elif option == 7:
        usefulLinks()
    elif option == 8:
        ImportantLinks()
    elif option == 9:
        personalProfile()
    elif option == 10:
        seeListOfFriends()
    elif option == 11:
        seeFriendRequests()
    elif option == 12:
        messagesPage()
    elif option == 13:
        training()
    elif option == 14:
        return
    else:
        print("Invalid option.")
        menu()


# this function returns the number of accounts created in the system
def accountCount():
    file = open("Login.txt", "r")
    count = 0
    for line in file:
        if line != "\n":
            count += 1
    file.close()
    return count


# create an account and print a statement to let user it was done successfully
def create(accCount):
    global titleOpt
    global majorOpt
    global UniOpt
    global aboutOpt
    global expOpt1Title
    global expOpt1Emp
    global expOpt1Start
    global expOpt1End
    global expOpt1Des
    global expOpt2Title
    global expOpt2Emp
    global expOpt2Start
    global expOpt2End
    global expOpt2Des
    global expOpt3Title
    global expOpt3Emp
    global expOpt3Start
    global expOpt3End
    global expOpt3Des
    global eduOptSchool
    global eduOptDegree
    global eduOptYears
    global placeholder
    filesize = os.path.getsize("Login.txt")  # check if there are any accounts already made or not
    print("\nCreate A Account")

    # if there are less than 10 accounts proceed
    if accCount < 10:
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        username = input("Username: ")
        password = input("Password: ")

        # check if the password is valid, if not keep asking for account name and password
        while not passCheck(password):
            username = input("Please Input a UserName: ")
            password = input("Please Input a Password: ")

        # get membership selection
        membership = input("Input S for Standard or P for Plus Membership: ")
        membership = membership.upper()
        while membership != "S" and membership != "P":
            membership = input("Input S for Standard or P for Plus Membership: ")

        if passCheck(password):
            now = datetime.now()
            now = str(now)
            # if password is valid and file is empty, then add user info to the system
            if filesize == 0:
                file = open("Login.txt", "a")
                memberfile = open("NewMembers.txt", "a")
                friendsfile = open("list_of_friends.txt", "a")
                requestsfile = open("friend_requests.txt", "a")
                messages = open("messages.txt", "a")
                newjob = open("NewJobs.txt", "a")
                timejob = open("job_time.txt", "a")
                courseFile = open("Course.txt", "a")
                file.write(firstName)
                # separate user info in file with space
                file.write("\t")
                file.write(lastName)
                file.write("\t")
                file.write(username)
                friendsfile.write(username + "\n")
                requestsfile.write(username + "\n")
                file.write("\t")
                file.write(password)
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("English")
                file.write("\t")
                file.write(titleOpt)
                file.write("\t")
                file.write(majorOpt)
                file.write("\t")
                file.write(UniOpt)
                file.write("\t")
                file.write(aboutOpt)
                file.write("\t")
                file.write(expOpt1Title)
                file.write("\t")
                file.write(expOpt1Emp)
                file.write("\t")
                file.write(expOpt1Start)
                file.write("\t")
                file.write(expOpt1End)
                file.write("\t")
                file.write("\t")
                file.write(expOpt1Loc)
                file.write("\t")
                file.write(expOpt1Des)
                file.write("\t")
                file.write(expOpt2Title)
                file.write("\t")
                file.write(expOpt2Emp)
                file.write("\t")
                file.write(expOpt2Start)
                file.write("\t")
                file.write(expOpt2End)
                file.write("\t")
                file.write(expOpt2Loc)
                file.write("\t")
                file.write(expOpt2Des)
                file.write("\t")
                file.write(expOpt3Title)
                file.write("\t")
                file.write(expOpt3Emp)
                file.write("\t")
                file.write(expOpt3Start)
                file.write("\t")
                file.write(expOpt3End)
                file.write("\t")
                file.write(expOpt3Loc)
                file.write("\t")
                file.write(expOpt3Des)
                file.write("\t")
                file.write(eduOptSchool)
                file.write("\t")
                file.write(eduOptDegree)
                file.write("\t")
                file.write(eduOptYears)
                file.write("\t")
                file.write(placeholder)
                file.write("\n")
                memberfile.write(username + "\n")
                newjob.write(username + "\n")
                messages.write(username)
                messages.write("\t")
                messages.write(membership)
                messages.write("\n")
                memberfile.close()
                timejob.write(username)
                timejob.write("\t")
                timejob.write(now)
                timejob.write("\n")
                courseFile.write("How to use In College learning" + "\t" + "Placeholder" + "\n")
                courseFile.write("Train the trainer" + "\t" + "Placeholder" + "\n")
                courseFile.write("Gamification of learning" + "\t" + "Placeholder" + "\t" + "Placeholder" + "\n")
                courseFile.write("Understanding the Architectural Design Process" + "\t" + "Placeholder" + "\n")
                courseFile.write("Process Management Simplified" + "\t" + "Placeholder" + "\n")
                courseFile.close()
                timejob.close()
                file.close()
                newjob.close()
                friendsfile.close()
                requestsfile.close()
                messages.close()
                output_users_API()
                print("\nAccount Created.\nNow You Can Log-In!")
                menu()
                return
            else:
                # if file has existing accounts, check to make sure user name is not already taken
                for line in open("Login.txt", "r").readlines():
                    userCheck = line.split("\t")
                    if not line.strip():
                        pass
                    elif username == userCheck[2]:
                        print("Username Already Exists, Please Try Again.")
                        create(accCount)
                        return
                memberfileread = open("NewMembers.txt", "r")
                listOfLines = memberfileread.readlines()
                temp = accCount
                while temp != 0:
                    listOfLines[temp - 1] = listOfLines[temp - 1].rstrip() + "\t" + firstName + " " + lastName + "\n"
                    temp += -1
                memberfileread.close()
                memberfilewrite = open("NewMembers.txt", "w")
                memberfilewrite.writelines(listOfLines)
                memberfilewrite.close()
                file = open("Login.txt", "a")
                newjob = open("NewJobs.txt", "a")
                friendsfile = open("list_of_friends.txt", "a")
                requestsfile = open("friend_requests.txt", "a")
                memberfile = open("NewMembers.txt", "a")
                messages = open("messages.txt", "a")
                timejob = open("job_time.txt", "a")
                file.write(firstName)
                file.write("\t")
                file.write(lastName)
                file.write("\t")
                file.write(username)
                friendsfile.write(username + "\n")
                requestsfile.write(username + "\n")
                file.write("\t")
                file.write(password)
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("English")
                file.write("\t")
                file.write(titleOpt)
                file.write("\t")
                file.write(majorOpt)
                file.write("\t")
                file.write(UniOpt)
                file.write("\t")
                file.write(aboutOpt)
                file.write("\t")
                file.write(expOpt1Title)
                file.write("\t")
                file.write(expOpt1Emp)
                file.write("\t")
                file.write(expOpt1Start)
                file.write("\t")
                file.write(expOpt1End)
                file.write("\t")
                file.write(expOpt1Loc)
                file.write("\t")
                file.write(expOpt1Des)
                file.write("\t")
                file.write(expOpt2Title)
                file.write("\t")
                file.write(expOpt2Emp)
                file.write("\t")
                file.write(expOpt2Start)
                file.write("\t")
                file.write(expOpt2End)
                file.write("\t")
                file.write(expOpt2Loc)
                file.write("\t")
                file.write(expOpt2Des)
                file.write("\t")
                file.write(expOpt3Title)
                file.write("\t")
                file.write(expOpt3Emp)
                file.write("\t")
                file.write(expOpt3Start)
                file.write("\t")
                file.write(expOpt3End)
                file.write("\t")
                file.write(expOpt3Loc)
                file.write("\t")
                file.write(expOpt3Des)
                file.write("\t")
                file.write(eduOptSchool)
                file.write("\t")
                file.write(eduOptDegree)
                file.write("\t")
                file.write(eduOptYears)
                file.write("\t")
                file.write(placeholder)
                file.write("\n")
                newjob.write(username + "\n")
                messages.write(username)
                messages.write("\t")
                messages.write(membership)
                messages.write("\n")
                memberfile.write(username + "\n")
                timejob.write(username)
                timejob.write("\t")
                timejob.write(now)
                timejob.write("\n")
                timejob.close()
                memberfile.close()
                file.close()
                newjob.close()
                friendsfile.close()
                requestsfile.close()
                messages.close()
                output_users_API()
                print("\nAccount Created.\nNow You Can Log-In!")
                menu()
                return

    else:
        # if there are over 10 accounts return to menu
        print("\nAll permitted accounts have been created, please come back later.")
        menu()
        return


def passCheck(password):  # check if password is valid
    returnVal = True
    # all the non alpha characters
    Symbols = [' ', '~', '!', '@', '#', '$', '^', '&', '*', '(', ')', '_', '-', '+',
               '=', '{', '}', '[', ']', '|', ':', ';', '<', ',', '>', '.', '?', '/']
    if len(password) < 8:  # check if password has 8 or more characters
        print("The length of the password should be at least 8 characters.")
        returnVal = False
    if len(password) > 12:  # check if password is within 12 characters
        print("The length of the password should not be greater than 12 characters.")
        returnVal = False
    if not any(char.isdigit() for char in password):  # check if password has at least 1 digit
        print("The password should have at least one digit.")
        returnVal = False
    if not any(char.isupper() for char in password):  # check if password has at least 1 uppercase letter
        print("The password should have at least one uppercase letter.")
        returnVal = False
    if not any(char in Symbols for char in password):  # check if password has at least one non alpha character
        print("The password should have at least one non-alpha character.")
        returnVal = False
    return returnVal


def login():  # login function
    global signedIn
    global current_Name
    global firstName
    global lastName
    global password
    global userName
    global emailOpt
    global advOpt
    global smsOpt
    global languageOpt
    global titleOpt
    global majorOpt
    global UniOpt
    global aboutOpt
    global expOpt1Title
    global expOpt1Emp
    global expOpt1Start
    global expOpt1End
    global expOpt1Loc
    global expOpt1Des
    global expOpt2Title
    global expOpt2Emp
    global expOpt2Start
    global expOpt2End
    global expOpt2Loc
    global expOpt2Des
    global expOpt3Title
    global expOpt3Emp
    global expOpt3Start
    global expOpt3End
    global expOpt3Loc
    global expOpt3Des
    global eduOptSchool
    global eduOptDegree
    global eduOptYears
    global subscription
    global placeholder

    print("\nLog In")
    # ask for user and password
    username = input("Please Enter Your UserName: ")
    password = input("Please Enter Your Password: ")

    # read in login text file to see if account exists
    for line in open("Login.txt", "r").readlines():
        # line split into list of strings
        # the 3rd and 4th elements in list will be user name and password
        info = line.split("\t")
        if not line.strip():  # if its an empty line skip
            pass
        # if the user and password input matches any of the ones stored proceed to log-in
        elif username == info[2] and password == info[3]:
            print("\nYou Have Successfully Logged In\n")
            signedIn = True
            current_Name = info[0] + " " + info[1]
            firstName = info[0]
            lastName = info[1]
            userName = info[2]
            password = info[3]
            emailOpt = info[4]
            smsOpt = info[5]
            advOpt = info[6]
            languageOpt = info[7]
            titleOpt = info[8]
            majorOpt = info[9]
            UniOpt = info[10]
            aboutOpt = info[11]

            expOpt1Title = info[12]
            expOpt1Emp = info[13]
            expOpt1Start = info[14]
            expOpt1End = info[15]
            expOpt1Loc = info[16]
            expOpt1Des = info[17]

            expOpt2Title = info[18]
            expOpt2Emp = info[19]
            expOpt2Start = info[20]
            expOpt2End = info[21]
            expOpt2Loc = info[22]
            expOpt2Des = info[23]

            expOpt3Title = info[24]
            expOpt3Emp = info[25]
            expOpt3Start = info[26]
            expOpt3End = info[27]
            expOpt3Loc = info[28]
            expOpt3Des = info[29]

            eduOptSchool = info[30]
            eduOptDegree = info[31]
            eduOptYears = info[32]
            placeholder = info[33]
            profileNotification()
            newMemberNotification()
            deleteNewMembersViewed()
            getSubscription()
            menu()
            return

    # if no matches in the system, allow user to try again
    print("Incorrect UserName/Password, Please Try Again")
    signedIn = False
    # repeat the log-in
    login()
    return


# find someone you know function
def findSomeone():
    global signedIn
    print("\nFind Someone You Know")
    firstName = input("Enter Their First Name: ")
    lastName = input("Enter Their Last Name: ")

    # read file and check if any user names match the user input
    for line in open("Login.txt", "r").readlines():
        # each line has a unique users info
        # info is a line from text file, that is split up into a list of strings
        info = line.split("\t")
        if not line.strip():
            pass
        # if user input matches a name in the system proceed
        elif firstName == info[0] and lastName == info[1]:
            print("They are a part of the InCollege system!")
            # if person is not signed-in allow them to log-in, sign-up, or return to menu
            if not signedIn:
                print("[1] Log In")
                print("[2] Sign Up to Join Friend")
                print("[3] Return to Options")
                choice = int(input("Please Select an Option: "))
                while choice != 3:
                    if choice == 1:
                        login()
                        return
                    elif choice == 2:
                        count = accountCount()
                        create(count)
                        return
            menu()
            return

    # person was not found in system
    print("They are not yet a part of the InCollege system yet!")
    menu()
    return


# search for a job function
def searchJob():
    print("\nSearch for a Job")
    global signedIn

    # if a person is signed-in they can post a job in the system
    if signedIn:
        newJobNotification()
        deleteJobsViewed()
        number_deleted_jobs = countDeletedJobs()
        jobsAppliedNotification()
        if number_deleted_jobs == 1:
            print("You applied for 1 job but it has been deleted.\n")
        if number_deleted_jobs > 1:
            print(f"You applied for {number_deleted_jobs} jobs which have been deleted.")
        print("[1] Post a Job")
        print("[2] Search for a job")
        print("[3] Generate saved jobs")
        print("[4] Generate unsaved jobs")
        print("[5] Return to menu")
        choice = int(input("Enter Your Option: "))
        while choice != 5:
            if choice == 1:
                postJob()
                return
            if choice == 2:
                displayJobs()
                return
            if choice == 3:
                displaySavedJobs()
                return
            if choice == 4:
                displayUnsavedJobs()
                return
            else:
                print("Invalid Option")
                searchJob()
                return
        print("Returning to Menu")
        menu()
        return
    # if a person is not signed-in they can't really do anything
    else:
        print("[1] Return to Options")
        choice = int(input("Enter Your Option: "))
        while choice != 1:
            print("Invalid Option")
            searchJob()
            return

        print("Returning to Menu")
        menu()
        return


# post a job function for search for job page
def postJob():
    # count the number of job posts in the system
    file = open("Job_Posts.txt", "r")
    postCount = 0
    for line in file:
        if line != "\n":
            postCount += 1
    file.close()

    file = open("Job_Posts.txt", "a")
    print("\nPost a Job!")
    # if job posts in the system is not 5 or more proceed
    if postCount < 10:
        title = input("Enter a Title: ")
        description = input("Enter a Description: ")
        employer = input("Enter an Employer: ")
        location = input("Enter a Location: ")
        salary = input("Enter a Salary: ")

        # write user input to job posts text file
        # info will be separated on line with a tab
        file.write(title)
        file.write("\t")
        file.write(description)
        file.write("\t")
        file.write(employer)
        file.write("\t")
        file.write(location)
        file.write("\t")
        file.write(salary)
        file.write("\t")
        file.write(current_Name)
        file.write("\t")
        file.write(userName)
        file.write("\t")
        file.write("applicants,")
        file.write("\t")
        file.write("saved,")
        file.write("\t")
        file.write("Placeholder")
        file.write("\n")
        file.close()
        count = 0
        for line in open("NewJobs.txt", "r"):
            if userName in line:
                break
            else:
                count += 1

        file = open("NewJobs.txt", "r")
        listOfLines = file.readlines()
        i = 0
        while i < len(listOfLines):
            if i != count:
                listOfLines[i] = listOfLines[i].rstrip() + "\t" + title + "\n"
                i += 1
            else:
                i += 1
        file.close()
        file = open("NewJobs.txt", "w")
        file.writelines(listOfLines)
        file.close()

        output_jobs_api()
        print("Job Posted!")
        searchJob()
        return
    # there are already 10 jobs posted, so user can't do anything
    else:
        print("There are already 10 jobs posted!")
        searchJob()
        return


def seeListOfFriends():
    global signedIn
    global userName

    file = open("list_of_friends.txt", "rt")
    if signedIn:
        for line in file:
            user_friends = line.split(",")
            if userName == user_friends[0] or userName + "\n" == user_friends[0]:
                friends = user_friends[1:]

                print("\nThis is your list of friends!\n")
                for friend in friends:
                    print("- {}".format(friend))
                print("\n What do you want to do now?")
                print("   [1] Add a friend!")
                print("   [2] Disconnect with a friend")
                print("   [3] See profile of a friend")
                print("   [4] Go back to menu\n")
                flag = True
                while flag:
                    try:
                        choice = int(input("Enter Your Option: "))
                        if choice == 1:
                            # here goes Dylan's function
                            flag = False
                            searchForStudents()
                            menu()
                            return
                        if choice == 2:
                            dis_friend = input("Type the user you want to disconnect with: ")
                            if dis_friend in friends or dis_friend + "\n" in friends:
                                flag = False
                                disconnectSomeone(dis_friend)
                                seeListOfFriends()
                                return
                            else:
                                print("This contact is not part of your Network!")
                        if choice == 3:
                            pro_friend = input("Type the user you want to see the profile: ")
                            if pro_friend in friends or pro_friend + "\n" in friends:
                                flag = False
                                viewProfileOfFriend(pro_friend)
                                seeListOfFriends()
                                return
                            else:
                                print("This user is not in your network or does not exist!\n"
                                      "You can not see this profile.")
                        if choice == 4:
                            flag = False
                            menu()
                            return
                        if choice < 1 or choice > 4:
                            print("You can only write options 1 to 4")
                    except ValueError:
                        print("Your option should only be an integer!")
                else:
                    print("\nYou don't have friends yet!")
                break
    else:
        print("\nYou have not logged in! ")
    file.close()
    menu()
    return


def seeFriendRequests():
    global signedIn
    global userName

    file = open("friend_requests.txt", "r+")

    if signedIn:
        content = []
        for line in file:
            user_requests = line.split((","))
            if userName == user_requests[0] or userName + "\n" == user_requests[0]:
                requests = user_requests[1:]
                if len(requests) > 0:
                    print("\nThese are your friend requests!\n")
                    for request in requests:
                        sender_status = request.split(":")
                        if sender_status[1] == "s" or sender_status[1] == "s\n":
                            print(f"You have a friend request from {sender_status[0]}\n")
                            print("What do you want to do?\n")
                            print("[1] Accept")
                            print("[2] Reject")
                            print("[3] Ignore\n")
                            flag = True
                            while flag:
                                try:
                                    choice = int(input("Enter Your Option: "))
                                    if choice == 1:
                                        sender_status[1] = "a"
                                        result = sender_status[0] + ":" + sender_status[1]
                                        line = line.replace(request, result)
                                        line = line + "\n"
                                        flag = False
                                        acceptFriend(sender_status[0], userName)

                                    elif choice == 2:
                                        sender_status[1] = "r"
                                        result = sender_status[0] + ":" + sender_status[1]
                                        line = line.replace(request, result)
                                        line = line + "\n"
                                        flag = False
                                    elif choice == 3:
                                        flag = False
                                    if choice != 1 and choice != 2 and choice != 3:
                                        print("You can only write options 1, 2 or 3")
                                except ValueError:
                                    print("Your option should only be an integer!")
            content.append(line)
        file = open("friend_requests.txt", "w")
        file.writelines(content)
        file.close()
    else:
        print("\nYou have not logged in! ")
    menu()
    return


def acceptFriend(sender, recipient):
    file = open("list_of_friends.txt", "r+")
    content = []
    for line in file:
        user = line.split(",")
        if user[0] == sender or user[0] == sender + "\n":
            line = line[0:len(line) - 1] + "," + recipient
            line = line + "\n"
        if user[0] == recipient or user[0] == recipient + "\n":
            line = line[0:len(line) - 1] + "," + sender
            line = line + "\n"
        content.append(line)
    file = open("list_of_friends.txt", "w")
    file.writelines(content)
    file.close()
    result = f"{sender} is now your new friend!\n"
    print(result)


def countRequests():
    global userName
    file = open("friend_requests.txt", "r")
    count = 0
    for line in file:
        user_requests = line.split(",")
        if userName == user_requests[0] or userName + "\n" == user_requests[0]:
            requests = user_requests[1:]
            if len(requests) > 0:
                for request in requests:
                    sender_status = request.split(":")
                    if sender_status[1] == "s" or sender_status[1] == "s\n":
                        count += 1
    return count


def disconnectSomeone(friend):
    global userName
    file = open("list_of_friends.txt", "r+")
    content = []
    for line in file:
        user = line.split(",")
        if user[0] == userName or user[0] == userName + "\n":
            line = line.replace("," + friend, "")
        if user[0] == friend or user[0] == friend + "\n":
            line = line.replace("," + userName, "")
        content.append(line)
    file = open("list_of_friends.txt", "w")
    file.writelines(content)
    file.close()
    result = f"{friend} has been removed from your network!\n"
    print(result)


def createANewFriendRequest(matchesStack, choice):
    infoArray = matchesStack[choice - 1]
    requestToAdd = "," + userName + ":s" + '\n'
    i = 0
    lineNumber = 0
    tempLine = ""
    data = [""] * 1
    with open('friend_requests.txt', 'r') as file:
        for line in file:
            data.append(line)
            if line.startswith(infoArray[2]) or line == infoArray[2]:
                tempLine = line
                tempLine = tempLine.rstrip("\n")
                tempLine = tempLine + requestToAdd
                lineNumber = i
            i += 1
    data.remove('')
    file.close()

    data[lineNumber] = tempLine
    with open('friend_requests.txt', 'w') as file:
        file.writelines(data)

    print("requestSent!")


def makeFriendSelection(numberOfChoices):
    it_is = False
    while not it_is:
        try:
            userInput = int(
                input("\nEnter the number corresponding with the student you'd like to send a friend request to: "))
            it_is = True
        except ValueError:
            print("Your input should only be an integer!")
        if it_is:
            if (userInput < 1) or (userInput > numberOfChoices):
                it_is = False
                print("Please Enter a number that corresponds to a given choice")
    return userInput


def searchByLastName():
    global userName
    enteredName = input("\nEnter the Last Name you are searching for: ")
    matchesStack = []
    with open('Login.txt', 'r') as file:
        for line in file:  # Line Scope
            if line != "\n":
                wordStack = line.split()
                if wordStack[1] == enteredName and wordStack[2] != userName:  # you can't be friends with yourself
                    matchesStack.append(wordStack)

    length = len(matchesStack)
    if length == 0:
        print("There are no matches, returning...")
        searchForStudents()
        return
    print("The matches to your search are shown below: ")
    i = 0
    while i < length:
        temp = "[" + str((i + 1)) + "]" + " " + matchesStack[i][0] + " " + matchesStack[i][1] + " School: "
        innerLength = len(matchesStack[i])
        j = 0
        while j < innerLength:
            if matchesStack[i][j] == "School:":
                k = 1
                while matchesStack[i][j + k] != "Years:":
                    temp = temp + matchesStack[i][j + k] + " "
                    k += 1
            j += 1
        print(temp)
        print(" ")
        i += 1
    choice = -1
    if len(matchesStack) > 0:
        choice = makeFriendSelection(len(matchesStack))
    createANewFriendRequest(matchesStack, choice)


def searchByUniversity():
    global userName
    enteredUniversity = input("\nEnter the University you are searching for: ")
    matchesStack = []
    with open('Login.txt', 'r') as file:
        for line in file:  # Line Scope
            if line != "\n":
                tabStack = line.split("\t")
                if tabStack[30] == ("School: " + enteredUniversity) and tabStack[2] != userName:
                    matchesStack.append(tabStack)

    length = len(matchesStack)
    if length == 0:
        print("There are no matches, returning...")
        searchForStudents()
        return
    i = 0
    while i < length:
        print("[" + str(i + 1) + "]" + " " + matchesStack[i][0] + " " + matchesStack[i][1] + " " + matchesStack[i][
            30] + " " + matchesStack[i][31])
        i += 1
    choice = -1
    if len(matchesStack) > 0:
        choice = makeFriendSelection(len(matchesStack))
    createANewFriendRequest(matchesStack, choice)


def searchByMajor():
    global userName
    enteredMajor = input("\nEnter the Major you are searching for: ")
    matchesStack = []
    with open('Login.txt', 'r') as file:
        for line in file:  # Line Scope
            if line != "\n":
                tabStack = line.split("\t")
                if tabStack[31] == ("Degree: " + enteredMajor) and tabStack[2] != userName:
                    matchesStack.append(tabStack)

    length = len(matchesStack)
    if length == 0:
        print("There are no matches, returning...")
        searchForStudents()
        return
    i = 0
    while i < length:
        print("[" + str(i + 1) + "]" + " " + matchesStack[i][0] + " " + matchesStack[i][1] + " " + matchesStack[i][
            30] + " " + matchesStack[i][31])
        i += 1
    choice = -1

    if len(matchesStack) > 0:
        choice = makeFriendSelection(len(matchesStack))
    createANewFriendRequest(matchesStack, choice)


def searchForStudents():
    print("\nChoose whether to search for students in the database by the following:")
    print("[1] Last Name")
    print("[2] University")
    print("[3] Major")
    print("[4] Go Back to Menu")

    option = input("Enter your option: ")
    it_is = False
    try:
        int(option)
        it_is = True
    except ValueError:
        it_is = False
    if it_is:
        option = int(option)
        if option == 1:
            searchByLastName()
        elif option == 2:
            searchByUniversity()
        elif option == 3:
            searchByMajor()
        elif option == 4:
            menu()
            return
        else:
            print("Invalid option.")
            searchForStudents()
    else:
        print("Invalid option.")
        searchForStudents()


# learn a skill page
def learnSkill():
    print("\nLearn a New Skill")
    print("[1] Learn ...")
    print("[2] Learn ...")
    print("[3] Learn ...")
    print("[4] Learn ...")
    print("[5] Learn ...")
    print("[6] Return")
    learn = int(input("Choose What You Want to Learn: "))

    while learn != 6:
        if learn == 1:
            # when more functionality is needed, add the different skill functions to here for calling
            print("Under Construction.")
            return
        elif learn == 2:
            print("Under Construction.")
            return
        elif learn == 3:
            print("Under Construction.")
            return
        elif learn == 4:
            print("Under Construction.")
            return
        elif learn == 5:
            print("Under Construction.")
            return
        else:
            # if invalid choice ask for something else
            print("Invalid Option, Try Again!")
            learn = int(input("Choose What You Want to Learn: "))

    menu()  # return to option screen if 6 is chosen
    return


def usefulLinks():
    print("\nUseful Links")
    print("[1] General")
    print("[2] Browse InCollege")
    print("[3] Business Solutions")
    print("[4] Directories")
    print("[5] Return to previous")
    usefulOpt = int(input("Choose an option: "))
    while usefulOpt != 5:
        if usefulOpt == 1:
            general()
            return
        elif usefulOpt == 2:
            print("Under Construction")
            return
        elif usefulOpt == 3:
            print("Under Construction")
            return
        elif usefulOpt == 4:
            print("Under Construction")
            return
        else:
            print("Invalid Option, Try Again!")
            usefulOpt = int(input("Choose an option: "))
    print("Returning...")
    menu()
    return


def ImportantLinks():
    print("\nImportant Links")
    print("[1] Copyright Notice")
    print("[2] About")
    print("[3] Accessibility")
    print("[4] User Agreement")
    print("[5] Privacy Policy")
    print("[6] Cookie Policy")
    print("[7] Copyright Policy")
    print("[8] Brand Policy")
    print("[9] Languages")
    print("[10] Return to previous")
    imptOpt = int(input("Choose an option: "))
    while imptOpt != 10:
        if imptOpt == 1:
            copyRightNotice()
            return
        elif imptOpt == 2:
            about()
            return
        elif imptOpt == 3:
            accessibility()
            return
        elif imptOpt == 4:
            userAgreement()
            return
        elif imptOpt == 5:
            privacy()
            return
        elif imptOpt == 6:
            cookiePolicy()
            return
        elif imptOpt == 7:
            copyRightPolicy()
            return
        elif imptOpt == 8:
            brandPolicy()
            return
        elif imptOpt == 9:
            language()
            return
        else:
            print("Invalid Option, Try Again!")
            imptOpt = int(input("Choose an option: "))

    print("Returning...")
    menu()
    return


# about page for important links
def about():
    print("\nAbout InCollege\n\n"
          "InCollege is an online application that has been designed exclusively for college \n"
          "students. Searching for a first job can be challenging, but InCollege provides \n"
          "tools that are needed in order to be successful. This service allows students at \n"
          "various universities to network and exchange information about school, jobs, \n"
          "salaries, offers, and projects.\n")
    ImportantLinks()
    return


# accessibility page for important links
def accessibility():
    print("\nAccessibility\n\n"
          "InCollege is a place for college students to connect and find opportunities"
          " in the workforce. \n\nWe’re here to help you succeed with any goals, ideas, or "
          "ambitions that you want to carry out. "
          "\n\nWith a diverse collection of InCollege members, accessibility is a major key \n"
          "for establishing a great community. Our aim is to design products, services, \n"
          "and environments for people for people who experience disabilities. We wish \n"
          "to identify, remove, and prevent barriers that would make it difficult for students \n"
          "to interact with the InCollege application.\n")
    ImportantLinks()
    return


# copyright policy page for important links
def copyRightPolicy():
    print("\nCopyright Policy\n\n"
          "InCollege respects the intellectual property rights of others and expects its \n"
          "users to do the same. It is InCollege’s policy to remove or terminate any users \n"
          "who repeatedly infringe or charged with infringing the copyrights or other intellectual \n"
          "property rights of others. Information posted by members should be accurate, lawful, \n"
          "and not in violation of any U.S copyright laws. Any complaints regarding copyright \n"
          "infringement can be handled in copyright notice.\n")
    ImportantLinks()
    return


# cookie policy page for important links
def cookiePolicy():
    print("\nCookie Policy\n\n"
          "By using InCollege, you consent to the use of cookies.\n\n"
          "Cookies are small blocks of data sent from web browser by the website you are on. A \n"
          "cookie file allows the InCollege or a third-party to recognize you and make your next \n"
          "visit easier.\n\n"
          "Cookies are used to enable certain functions of InCollege, provide analytics, store \n"
          "preferences and enable advertisement delivery. Essential cookies authenticate users \n"
          "and prevent fraudulent use of user accounts. \n\n"
          "Third – party cookies are used to report usage statistics and deliver advertisement \n"
          "for InCollege.\n")
    ImportantLinks()
    return


# copyright notice page for important links
def copyRightNotice():
    print("\nCopyright Notice\n\n"
          "This application and its content is copyright of InCollege. Any redistribution or \n"
          "reproduction of part or all of the contents in any form is prohibited. You may not, \n"
          "distribute or commercially exploit the content. Nor may you transmit or store it in any \n"
          "other website or other form of electronic retrieval system.\n\n"
          "If you notice any of copyright infringement please notify us at copyright@InCollege.com\n")
    ImportantLinks()
    return


# brand policy page for important links
def brandPolicy():
    print("\nBrand Policy\n\n"
          "Any trademarks and brand features are protected by law. You’ll need InCollege’s \n"
          "consent in order to use them. \n\n"
          "InCollege does not permit its members, third party developers, partners and the media \n"
          "to use its name, trademarks, logos, web pages, screenshots and other brand features. \n")
    ImportantLinks()
    return


# user agreement page for important links
def userAgreement():
    print("\nUser Agreement \n\n"
          "Users are expected to follow all policies, provide accurate information, and use all "
          "services in a professional manner.")
    ImportantLinks()
    return


def privacy():
    print("\nPrivacy Policy\n\n"
          "Personal information is only processed with your consent, or on another legal basis. \n"
          "In addition, privacy settings can be changed by any signed-in user to meet specific needs.\n")
    global signedIn
    if signedIn:
        print("\nGuest Controls")
        print("[1] Toggle Email notifications")
        print("[2] Toggle SMS notifications")
        print("[3] Toggle Targeted Advertising features")
        print("[4] Return to previous")
        privacyOpt = int(input("Choose an option: "))
        while privacyOpt != 4:
            if privacyOpt == 1:
                email()
                return
            elif privacyOpt == 2:
                sms()
                return
            elif privacyOpt == 3:
                adv()
                return
            else:
                print("Invalid Option, Try Again!")
                privacyOpt = int(input("Choose an option: "))

        print("Returning...")
        ImportantLinks()
        return
    else:
        print("[1] Return to previous")
        privacyOpt = int(input("Choose an option: "))
        while privacyOpt != 1:
            print("Invalid Option, Try Again!")
            privacyOpt = int(input("Choose an option: "))
        print("Returning...")
        ImportantLinks()
        return


def email():
    global emailOpt
    count = 0
    if emailOpt == "On":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("Email notifications turned off.")
        emailOpt = "Off"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    else:
        print("Email notifications turned on.")
        emailOpt = "On"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    privacy()
    return


def sms():
    global smsOpt
    count = 0
    if smsOpt == "On":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("SMS notifications turned off.")
        smsOpt = "Off"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"

    else:
        print("SMS notifications turned on.")
        smsOpt = "On"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    privacy()
    return


def adv():
    global advOpt
    count = 0
    if advOpt == "On":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("Targeted Advertising notifications turned off.")
        advOpt = "Off"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    else:
        print("Targeted Advertising notifications turned on.")
        advOpt = "On"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    privacy()
    return


def language():
    global languageOpt
    print("\nLanguage")
    if signedIn:
        if languageOpt == "English":
            print("[1] Change language to Spanish.")
            print("[2] Return to previous")
        else:
            print("[1] Change language to English.")
            print("[2] Return to previous")
        languageChoice = int(input("Choose an option: "))
        while languageChoice != 2:
            if languageChoice == 1:
                switchLanguage()
                return
            else:
                print("Invalid option, Try Again!")
                languageChoice = int(input("Choose an option: "))
        print("Returning...")
        ImportantLinks()
        return
    else:
        print("[1] Return to previous")
        languageChoice = int(input("Choose an option: "))
        while languageChoice != 1:
            print("Invalid option, Try Again!")
            languageChoice = int(input("Choose an option: "))
        print("Returning...")
        ImportantLinks()
        return


def switchLanguage():
    global languageOpt
    count = 0
    if languageOpt == "English":
        temp = 1
    else:
        temp = 0
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if temp == 1:
        print("Switched the language to Spanish.")
        languageOpt = "Spanish"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    else:
        print("Switched the language to English.")
        languageOpt = "English"
        if count == 0:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + placeholder + "\n"
        else:
            listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                                 emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                                 + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                                 + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                                 + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                                 + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                                 + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                                 + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                                 + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    ImportantLinks()
    return


def general():
    print("\nGeneral")
    print("[1] Sign Up")
    print("[2] Help Center")
    print("[3] About")
    print("[4] Press")
    print("[5] Blogs")
    print("[6] Careers")
    print("[7] Developers")
    print("[8] Return to previous")
    generalOpt = int(input("Choose an option: "))
    while generalOpt != 8:
        if generalOpt == 1:
            create(accountCount())
            return
        elif generalOpt == 2:
            print("We're here to help.")
            return
        elif generalOpt == 3:
            print("In College: Welcome to In College, the world's largest college student network with many users")
            print("in many countries and territories worldwide.")
            return
        elif generalOpt == 4:
            print("In College Pressroom: Stay on top of the latest news, updates and reports.")
            return
        elif generalOpt == 5:
            print("Under Construction")
            return
        elif generalOpt == 6:
            print("Under Construction")
            return
        elif generalOpt == 7:
            print("Under Construction")
            return
        else:
            print("Invalid Option, Try Again!")
            generalOpt = int(input("Choose an option: "))
    usefulLinks()
    return


def personalProfile():
    global signedIn
    print("Profile")
    if signedIn:
        print("[1] Edit Profile")
        print("[2] View Profile")
        print("[3] Return to menu")
        profileOpt = int(input("Choose an option: "))
        while profileOpt != 3:
            if profileOpt == 1:
                editProfile()
                return
            elif profileOpt == 2:
                viewProfile()
                return
            else:
                print("Invalid option, Try Again!")
                profileOpt = int(input("Choose an option: "))
        print("Returning to menu...")
        menu()
        return
    else:
        print("[1] Return to menu")
        profileOpt = int(input("Choose an option: "))
        while profileOpt != 1:
            print("Invalid option, Try Again!")
        print("Returning to menu...")
        menu()
        return


def editProfile():
    print("[1] Title")
    print("[2] Major")
    print("[3] University Name")
    print("[4] About")
    print("[5] Work experience")
    print("[6] Education")
    print("[7] Return to previous")
    editOpt = int(input("Choose an option: "))
    while editOpt != 7:
        if editOpt == 1:
            profileTitle()
            return
        elif editOpt == 2:
            profileMajor()
            return
        elif editOpt == 3:
            profileUni()
            return
        elif editOpt == 4:
            profileAbout()
            return
        elif editOpt == 5:
            profileExp()
            return
        elif editOpt == 6:
            profileEdu()
            return
        else:
            print("Invalid option, Try Again!")
            editOpt = int(input("Choose an option: "))
    print("Returning...")
    personalProfile()
    return


def profileTitle():
    global titleOpt
    count = 0
    title = input("Enter a title: ")
    titleOpt = title
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if count == 0:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + placeholder + "\n"
    else:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    output_profiles_API()
    editProfile()
    return


def profileMajor():
    global majorOpt
    count = 0
    major = input("Enter a major: ")
    majorOpt = major.title()
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if count == 0:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + placeholder + "\n"
    else:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    output_profiles_API()
    editProfile()
    return


def profileUni():
    global UniOpt
    count = 0
    Uni = input("Enter a University: ")
    UniOpt = Uni.title()
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if count == 0:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + placeholder + "\n"
    else:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    output_profiles_API()
    editProfile()
    return


def profileAbout():
    global aboutOpt
    count = 0
    about = input("Enter an About: ")
    aboutOpt = about
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if count == 0:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + placeholder + "\n"
    else:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    output_profiles_API()
    editProfile()
    return


def profileExp():
    global variable
    print("Enter information about your past jobs, up to three past jobs")
    print("[1] Job 1")
    print("[2] Job 2")
    print("[3] Job 3")
    print("[4] Return to previous")
    profileExpOpt = int(input("Choose an option: "))
    while profileExpOpt != 4:
        if profileExpOpt == 1:
            variable = 1
            jobExp(variable)
            output_profiles_API()
            return
        elif profileExpOpt == 2:
            variable = 2
            jobExp(variable)
            output_profiles_API()
            return
        elif profileExpOpt == 3:
            variable = 3
            jobExp(variable)
            output_profiles_API()
            return
        else:
            print("Invalid option, Try Again!")
            profileExpOpt = int(input("Choose an option: "))
    print("Returning...")
    editProfile()
    return


def profileEdu():
    global eduOptSchool
    global eduOptDegree
    global eduOptYears
    count = 0
    print("Enter information about your education here")
    school = input("Enter school name: ")
    degree = input("Enter your degree: ")
    years = (input("Enter how many years attended: "))
    eduOptSchool = "School: " + school
    eduOptDegree = "Degree: " + degree
    eduOptYears = "Years: " + years
    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if count == 0:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + placeholder + "\n"
    else:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    output_profiles_API()
    editProfile()
    return


def jobExp(x):
    global expOpt1Title
    global expOpt1Emp
    global expOpt1Start
    global expOpt1End
    global expOpt1Loc
    global expOpt1Des
    global expOpt2Title
    global expOpt2Emp
    global expOpt2Start
    global expOpt2End
    global expOpt2Loc
    global expOpt2Des
    global expOpt3Title
    global expOpt3Emp
    global expOpt3Start
    global expOpt3End
    global expOpt3Loc
    global expOpt3Des
    count = 0
    print("Enter information about your past jobs here")
    jobTitle = input("Enter the job title: ")
    jobEmployer = input("Enter the employer of the job: ")
    jobStart = input("Enter the start date of the job: ")
    jobEnd = input("Enter the end date of the job: ")
    jobLocation = input("Enter the location of the job: ")
    jobDes = input("Enter a description of the job: ")

    if x == 1:
        expOpt1Title = "Title: " + jobTitle
        expOpt1Emp = "Employer: " + jobEmployer
        expOpt1Start = "Start Date: " + jobStart
        expOpt1End = "End Date: " + jobEnd
        expOpt1Loc = "Job Location: " + jobLocation
        expOpt1Des = "Description: " + jobDes
    elif x == 2:
        expOpt2Title = "Title: " + jobTitle
        expOpt2Emp = "Employer: " + jobEmployer
        expOpt2Start = "Start Date: " + jobStart
        expOpt2End = "End Date: " + jobEnd
        expOpt2Loc = "Job Location: " + jobLocation
        expOpt2Des = "Description: " + jobDes
    elif x == 3:
        expOpt3Title = "Title: " + jobTitle
        expOpt3Emp = "Employer: " + jobEmployer
        expOpt3Start = "Start Date: " + jobStart
        expOpt3End = "End Date: " + jobEnd
        expOpt3Loc = "Job Location: " + jobLocation
        expOpt3Des = "Description: " + jobDes

    for line in open("Login.txt", "r"):
        info = line.split("\t")
        if userName != info[2]:
            count = count + 1
            pass
        else:
            break
    file = open("Login.txt", "r")
    listOfLines = file.readlines()
    if count == 0:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + placeholder + "\n"
    else:
        listOfLines[count] = firstName + "\t" + lastName + "\t" + userName + "\t" + password + "\t" + \
                             emailOpt + "\t" + smsOpt + "\t" + advOpt + "\t" + languageOpt + "\t" \
                             + titleOpt + "\t" + majorOpt + "\t" + UniOpt + "\t" + aboutOpt + "\t" \
                             + expOpt1Title + "\t" + expOpt1Emp + "\t" + expOpt1Start + "\t" + expOpt1End \
                             + "\t" + expOpt1Loc + "\t" + expOpt1Des + "\t" + expOpt2Title + "\t" + expOpt2Emp \
                             + "\t" + expOpt2Start + "\t" + expOpt2End + "\t" + expOpt2Loc + "\t" + expOpt2Des \
                             + "\t" + expOpt3Title + "\t" + expOpt3Emp + "\t" + expOpt3Start + "\t" + expOpt3End \
                             + "\t" + expOpt3Loc + "\t" + expOpt3Des + "\t" + eduOptSchool + "\t" + eduOptDegree \
                             + "\t" + eduOptYears + "\t" + " " + "\n"
    file = open("Login.txt", "w")
    file.writelines(listOfLines)
    file.close()
    output_profiles_API()
    profileExp()
    return


def viewProfile():
    global variable
    global current_Name
    print("\n" + current_Name)
    print("Title: " + titleOpt)
    result = majorOpt.title()
    print("Major: " + result)
    result = UniOpt.title()
    print("University: " + result)
    print("About: " + aboutOpt)
    print("\nJob Experience1")
    print(expOpt1Title)
    print(expOpt1Emp)
    print(expOpt1Start)
    print(expOpt1End)
    print(expOpt1Loc)
    print(expOpt1Des)
    print("\nJob Experience2")
    print(expOpt2Title)
    print(expOpt2Emp)
    print(expOpt2Start)
    print(expOpt2End)
    print(expOpt2Loc)
    print(expOpt2Des)
    print("\nJob Experience3")
    print(expOpt3Title)
    print(expOpt3Emp)
    print(expOpt3Start)
    print(expOpt3End)
    print(expOpt3Loc)
    print(expOpt3Des)
    print("\nEducation")
    print(eduOptSchool)
    print(eduOptDegree)
    print(eduOptYears + "\n")
    personalProfile()
    return


def viewProfileOfFriend(friend):
    file = open("Login.txt", "r")
    for line in file:
        user_info = line.split("\t")
        if user_info[2] == friend:
            title = user_info[8]
            major = user_info[9]
            uni = user_info[10]
            about_user = user_info[11]
            if title != "None" or major != "None" or uni != "None" or about_user != "None":
                print(f"\n {user_info[0]} {user_info[1]}")
                print("Title: " + title)
                print("Major: " + major)
                print("University: " + uni)
                print("About: " + about_user)
                print("\nJob Experience1")
                print(user_info[12])
                print(user_info[13])
                print(user_info[14])
                print(user_info[15])
                print(user_info[16])
                print(user_info[17])
                print("\nJob Experience2")
                print(user_info[18])
                print(user_info[19])
                print(user_info[20])
                print(user_info[21])
                print(user_info[22])
                print(user_info[23])
                print("\nJob Experience3")
                print(user_info[24])
                print(user_info[25])
                print(user_info[26])
                print(user_info[27])
                print(user_info[28])
                print(user_info[29])
                print("\nEducation")
                print(user_info[30])
                print(user_info[31])
                print(user_info[32] + "\n")
            else:
                print(f"You can not see this profile because {friend} has not created a profile yet!")


def displaySavedJobs():
    file = open("Job_Posts.txt", "r")
    for line in file:
        info = line.split("\t")
        if userName in info[8]:
            print("Title: " + info[0])
            print("Job Description: " + info[1])
            print("Employer: " + info[2])
            print("Location: " + info[3])
            print("Salary: " + info[4])
            print("Posted By: " + info[5])
            print('\n')
    option = input("Type anything to Return To Menu: ")
    menu()


def displayUnsavedJobs():
    file = open("Job_Posts.txt", "r")
    for line in file:
        info = line.split("\t")
        if userName not in info[8]:
            print("Title: " + info[0])
            print("Job Description: " + info[1])
            print("Employer: " + info[2])
            print("Location: " + info[3])
            print("Salary: " + info[4])
            print("Posted By: " + info[5])
            print('\n')
    option = input("Type anything to Return To Menu: ")
    menu()


def saveAJob(choice):
    info = []
    i = 1
    tempstring = ""
    for line in open("Job_Posts.txt", "r"):
        if i == choice:
            info = line.split("\t")
        i += 1
    applicants = info[8]
    if userName in applicants:
        print("The job has been unsaved.")
        temp = applicants.split(",")
        x = 0
        while x < (len(temp) - 1):
            if temp[x] == userName:
                x += 1
            else:
                tempstring = tempstring + temp[x] + ","
                x += 1
        file = open("Job_Posts.txt", "r")
        listOfLines = file.readlines()
        file.close()
        listOfLines[choice - 1] = info[0] + '\t' + info[1] + '\t' + info[2] + '\t' + info[3] + '\t' + info[4] \
                                  + '\t' + info[5] + '\t' + info[6] + '\t' + info[7] + '\t' + tempstring + "\t" + \
                                  info[9]
        file = open("Job_Posts.txt", "w")
        file.writelines(listOfLines)
        file.close()
        menu()
        return
    else:
        print("The job has been saved.")
        applicants = applicants + userName + ","
        print(applicants)
        listOfLines = []
        file = open("Job_Posts.txt", "r")
        listOfLines = file.readlines()
        file.close()
        listOfLines[choice - 1] = info[0] + '\t' + info[1] + '\t' + info[2] + '\t' + info[3] + '\t' + info[4] \
                                  + '\t' + info[5] + '\t' + info[6] + '\t' + info[7] + '\t' + applicants + "\t" + \
                                  info[9]
        file = open("Job_Posts.txt", "w")
        file.writelines(listOfLines)
        file.close()
        output_savedJobs_API()
        menu()
        return


def applyForAJob(choice):
    global userName
    info = []
    i = 1
    for line in open("Job_Posts.txt", "r"):
        if i == choice:
            info = line.split("\t")
        i += 1

    jobName = info[0] + " " + info[1] + " " + info[2] + " " + info[3] + " " + info[4]
    applicants = info[7]
    if userName in applicants:
        print("You've already applied for this job!")
        menu()
        return
    else:
        applicants = applicants + userName + ","
        listOfLines = []
        file = open("Job_Posts.txt", "r")
        listOfLines = file.readlines()
        file.close()
        listOfLines[choice - 1] = info[0] + '\t' + info[1] + '\t' + info[2] + '\t' + info[3] + '\t' + info[4] \
                                  + '\t' + info[5] + '\t' + info[6] + '\t' + applicants + "\t" + info[8] + "\t" \
                                  + info[9]
        file = open("Job_Posts.txt", "w")
        file.writelines(listOfLines)
        file.close()
        graduationDate = input("Please enter a graduation date: ")
        startDate = input("Please enter the date you can start working: ")
        paragraph = input("Please submit a paragraph stating why you would be good for this job: ")

        now = datetime.now()
        now = str(now)
        count = 0
        for line in open("job_time.txt", "r"):
            info = line.split("\t")
            if userName == info[0].rstrip():
                break
            else:
                count += 1

        timeFile = open("job_time.txt", "r")
        listOfLines = timeFile.readlines()
        listOfLines[count] = userName + "\t" + now + "\n"
        timeFile.close()

        timeFile = open("job_time.txt", "w")
        timeFile.writelines(listOfLines)
        timeFile.close()

        test = open("applicants.txt", "a")
        test.write(userName)
        test.write("\t")
        test.write(jobName)
        test.write("\t")
        test.write(paragraph)
        test.write("\n")
        test.close()
        output_appliedJobs_API()
        menu()
        return


def displayJobDetails(choice):
    i = 1
    info = []
    for line in open("Job_Posts.txt", "r"):
        if i == choice:
            info = line.split("\t")
            break
        i += 1

    print("Title: " + info[0])
    print("Job Description: " + info[1])
    print("Employer: " + info[2])
    print("Location: " + info[3])
    print("Salary: " + info[4])
    print("Posted By: " + info[5])
    if userName == info[6]:  # case in which user selected a job that they posted
        print("[1] Delete This Job Post")
        print("[2] Return to Menu")
        it_is = False
        choiceToDelete = ""
        while not it_is:
            choiceToDelete = input("Enter your selection: ")
            try:
                int(choiceToDelete)
                it_is = True
            except ValueError:
                print("Invalid entry, please enter a number")
            if it_is:
                choiceToDelete = int(choiceToDelete)
                if (choiceToDelete < 0) or (choiceToDelete > 2):
                    print("invalid entry: please enter a choice within range")
                    it_is = False
        if choiceToDelete == 1:
            deleteJob(choice)
            return
        else:
            menu()
            return
    else:  # case in which user selected a job that they HAVE NOT posted
        print("[1] Apply For This Job")
        print("[2] Save/Unsave this Job")
        print("[3] Return to Menu")
        it_is = False
        choiceToApply = ""
        while not it_is:
            choiceToApply = input("Enter your selection: ")
            try:
                int(choiceToApply)
                it_is = True
            except ValueError:
                print("Invalid entry, please enter a number")
            if it_is:
                choiceToApply = int(choiceToApply)
                if (choiceToApply < 0) or (choiceToApply > 3):
                    print("invalid entry: please enter a choice within range")
                    it_is = False
        if choiceToApply == 1:
            applyForAJob(choice)
            return
        elif choiceToApply == 2:
            saveAJob(choice)
            return
        else:
            menu()
            return


def selectJob(numOfChoices):
    it_is = False
    choice = ""
    choice = input("Enter your selection: ")
    try:
        int(choice)
        it_is = True
    except ValueError:
        print("Invalid entry, please enter a number")
    if it_is:
        choice = int(choice)
        if (choice >= 1) and (choice <= numOfChoices):
            displayJobDetails(choice)
        else:
            print("Invalid entry, please enter a number within range")
            selectJob(numOfChoices)

    else:
        selectJob(numOfChoices)


def displayJobs():
    jobTitles = []
    for line in open("Job_Posts.txt", "r"):
        info = line.split("\t")
        if userName in info[7]:
            info[0] = info[0] + " - Applied For"
        jobTitles.append(info[0])
    j = 1
    for i in jobTitles:
        print("[" + str(j) + "]" + " " + i)
        j += 1
    j -= 1
    if len(jobTitles) == 0:
        print("No Jobs have been posted")
        menu()
        return
    selectJob(j)


def deleteJob(choice):
    f = open("Job_Posts.txt", "r")
    lines = f.readlines()
    f.close()
    app = lines[choice - 1].split("\t")
    dele = app[7].split(",")
    i = 1
    fileDel = open("job_deletions.txt", "a")
    while i < (len(dele) - 1):
        fileDel.write(dele[i] + "\n")
        i += 1
    fileDel.close()
    with open("Job_Posts.txt", "w") as f:
        for line in lines:
            if line != lines[choice - 1]:
                f.write(line)
        f.close()
    output_jobs_api()
    menu()
    return


def countDeletedJobs():
    global userName
    count = 0
    filesize = os.path.getsize("job_deletions.txt")
    if filesize == 0:
        return count
    else:
        file = open("job_deletions.txt", "r")
        for line in file:
            jobs = line.split("\n")
            if userName == jobs[0] or userName + "\n" == jobs[0]:
                count += 1
        file.close()
        file = open("job_deletions.txt", "r")
        lines = file.readlines()
        file.close()

        new_file = open("job_deletions.txt", "w")
        for line in lines:
            if line.strip("\n") != userName:
                new_file.write(line)
        file.close()
        return count


def getSubscription():
    global subscription
    file = open("messages.txt", "r")
    for line in file:
        temp = line.split("\t")
        if userName == temp[0]:
            subscription = temp[1].rstrip()


def messagesPage():
    global signedIn

    if not signedIn:
        menu()
        return

    print("\nMessages Page")
    print("[1] Send A Message")
    print("[2] View Messages")
    print("[3] Return To Menu")

    choice = int(input("Enter Option: "))
    if choice == 1:
        sendMessage()
        messagesPage()
        return
    elif choice == 2:
        viewMessages()
        messagesPage()
        return
    elif choice == 3:
        menu()
        return
    else:
        print("Choice does not exist!")
        messagesPage()
        return



def sendMessage():
    print(subscription)
    print("\nSend A Message!")
    if subscription == "S":
        # show list of friends
        file = open("list_of_friends.txt", "rt")
        friends = ""

        for line in file:
            friends = line.split(",")
            if userName == friends[0] or userName + "\n" == friends[0]:
                friends = friends[1:]
                break
        file.close()

        if len(friends) == 0:
            print("You don't have any friends to a send a message to!")
            return

        if friends != "":
            option = 1
            print("\nThis is your list of friends!\n")
            for friend in friends:
                print("{0}. {1}".format(option, friend))
                option += 1

            selection = int(input("\nEnter number corresponding with the student you'd like to send a message to: "))
            while selection < 0 or selection > len(friends):
                print("I'm sorry you are not friends with that person.")
                selection = int(input("\nEnter number corresponding with the student you'd like to send a message to: "))

            selection = selection - 1
            person = friends[selection].rstrip()

            message = input("Enter Message: ")
            count = 0
            for line in open("messages.txt", "r"):
                info = line.split("\t")
                if person == info[0]:
                    break
                else:
                    count += 1

            messageFile = open("messages.txt", "r")
            listOfLines = messageFile.readlines()
            listOfLines[count] = listOfLines[count].rstrip() + "\t" + userName + "\t" \
                                 + message + "\t" + "New" + "\n"

            messageFile.close()

            messageFile = open("messages.txt", "w")
            messageFile.writelines(listOfLines)
            messageFile.close()
            return
    else:
        file = open("list_of_friends.txt", "rt")
        friends = ""

        for line in file:
            friends = line.split(",")
            if userName == friends[0] or userName + "\n" == friends[0]:
                friends = friends[1:]
                break
        file.close()

        if len(friends) != 0:
            friends = [line.strip() for line in friends]
            print(friends)

        listOfPeople = []
        file = open("messages.txt", "r")
        for line in file:
            if line != "\n":
                info = line.split("\t")
                if info[0] != userName:
                    listOfPeople.append(info[0].rstrip())

        if len(listOfPeople) == 0:
            print("\nThere are no users in the system!")
            return

        if len(listOfPeople) != 0:
            option = 1
            print("\nThis is a list of InCollege students!\n")
            for people in listOfPeople:
                if people in friends:
                    print("{0}. {1} (friend)".format(option, people))
                else:
                    print("{0}. {1}".format(option, people))
                option += 1

            selection = int(input("\nEnter number corresponding with the student you'd like to send a message to: "))
            selection = selection - 1
            person = listOfPeople[selection].rstrip()

            message = input("Enter Message: ")
            count = 0
            for line in open("messages.txt", "r"):
                info = line.split("\t")
                if person == info[0]:
                    break
                else:
                    count += 1

            messageFile = open("messages.txt", "r")
            listOfLines = messageFile.readlines()
            listOfLines[count] = listOfLines[count].rstrip() + "\t" + userName + "\t" \
                                 + message + "\t" + "New" + "\n"

            messageFile.close()

            messageFile = open("messages.txt", "w")
            messageFile.writelines(listOfLines)
            messageFile.close()

            return


def viewMessages():
    messagesFile = open("messages.txt", "r")
    messages = ""
    userAndStatus = ""
    for line in messagesFile:
        messages = line.rstrip()
        messages = messages.split("\t")
        if userName == messages[0]:
            userAndStatus = messages[:2]
            messages = messages[2:]
            break
    messagesFile.close()

    if len(messages) == 0:
        print("You have no messages!")
        return

    if messages != "":
        print("\nHere are all your messages.")
        print("Messages with a * are New.")
        option = 0
        for i in range(len(messages)):
            if (i % 3) == 0:
                option += 1
                if messages[i+2] == "New":
                    print("{0}. {1}*".format(option, messages[i]))
                else:
                    print("{0}. {1}".format(option, messages[i]))

        choice = int(input("Enter number option: "))

        option = 1
        pos = 0
        sender = ""
        for i in range(len(messages)):
            if (i % 3) == 0 and option == choice:
                pos = i
                sender = messages[i]
                messages[i+2] = "Old"
                print("\nFrom: {0}\n{1}".format(messages[i], messages[i + 1]))
                break
            elif (i % 3) == 0:
                option += 1
            else:
                pass

        count = 0
        for line in open("messages.txt", "r"):
            info = line.split("\t")
            if userAndStatus == info[:2]:
                break
            else:
                count += 1

        messageFile = open("messages.txt", "r")
        listOfLines = messageFile.readlines()
        listOfLines[count] = "\t".join(userAndStatus) + "\t" + "\t".join(messages) + "\n"
        messageFile.close()

        messageFile = open("messages.txt", "w")
        messageFile.writelines(listOfLines)
        messageFile.close()

        print("\n[1] Return To Messages Page")
        print("[2] Delete Message")
        print("[3] Reply to Message")

        choice = int(input("Enter Option: "))

        while choice < 1 or choice > 3:
            print("Not A Valid Option")
            print("\n[1] Return To Messages Page")
            print("[2] Delete Message")
            print("[3] Reply to Message")

            choice = int(input("Enter Option: "))

        if choice == 1:
            return
        elif choice == 2:
            messages = deleteMessage(messages, pos)
        elif choice == 3:
            replyToMessage(sender)

        count = 0
        for line in open("messages.txt", "r"):
            info = line.split("\t")
            if userAndStatus == info[:2]:
                break
            else:
                count += 1

        messageFile = open("messages.txt", "r")
        listOfLines = messageFile.readlines()
        listOfLines[count] = "\t".join(userAndStatus) + "\t" + "\t".join(messages) + "\n"
        messageFile.close()

        messageFile = open("messages.txt", "w")
        messageFile.writelines(listOfLines)
        messageFile.close()

        return


def deleteMessage(messages, pos):
    messages.pop(pos)
    messages.pop(pos)
    messages.pop(pos)
    return messages


def replyToMessage(name):
    person = name
    message = input("\nEnter Reply Message: ")
    count = 0
    for line in open("messages.txt", "r"):
        info = line.split("\t")
        if person == info[0]:
            break
        else:
            count += 1

    messageFile = open("messages.txt", "r")
    listOfLines = messageFile.readlines()
    listOfLines[count] = listOfLines[count].rstrip() + "\t" + userName + "\t" \
                         + message + "\t" + "New" + "\n"

    messageFile.close()

    messageFile = open("messages.txt", "w")
    messageFile.writelines(listOfLines)
    messageFile.close()

    return


def countMessages(name):
    file = open("messages.txt", "r")
    count = 0
    for line in file:
        info = line.rstrip("\n")
        info = info.split("\t")
        if name == info[0]:
            for element in info:
                if element == "New":
                    count += 1

    file.close()

    return count


def profileNotification():
    file = open("Login.txt", "r")
    for line in file:
        info = line.split("\t")
        if info[2] == userName:
            if info[8] == "None" and info[9] == "None" and info[10] == "None" and info[11] == "None":
                print("Don't forget to create a profile.")
    file.close()
    return


def newJobNotification():
    i = 0
    x = 1
    file = open("NewJobs.txt", "r")
    for line in file:
        info = line.split("\t")
        if info[0] == userName and len(info) > 1:
            while x < len(info):
                print("New posted job titled: " + info[x])
                x += 1
    file.close()
    return


def deleteJobsViewed():
    count = 0
    for line in open("NewJobs.txt", "r"):
        if userName in line:
            break
        else:
            count += 1
    file = open("NewJobs.txt", "r")
    listOfLines = file.readlines()
    listOfLines[count] = userName + "\n"
    file.close()
    file = open("NewJobs.txt", "w")
    file.writelines(listOfLines)
    file.close()
    return


def newMemberNotification():
    i = 0
    x = 1
    file = open("NewMembers.txt", "r")
    for line in file:
        info = line.split("\t")
        if info[0] == userName and len(info) > 1:
            while x < len(info):
                print("New member joined: " + info[x])
                x += 1
    file.close()
    return


def deleteNewMembersViewed():
    count = 0
    for line in open("NewMembers.txt", "r"):
        info = line.split("\t")
        if userName == info[0]:
            break
        else:
            count += 1
    if len(info) > 1:
        file = open("NewMembers.txt", "r")
        listOfLines = file.readlines()
        listOfLines[count] = userName + "\n"
        file.close()
        file = open("NewMembers.txt", "w")
        file.writelines(listOfLines)
        file.close()
        return
    else:
        return


def jobsAppliedNotification():
    count = 0
    file = open("Job_Posts.txt", "r")
    for line in file:
        info = line.split("\t")
        if userName in info[7]:
            count += 1
    print("Number of applied jobs: " + str(count))
    file.close()
    return


def jobTimeNotification():
    global userName
    file = open("job_time.txt", "r")
    for line in file:
        info = line.split("\t")
        if userName == info[0]:
            dateandtime = info[1].split(" ")
            date = dateandtime[0].split("-")
            time = dateandtime[1].split(":")

            now = datetime.now()
            now = str(now)
            now = now.split(" ")
            nowdate = now[0].split("-")
            nowtime = now[1].split(":")

            temp1 = time[2].rstrip()
            temp1 = float(temp1)
            temp2 = float(nowtime[2])

            day1 = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]),
                            int(time[1]), int(temp2))

            day2 = datetime(int(nowdate[0]), int(nowdate[1]), int(nowdate[2]), int(nowtime[0]),
                            int(nowtime[1]), int(temp1))

            delta = day2 - day1
            totaldays = int(delta.days)
            if totaldays >= 7:
                print("Remember – you're going to want to have a job when you graduate. "
                      "\nMake sure that you start to apply for jobs today!")

            break
    file.close()
    return


def training():
    print("[1] Training and Education")
    print("[2] IT Help Desk")
    print("[3] Business Analysis and Strategy")
    print("[4] Security")
    print("[5] Return to menu")
    choice = int(input("Enter Option: "))
    while choice != 5:
        if choice == 1:
            trainAndEdu()
            return
        elif choice == 2:
            print("Coming Soon!")
            training()
            return
        elif choice == 3:
            BusinessAnalysisAndStrategy()
            return
        elif choice == 4:
            print("Coming Soon!")
            training()
            return
        else:
            print("Invalid Option!")
            choice = int(input("Enter Option: "))
    menu()
    return


def trainAndEdu():
    print("[1] Python Programming")
    print("[2] Database Usages")
    print("[3] The Agile Process")
    print("[4] Software Engineering")
    print("[5] Return")
    choice = int(input("Enter Option: "))
    while choice != 5:
        if choice == 1:
            print("Under Construction")
            trainAndEdu()
            return
        elif choice == 2:
            print("Under Construction")
            trainAndEdu()
            return
        elif choice == 3:
            print("Under Construction")
            trainAndEdu()
            return
        elif choice == 4:
            print("Under Construction")
            trainAndEdu()
            return
        else:
            print("Invalid Option!")
            choice = int(input("Enter Option: "))
    training()
    return


def BusinessAnalysisAndStrategy():
    if signedIn:
        print("[1] In College Learning")
        print("[2] Return")
        choice = int(input("Enter Option: "))
        while choice != 2:
            if choice == 1:
                InCollegeLearn()
                return
            else:
                print("Invalid Option!")
                choice = int(input("Enter Option: "))
        training()
        return
    else:
        print("[1] How to use In College learning")
        print("[2] Train the trainer")
        print("[3] Gamification of learning")
        print("[4] Not seeing what you're looking for? Sign in to see all 7609 results.")
        print("[5] Return")
        choice = int(input("Enter Option: "))
        while choice != 5:
            if choice == 1:
                login()
                return
            elif choice == 2:
                login()
                return
            elif choice == 3:
                login()
                return
            elif choice == 4:
                login()
                return
            else:
                print("Invalid Option!")
                choice = int(input("Enter Option: "))
        training()
        return


def InCollegeLearn():
    file = open("Course.txt", "r")
    listOfLines = file.readlines()
    arrayOfCourseTitles = []
    for line in listOfLines:
        temp = line.split('\t')
        arrayOfCourseTitles.append(temp[0])
    file.close()
    file = open("Course.txt", "r")
    count = 1
    taken = "-already taken"
    for line in file:
        info = line.split("\t")
        string = info[0]
        if userName in line:
            print("[{0}] {1} {2}".format(str(count), string, taken))
            count += 1
        else:
            print("[{0}] {1}".format(str(count), string))
            count += 1
    print("[" + str(count) + "] Return")
    file.close()
    choice = int(input("Enter Option: "))
    while choice != count:  # change to number of training courses plus 1
        if (choice > 0) and (choice < count):
            string = arrayOfCourseTitles[choice - 1]
            print(string)
            learn(string)
            return
        else:
            print("Invalid Option!")
            choice = int(input("Enter Option: "))
    BusinessAnalysisAndStrategy()
    return


def learn(string):
    temp = 0
    file = open("Course.txt", "r")
    for line in file:
        info = line.split("\t")
        if string == info[0]:
            if userName in line:
                print("You have already taken this course, do you want to take it again?")
                print("[1] Yes, take the course again")
                print("[2] No, don't take the course again")
                choice = int(input("Enter Option: "))
                while choice < 0 and choice > 2:
                    print("Invalid Option!")
                    choice = int(input("Enter Option: "))
                if choice == 1:
                    print("You have now completed this training")
                    InCollegeLearn()
                    return
                elif choice == 2:
                    print("Course Cancelled")
                    InCollegeLearn()
                    return
            else:
                break
        else:
            temp += 1
    file.close()
    file = open("Course.txt", "r")
    listOfLines = file.readlines()
    listOfLines[temp] = listOfLines[temp].rstrip() + "\t" + userName + "\n"
    file.close()
    file = open("Course.txt", "w")
    file.writelines(listOfLines)
    file.close()
    print("You have now completed this training")
    output_training_API()
    InCollegeLearn()
    return


def is_file_empty(file_path):
    if not os.path.exists(file_path):
        return True

    if os.stat(file_path).st_size == 0:
        return True

    return False


def output_profiles_API():
    e = is_file_empty("Login.txt")
    if e == True:
        return

    file = open("Login.txt", "r")
    file2 = open("MyCollege_profiles.txt", "w")
    for line in file:
            info = line.strip()
            info = info.split("\t")
            file2.write(info[2])
            file2.write("\n")
            temp = info[8:]

            while "" in temp:
                temp.remove("")

            for i in range(len(temp)):
                file2.write(temp[i])
                file2.write("\n")
            file2.write("====")
            file2.write("\n")

    file.close()
    file2.close()


def output_jobs_api():
    e = is_file_empty("Job_Posts.txt")
    if e == True:
        return

    file = open("Job_Posts.txt", "r")
    jobInfo = []
    for line in file:
        info = line.split("\t")
        info = info[:len(info) - 5]
        jobInfo.extend(info)
    file.close()

    file = open("MyCollege_jobs.txt", "w")
    for i in range(len(jobInfo)):
        if i % 5 == 0:
            file.write(jobInfo[i])
            file.write("\n")
            file.write(jobInfo[i + 1])
            file.write("\n")
            file.write(jobInfo[i + 2])
            file.write("\n")
            file.write(jobInfo[i + 3])
            file.write("\n")
            file.write(jobInfo[i + 4])
            file.write("\n")
            file.write("====")
            file.write("\n")

    file.close()


def output_users_API():
    e = is_file_empty("messages.txt")
    if e:
        return

    file = open("messages.txt", "r")
    userInfo = []
    for line in file:
        info = line.split("\t")
        userInfo.extend(info)
    file.close()

    file = open("MyCollege_users.txt", "w")
    for i in range(len(userInfo)):
        if i % 2 == 0:
            file.write(userInfo[i])
            file.write("\t")
            if userInfo[i + 1].rstrip() == "S":
                file.write("standard")
            else:
                file.write("plus")
            file.write("\n")

    file.close()


def output_savedJobs_API():
    e = is_file_empty("Job_Posts.txt")
    if e == True:
        return
    e = is_file_empty("messages.txt")
    if e == True:
        return

    # Get all usernames
    file = open("messages.txt", "r")
    user_names = []
    for line in file:
        info = line.split("\t")
        user_names.append(info[0])
    file.close()

    savedJobs = {}
    for names in user_names:
        savedJobs[names] = []

    for name in user_names:
        file = open("Job_Posts.txt", "r")
        for line in file:
            info = line.split("\t")
            if name in info[8]:
                savedJobs[name].append(info[0])
        file.close()

    file = open("MyCollege_savedJobs.txt", "w")
    for k, v in savedJobs.items():
        file.write(k)
        file.write("\n")
        for job in v:
            file.write(job)
            file.write("\n")

        file.write("====")
        file.write("\n")

    file.close()


def output_training_API():
    e = is_file_empty("Course.txt")
    if e == True:
        return

    e = is_file_empty("messages.txt")
    if e == True:
        return

    # Get all usernames
    file = open("messages.txt", "r")
    user_names = []
    for line in file:
        info = line.split("\t")
        user_names.append(info[0])
    file.close()

    coursesTaken = {}
    for names in user_names:
        coursesTaken[names] = []

    for name in user_names:
        file = open("Course.txt", "r")
        for line in file:
            info = line.strip()
            info = info.split("\t")
            if name in info:
                coursesTaken[name].append(info[0])
        file.close()

    file = open("MyCollege_training.txt", "w")
    for k, v in coursesTaken.items():
        file.write(k)
        file.write("\n")
        for course in v:
            file.write(course)
            file.write("\n")

        file.write("====")
        file.write("\n")

    file.close()


def output_appliedJobs_API():
    e = is_file_empty("Job_Posts.txt")
    if e == True:
        return

    e = is_file_empty("Course.txt")
    if e == True:
        return

    # get job posts
    jobPosts = []
    file = open("Job_Posts.txt", "r")
    for line in file:
        info = line.split("\t")
        jobPosts.append(info[0] + " " + info[1] + " " + info[2] + " " + info[3] + " " + info[4])
    file.close()

    jobs = {}
    for name in jobPosts:
        jobs[name] = []

    file = open("applicants.txt", "r")
    for line in file:
        info = line.strip()
        info = info.split("\t")
        jobs[info[1]].append(info[0])
        jobs[info[1]].append(info[2])
    file.close()

    file = open("MyCollege_appliedJobs.txt", "w")
    for k, v in jobs.items():
        file.write(k)
        file.write("\n")
        for i in range(len(v)):
            if (i % 2 == 0):
                file.write(v[i])
                file.write("\t")
                file.write(v[i + 1])
                file.write("\n")

        file.write("====")
        file.write("\n")

    file.close()


output_users_API()
output_jobs_api()
output_appliedJobs_API()
output_training_API()
output_savedJobs_API()
output_profiles_API()
# create log-in text file if it does not exist
loginFile = "Login.txt"
loginPath = Path(loginFile)
if loginPath.is_file():
    pass
else:
    CreateFile = open("Login.txt", "a")
    CreateFile.close()

# create job posts text file if it does not exist
jobFile = "Job_Posts.txt"
jobPath = Path(jobFile)
if jobPath.is_file():
    pass
else:
    createFile = open("Job_Posts.txt", "a")
    createFile.close()

# list of friend creation
friendFile = "list_of_friends.txt"
friendPath = Path(friendFile)
if friendPath.is_file():
    pass
else:
    createFile = open("list_of_friends.txt", "a")
    createFile.close()

# friend request creation
requestFile = "friend_requests.txt"
requestPath = Path(requestFile)
if requestPath.is_file():
    pass
else:
    createFile = open("friend_requests.txt", "a")
    createFile.close()

# job deletion creation
deletedJobsFile = "job_deletions.txt"
deletedJobsPath = Path(deletedJobsFile)
if deletedJobsPath.is_file():
    pass
else:
    createFile = open("job_deletions.txt", "a")
    createFile.close()

messagesFile = "messages.txt"
messagesPath = Path(messagesFile)
if messagesPath.is_file():
    pass
else:
    CreateFile = open("messages.txt", "a")
    CreateFile.close()

newjobFile = "NewJobs.txt"
newjobPath = Path(newjobFile)
if newjobPath.is_file():
    pass
else:
    CreateFile = open("NewJobs.txt", "a")
    CreateFile.close()

newmemberFile = "NewMembers.txt"
newmemberPath = Path(newmemberFile)
if newmemberPath.is_file():
    pass
else:
    CreateFile = open("NewMembers.txt", "a")
    CreateFile.close()

jobTimeFile = "job_time.txt"
jobTimePath = Path(jobTimeFile)
if jobTimePath.is_file():
    pass
else:
    CreateFile = open("job_time.txt", "a")
    CreateFile.close()

courseFile = "Course.txt"
coursePath = Path(courseFile)
if coursePath.is_file():
    pass
else:
    CreateFile = open("Course.txt", "a")
    CreateFile.close()
# call menu

# beginning of API searches and initial execution
studentAPIInputFile = "studentAccounts.txt"
studentAPIInputFilePath = Path(studentAPIInputFile)
# the next thing I wish to do is get a list of every single registered username in the database
if studentAPIInputFilePath.is_file():
    # case in which file exists
    usersAlreadyInDatabase = []
    database = open("login.txt", "r")
    listOfLines = database.readlines()
    for line in listOfLines:
        temp = line.split('\t')
        usersAlreadyInDatabase.append(temp[2])
    # Now I have a list of every username in the database as usersAlreadyInDatabase
    file = open("studentAccounts.txt", "r")
    listOfLines = file.readlines()
    iteration = 0
    IsInDatabase = False  # bool to test if the user we are evaluating is already in the database
    APIUsername = ""
    APIPassword = ""
    APIFirstName = ""
    APILastName = ""
    database.close()
    file.close()
    for line in listOfLines:
        if iteration % 3 == 0: # Every first line in a set follows this format: username\tfirstName\tlastName
            IsInDatabase = False
            temp = line.split('\t')
            for usernames in usersAlreadyInDatabase:  # I must now iterate through this list to see if we already have
                if temp[0] == usernames:              # this user
                    IsInDatabase = True
            # I now have a bool telling me if the user is already in the database
            if not IsInDatabase:
                APIUsername = temp[0]
                APIFirstName = temp[1]
                APILastName = temp[2]
        if iteration % 3 == 1: # Every second line in a set follows this format: password\n
            if not IsInDatabase:
                temp = line.split('\t')
                APIPassword = temp[0]
        if iteration % 3 == 2:
            if not IsInDatabase and (accountCount() < 10):
                APILastName = APILastName.strip()
                APIPassword = APIPassword.strip()
                now = datetime.now()
                now = str(now)
                file = open("Login.txt", "a")
                newjob = open("NewJobs.txt", "a")
                friendsfile = open("list_of_friends.txt", "a")
                requestsfile = open("friend_requests.txt", "a")
                memberfile = open("NewMembers.txt", "a")
                messages = open("messages.txt", "a")
                timejob = open("job_time.txt", "a")
                file.write(APIFirstName)
                file.write("\t")
                file.write(APILastName)
                file.write("\t")
                file.write(APIUsername)
                friendsfile.write(APIUsername + "\n")
                requestsfile.write(APIUsername + "\n")
                file.write("\t")
                file.write(APIPassword)
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("On")
                file.write("\t")
                file.write("English")
                file.write("\t")
                file.write(titleOpt)
                file.write("\t")
                file.write(majorOpt)
                file.write("\t")
                file.write(UniOpt)
                file.write("\t")
                file.write(aboutOpt)
                file.write("\t")
                file.write(expOpt1Title)
                file.write("\t")
                file.write(expOpt1Emp)
                file.write("\t")
                file.write(expOpt1Start)
                file.write("\t")
                file.write(expOpt1End)
                file.write("\t")
                file.write(expOpt1Loc)
                file.write("\t")
                file.write(expOpt1Des)
                file.write("\t")
                file.write(expOpt2Title)
                file.write("\t")
                file.write(expOpt2Emp)
                file.write("\t")
                file.write(expOpt2Start)
                file.write("\t")
                file.write(expOpt2End)
                file.write("\t")
                file.write(expOpt2Loc)
                file.write("\t")
                file.write(expOpt2Des)
                file.write("\t")
                file.write(expOpt3Title)
                file.write("\t")
                file.write(expOpt3Emp)
                file.write("\t")
                file.write(expOpt3Start)
                file.write("\t")
                file.write(expOpt3End)
                file.write("\t")
                file.write(expOpt3Loc)
                file.write("\t")
                file.write(expOpt3Des)
                file.write("\t")
                file.write(eduOptSchool)
                file.write("\t")
                file.write(eduOptDegree)
                file.write("\t")
                file.write(eduOptYears)
                file.write("\n")
                newjob.write(APIUsername + "\n")
                messages.write(APIUsername)
                messages.write("\t")
                messages.write("S")
                messages.write("\n")
                memberfile.write(APIUsername + "\n")
                timejob.write(APIUsername)
                timejob.write("\t")
                timejob.write(now)
                timejob.write("\n")
                timejob.close()
                memberfile.close()
                file.close()
                newjob.close()
                friendsfile.close()
                requestsfile.close()
                messages.close()
        iteration = iteration + 1
    file.close()
    # I must now do the job API, the first thing I need to do is get the titles of all the jobs currently in database
jobAPIInputFile = "newJobsAPI.txt"
jobAPIInputFilePath = Path(jobAPIInputFile)
if jobAPIInputFilePath.is_file():
    print("found")
    # case in which file exists
    jobsAlreadyInDatabase = []
    database = open("Job_Posts.txt", "r")
    listOfLines = database.readlines()
    for line in listOfLines:
        temp = line.split('\t')
        temp[0] = temp[0].strip()
        jobsAlreadyInDatabase.append(temp[0])
    print(jobsAlreadyInDatabase)
    database.close()
    file = open("newJobsAPI.txt", "r")
    listOfLines = file.readlines()
    iteration = 0
    IsInDatabase = False  # bool to test if the job we are evaluating is already in the database
    APIJobTitle = ""
    APIJobDescription = ""
    APIJobPoster = ""
    APIJobEmployer = ""
    APIJobLocation = ""
    APIJobSalary = ""
    for line in listOfLines:
        print(line)
        print(iteration)
        if iteration % 7 == 0:
            APIJobTitle = ""
            APIJobDescription = ""
            APIJobPoster = ""
            APIJobEmployer = ""
            APIJobLocation = ""
            APIJobSalary = ""
            IsInDatabase = False
            temp = line.split('\n')
            for jobs in jobsAlreadyInDatabase:
                if temp[0] == jobs:  # this user
                    IsInDatabase = True
            # I now have a bool telling me if the user is already in the database
            if not IsInDatabase: # case in which job title isn't in database
                APIJobTitle = temp[0]
                # print(temp[0])
                # print("match")
            iteration = iteration + 1
        elif iteration % 7 == 1:
            if not IsInDatabase :
                if "&&&" in line: # we're at end of description
                    line = line[:-5]
                    APIJobDescription = APIJobDescription + line
                    iteration = iteration + 1
                else: # we're not at the end
                    line = line.strip()
                    APIJobDescription = APIJobDescription + line + " "
            else: # continue reading through newJobs.txt
                if "&&&" in line:
                    iteration = iteration + 1
                else:
                    pass
        elif iteration % 7 == 2:
            APIJobPoster = line.strip()
            iteration = iteration + 1
        elif iteration % 7 == 3:
            APIJobEmployer = line.strip()
            iteration = iteration + 1
        elif iteration % 7 == 4:
            APIJobLocation = line.strip()
            iteration = iteration + 1
        elif iteration % 7 == 5:
            APISalary = line.strip()
            iteration = iteration + 1
            if not IsInDatabase: # start of pasted function
                #pass
                # count the number of job posts in the system
                file = open("Job_Posts.txt", "r")
                postCount = 0
                for line in file:
                    if line != "\n":
                        postCount += 1
                file.close()

                file = open("Job_Posts.txt", "a")
                # if job posts in the system is not 5 or more proceed
                if postCount < 10:
                    file.write(APIJobTitle)
                    file.write("\t")
                    file.write(APIJobDescription)
                    file.write("\t")
                    file.write(APIJobEmployer)
                    file.write("\t")
                    file.write(APIJobLocation)
                    file.write("\t")
                    file.write(APIJobSalary)
                    file.write("\t")
                    file.write("NULL")
                    file.write("\t")
                    file.write(APIJobPoster)
                    file.write("\t")
                    file.write("applicants,")
                    file.write("\t")
                    file.write("saved,")
                    file.write("\t")
                    file.write("Placeholder")
                    file.write("\n")
                    file.close()
                    count = 0
                    for line in open("NewJobs.txt", "r"):
                        if userName in line:
                            break
                        else:
                            count += 1

                    file = open("NewJobs.txt", "r")
                    listOfLines = file.readlines()
                    i = 0
                    while i < len(listOfLines):
                        if i != count:
                            listOfLines[i] = listOfLines[i].rstrip() + "\t" + APIJobTitle + "\n"
                            i += 1
                        else:
                            i += 1
                    file.close()
                    file = open("NewJobs.txt", "w")
                    file.writelines(listOfLines)
                    file.close()
        elif iteration % 7 == 6:
            iteration = iteration + 1
    # I have a list of jobs already in the database under jobsAlreadyInDatabase
    # Now is the time to parse through the input API

    trainingAPIInputFile = "newtraining.txt"
    trainingAPIInputFilePath = Path(trainingAPIInputFile)
    if trainingAPIInputFilePath.is_file():
        file = open("course.txt", "r")
        listOfLines = file.readlines()
        coursesAlreadyInDatabase = []
        for line in listOfLines:
            temp = line.split('\t')
            coursesAlreadyInDatabase.append(temp[0])
        # we now have all the courses in the database
        # Now for the training Input API
        trainingAPIInputFile = open("newtraining.txt", "r")
        listOfLines = trainingAPIInputFile.readlines()
        courseInDatabase = False
        for line in listOfLines:
            print(line)
            courseInDatabase = False
            line = line.strip()
            for course in coursesAlreadyInDatabase:
                if line == course:
                    courseInDatabase = True
            print(courseInDatabase)
            if not courseInDatabase:
                courseFile = open("Course.txt", "a")
                courseFile.write(line)
                courseFile.write('\t')
                courseFile.write('Placeholder')
                courseFile.write('\n')
                courseFile.close()
        trainingAPIInputFile.close()

profilesFile = "MyCollege_profiles.txt"
profilesPath = Path(profilesFile)
if profilesPath.is_file():
    pass
else:
    createFile = open("MyCollege_profiles.txt", "a")
    createFile.close()
jobsAPIFile = "MyCollege_jobs.txt"
jobsAPIPath = Path(jobsAPIFile)
if jobsAPIPath.is_file():
    pass
else:
    CreateFile = open("MyCollege_jobs.txt", "a")
    CreateFile.close()

usersAPIFile = "MyCollege_users.txt"
usersAPIPath = Path(usersAPIFile)
if usersAPIPath.is_file():
    pass
else:
    CreateFile = open("MyCollege_users.txt", "a")
    CreateFile.close()

savedJobsAPIFile = "MyCollege_savedJobs.txt"
savedJobsAPIPath = Path(savedJobsAPIFile)
if savedJobsAPIPath.is_file():
    pass
else:
    CreateFile = open("MyCollege_savedJobs.txt", "a")
    CreateFile.close()

trainingAPIFile = "MyCollege_training.txt"
trainingAPIPath = Path(trainingAPIFile)
if trainingAPIPath.is_file():
    pass
else:
    CreateFile = open("MyCollege_training.txt", "a")
    CreateFile.close()

appliedJobsAPIFile = "MyCollege_appliedJobs.txt"
appliedJobsAPIPath = Path(appliedJobsAPIFile)
if appliedJobsAPIPath.is_file():
    pass
else:
    CreateFile = open("MyCollege_appliedJobs.txt", "a")
    CreateFile.close()

applicantsFile = "applicants.txt"
applicantsPath = Path(applicantsFile)
if applicantsPath.is_file():
    pass
else:
    CreateFile = open("applicants.txt", "a")
    CreateFile.close()

menu()
