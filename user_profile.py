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
        return self.__user_name


    def set_user_name(self, name:str):
        '''
        This method is at instance level 
        it takes one string input a the new name and update the user_name to it     
        '''    
        User.USER_DATA[self.user_number]["user name"]= name.lower()


    
    
    #These are methods to get and set the age
    def get_age(self)->int:
        '''
        This method is at instance level, it takes no 
        arguments and simply print the age of the user
        '''  
        return self.__age


    def set_age(self, new_age:int):
        '''
        This method is at instance level, it takes one argument, 
        as the new age to reset it in the profile
        '''
        User.USER_DATA[self.user_number]["age"]= new_age

        


    #This is a method to get  the gender of the user 
    def get_gender(self)->str:
        '''
        This method is at instance level, it takes no arguments
        but simply print the user gender
        '''   
        return  self.__gender




    #These are methods to set/get experience of the user
    def get_experience(self)->int:
        '''
        This method is at instance level, it takes no arguments
        and simply print the experience years of the user
        '''
        return self.__experience



    def set_experience(self, years:int)->None:
        '''
        This method is at instance level it takes one integer argument, 
        as the new experience of the user
        '''   
        User.USER_DATA[self.user_number]["experience"] = years
       



    #These methods to get/add/remove companies from user profile
    def get_companies(self)->set:
        '''
        This is a method at instance level , it takes no arguments
        it simply print the companies that the user works at
        '''   
        return self.__companies


    def add_companies(self, comp:str)->None:
       '''
       This is a method at instance level, it takes one string argument
       as the new company and adds it to the set of companies
       that the user works at
       '''
       if comp.lower() not in self.__companies:
           self.__companies.add(comp.lower())

    def remove_companies(self, comp:str)->None:
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
        return self.__prog_lang

    def add_prog_lang(self, pl:str)->None:
        '''
        This method is at instance level, it takes one string argument
        as the new programming language to add to the set of 
        programming languages of the user      
        '''    
        if pl.lower() not in self.__prog_lang:
            self.__prog_lang.add(pl.lower())

    def remove_prog_lang(self, pl:str)->None:
        '''
        This method is at instance level, it takes one string argument
        as the  programming language to be removed from the set of 
        programming languages of the user        
        ''' 

        if pl.lower() in self.__prog_lang:
            self.__prog_lang.remove(pl.lower())




    #These are get/set functions for ready to help part in the user profile
    def check_if_ready(self)->bool:
        '''
        This method is at instance level, it takes no arguments
        and simply print a phrase telling if the user is ready to 
        help other coder or not       
        '''               
        return self.__ready
          
    
    def set_ready(self, ready:bool)->None:
        '''
        This method is at instance level, it takes one argument
        that  is the new boolean value for the status   
        '''
        User.USER_DATA[self.user_number]["Ready to help"] = ready
        



    #These are get/set functions for in need for help part in the user profile
    def check_if_needy(self)->bool:
        '''
        This method is at instance level, it takes no arguments
        and simply print a phrase telling if the user is in need for
        other coders' help  or not  
        '''    
        return self.__needy
        
    

    def set_needy(self, needy:bool)->None:
        '''
        This method is at instance level, it takes one argument
        that is the new boolean value for the status 
        '''
        User.USER_DATA[self.user_number]["In need for help"] = needy


    #This is a method to get the entire data of the user
    def get_data(self):
        for user, d in  self.__data.items():
            print(user, ':' , d) 





"========================================================================================================================================================================================="   
#we are all done with the user class, now we are going to build the graph class over it 
#in the graph class we have many features: add and remove users from the site
#build new connections and cncel some other connections
#sort the users and search them , in addition to many other details
#all the statistics are done in this class
#visualization is also in this class

class Graph:
    

    #initially we set the class to take no arguments
    def __init__(self):
        
        #This is the list where we are going to store the number of users
        self.__nodes_list =[]
           
        #This is an adjacency list dictionary to keep track of the connections in the class
        self.__requests_list = {} 

        #set the number of users to 0 initially
        self.__number_of_nodes =0
        

        #This is a list to store tuples of connections to use them as edges in the visualization function later
        self.__connections_components = []

        #set the number of edges in the graph initially to 0
        self.number_of_connections =0




    #This is a function to add new users to the graph    
    def add_users(self,user:User)->None:
        '''
        This is a method at the level of instance, it takes user of class User as an 
        argument and store its number in the class
        '''

        #first check if the user already exists, ecause we don't want to add a user twice
        if user.user_number not in self.__nodes_list:

            #we add this user to the list of nodes
            self.__nodes_list.append(user.user_number)

            #add it as a key in the dictionary of adjacency list with an empty list as a value
            self.__requests_list[user.user_number]=[]

            #increment the number of nodes in the graph by 1
            self.__number_of_nodes += 1
    



     #This is a function to remove a user from the graph
    def remove_user(self, user:User)->None:
        '''
        This is a methad at the level of instance, it takes user of class User as an argument
        and delete its data from the graph        
        '''
        
        #first check if this user exists in the users list of the graph
        if user.user_number in self.__nodes_list:

            #if exists remove it from the list of users
            self.__nodes_list.remove(user.user_number)

            #and delete its key, value pair from the adjacency list dictionary
            del self.__requests_list[user.user_number]

            #decrement the number of nodes of this graph by 1
            self.__number_of_nodes -= 1
            

            #remove this node from other lists of the other nodes in the adjacency list dictionary if exists
            for  v in self.__requests_list.values():
                if user.user_number in v:
                    v.remove(user.user_number)

            #we also need to remove all the connections with it from the connections matrix
            # we set the number of deleting times to 0 initially to decrement it from the total number of connections in the graph        
            number_of_delete =0
            connections_to_remove = []        
            for a, b in self.__connections_components:
                if a==user.user_number or b==user.user_number:
                   connections_to_remove.append((a,b))
            
            for connection in connections_to_remove:
                self.__connections_components.remove(connection)
                number_of_delete += 1
            self.number_of_connections -= number_of_delete
            




    #This is a function to add an edge between 2 nodes in the graph  
    def add_connection(self, userF:User, userS:User)->None:
        '''
        This is a method at the instance level, that takes 2 users of class User as arguuents
        and build a directed edge from userF to userS
        '''

        #first we have to check if there are any connection from userF to userS
        if userS.user_number not in self.__requests_list[userF.user_number]:

            #we add userS to the value list in the adj-list dictionary
            self.__requests_list[userF.user_number].append(userS.user_number)

            #we append a tuple of the new connected pairs to the connections matrix
            self.__connections_components.append((userF.user_number, userS.user_number))

            #increment the number of connections by 1
            self.number_of_connections += 1

            #apply the request method from class User to perform all the needed updation to the user profile and data
            userF.request(userS.user_number)        




    
    #This is a function to remove an edge between two nodes in the graph    
    def cancel_request(self, userF:User, userS:User)->None:
        '''
        This is a method at the instance level, that takes 2 users of class User as arguuents
        and break a directed edge from userF to userS        
        '''

        #first we have to check if there is an edge between these 2 nodes directed from userF to userS
        if userS.user_number in self.__requests_list[userF.user_number]:

            #we remove userS from the value list of userF in the adj-list dictionary
            self.__requests_list[userF.user_number].remove(userS.user_number)

            #we remove the tuple of connection directed from userF to userS from the connection  matrix
            self.__connections_components.remove((userF.user_number, userS.user_number))

            #we decrement the number of edges in this graph by 1
            self.number_of_connections -= 1

            #we apply the cancel_request method from class User to update the users profiles and data
            userF.cancel_request(userS.user_number)       




    #This is a function to get the number of edges in the current graph
    def get_connections(self)->int:
      '''
      This is a method at the instance level, that takes no arguments and returns 
      the number of edges in this graph
      '''
      return self.number_of_connections

    

    #This is a function to get the edges direction -components- in the graph
    def get_connections_components(self)->list[tuple]:
        '''
        This is a method at the level of instance, that takes no arguments and return 
        the edges components in the current graph
        '''
        return self.__connections_components  
    


    #This is a function to get the outdegrees of all nodes in the graph in a dictionary    
    def get_out_degrees(self)->dict:
        '''
        This is a function at the level of instance that takes no arguments and it returns
        a dictionary
        '''
        out_degrees = []
        
        #we iterate through keys, and values of the adj-list dictionary
        for u, v in self.__requests_list.items():
            out_degrees.append((u, {f"The outdegree":len(v)}))
        return out_degrees 
    



    #This is a function to get the indegrees of all nodes in the graph in a dictionary
    def get_in_degrees(self)->dict:
        '''
        This is a method at the level of instance, that takes no arguments
        and it returns a dictionary 
        '''
        in_degrees =[]

        #we iterate over the keys of adj-list dictionary and check the indegrees from the user data in the class user
        for u in self.__nodes_list:
            in_degrees.append((u, {'the indegrees': User.USER_DATA[u]["number of people requested this user"]}))
        return in_degrees 
    


    #This is a function to get the degrees of all nodes in the graph in a dictionary
    def get_degrees(self):
        '''
        This is a method at the level of instance, that takes no arguments
        and return the degrees of nodes in a dictionary
        '''
        degrees = []
        for u, v in self.__requests_list.items():
            degrees.append((u, {'the degree is:': (len(v)+User.USER_DATA[u]["number of people requested this user"])}))
        return degrees  
    

    #This is a function to get the percentage of ppl who are ready to help
    def helpful_percentage(self)->float:
        '''
        This method is at class level, it takes no arguments,
        it simply prints out the percentage of coders who are welling to help     
        '''  
        summ = 0
        for u in self.__nodes_list:
            if User.USER_DATA[u]['Ready to help']==True:
                summ += 1
                
        percentage = ((summ/self.__number_of_nodes)*100)
        rounded = round(percentage, 2)
        return rounded   
    

















    
    


    


