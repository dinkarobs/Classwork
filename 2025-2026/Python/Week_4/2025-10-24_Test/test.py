# Directions:
# You will use set.intersection(set2), set.union(set2), and/or set.difference(set2) to answer the following:
# 1. What is the print out of the union of Sergio and Anderling?
# 2. What is the print out of the difference between Jessellyz and Samaya?
# 3. What is the print out of the intersection of DruKiel and Santiago?
# 4. Who has the first name that matches the most of the letters in your name?
# 5. Who has the first name that matches the least of the letters in your name?
# HINT for 4 and 5. You can write 14 lines of code or 2 to answer 4 and 5.
# You may use your notes and vocabulary web page. Nothing else from the web.



def main():
    Abdullahi = {'A', 'b', 'd', 'u', 'l', 'l', 'a', 'h', 'i'}
    Mustafa = {'M', 'u', 's', 't', 'a', 'f', 'a'}
    Sergio = {'S', 'e', 'r', 'g', 'i', 'o'}
    Robert = {'R', 'o', 'b', 'e', 'r', 't'}
    Yonatan = {'Y', 'o', 'n', 'a', 't', 'a', 'n'}
    Santiago = {'S', 'a', 'n', 't', 'i', 'a', 'g', 'o'}
    Jose_Gabriel = {'J', 'o', 's', 'e', ' ', 'G', 'a', 'b', 'r', 'i', 'e', 'l'}
    Yofreilin = {'Y', 'o', 'f', 'r', 'e', 'i', 'l', 'i', 'n'}
    Jessellyz = {'J', 'e', 's', 's', 'e', 'l', 'l', 'y', 'z'}
    Ismael = {'I', 's', 'm', 'a', 'e', 'l'}
    Anderling = {'A', 'n', 'd', 'e', 'r', 'l', 'i', 'n', 'g'}
    Juan = {'J', 'u', 'a', 'n'}
    Jonatan = {'J', 'o', 'n', 'a', 't', 'a', 'n'}
    Samayah = {'S', 'a', 'm', 'a', 'y', 'a', 'h'}
    DruKiel = {'D', 'r', 'u', 'K', 'i', 'e', 'l'}
    names = [Abdullahi, Mustafa, Sergio, Robert, Yonatan, Santiago, Jose_Gabriel, Yofreilin ,Jessellyz, Ismael, Anderling, Juan, Jonatan, Samayah, DruKiel]

    print(set.union(Sergio,Anderling ))
    print(set.difference(Jessellyz,Samayah))
    print(set.intersection(Santiago,DruKiel))
    print(set.intersection(Santiago,DruKiel))
    print(set.intersection(DruKiel,Abdullahi))
    print(set.intersection(DruKiel,Mustafa ))
    print(set.intersection(DruKiel,Sergio ))
    print(set.intersection(DruKiel,Robert ))
    print(set.intersection(DruKiel,Yonatan ))
    print(set.intersection(DruKiel,Jose_Gabriel ))
    print(set.intersection(DruKiel,Yofreilin))
    print(set.intersection(DruKiel,Jessellyz ))
    print(set.intersection(DruKiel,Ismael ))
    print(set.intersection(DruKiel, Anderling))
    print(set.intersection(DruKiel,Juan ))
    print(set.intersection(DruKiel,Jonatan ))
    print(set.intersection(DruKiel,Samayah))

    #1.nlSireAdog
    #2.lJzse
    #3.i
    #4.Jose_Gabriel, Anderling, Yofreilin matches most of the letters in my name
    #5.#Yonatan,Jonatan,Samayah, all have the least letters that matches with my name
if __name__ == "__main__":
    main()