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
    def request(user1:int, user:int)->None:
        '''
        This is a function at the level of instance, that takes one integer argument as the user number
        and makes a request from the user to that user of this given integer       
        '''
        if user not in User.USER_DATA[user1]["requests"] and user!=user1:
            #first add the number of the requested user to the list of requests of the current user
            User.USER_DATA[user1]["requests"].append(user)

            #increase the number of requests for this current user by 1
            User.USER_DATA[user1]["number of requests"] += 1

            #add the current user to the requested_by list of the other user
            User.USER_DATA[user]["requested by"].append(user1)

            #increment the number of people who requested the other user by 1
            User.USER_DATA[user]["number of people requested this user"] += 1




    #This is a function to delete the request from one user to another
    def cancel_request(user1:int, user:int)->None:
        '''
        This is a method at the level of instance, that takes one integer argument as the user number
        and cancels a request from the user to that user of this given integer       
        '''

        #fist we have to make sure that this user is in the requests list of the current user
        if user in User.USER_DATA[user1]["requests"]:
            #if there, all we need to do is to delete this user number from the requests list of the current user
            User.USER_DATA[user1]["requests"].remove(user)  

            #modify the number of requests of the current user, decrease it by 1
            User.USER_DATA[user1]["number of requests"] -= 1 

            #remove the current user from the requested_by list of the other user
            User.USER_DATA[user]["requested by"].remove(user1)

            #decrement the number of people requesting the other  user by 1
            User.USER_DATA[user]["number of people requested this user"] -= 1




    #This is a function to get the number of requests of a user
    def get_number_of_requests(user: int)->int:
        '''
        This is a method at the instance level, that takes no arguments, and returns the 
        number of requests of this user
        '''
        return User.USER_DATA[user]["number of requests"]


    #this is a function to get the requests list of a user
    def get_requests(user: int)->list:
        '''
        This is a method at the level of instance, it takes no arguments, and returns the 
        coders who this user requested
        '''
        
        return User.USER_DATA[user]['requests']



    #This is a function to get the people requested this user
    def get_requested_by(user: int)->list:
        '''
        This is a method at the level of instance, it takes no arguments, and returns the 
        coders who have requested this user
        '''
        return User.USER_DATA[user]['requested by']


    #This is a function to get the number of users requested this user
    def get_number_of_followers(user:int)->int:
        '''
        This is a method at the level of instance, it takes no arguments 
        it returns the number of users reequested the instance user
        ''' 
        return User.USER_DATA[user]["number of people requested this user"]




    #first getter/setter for user_name
    def get_user_name(user:int)->str:
        '''
        This method is instance level
        it takes no arguments, and simply print the name of the user                 
        '''   
        return User.USER_DATA[user]["user name"]


    def set_user_name(user:int, name:str):
        '''
        This method is at instance level 
        it takes one string input a the new name and update the user_name to it     
        '''    
        User.USER_DATA[user]["user name"]= name.lower()


    
    
    #These are methods to get and set the age
    def get_age(user:int)->int:
        '''
        This method is at instance level, it takes no 
        arguments and simply print the age of the user
        '''  
        return User.USER_DATA[user]["age"]


    def set_age(user: int, new_age:int):
        '''
        This method is at instance level, it takes one argument, 
        as the new age to reset it in the profile
        '''
        User.USER_DATA[user]["age"]= new_age

        


    #This is a method to get  the gender of the user 
    def get_gender(user:int)->str:
        '''
        This method is at instance level, it takes no arguments
        but simply print the user gender
        '''   
        return  User.USER_DATA[user]["gender"]




    #These are methods to set/get experience of the user
    def get_experience(user:int)->int:
        '''
        This method is at instance level, it takes no arguments
        and simply print the experience years of the user
        '''
        return User.USER_DATA[user]["experience"]



    def set_experience(user:int, years:int)->None:
        '''
        This method is at instance level it takes one integer argument, 
        as the new experience of the user
        '''   
        User.USER_DATA[user]["experience"] = years
       



     #These methods to get/add/remove companies from user profile
    def get_companies(user:int)->set:
        '''
        This is a method at instance level , it takes no arguments
        it simply print the companies that the user works at
        '''   
        return User.USER_DATA[user]["companies"]


    def add_companies(user:int, comp:str)->None:
       '''
       This is a method at instance level, it takes one string argument
       as the new company and adds it to the set of companies
       that the user works at
       '''
       if comp.lower() not in User.USER_DATA[user]["companies"]:
           User.USER_DATA[user]["companies"].add(comp.lower())

    def remove_companies(user:int, comp:str)->None:
        '''
        This is a method at instance level, it takes one string argument
       as the  company to be removed from  the set of companies
       that the user works at       
        '''
        if comp.lower() in User.USER_DATA[user]["companies"]:
            User.USER_DATA[user]["companies"].remove(comp.lower())





    #These methods are to get/add/remove programming languages from the user profile
    def get_prog_lang(user: int)->set:
        '''
        This method is at instance level, it takes no arguments
        it simply print the programming languages that the user knows
        '''               
        return User.USER_DATA[user]["programming langs"]

    def add_prog_lang(user:int, pl:str)->None:
        '''
        This method is at instance level, it takes one string argument
        as the new programming language to add to the set of 
        programming languages of the user      
        '''    
        if pl.lower() not in User.USER_DATA[user]["programming langs"]:
            User.USER_DATA[user]["programming langs"].add(pl.lower())

    def remove_prog_lang(user: int, pl:str)->None:
        '''
        This method is at instance level, it takes one string argument
        as the  programming language to be removed from the set of 
        programming languages of the user        
        ''' 

        if pl.lower() in User.USER_DATA[user]["programming langs"]:
            User.USER_DATA[user]["programming langs"].remove(pl.lower())




    #These are get/set functions for ready to help part in the user profile
    def check_if_ready(user:int)->bool:
        '''
        This method is at instance level, it takes no arguments
        and simply print a phrase telling if the user is ready to 
        help other coder or not       
        '''               
        return User.USER_DATA[user]["Ready to help"]
          
    
    def set_ready(user: int, ready:bool)->None:
        '''
        This method is at instance level, it takes one argument
        that  is the new boolean value for the status   
        '''
        User.USER_DATA[user]["Ready to help"] = ready
        



    #These are get/set functions for in need for help part in the user profile
    def check_if_needy(user:int)->bool:
        '''
        This method is at instance level, it takes no arguments
        and simply print a phrase telling if the user is in need for
        other coders' help  or not  
        '''    
        return User.USER_DATA[user]["In need for help"]
        
    

    def set_needy(user:int, needy:bool)->None:
        '''
        This method is at instance level, it takes one argument
        that is the new boolean value for the status 
        '''
        User.USER_DATA[user]["In need for help"] = needy


        

    #This is a method to get the entire data of the user
    def get_data(user:int):
        for user, d in  User.USER_DATA[user].items():
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
        self.nodes_list =[]
           
        #This is an adjacency list dictionary to keep track of the connections in the class
        self.__requests_list = {} 

        #set the number of users to 0 initially
        self.__number_of_nodes =0
        

        #This is a list to store tuples of connections to use them as edges in the visualization class later
        self.__connections_components = []

        #set the number of edges in the graph initially to 0
        self.number_of_connections =0


    #This is a function to add new users to the graph    
    def add_users(self,user:int)->None:
        '''
        This is a method at the level of instance, it takes user of class User as an 
        argument and store its number in the class
        '''

        #first check if the user already exists, because we don't want to add a user twice
        if user not in self.nodes_list:

            #we add this user to the list of nodes
            self.nodes_list.append(user)

            #add it as a key in the dictionary of adjacency list with an empty list as a value
            self.__requests_list[user]=[]

            #increment the number of nodes in the graph by 1
            self.__number_of_nodes += 1
    
    

    #This is a function to remove a user from the graph
    def remove_user(self, user:int)->None:
        '''
        This is a methad at the level of instance, it takes user of class User as an argument
        and delete its data from the graph        
        '''
        
        #first check if this user exists in the users list of the graph
        if user in self.nodes_list:

            #if exists remove it from the list of users
            self.nodes_list.remove(user)

            #and delete its key, value pair from the adjacency list dictionary
            del self.__requests_list[user]

            #decrement the number of nodes of this graph by 1
            self.__number_of_nodes -= 1
            

            #remove this node from other lists of the other nodes in the adjacency list dictionary if exists
            for  v in self.__requests_list.values():
                if user in v:
                    v.remove(user)

            #we also need to remove all the connections with it from the connections matrix
            # we set the number of deleting times to 0 initially to decrement it from the total number of connections in the graph        
            number_of_delete =0
            connections_to_remove = []        
            for a, b in self.__connections_components:
                if a==user or b==user:
                   connections_to_remove.append((a,b))
            
            for connection in connections_to_remove:
                self.__connections_components.remove(connection)
                number_of_delete += 1
            self.number_of_connections -= number_of_delete        
        


        
    #This is a function to add an edge between 2 nodes in the graph  
    def add_connection(self, userF:int, userS:int)->None:
        '''
        This is a method at the instance level, that takes 2 users of class User as arguuents
        and build a directed edge from userF to userS
        '''

        #first we have to check if there are any connection from userF to userS
        if  userS in self.nodes_list and userF in self.nodes_list and userS not in self.__requests_list[userF] and userF != userS:

            #we add userS to the value list in the adj-list dictionary
            self.__requests_list[userF].append(userS)

            #we append a tuple of the new connected pairs to the connections matrix
            self.__connections_components.append((userF, userS))

            #increment the number of connections by 1
            self.number_of_connections += 1

            #apply the request method from class User to perform all the needed updation to the user profile and data
            User.request(userF, userS)

    

    #This is a function to remove an edge between two nodes in the graph    
    def cancel_request(self, userF:int, userS:int)->None:
        '''
        This is a method at the instance level, that takes 2 users of class User as arguuents
        and break a directed edge from userF to userS        
        '''

        #first we have to check if there is an edge between these 2 nodes directed from userF to userS
        if userS in self.nodes_list and userF in self.nodes_list and  userS in self.__requests_list[userF]:

            #we remove userS from the value list of userF in the adj-list dictionary
            self.__requests_list[userF].remove(userS)

            #we remove the tuple of connection directed from userF to userS from the connection  matrix
            self.__connections_components.remove((userF, userS))

            #we decrement the number of edges in this graph by 1
            self.number_of_connections -= 1

            #we apply the cancel_request method from class User to update the users profiles and data
            User.cancel_request(userF, userS)        
      


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
    

    
    def check_connection(self, userF:int, userS:int):
        if userF in self.nodes_list and userS in self.nodes_list:
            res = []
            for connection in self.get_connections_components():
                a, b = connection
               
                if (a==userF and b==userS):
                    res.append(True)
                res.append(False)
            if True in res: return True
            else: return False        
            

    def get_weight(self, userF:int, userS:int):
        weight = 0
        for connection in self.__connections_components:           
            a, b = connection
            if (userF == a) and (userS==b):
                c= User.USER_DATA[a]
                d = User.USER_DATA[b]

                if c['user name'] == d['user name']:
                   weight += 1
                if c['gender']==d['gender']:
                    weight += 1
                if c['age'] == d['age']:
                    weight += 1
                if c['experience']== d['experience']:
                    weight += 1
                if c['In need for help'] == d["Ready to help"]:
                    weight += 1
                for company in c["companies"] :
                    if company in d["companies"]:
                        weight += 1
                for pl in c["programming langs"]:
                    if pl in d["programming langs"]:
                        weight += 1 
                     
        return weight       

                         


    def neighbors_weights_dict(self)->dict:
        res = {}
        for k, vl in self.__requests_list.items():
            if vl:
               res[k] = {v:(self.get_weight(k, v)) for v in vl}
        return res    
    
           



    def get_weighted_connections(self)->list:
        
        lst = []
        for connection in self.__connections_components:
           
            weight = 0
            
            a, b = connection
            c= User.USER_DATA[a]
            d = User.USER_DATA[b]

            if c['user name'] == d['user name']:
                weight += 1
            if c['gender']==d['gender']:
                weight += 1
            if c['age'] == d['age']:
                weight += 1
            if c['experience']== d['experience']:
                weight += 1
            if c['In need for help'] == d["Ready to help"]:
                weight += 1
            for company in c["companies"] :
                if company in d["companies"]:
                    weight += 1
            for pl in c["programming langs"]:
                if pl in d["programming langs"]:
                    weight += 1           
                   
                

        
            lst.append((a, b, weight))
        return lst   
    

    def get_recommendation(self, user:int)->list:
        res =[]
       

        a  =user
        for u in self.nodes_list:
            if u!= a:
                weight =0
                d1 = User.USER_DATA[a]
                d2 = User.USER_DATA[u]
                if d1['user name'] == d2['user name']:
                    weight += 1
                if d1['gender']==d2['gender']:
                    weight += 1
                if d1['age'] == d2['age']:
                    weight += 1
                if d1['experience']== d2['experience']:
                    weight += 1
                if d1['In need for help'] == d2["Ready to help"]:
                    weight += 1
                for company in d1["companies"] :
                    if company in d2["companies"]:
                       weight += 1
                for pl in d1["programming langs"]:
                    if pl in d2["programming langs"]:
                       weight += 1  
                if weight >= 4:
                    res.append(u)
        return res                         


    

    def get_connections_by_names(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            
            a = User.USER_DATA[a]["user name"]+'('+str(a)+')'
            b = User.USER_DATA[b]["user name"]+'('+str(b)+')'
            lst.append((a, b))
        return lst    
    

    def get_connections_by_companies(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(User.USER_DATA[a]['companies'])+str(a)
            b = str(User.USER_DATA[b]['companies'])+str(b)
            lst.append((a, b))
        return lst  

    def get_connections_by_pl(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(User.USER_DATA[a]['programming langs'])+str(a)
            b = str(User.USER_DATA[b]["programming langs"])+str(b)
            lst.append((a, b)) 
        return lst    

    def get_connections_by_exp(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(a)+':'+str(User.USER_DATA[a]["experience"])
            b = str(b)+':'+str(User.USER_DATA[b]["experience"])
            lst.append((a, b)) 
        return lst  
        
    def get_components_by_age(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(a)+':'+str(User.USER_DATA[a]["age"])
            b = str(b)+':'+str(User.USER_DATA[b]["age"])
            lst.append((a, b)) 
        return lst  
    
    def get_components_by_degree(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(a)+':'+str(User.USER_DATA[a]["number of requests"]+User.USER_DATA[a]["number of people requested this user"])
            b = str(b)+':'+str(User.USER_DATA[b]["number of requests"]+User.USER_DATA[b]["number of people requested this user"])
            lst.append((a, b)) 
        return lst 

    def get_components_by_indegrees(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(a)+':'+str(User.USER_DATA[a]["number of people requested this user"])
            b = str(b)+':'+str(User.USER_DATA[b]["number of people requested this user"])
            lst.append((a, b)) 
        return lst 
    
    def get_components_by_outdegrees(self):
        lst = []
        for connection in self.get_connections_components():
            a, b = connection
            a = str(a)+':'+str(User.USER_DATA[a]["number of requests"])
            b = str(b)+':'+str(User.USER_DATA[b]["number of requests"])
            lst.append((a, b)) 
        return lst 







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
        for u in self.nodes_list:
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
            degrees.append((u, {'degree:': (len(v)+User.USER_DATA[u]["number of people requested this user"])}))
        return degrees  
    


    #This is a function to get the percentage of ppl who are ready to help
    def helpful_percentage(self)->float:
        '''
        This method is at class level, it takes no arguments,
        it simply prints out the percentage of coders who are welling to help     
        '''  
        summ = 0
        for u in self.nodes_list:
            if User.USER_DATA[u]['Ready to help']==True:
                summ += 1
                
        percentage = ((summ/self.__number_of_nodes)*100)
        rounded = round(percentage, 2)
        unhelpful = round((100 - rounded), 2)
        return [rounded, unhelpful]  




    #This is  a function to get the percentage of people who are in need for help
    def needy_percentage(self)->float:
        '''
        This method is at class level, it takes no arguments,
        it simply prints out the percentage of coders who are in need for 
        other coders help          
        '''
        summ = 0
        for u in self.nodes_list:
            if User.USER_DATA[u]["In need for help"]==True:
                summ+= 1


        percentage = ((summ/self.__number_of_nodes)*100)
        rounded = round(percentage, 2)
        not_needy = round((100 - rounded), 2)
        return [rounded, not_needy]




    
    #This is a function to get the percentage of users sorted by gender
    def gender_percentage(self)->float:
        '''
        This is a function of the class that takes no arguments and it returns the 
        percentsge of users' genders in the program        
        '''         
        sumf = 0
        for  u in self.nodes_list:
            if User.USER_DATA[u]["gender"]=='female':
                sumf += 1

        percentage_females = (sumf / self.__number_of_nodes* 100)
        roundedf = round(percentage_females, 2)
        percentage_males = 100 - percentage_females
        roundedm = round(percentage_males, 2)

        return [roundedf, roundedm]
    


     #This is a function to get the average age of the users
    def average_age(self)->float:
        '''
        This methaod is at class level ,it takes no arguments,
        it simply print out the average age of users      
        '''
        age_list = []
        for u in self.nodes_list:
            age_list.append(User.USER_DATA[u]["age"])

        average = sum(age_list)/self.__number_of_nodes
        rounded = round(average, 2)
        return rounded









    #This is a function to get the average experience of the users
    def average_experience(self)->float:
        '''
        This methaod is at class level ,it takes no arguments,
        it simply print out the average experience of users        
        '''
        experience = []
        for u in self.nodes_list:
            experience.append(User.USER_DATA[u]["experience"])
        average = sum(experience)/self.__number_of_nodes
        rounded = round(average, 2)
        return rounded



    #This is a function to get the density of the graph
    def density(self)->float:
        '''
        This is a method at the level of instance, that takes no arguments 
        and it calculate th edensity of a graph
        '''
        d = round((self.number_of_connections) /((self.__number_of_nodes) *(self.__number_of_nodes-1)), 3)
        return [d]
    
    

    #This is a function to sort the users by their age
    def sort_by_age(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns the ages as keys and users in  a list
        '''

        #first store teh user number as a key and the age as a value
        age_map = {}
        for u in self.nodes_list:
            age_map[u]=User.USER_DATA[u]["age"]

        #we use defaultdict inorder  to ensure that certain keys always have a default value -list-, even if they haven't been explicitly set yet.   
        age_store = defaultdict(list)

        #set values as keys and append keys of same values to the same list
        for key, value in  age_map.items():
            age_store[value].append(key)
        return age_store 

    

    #This is  a function to sort the users by their experience
    def sort_by_experience(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns the experiences  as keys and users in  a list
        '''
        exp_map = {}
        for u in self.nodes_list:
            exp_map[u]=User.USER_DATA[u]["experience"]   
        exp_store = defaultdict(list)
        for key, value in exp_map.items():
            exp_store[value].append(key)
        return exp_store       
    



    #This is a funcrtion to sort the users by their followers
    def sort_by_followers(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns the number of followers  as keys and users in  a list
        '''
        requested_by_map = {}
        for u in self.nodes_list:
            requested_by_map[u]=User.USER_DATA[u]["number of people requested this user"]
        followers_nbr_store = defaultdict(list)
        for key , value in requested_by_map.items():
            followers_nbr_store[value].append(key)
        return followers_nbr_store  
    



    #this is a funcrtion to sort the users by their followings
    def sort_by_followings(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns the number of followings  as keys and users in  a list
        '''
        request_map ={}
        for u in self.nodes_list:
            request_map[u]=User.USER_DATA[u]["number of requests"]   
        following_nbr = defaultdict(list)
        for key, value in request_map.items():
            following_nbr[value].append(key)      
        return following_nbr 
         
    

    #This is a funcrtion to sort the users by their user names
    def sort_by_user_name(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns their names  as keys and users in  a list
        '''
        names_map = {}
        for u in self.nodes_list:
            names_map[u] = User.USER_DATA[u]["user name"]
        sort_by_name = defaultdict(list)
        for key, value in names_map.items():
            sort_by_name[value].append(key)
        return sort_by_name
    


    #This is a funcrtion to sort the users by their readiness to help
    def sort_by_readiness(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns their readiness to help  as keys and users in  a list
        '''
        readiness_map ={}
        for u in self.nodes_list:
            readiness_map[u]=User.USER_DATA[u]['Ready to help']
        readiness_sort =defaultdict(list)
        for key, value in readiness_map.items():
            readiness_sort[value].append(key)
        return readiness_sort       
    


    #This is a funcrtion to sort the users by their need for help
    def sort_by_need(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns their need for  help  as keys and users in  a list
        '''
        need_map = {}
        for u in self.nodes_list:
            need_map[u] = User.USER_DATA[u]["In need for help"]
        needy_sort  = defaultdict(list)
        for key , value in need_map.items():
            needy_sort[value].append(key)
        return needy_sort  
        


    #This is a funcrtion to sort the users by the companies they work for
    def sort_by_companies(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns the companies that they work at as keys and users in  a list
        '''
        companies_map ={}
        for u in self.nodes_list:
            companies_map[u]=User.USER_DATA[u]["companies"]
        companies_sort = {}
        for key, value in companies_map.items():
            for v in value:
                #here we use setdefault method to set default values to the keys even before defining them
                companies_sort.setdefault(v, []).append(key)
        return companies_sort  



    #This is a funcrtion to sort the users by their genders
    def sort_by_gender(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns their gender as keys and users in  a list
        '''

        gender_map = {}
        for u in self.nodes_list:
            gender_map[u]=User.USER_DATA[u]["gender"]
        sort_by_gender = defaultdict(list)
        for key, value in gender_map.items():
            sort_by_gender[value].append(key)
        return sort_by_gender 
              



    #This is a funcrtion to sort the users by their programming languages
    def sort_by_prog_lang(self)->dict:
        '''
        This is a method at the level of instance that takes no arguments
        and returns their programming languages as keys and users in  a list
        '''
        prog_lang_map ={}
        for u in self.nodes_list:
            prog_lang_map[u]=User.USER_DATA[u]["programming langs"]
        sorting_by_pl = {}
        for key, value in prog_lang_map.items():
            for v in value:
                sorting_by_pl.setdefault(v, []).append(key)
        return sorting_by_pl  
    
    

   #This is a function to check the users who have the given name
    def check_user_name(self, name:str)->list:
        '''
        This is a method at the level of instance, that takes 1 string 
        argument and return a ist of users' numbers who have the same name
        '''
        #we call the sort_by_name function to get all the names as keys and users as values 
        sort_by_name = self.sort_by_user_name()
        for key in sort_by_name.keys():
            if key.lower() == name.lower():
                return sort_by_name[key]

         

    #This is a function to check the users who have the given age     
    def check_age(self, age:int)->list:
        '''
        This is a method at the level of instance, that takes 1 integer 
        argument and return a ist of users' numbers who have the same age
        '''

        d =self.sort_by_age()
        for key in d.keys():
            if key == age:
                return d[key]
            
           

    #This is a function to check the users who have the given experience
    def check_experience(self, exp:int)->list:
        '''
        This is a method at the level of instance, that takes 1 integer 
        argument and return a ist of users' numbers who have the same experience
        '''

        d = self.sort_by_experience()
        for key in d.keys():
            if key == exp:
                return d[key]


    #This is a function to check the users who have the given status(readiness)
    def check_status(self, ready=True)->list:
        '''
        This is a method at the level of instance, that takes 1 boolean 
        argument and return a ist of users' numbers who have the same readiness
        '''

        d = self.sort_by_readiness() 
        for key in d.keys():
            if key == ready:
                return d[key]                      
    


    #This is a function to check the users who have the given status(need)
    def check_needys(self, needy=True)->list:
        '''
        This is a method at the level of instance, that takes 1 boolean 
        argument and return a ist of users' numbers who have the same need
        '''

        d = self.sort_by_need()
        for key in d.keys():
            if key == needy:
                return d[key]
            

    #This is a function to check the users who work at the given company
    def check_company(self, comp:str)->list:
        '''
        This is a method at the level of instance, that takes 1 boolean 
        argument and return a ist of users' numbers who work at the same company
        '''
        d = self.sort_by_companies()
        for key in d.keys():
            if key.lower()==comp.lower():
                return d[key] 

            

    #This is a function to check the users who have the given programming language
    def check_prog_lang(self, pl:str)->list:
        '''
        This is a method at the level of instance, that takes 1 string
        argument and return a ist of users' numbers who have the same programming language
        '''

        d = self.sort_by_prog_lang()
        for key in d.keys():
            if key.lower() == pl.lower():
                return d[key]   



    #This is a function to check the users who have the given gender
    def check_gender(self, g:str)->list:
        '''
        This is a method at the level of instance, that takes 1 string
        argument and return a ist of users' numbers who have the same gender
        '''

        d = self.sort_by_gender()
        for key in d.keys():
            if key.lower() == g.lower():
                return d[key]

     #This is a function to print out all the graph data
    def get_garph_data(self):
        print(f"The number of users in this graph is : {self.__number_of_nodes}\nThe requests list is :{self.__requests_list}\nThe users in this class are: {self.nodes_list}\nThe number of connections in this garph is : {self.number_of_connections}\nThe connections in this graph are:{self.__connections_components}")

        
            





   #This is a new class to visualize the graphs and the statistical studies of the network
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from heapq import heapify, heappop, heappush
import sys



def Dijkstra( graph:Graph, start, target):
    g= graph.neighbors_weights_dict()
    inf = sys.maxsize
    node_data = {n:{'cost':inf, 'pred':[]} for n in graph.nodes_list}
    node_data[start]['cost']= 0
    min_heap = []
    heappush(min_heap, (0, start))
    visited = set()
    while min_heap:
        current_cost, temp = heappop(min_heap)

        if temp not in visited:
            visited.add(temp)
            for j in g.get(temp, {}):
                if j not in visited:
                    cost  = node_data[temp]['cost'] + g[temp][j]
                    if cost <  node_data[j]['cost']:
                        node_data[j]['cost'] = cost 
                        node_data[j]['pred'] = node_data[temp]['pred']+ [temp]
                        heappush(min_heap, (cost, j))

    return (node_data[target]['pred']  + [target] , node_data[target]['cost'])   


def BFS(graph, start_node, target, visited):
    visited= set([start_node])
    q = [start_node]
    order = []

    while q:
        vertex = q.pop(0)
        order.append(vertex)
        if vertex ==target:
            return order

        for node in graph[vertex]:
            if node not in visited:
                visited.add(node)
                q.append(node)
    return [target]


class Visualize:
    
    def by_age(self, title, graph:Graph):
        self.title= title 
        G = nx.DiGraph()
        age = [str(u)+':'+str(User.USER_DATA[u]["age"]) for u in graph.nodes_list]
        G.add_nodes_from(age)
        G.add_edges_from(graph.get_components_by_age())
        seed = 42
        lay_out = nx.spring_layout(G, seed)
        self.age = {user : User.USER_DATA[user]["age"] for user in graph.nodes_list}
        nodes_sizes = [3+ 10*self.age[user] for user in graph.nodes_list]   
        plt.figure()
        plt.title(title) 
        nx.draw(G,with_labels =True,pos = lay_out, node_size = nodes_sizes, node_color = 'pink', font_color = 'indigo', width = 1, font_size=4 )
       
        plt.show() 



    def by_gender(self, title, graph:Graph):    
        self.title = title
        G = nx.DiGraph()
        self.lst =[]
        self.colors =[]
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        seed = 42
        lay_out = nx.spring_layout(G, seed)
        for u in graph.nodes_list:
            self.lst.append((u, {'gender':User.USER_DATA[u]['gender']}))

        color_map = {'female':'pink', 'male':'lightblue'}  

        self.colors = [color_map[node_data["gender"]] for _, node_data in self.lst]
        plt.figure()
        plt.title(title) 
        nx.draw(G, with_labels=True,pos = lay_out, node_color = self.colors, node_size=500, width = 1, font_size= 6, font_color = 'indigo')
        plt.show()


    def by_experience(self, title, graph:Graph):
        self.title= title 
        G = nx.DiGraph()
        exp = [str(u)+':'+str(User.USER_DATA[u]["experience"]) for u in graph.nodes_list]
        G.add_nodes_from(exp)
        G.add_edges_from(graph.get_connections_by_exp())
        seed = 42
        lay_out = nx.spring_layout(G, seed)
        self.exp = {user : User.USER_DATA[user]["experience"] for user in graph.nodes_list}
        nodes_sizes = [100+ 10*self.exp[user] for user in graph.nodes_list] 
        plt.figure()
        plt.title(title) 
        nx.draw(G,with_labels =True,pos = lay_out, node_size = nodes_sizes, node_color = 'pink', font_color = 'indigo', width = 1, font_size=4 )
        
        plt.show()
    


    def by_user_name(self, title, graph:Graph):
        self.title = title
        G = nx.DiGraph()
        names = [User.USER_DATA[u]["user name"]+'('+str(u)+')' for u in graph.nodes_list]
        G.add_nodes_from(names)
        G.add_edges_from(graph.get_connections_by_names())
        layout = nx.spring_layout(G, 42)

        plt.figure()
        plt.title(title)
        nx.draw(G, with_labels= True, pos = layout, node_color = 'lightblue', node_size = 500, font_size = 4, font_color = 'indigo', width = 1)
       
        plt.show()


    def by_companies(self, title, graph:Graph): 
        self.title = title
        G = nx.DiGraph()
        companies = [str(User.USER_DATA[u]['companies'])+str(u) for u in graph.nodes_list]
        G.add_nodes_from(companies)
        edges = [(u, v) for (u, v) in graph.get_connections_by_companies() if u != v]
        G.add_edges_from(edges)
        ''' G .add_edges_from(graph.get_connections_by_companies())'''
        layout = nx.spring_layout(G, 42)
        plt.figure()
        plt.title(title)
        nx.draw(G, with_labels = True, pos = layout, node_size = 500, node_color = 'lightgreen', font_size = 6, font_color = 'indigo', width = 1 )   
        
        plt.show()


    def by_pl(self, title, graph:Graph):
        self.title = title
        G = nx.DiGraph()
        pl = [str(User.USER_DATA[u]["programming langs"])+str(u) for u in graph.nodes_list] 
        G.add_nodes_from(pl)
        G.add_edges_from(graph.get_connections_by_pl())
        layout = nx.spring_layout(G, 42)
        plt.figure()
        plt.title(title)
        nx.draw(G, pos = layout, with_labels = True, node_size = 500, node_color = 'pink', font_size = 4, font_color = 'indigo', width = 1)
        
        plt.show()  

    def by_readiness(self, title, graph:Graph):
        self.title = title
        G = nx.DiGraph()
        
        self.colors =[]
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        layout = nx.spring_layout(G, 42)
        self.lst = [(u,{'readiness': User.USER_DATA[u]['Ready to help']}) for u in graph.nodes_list]
        color_map = {True: 'lightgreen', False:'grey'}
        self.colors = [color_map[node_data['readiness']] for _, node_data in self.lst]
        plt.figure()
        plt.title(title)
        nx.draw(G, pos=layout, with_labels=True, node_size=500, node_color=self.colors, font_size = 8, font_color ="white", width = 1)
        
        plt.show()

    def by_need(self, title, graph:Graph): 
        self.title = title
        G = nx.DiGraph()
        
        self.colors =[]
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        layout = nx.spring_layout(G, 42)
        self.lst = [(u,{'need': User.USER_DATA[u]['In need for help']}) for u in graph.nodes_list]
        color_map = {True: 'yellow', False:'grey'}
        self.colors = [color_map[node_data['need']] for _, node_data in self.lst]
        plt.figure()
        plt.title(title)
        nx.draw(G, pos=layout, with_labels=True, node_size=500, node_color=self.colors, font_size = 8, font_color ="black", width = 1)
        
        plt.show()
    

    def by_degree(self, title, graph:Graph):
        self.title= title 
        G = nx.DiGraph()
        degree= [str(u)+':'+str(User.USER_DATA[u]["number of requests"]+User.USER_DATA[u]["number of people requested this user"]) for u in graph.nodes_list]
        G.add_nodes_from(degree)
        G.add_edges_from(graph.get_components_by_degree())
        seed = 42
        lay_out = nx.spring_layout(G, seed)
        self.deg = {user : User.USER_DATA[user]['number of requests']+User.USER_DATA[user]["number of people requested this user"] for user in graph.nodes_list}
        nodes_sizes = [50+ 200*self.deg[user] for user in graph.nodes_list] 
        plt.figure()
        plt.title(title) 
        nx.draw(G,with_labels =True,pos = lay_out, node_size = nodes_sizes, node_color = 'orange', font_color = 'indigo', width = 1, font_size=4 )
        
        plt.show()


    def by_in_degrees(self, title, graph:Graph):   
        self.title= title 
        G = nx.DiGraph()
        indegree= [str(u)+':'+str(User.USER_DATA[u]["number of people requested this user"]) for u in graph.nodes_list]
        G.add_nodes_from(indegree)
        G.add_edges_from(graph.get_components_by_indegrees())
        seed = 42
        lay_out = nx.spring_layout(G, seed)
        self.ind = {user : User.USER_DATA[user]["number of people requested this user"] for user in graph.nodes_list}
        nodes_sizes = [50+ 100*self.ind[user] for user in graph.nodes_list] 
        plt.figure()
        plt.title(title) 
        nx.draw(G,with_labels =True,pos = lay_out, node_size = nodes_sizes, node_color = 'lightgreen', font_color = 'black', width = 1, font_size=4 )
        
        plt.show() 

    def by_out_degrees(self, title, graph:Graph):
        self.title= title 
        G = nx.DiGraph()
        outdegree= [str(u)+':'+str(User.USER_DATA[u]["number of requests"]) for u in graph.nodes_list]
        G.add_nodes_from(outdegree)
        G.add_edges_from(graph.get_components_by_outdegrees())
        seed = 42
        lay_out = nx.spring_layout(G, seed)
        self.outd = {user : User.USER_DATA[user]["number of requests"] for user in graph.nodes_list}
        nodes_sizes = [50+ 100*self.outd[user] for user in graph.nodes_list] 
        plt.figure()
        plt.title(title) 
        nx.draw(G,with_labels =True,pos = lay_out, node_size = nodes_sizes, node_color = 'pink', font_color = 'black', width = 1, font_size=4 )
        
        plt.show() 



    def search_user_BFS(self, title, graph:Graph,start,  target):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        pos = nx.spring_layout(G, 42)
        plt.figure()
        plt.title(title)
        
        order = BFS(G,start,  target, set())
        for i, node in enumerate(order, start=1):
            plt.clf()
            plt.title(title)
            nx.draw(G, pos=pos, node_size= 100, node_color=['yellow' if n==node else 'grey' for n in G.nodes], with_labels= True, width = 0.5)
            plt.draw()
            plt.pause(1.5)
        plt.show()
        time.sleep(1.5)  




    def search_user(self, title, graph:Graph, target:list[int]):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        pos = nx.spring_layout(G, 42)
        plt.figure()
        plt.title(title)
        color_map = {node: 'yellow' if node in target else 'grey' for node in G.nodes}
        colors = [color_map[node] for node in G.nodes]     
        nx.draw(G, pos = pos, with_labels = True, node_size = 100, node_color = colors)
        plt.show()


    def search_user_name(self, title, graph:Graph, target:str):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        if  graph.check_user_name(target):
            order = graph.check_user_name(target)
        else:
            order = []    
        plt.figure()
        plt.title(title)
        pos = nx.spring_layout(G, 42)
        color_map = {node :'yellow' if node in order else 'grey' for node in G.nodes}
        colors = [color_map[node] for node in G.nodes]
        nx.draw(G, pos = pos, with_labels = True, node_color = colors, node_size = 200, width = 0.5)
        plt.show()


    def search_user_age(self, title, graph:Graph, target:int):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        if  graph.check_age(target):
            order = graph.check_age(target)
        else:
            order = []    
        plt.figure()
        plt.title(title)
        pos = nx.spring_layout(G, 42)
        color_map = {node :'yellow' if node in order else 'grey' for node in G.nodes}
        colors = [color_map[node] for node in G.nodes]
        nx.draw(G, pos = pos, with_labels = True, node_color = colors, node_size = 200, width = 0.5)
        plt.show()
    


    def search_user_company(self, title, graph:Graph, target:str):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        if  graph.check_company(target):
            order = graph.check_company(target)
        else:
            order = []    
        plt.figure()
        plt.title(title)
        pos = nx.spring_layout(G, 42)
        color_map = {node :'yellow' if node in order else 'grey' for node in G.nodes}
        colors = [color_map[node] for node in G.nodes]
        nx.draw(G, pos = pos, with_labels = True, node_color = colors, node_size = 200, width = 0.5)
        plt.show()


    def search_user_experience(self, title, graph:Graph, target:int):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        if  graph.check_experience(target):
            order = graph.check_experience(target)
        else:
            order = []    
        plt.figure()
        plt.title(title)
        pos = nx.spring_layout(G, 42)
        color_map = {node :'yellow' if node in order else 'grey' for node in G.nodes}
        colors = [color_map[node] for node in G.nodes]
        nx.draw(G, pos = pos, with_labels = True, node_color = colors, node_size = 200, width = 0.5)
        plt.show()
    


    def search_user_prog_lang(self, title, graph:Graph, target:str):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)
        G.add_edges_from(graph.get_connections_components())
        if  graph.check_prog_lang(target):
            order = graph.check_prog_lang(target)
        else:
            order = []    
        plt.figure()
        plt.title(title)
        pos = nx.spring_layout(G, 42)
        color_map = {node :'yellow' if node in order else 'grey' for node in G.nodes}
        colors = [color_map[node] for node in G.nodes]
        nx.draw(G, pos = pos, with_labels = True, node_color = colors, node_size = 200, width = 0.5)
        plt.show()



    def get_weighted(self, title, graph:Graph):
        G = nx.DiGraph()
        G.add_nodes_from(graph.nodes_list)  
        
        G.add_edges_from(graph.get_connections_components())
        edges = graph.get_weighted_connections()
        weights =  np.array([edge[2] for edge in edges] )
        norm = plt.Normalize(weights.min(), weights.max())
        cmap = cm.coolwarm
        edge_colors = [cmap(norm(weight)) for weight in weights]
    
        
        plt.figure(figsize=(3, 4))
        pos = nx.spring_layout(G, 42)
        nx.draw(G, pos = pos, with_labels = True, node_color = 'red', node_size = 60, width = 1, edge_color = edge_colors , font_size = 3, font_color = 'white', font_weight ='bold')
        sm = plt.cm.ScalarMappable(cmap = cmap, norm = norm)
        ax = plt.gca()
        ax.set_axis_off()
        plt.colorbar(sm, ax = ax)
        plt.title(title)
        plt.show()


    def get_gender_percentage(self, title, graph:Graph):
        genders = ['females', 'males']
        percentages = graph.gender_percentage()
        plot = plt.bar(x = genders, height = percentages, color =('pink', 'lightblue'), ec ='lightgray')
        plt.bar_label(plot, labels = percentages, label_type = 'edge', padding = 3)
        plt.ylim([0, 100])
        plt.title(title)
        plt.xlabel('gender')
        plt.ylabel('percentage')
        plt.show()

    def get_users_activity(self, title, graph:Graph):
        status = ['Ready to help', 'Not Ready to help']
        percentage = graph.helpful_percentage()
        plot = plt.bar(x = status, height = percentage, color =('yellow', 'grey'), ec ='black')
        plt.bar_label(plot, labels = percentage, label_type = 'edge', padding = 3)
        plt.ylim([0, 100])
        plt.title(title)
        plt.xlabel('user\'s activity')
        plt.ylabel('percentage')
        plt.show()

    def get_users_status(self, title, graph:Graph):
        status = ['In need', 'Not in need']
        percentage = graph.needy_percentage()
        plot = plt.bar(x = status, height = percentage, color =('yellow', 'grey'), ec ='black')
        plt.bar_label(plot, labels = percentage, label_type = 'edge', padding = 3)
        plt.ylim([0, 100])
        plt.title(title)
        plt.xlabel('user\'s status')
        plt.ylabel('percentage')
        plt.show()
    

    def get_graph_density(self, title, graph:Graph):
        status = ['density']
        percentage = graph.density()
        plot = plt.bar(x = status, height = percentage, color =('yellow'), ec ='black')
        plt.bar_label(plot, labels = percentage, label_type = 'edge', padding = 3)
        plt.ylim([0, 1])
        plt.title(title)
        plt.xlabel('graph')
        plt.ylabel('density')
        plt.show()


    def shortest_path(self, title, graph:Graph, start:int, target:int):
        s = start
        t = target
        path = Dijkstra(graph, s, t )
        self.search_user(title, graph, path[0])

    

    def average_age(self, title, graph:Graph):
        users = graph.nodes_list
        ages = [User.USER_DATA[u]["age"] for u in users]
        av = graph.average_age()
        plt.figure(figsize = (10, 6))
       
        plt.scatter(users, ages, color = 'blue', linestyle ='--', alpha = 0.6, zorder = 1)
        plt.axhline(y=av, color = 'red', linestyle = '-', label = f"average({av})", zorder = 0)
        plt.xlabel('users')
        plt.ylabel('ages')
        plt.title(title)
        plt.legend()
        plt.show()

    def average_experience(self, title, graph:Graph):
        users = graph.nodes_list
        experiences = [User.USER_DATA[u]["experience"] for u in users]
        av = graph.average_experience()
        plt.figure(figsize = (8, 6))
       
        plt.scatter(users, experiences, color = 'blue', linestyle ='--', alpha = 0.6, zorder = 1)
        plt.axhline(y=av, color = 'red', linestyle = '-', label = f"average({av})", zorder = 0)
        plt.xlabel('users')
        plt.ylabel('experiences')
        plt.title(title)
        plt.legend()
        plt.show()


    def get_recommendation(self, title, graph:Graph, user:int):
        recommended = graph.get_recommendation(user)
        self.search_user(title, graph, recommended)





        

def main():
    i = int(input("Hello to my coder world Analytic Program!\nHere you can visualize and get all sorts of needed inforamtion about your users and program\nTo start enter the number of your users: "))

    menu1 =''''
    if you want to update user's profiles or get any thing related to them type: 'user'
    if yu want to work with graph, to add and remove edges and nodes, type : 'graph'
    if you want to visualize any feature type: 'visualize' 
    if you want tpo exit type : 'exit
    ''' 


    menu2 ='''
    you chose user:

    to get setters enter : A 
    -to update user name : A/1
    -to update user age : A/2
    -to update user exp : A/3
    -to add company : A/4
    -to remove company : A/5
    -to add programming language : A/6
    -to remove programming language : A/7
    -to update status of need : A/8
    -to update activity (readiness to help): A/9

    to get data enter : B
    -to get user name: B/1
    -to get user age :B/2
    -to get user gender : B/3
    -to get user companies: B/4
    -to get user experience : B/5
    -to get user status of need :B/6
    -to get user status of readiness: B/7
    -to get user followers : B/8
    -to get user followings : B/9
    -to get the user number of followings : B/10
    -to get the users's number of followers : B/11
    -to get all the users data : users
    '''

    menu3= '''
    you chose graph: 

    To add users to the graph: 1
    To remove users from the graph : 2
    To add connections between 2 users : 3
    To remove connection between 2 users : 4
    To get the number of edges : 5
    To get the connections components : 6
    To get weighted connections of users : 7
    To check a connection between 2 users : 8
    To find the shortest path between 2 users : 9
    To find users who share same name: 10
    To find users who share same age : 11
    To find users who share same experience: 12
    To find users who share same gender : 13
    To find users who share same company : 14
    To find users who share same programming language : 15
    To find users who are ready to help : 16
    To find users who are in need for help : 17
    To get indegrees : 18
    To get out degrees : 19
    To get degrees : 20
    To get the graph data : data
    '''


    menu4='''
    you chose visualize:

    To Show ages : 1
    To show genders : 2
    To show experience : 3
    To show users names : 4
    To show companies : 5
    To show programming languages : 6
    To show users activities : 7
    To show users status: 8
    To show users degrees : 9
    To show users in degrees : 10
    To show users out degrees : 11
    To search uers by BFS : 12
    To search users : 13
    To search user name : 14
    To search users age : 15
    To search company = 16
    To search an experience : 17
    To search user programming language : 18
    To get weighted graph ; 19
    To get gender percentages : 20
    To get users activities percentages: 21
    To get iusers status percentages : 22
    To get the density of the graph : 23
    To show the shortest path : 24
    To get the average age : 25
    To get the average experiece : 26
    To get recommendations : 27
    '''

    while i>0:
        name =input("Enter your user name: ").strip()
        age = int(input("Enter your user age: ").strip())
        exp= int(input('exp: '))
        g = input('gender : ').strip()
        comp = input("companies separated by (,): ").split(',')
        pl = input("prog langs separated by (,): ").split(',')
        ready = input('enter (yes/no) if ready or not: ').strip().lower()
        needy = input('enter (yes/no) if needy or not: ').strip().lower()
        if ready == 'yes': act=True
        else: act=False
        if needy =='yes' : st = True
        else: st= False
        companies = set()
        prog_lang = set()
        for c in comp:
            companies.add(c)
        for l in pl:
            prog_lang.add(l)

           
        user = User(name, age, companies, exp,g, prog_lang,act , st )
        i -= 1
    r = int(input('to get the data of any of your users enter the number of the user you want to check, if you do not want pass 0: '))
    if r ==0 :
        pass

    if r:
        print(User.USER_DATA[r])  
    print(menu1)
    i = input('Choose where you want to work: ').strip().lower()
    if not i:
        return
    while i=='user' and i!= 'exit':
        print(menu2)
        choice = input('enter your choice: ')
        if choice == 'A/1':
            name = input('enter the new user name: ').lower()
            user = int(input('enter the user number: '))
            User.set_user_name(user, name)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower()    

        if choice =='A/2':
            age = int(input('enter the new age : '))
            user =int(input('enter the number of user: '))
            User.set_age(user, age)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 'A/3':
            exp = int(input('enter the new experience: '))
            user = int(input('enter the number of user: '))
            User.set_experience(user, exp)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'A/4':
            comp = input('enter the company you want to add: ').lower()
            user = int(input('enter the number of user: '))
            User.add_companies(user, comp)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower() 

        if choice =='A/5':
            comp = input('enter the name of company you want to remove: ')
            user = int(input('enter the number of user: '))
            User.remove_companies(user, comp)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower() 

        if choice =='A/6': 
            pl = input('enter the programming language you want to add: ').lower()
            user = int(input('ente the number of user: '))
            User.add_prog_lang(user, pl)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 'A/7':
            pl = input('enter the programming language you want to remove: ').lower()
            user = int(input('ente the number of user: '))
            User.remove_prog_lang(user, pl)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 'A/8':
            need = input('enter the new status of the user(true/false): ').strip().lower()
            user = int(input('enter the number of the user: '))
            if need == 'true':
                st  = True
            else:
                st = False
            User.set_needy(user, st)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower() 


        if choice =='A/9':
            ready = input('enter the new activity of your user(true/false): ').strip().lower()
            user = int(input('enter the number of your user: '))
            if ready == 'true':
                act = True
            else:
                act = False
            User.set_ready(user, act)
            r = input('if you want to get the user updated data, print(yes), else:(no):').strip().lower()
            if r == 'yes': 
                print(User.USER_DATA[user])
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 'B/1':
            user = int(input('enter the nuber of your user: '))
            print(User.get_user_name(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/2': 
            user = int(input('enter the nuber of your user: '))
            print(User.get_age(user)) 
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/3':
            user = int(input('enter the nuber of your user: '))
            print(User.get_gender(user)) 
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/4':
            user = int(input('enter the nuber of your user: '))
            print(User.get_companies(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice =='B/5':
            user = int(input('enter the nuber of your user: '))
            print(User.get_experience(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/6':
            user = int(input('enter the nuber of your user: '))
            print(User.check_if_needy(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/7':
            user = int(input('enter the nuber of your user: '))
            print(User.check_if_ready(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/8':
            user = int(input('enter the nuber of your user: '))
            print(User.get_requested_by(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/9':
            user = int(input('enter the nuber of your user: '))
            print(User.get_requests(user)) 
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/10':
            user = int(input('enter the nuber of your user: '))
            print(User.get_number_of_requests(user))
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 'B/11':
            user = int(input('enter the nuber of your user: '))
            print(User.get_number_of_followers(user)) 
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 'users':
            print(User.USER_DATA)     

    graph = Graph()
    while i == 'graph' and i != 'exit' :
        
        print(menu3)
        choice = int(input('enter your choice: '))
        if choice == 1:
            user = int(input('Enter the number of user you want to add: '))
            graph.add_users(user)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 2:
            user = int(input('Enter the number of user you want to remove: '))
            graph.remove_user(user)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 3:
            user1 = int(input('Enter the number of the first user in the connection: '))
            user2 = int(input('Enter the number of the second user in the connection: '))
            graph.add_connection(user1, user2)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 4:
            user1 = int(input('Enter the number of the first user in the connection: '))
            user2 = int(input('Enter the number of the second user in the connection: '))
            graph.cancel_request(user1, user2)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 5:
            print(f"the number of edges in your graph is : {graph.number_of_connections}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 6:
            print(f"The connections components in your graph are as follows: {graph.get_connections_components()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 7:
            print(f"The connections with their weights in your graph are as follows: {graph.get_weighted_connections()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 8:
            user1 = int(input('Enter the number of the first user in the connection: '))
            user2 = int(input('Enter the number of the second user in the connection: '))
            print(graph.check_connection(user1, user2))
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 9:
            user1 = int(input('Enter the number of the first user in the connection: '))
            user2 = int(input('Enter the number of the second user in the connection: '))
            print(f"the shortest path and distance between these 2 users is : {Dijkstra(graph, user1, user2)}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 10:
            print(f"The users of your graph sorted by their names : {graph.sort_by_user_name()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 11:
            print(f"The users of your graph sorted by their ages : {graph.sort_by_age()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 12:
            print(f"The users of your graph sorted by their experience : {graph.sort_by_experience()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 13:
            print(f"The users of your graph sorted by their genders : {graph.sort_by_gender()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 14:
            print(f"The users of your graph sorted by their companies : {graph.sort_by_companies()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()  



        if choice == 15:
            print(f"The users of your graph sorted by their programming languages : {graph.sort_by_prog_lang()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 16:
            print(f"The users of your graph sorted by their readiness to help : {graph.sort_by_readiness()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 17:
            print(f"The users of your graph sorted by their need for help : {graph.sort_by_need()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 18:
            print(f"The users of your graph sorted by their indegrees : {graph.get_in_degrees()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 19:
            print(f"The users of your graph sorted by their out degrees : {graph.get_out_degrees()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()  

        if choice == 20:
            print(f"The users of your graph sorted by their degrees: {graph.get_degrees()}")
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()   



    G = Visualize()
    while i == 'visualize' and i!= 'exit':
        print(menu4)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            i = input('Choose where you want to work: ').strip().lower()
            G.by_age('users sorted by ages', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            


        if choice == 2: 
            G.by_gender('users sorted by their gender', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 3:
            G.by_experience('users sorted by experiences', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 4:
            G.by_user_name('users sorted by user name', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()


        if choice == 5:
            G.by_companies('users sorted by their companies', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 6:
            G.by_pl('users sorted by their programming languages', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 7:
            G.by_readiness('users sorted by their activity, colored ones are active', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if  choice == 8:
            G.by_need('users sorted by their need, colored ones are in need', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 



        if choice == 9:
            G.by_degree('The bigger node the highest degree', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 10:
            G.by_out_degrees('The bigger the node the higher out degree it has', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 11:
            G.by_in_degrees("The bigger the node the higher in degree it has", graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 12:
            start = int(input('enter the starting user for BFS: '))
            target = int(input('enter the targeted user by BFS; '))
            G.search_user_BFS('search a user by BFS', graph,start, target )
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 13:
            users0 = input('enter your users separated by commas: ')
            users1 = users0.split(',')
            users = [int(user) for user in users1.split(',')] 
            G.search_user('search a user or list of users', graph, users)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 
   
    
        if choice == 14:
            name = input('enter the name you are lokking for: ').strip().lower()
            G.search_user_name('the users with the searched user name', graph, name)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 15:
            age = int(input('enter the age you are looking for: '))
            G.search_user_age('the users of the search age', graph, age)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 16:
            comp = input('enter the company you are looking for: ').strip().lower()
            G.search_user_company('the users of the companies you are looking for', graph, comp)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 17:
            exp = int(input('enter the experience you are looking for: '))
            G.search_user_experience('the users of the experience you are looking for', graph, exp)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 18:
            pl = input('enter the programming language you are looking for: ').strip().lower()
            G.search_user_prog_lang('users of the searched programming language', graph, pl)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower()

        if choice == 19:
            G.get_weighted('the weighted graph', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 20:
            G.get_gender_percentage('The gender percentages', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 21:
            G.get_users_activity('the uers activity', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 
        

        if choice == 22:
            G.get_users_status('The users status', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 23:
            G.get_graph_density('The graph density', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

        if choice == 24:
            u1 = int(input('enter the first user: '))
            u2 = int(input('enter the second user: '))
            G.shortest_path('The shortest path',graph, u1, u2)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 25:
            G.average_age('The average age of users', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 

                
           


        if choice == 26:
            G.average_experience('The average experience of the users', graph)
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 


        if choice == 27:
            u = int(input('enter the user you want to get recommendation for: '))
            G.get_recommendation('the recommended users', graph, u) 
            r = input('if you want to get the graph data print(yes) else (no): ').strip().lower()
            if r == 'yes':
                print(graph.get_garph_data())
            i = input('Choose where you want to work: ').strip().lower() 
   
main()    
    
    
     


         
