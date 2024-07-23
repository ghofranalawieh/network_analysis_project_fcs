#This file will be presenting the user_profile and the graph data and visualization
#Initially we will be working on the user class with all the needed features for the user's profile
#Including: user name, age, experience, companies that the user works at, gender, programming languages that the user knows
#in addition to the user status if they are in need for other coders help or ready to help other coder in code review
#PLus the requests from this user to other users and other requests to them 



#we import defaultdict from collections because we are going to use it later in the graph class
from collections import defaultdict


class User:
    #first we define a variable to calculate the number of users 
    #set it initially to 0
    number_of_users = 0


    #This is the dictionary to store the users data, where every user data is another dictionary
    #it takes the number of the user as the key
    #it automatically update the number of user when you add, remove  users from the beginning,middle, end
    USER_DATA = {}

    def __init__(self, user_name:str, age:int, companies:set, experience:int, gender:str, prog_lang:set, ready:bool, needy:bool):
       
       #when having new user we increment the number of users by 1
       User.number_of_users += 1  

       # we do not user self.__user_number because we will be using this feature later in the other class
       self.user_number = User.number_of_users

       #set the user's data
       #we use .lower() method for data storage and comparison later  
       self.__user_name = user_name  
       self.__age  = age
       self.__companies = {comp.lower() for comp in companies}
       self.__experience = experience
       self.__gender = gender.lower()
       self.__prog_lang = {pl.lower() for pl in prog_lang}
       self.__ready = ready
       self.__needy = needy

       #These dictionaries that we want to use in order to manage user requests and followers
       self.__requested_by =[]
       self.__requests = []
       self.__number_of_requests =0
       self.__number_of_requested_by= 0
   


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
           'In need for help':self.__needy,
           'requested by' : self.__requested_by,
           'requests': self.__requests,
           'number of requests':self.__number_of_requests,
           'number of people requested this user':self.__number_of_requested_by
       }

    

       #update the USER_DATA dictionary
       User.USER_DATA[self.user_number]=self.__data


    #This is a function to add new requests to the user requets dictionary
    def request(self, user:int)->None:
        '''
        This is a function at the level of instance, that takes one integer argument as the user number
        and makes a request from the user to that user of this given integer       
        '''
        if user not in self.__requests and user!=self.user_number:
            #first add the number of the requested user to the list of requests of the current user
            self.__requests.append(user)

            #increase the number of requests for this current user by 1
            User.USER_DATA[self.user_number]["number of requests"] += 1

            #add the current user to the requested_by list of the other user
            User.USER_DATA[user]["requested by"].append(self.user_number)

            #increment the number of people who requested the other user by 1
            User.USER_DATA[user]["number of people requested this user"] += 1




    #This is a function to delete the request from one user to another
    def cancel_request(self, user:int)->None:
        '''
        This is a method at the level of instance, that takes one integer argument as the user number
        and cancels a request from the user to that user of this given integer       
        '''

        #fist we have to make sure that this user is in the requests list of the current user
        if user in self.__requests:
            #if there, all we need to do is to delete this user number from the requests list of the current user
            self.__requests.remove(user)  

            #modify the number of requests of the current user, decrease it by 1
            User.USER_DATA[self.user_number]["number of requests"] -= 1 

            #remove the current user from the requested_by list of the other user
            User.USER_DATA[user]["requested by"].remove(self.user_number)

            #decrement the number of peoplr requesting the other  user by 1
            User.USER_DATA[user]["number of people requested this user"] -= 1




    #This is a function to get the number of requests of a user
    def get_number_of_requests(self)->int:
        '''
        This is a method at the instance level, that takes no arguments, and returns the 
        number of requests of this user
        '''
        return self.__number_of_requests


    #this is a function to get the requests dictionary of a user
    def get_requests(self)->dict:
        '''
        This is a method at the level of instance, it takes no arguments, and returns the 
        coders who this user requested
        '''
        
        return self.__requests 



    #This is a function to get the number of people requested this user
    def get_requested_by(self)->dict:
        '''
        This is a method at the level of instance, it takes no arguments, and returns the 
        coders who have requested this user
        '''
        return self.__requested_by
   
   


    #first getter/setter for user_name
    def get_user_name(self)->str:
        '''
        This method is instance level
        it takes no arguments, and simply print the name of the user                 
        '''   
        print(f"The name of this user is {self.__user_name}")


    def set_user_name(self, name:str):
        '''
        This method is at instance level 
        it takes one string input a the new name and update the user_name to it     
        '''    
        self.__user_name  = name.lower()
    
    
    #These are methods to get and set the age
    def get_age(self)->int:
        '''
        This method is at instance level, it takes no 
        arguments and simply print the age of the user
        '''  
        print(f"This user is : {self.__age} years old")

    def set_age(self, new_age:int, index:int):
        '''
        This method is at instance level, it takes two arguments, 
        one is integer -the new age- other is the index that
        represents the number of the user
        in the age list to update its value
        '''
        if new_age<self.__age:
            return -1
        self.__age= new_age
        User.age_list[index-1] = new_age


    #This is a method to get  the gender of the user 
    

    def get_gender(self)->str:
        '''
        This method is at instance level, it takes no arguments
        but simply print the user gender
        '''   
        print(f"The gender of the user is : {self.__gender}")


    #These are methods to set/get experience of the user
    def get_experience(self)->int:
        '''
        This method is at instance level, it takes no arguments
        and simply print the experience years of the user
        '''
        print(f"This user has : {self.__experience} years of experience")



    def set_experience(self, years:int, index:int):
        '''
        This method is at instance level it takes two integer arguments, 
        one is the new years of experience, other is the number of the user that represent
        its inddex in the experience list to update it
        '''   
        self.__experience = years
        User.experience_list[index-1] = years



     #These methods to get/add/remove companies from user profile
    def get_companies(self)->set:
        '''
        This is a method at instance level , it takes no arguments
        it simply print the companies that the user works at
        '''   
        print(f"The user works at: {self.__companies}")


    def add_companies(self, comp:str):
       '''
       This is a method at instance level, it takes one string argument
       as the new company and adds it to the set of companies
       that the user works at
       '''
       if comp.lower() not in self.__companies:
           self.__companies.add(comp.lower())

    def remove_companies(self, comp:str):
        '''
        This is a method at instance level, it takes one string argument
       as the  company to be removed from  the set of companies
       that the user works at       
        '''
        if comp.lower() in self.__companies:
            self.__companies.remove(comp.lower())



    #These methods are to get/add/remove programming languages from the user profile
    def get_prog_lang(self)->set:
        '''
        This method is at instance level, it takes no arguments
        it simply print the programming languages that the user knows
        '''               
        print(f"The programming languages that the user knows are: {self.__prog_lang}")


    def add_prog_lang(self, pl:str):
        '''
        This method is at instance level, it takes one string argument
        as the new programming language to add to the set of 
        programming languages of the user      
        '''    
        if pl.lower() not in self.__prog_lang:
            self.__prog_lang.add(pl.lower())



    def remove_prog_lang(self, pl:str):
        '''
        This method is at instance level, it takes one string argument
        as the  programming language to be removed from the set of 
        programming languages of the user        
        ''' 

        if pl.lower() in self.__prog_lang:
            self.__prog_lang.remove(pl.lower()) #These are get/set functions for ready to help part in the user profile


    def check_if_ready(self)->bool:
        '''
        This method is at instance level, it takes no arguments
        and simply print a phrase telling if the user is ready to 
        help other coder or not       
        '''               
        if self.__ready==True:
            print("ready to help!")
        else:
            print("Not ready to help!")    
    
    def set_ready(self, ready:bool, index:int):
        '''
        This method is at instance level, it takes two arguments
        one is the new boolean value for the status, other is an integer
        as the index of the user in the list of ready to update it       
        '''
        self.__ready = ready
        User.ready_to_help[index-1]=ready #we use index-1 not index because the list starts from 0


    #These are get/set functions for in need for help part in the user profile
    def check_if_needy(self)->bool:
        '''
        This method is at instance level, it takes no arguments
        and simply print a phrase telling if the user is in need for
        other coders' help  or not  
        '''    
        if self.__needy ==True:
            print("I need your help!")
        else:
            print("Everything is OK!")    
    

    def set_needy(self, needy:bool, index :int):
        '''
        This method is at instance level, it takes two arguments
        one is the new boolean value for the status, other is an integer
        as the index of the user in the list of needy to update it 
        '''
        self.__needy = needy
        User.in_need_for_help[index-1]=needy


       #This is a function to get the percentage of ppl who are ready to help
    def helpful_percentage()->float:
        '''
        This method is at class level, it takes no arguments,
        it simply prints out the percentage of coders who are welling to help     
        '''    
        summ = 0
        for i in User.ready_to_help:
            if i== True:
                summ += 1
        percentage = (summ/len(User.ready_to_help)*100)
        rounded = round(percentage, 2)
        print(f"The percentage of coders who are ready to help: {rounded} %")
    

    

    #This is  a function to get the percentage of people who are in need for help
    def needy_percentage()->float:
        '''
        This method is at class level, it takes no arguments,
        it simply prints out the percentage of coders who are in need for 
        other coders help          
        '''
        summ = 0
        for i in User.in_need_for_help:
            if i==True:
                summ += 1
        percentage = (summ/len(User.in_need_for_help)*100)
        rounded = round(percentage, 2)
        print(f"The percentage of needy coders is : {rounded} %")
    

    

    #This is a function to get the percentage of users sorted by gender
    def gender_percentage()->float:
        '''
        This is a function of the class that takes no arguments and it returns the 
        percentsge of users' genders in the program        
        '''         
        sumf = 0
        for i in User.gender_list:
            if i == 'female':
                sumf += 1
        percentage_females = (sumf / len(User.gender_list) * 100)
        roundedf = round(percentage_females, 2)
        percentage_males = 100 - percentage_females
        roundedm = round(percentage_males, 2)

        print(f"The percentage of female users is : {roundedf} %\nThe percentage of male users is : {roundedm} %")
    

    
    #This is a function to get the average age of the users
    def average_age()->float:
        '''
        This methaod is at class level ,it takes no arguments,
        it simply print out the average age of users      
        '''
        average = sum(User.age_list)/len(User.age_list)
        rounded = round(average, 2)
        print(f"The average age of users is : {rounded}")
    


    #This is a function to get the average experience of the users
    def average_experience()->float:
        '''
        This methaod is at class level ,it takes no arguments,
        it simply print out the average experience of users        
        '''
        average = sum(User.experience_list)/len(User.experience_list)
        rounded = round(average, 2)
        print(f"The average experience of users is : {rounded}")
    


    


