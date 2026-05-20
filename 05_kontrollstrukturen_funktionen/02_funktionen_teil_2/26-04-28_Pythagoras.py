1   def berechne_pythagoras(kathete1, kathete2):
2	    hypotenuse = ( (kathete1 ** 2) + (kathete2 ** 2) ) ** 0.5
3	    return hypotenuse
4	    
5	    
6	def berechne_zaunlänge(str1, str2):  
7	    str3 = berechne_pythagoras(str1, str2) 
8	    zaun = str1 + str2 + str3
9	    print("Du brauchst", zaun, "meter Zaun")
10	    return zaun
11	    
12	    
13	    
14      land_str = 30
15	    adenauer_str = 40
16	    
17	
18	    berechne_zaunlänge(land_str, adenauer_str)
