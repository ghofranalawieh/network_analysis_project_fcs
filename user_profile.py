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
    


    


