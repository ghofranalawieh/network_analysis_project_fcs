#This file will be presenting the user_profile
#The features we are going to implement are:
#age, name, gender, prog_lang, companies, experience, ready to help
# (The user activity. if they are ready  to help other codres or not), 


#in need for help(if the user is in need for other programmers help to review their code) 
# characteristics of the user




class User:
    #first we define a variable to calculate the number of users 
    #set it initially to 0
    number_of_users = 0

    #a bunch of needed lists for the sake of statistical inf
    #about the users of the class (%, averages)
    #And these statistics will help inprove the features of the program to tolerate the users' needs

    gender_list = []
    ready_to_help = []
    in_need_for_help = [] 
    age_list = []
    experience_list = []

    #This is the dictionary to store the users data, where every user data is another dictionary
    #it takes the number of the user as the key
    #it automatically update the number of user when you add, remove  users from the beginning,middle, end
    USER_DATA = {}

    def __init__(self, user_name:str, age:int, companies:set, experience:int, gender:str, prog_lang:set, ready:bool, needy:bool):
         
       #set the user's data
       #we use .lower() method for data storage and comparison later
       self.__user_name = user_name.lower()
       self.__age  = age
       self.__companies = {comp.lower() for comp in companies}
       self.__experience = experience
       self.__gender = gender.lower()
       self.__prog_lang = {pl.lower() for pl in prog_lang}
       self.__ready = ready
       self.__needy = needy
   


       #This small dictionary is the value of the key in USER_DATA
       #Here we store all the needed inforamtion about the user
       self.__data ={
           'user name':self.__user_name,
           'age': self.__age,
           'companies':self.__companies,
           'experience':self.__experience,
           'gender':self.__gender,
           'programming langs':self.__prog_lang,
           'Ready to help': self.__ready,
           'In need for help':self.__needy
       }

       

       #increment the number of users by 1
       User.number_of_users += 1


       #update the USER_DATA dictionary
       User.USER_DATA[User.number_of_users]=self.__data



       #append the needed data to the lists 
       User.gender_list.append(self.__gender)
       User.ready_to_help.append(self.__ready)
       User.in_need_for_help.append(self.__needy)
       User.age_list.append(self.__age)
       User.experience_list.append(self.__experience)

