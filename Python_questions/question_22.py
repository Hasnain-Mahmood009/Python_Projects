#Write a phyton program that prints out all colors from color _list_1 
#that are not present in color _list_2.

color_list_1 = {"red","green","blue","yallow"}
color_list_2 = {"yallow","cyan","green"}
common = color_list_1.intersection(color_list_2)
print("Common color is : ",common)
