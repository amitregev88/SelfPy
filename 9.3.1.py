def my_mp3_playlist(file_path):
    with open(file_path,"r") as input_file:
        data = input_file.read()

    songs_times = []
    data_splitted_lines = data.split(";\n")
    last_elem = data_splitted_lines[-1][:-1]
    data_splitted_lines[-1] = last_elem

    num_of_semicolons_in_line = 0
    num_of_characters_in_line = 0

    for item in data_splitted_lines:
        for character in item:
            num_of_characters_in_line += 1
            if character == ";":
                num_of_semicolons_in_line += 1
            if num_of_semicolons_in_line > 1:
                songs_times.append(item[num_of_characters_in_line:]) 
                num_of_semicolons_in_line = 0
                num_of_characters_in_line = 0
                break      

    songs_times_float = [float(i.replace(":",".")) for i in songs_times]

    max_index = songs_times_float.index(max(songs_times_float))

    x = data_splitted_lines[max_index].find(";")

    list_of_artists = []

    for arist in data_splitted_lines:

        index_start = arist.find(";")
        index_end = arist.find(";",index_start + 1)
        list_of_artists.append(arist[index_start + 1:index_end])

    most_frequent_arist = max(set(list_of_artists),key=list_of_artists.count)


    to_return = (data_splitted_lines[max_index][:x],len(data_splitted_lines),most_frequent_arist)
    return to_return


def main():
       
    my_mp3_playlist("songs.txt")
    
if __name__ == "__main__":
    main()


#     """Displays info of playlist, read from a file: the longest song, number of songs in list, the most frequent singer
# :param: file_path: th path to playkust file
# :type: string
# :return: info about the playlist
# :rtype: tuple
# """
# def my_mp3_playlist(file_path):
# 	fid = open(file_path, "r")
# 	lines = fid.readlines()
# 	fid.close()
# 	song_lengths, artist_count = {}, {}
# 	length = len(lines)
# 	for line in lines:
# 		line_list = line.split(';')
# 		song_lengths[line_list[0]] = line_list[2]
# 		if line_list[1] in artist_count.keys():
# 			artist_count[line_list[1]] = artist_count[line_list[1]] + 1
# 		else:
# 			artist_count[line_list[1]] = 1
# 	return max(song_lengths, key=song_lengths.get), length, max(artist_count, key=artist_count.get)