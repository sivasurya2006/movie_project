import json
try:
    with open("movie.json","r") as file:
        movie=json.load(file)
except:
    movie=[]
    
while True:
    print("1.ADD_MOVIE:")
    print("2.VIEW_MOVIE:")
    print("3.SEARCH_MOVIES:")
    print("4.UPDATE_RATING:")
    print("5.DELETE_MOVIES:")
    print("6.SORTED_MOVIES:")
    print("7.SORTED_YEAR:")
    print("8.TOTAL_MOVIES:")
    print("9.VIEW.MOVIES_BY.GENRE")
    print("10.PREVENT.DUPLICATE.MOVIE")

    choice=int(input("ENTER THE CHOICE:"))

    if(choice==1):
        title=input("enter the movie name:")
        genre=input("enter the type of movie:")
        year=int(input("enter the year of movie:"))
        rating=float(input("enter the rating of movies:"))
        addmovie={
            "title":title,
            "genre":genre,
            "year":year,
            "rating":rating
            }
        movie.append(addmovie)

        with open("movie.json","w") as file:
            json.dump(movie,file,indent=4)

        print("movie added sucessfully:")

    elif(choice==2):
        with open("movie.json","r") as file:
            data=json.load(file)
            print(data)
    

    elif(choice==3):
       userinput=input("enter the movie name:")
       found=False
       for fck in movie:
           if(userinput == fck["title"]):
               print("yes movie founded")
               print(fck)
               found=True
               break
       else:
           print("MOVIE NOT FOUNDED :")

    elif(choice==4):
        usermoviename=input("enter the movie name")
        found=False
        for fck in movie:
            if(usermoviename == fck["title"]):
                    newrating=float(input("enter the rating:"))
                    fck["rating"]=newrating
                    print("RATING UPDATED SUCESSFULLY")
                    print(newrating)
                    with open("movie.json","w") as file:
                        json.dump(movie,file,indent=4)
                        found=True
                        break
        else :
            print("MOVIE NOT FOUNDED!!!")
            with open("movie.json","w") as file:
                json.dump(movie,file,indent=4)
            
    elif(choice==5):
        userinput=input("enter the movie name:")
        found=False
        for fck in movie:
            if(userinput == fck["title"]):
                movie.remove(fck)
                print("DELETED SUCESSFULLY")
                with open("movie.json","w") as file:
                    json.dump(movie,file,indent=4)
                    found=True
                    break
        else:
            print("movie not founded")
    elif(choice==6):
        movie.sort(key=lambda x: x["rating"],reverse=True)
        for fck in movie:
            print("successfully sorting the movies:")
            print("movie name:",fck["title"])
            print("rating:",fck["rating"])
    elif(choice==7):
        movie.sort(key=lambda x: x["year"])
        for fck in movie:
            print("movie name:",fck["title"])
            print("movie genre:",fck["genre"])
            print("release year:",fck["year"])
    elif(choice==8):
         count=0
         for fck in movie:
              count=count+1
              print("total number of movies:",count)
    elif(choice==9):
        userinput=input("enter the genre type:")
        found=False
        for fck in movie:
            if(userinput == fck["genre"]):
                print(fck)
                found=True
                break
            else:
                print("GENRE not founded:")
    elif(choice==10):
        userinput=input("enter the movie")
        found=False
        for fck in movie:
            if(userinput == fck["title"]):
                print("already Exists!!!")
                found =True
                break
        else:
                print("you enter the new movie name")
                title=input("enter the movie name:")
                genre=input("enter the type of movie:")
                year=int(input("enter the year of movie:"))
                rating=float(input("enter the rating of movies:"))
                addmovie= {
                    "title":title,
                    "genre":genre,
                    "year":year,
                    "rating":rating
                    }
                movie.append(addmovie)
                print("added sucessfully")
                with open("movie.json","w") as file:
                    json.dump(movie,file,indent=5)
                
        
        
            
            
        

    
    
        
                
                
        

    


