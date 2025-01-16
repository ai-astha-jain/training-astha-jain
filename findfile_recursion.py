def search(dictionary, find_file, path = []):
    
    for key, values in dictionary.items():
        file_path = path + ["/"] + [key]
        if key == find_file or values == find_file:
            return file_path
        elif hasattr(values, 'items'):
            search_file = search(values, find_file, file_path)
            if search_file is not None:
                return search_file 
                

dictionary = {
     'Documents': { 'work' : { 'project1.txt':None, 'project2.txt':None}, 'person' : { 'name.docx':None, 'address.txt':None} },
     
     'Downloads': {'movies.txt':None},
     
     'Songs': {'MyFavourite':{'doubletake.mp3':None, 'TheNightWeMet.mp3':None}, 'AllTimeFavourite': {'Do-i-wanna-know?.mp3':None, 'beautiful_things.mp3':None}}
}

print(dictionary)

find_file = input("\n\nEnter the file you want to find: ")
search(dictionary, find_file)
print(f"The file {find_file} is found at: {id(find_file)}")
try:
	print(*search(dictionary, find_file))
except TypeError:
	print("File not")
	
