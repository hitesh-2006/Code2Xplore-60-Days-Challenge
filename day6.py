n=int(input("Enter Number of songs: "))
songs=[0]*n
for i in range(n):
    songs[i]=int(input("Enter duration: "))


for s in songs:
    if s<=0:
        print("Invalid Playlist")
        break
        
    Tl_Duration=sum(songs)
    no_song=len(songs)

    re_song=False
    for s in songs:
        if songs.count(s)>1:
            re_song=True
            break
    if Tl_Duration<300:
        p="Too Short Playlist"
        q="Add more time "
    elif Tl_Duration>3600:
        p="Too Long Playlist"
        q="Listen less time"
    elif re_song:
        p="Repetitive Playlist"
        q="Lsten Different songs"
    elif max(songs)<=600:
        p="Balanced Playlist"
        q="Good Duration"
    else:
        p="Irregular Playlist"
        q="Spend Good time on Music"
    
    print("Total Duration: ",Tl_Duration)
    print("songs: ",no_song)
    print("Category: ",p)
    print("Recommendation: ",q)