# scrambled_message = "world the save to time no is there"

# # Output
# # there is no time to save the world

# scrambled_list = scrambled_message.split(" ")

# unscrambled_list = scrambled_list[::-1]

# unscrambled_str = " ".join(unscrambled_list)

# print(unscrambled_str)


playlist = "🎵Dancing Queen;🎸Sweet Child O' Mine;🎹Piano Man;🎤Bohemian Rhapsody;🎺All That Jazz"
playlist_list = playlist.split(";")
print("My favorite playlist:")
for i in range(len(playlist_list)):
    print(f"{i + 1}. {playlist_list[i]}")
