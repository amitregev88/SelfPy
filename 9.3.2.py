def my_mp4_playlist(file_path, new_song):
    with open(file_path) as songs_file:
        songs = songs_file.readlines()

    if len(songs) < 3:
        with open(file_path, 'a') as songs_file:
            songs_file.write('\n' * (2 - len(songs)))
            songs_file.write(new_song + ';')
    
    else:
        old_song = songs[2].split(';', 1)[0]
        songs[2] = songs[2].replace(old_song, new_song)
        full_content = ''.join(songs)

        with open(file_path, 'w') as songs_file:
            songs_file.write(full_content)
    
    with open(file_path) as songs_file:
        print(songs_file.read())


# """Changes the content of a playlist, read from a given file. The changed playlist is writen back to the same file.
# :param: file_name: the path of the file contains the playlist
# :param: new_song: a new name, to cjange the name of a song from the list
# :type: strings
# """
# def my_mp4_playlist(file_path, new_song):
# 	fid = open(file_path, "r")
# 	lines = fid.readlines()
# 	fid.close()
# 	if len(lines) >= 3:
# 		lines[2] = new_song + lines[2][lines[2].find(';'):]
# 		#open(file_path, "w").writelines(lines)
# 	else:
# 		for n in range(2 - len(lines)):
# 			lines.append("\n")
# 		lines.append(new_song+ ";")
# 		#open(file_path, "w").writelines(lines)
# 	#print(open(file_path, "r").read())
# 	text=''
# 	for i in range(len(lines)):
# 		text=text+lines[i]
# 	print(text)
        
def main():
       
    my_mp4_playlist("words.txt",3)
    
if __name__ == "__main__":
    main()