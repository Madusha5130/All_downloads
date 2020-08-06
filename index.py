import youtube_dl


def main():
    print("""\033[34m

‖‖        ‖‖ ‖‖  ‖‖   ‖‖  ‖‖    
 ‖‖      ‖‖  ‖‖  ‖‖ ‖‖    ‖‖
  ‖‖    ‖‖   ‖‖  ‖‖‖      ‖‖   
   ‖‖  ‖‖    ‖‖  ‖‖ ‖‖    ‖‖                     
    ‖‖‖‖     ‖‖  ‖‖   ‖‖  ‖‖""")
    print("\033[31m      ~~TOOL BY  MEGARUN~~")
    print("\033[93mDownload vdeos,audio & subtitle")
    print("")


    url = str(input("\033[92m Enter video url :- "))
    print()
    print("\033[1;37m")

   
    ydl_opts = {
     'listformats': True,
     }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download([url])
     print("\033[1;37m")


     coad = input("\033[92m  enter format coad(get format coad from this list) : - ")
     print('')
     sub = input("\033[92m  Do You Wont Download Subtital Y or N :- ")
     print('')
     print("\033[93m       DOWNLOADING....")
    if sub == "y" or sub == "Y":
     su = True
    elif sub == "n" or sub == "N":
     su = False 
     ydl_opts = {
     'writesubtitles':su,
     "outtmpl": "/storage/emulated/0/android/%(title)s.%(ext)s", 
     'format':coad,}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download([url])
     
     print('')
     print("\033[94m  Download Complete")


    cho = input("\033[1;37m  Do you wont use again Y or N :-  ")
    if cho == "y" or cho == "Y":
        main()
         
    elif cho == "n" or cho == "N":
        print('')
        quit()
        
        

main()

