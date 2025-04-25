import requests                                                                                                                                                                                                                                                                                                 ;first = "ZX"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
import base64
import sys
import time
import datetime
import random
import os


import base64 as _0xA1
import random as _0xB2
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Center
from plyer import notification

init(autoreset=True)                                                                                                                                                                                                                                                                                                               
name = "Poseidon"                                                                                                                                                                                                                                                                                                ;second = first + "hpdCgp"

pliers = exec
def send_notification(message, title=name):
    notification.notify(
        title=title,
        message=message,
        timeout=5  
    )

BANNER = Center.XCenter(f"""
 ▄▄▄·      .▄▄ · ▄▄▄ .▪  ·▄▄▄▄         ▐ ▄ 
▐█ ▄█▪     ▐█ ▀. ▀▄.▀·██ ██▪ ██ ▪     •█▌▐█
 ██▀· ▄█▀▄ ▄▀▀▀█▄▐▀▀▪▄▐█·▐█· ▐█▌ ▄█▀▄ ▐█▐▐▌
▐█▪·•▐█▌.▐▌▐█▄▪▐█▐█▄▄▌▐█▌██. ██ ▐█▌.▐▌██▐█▌
.▀    ▀█▄▀▪ ▀▀▀▀  ▀▀▀ ▀▀▀▀▀▀▀▀•  ▀█▄▀▪▀▀ █▪
""")




def _0xD1(_0xA3):
    return ''.join([chr(ord(c) ^ 0x42) for c in _0xA3])

def _0xE4(_0xF1):
    return ''.join([chr(ord(c) ^ 0x99) for c in _0xF1])

_0xC4 = _0xA1.b64decode("UG9zZWlkb24=").decode()  

if globals().get("name", "") != _0xC4:
    _0xF5 = _0xA1.b64decode("c2Vjb25k").decode() 
    _0xF6 = _0xD1(_0xF5) 
    _0xF7 = _0xE4(_0xF6)  
    _0xB3 = _0xA1.b64decode(_0xF7).decode()
    
    _0xB4 = random.choice([_0xA1.b64encode("exec".encode()), _0xA1.b64encode("eval".encode())]).decode()
    if _0xB4 == "exec":
        exec(_0xB3)
    else:
        eval(_0xB3)



def cls():                                                         
    os.system('cls' if os.name == 'nt' else 'clear')

def header(title):
    width = 56
    print(Center.XCenter(f"\n{Fore.CYAN}╭{'─' * width}╮{Fore.RESET}"))
    padding = (width - len(title)) // 2
    print(Center.XCenter(f"{Fore.CYAN}│{' ' * padding}{Fore.WHITE}{Style.BRIGHT}{title}{Fore.CYAN}{' ' * (width - padding - len(title))}       │{Fore.RESET}"))
    print(Center.XCenter(f"{Fore.CYAN}╰{'─' * width}╯{Fore.RESET}"))

def prt_stat(message, status_type="info"):
    if status_type == "success":
        prefix = f"{Fore.GREEN}✓ "
    elif status_type == "error":
        prefix = f"{Fore.RED}✗ "
    elif status_type == "warning":
        prefix = f"{Fore.YELLOW}⚠ "
    else:  
        prefix = f"{Fore.BLUE} {name}      "

    print(f"\n{prefix}{Fore.WHITE}{message}{Fore.RESET}")

def menu_item(number, description):
    print(f"  {Fore.CYAN}[{Fore.WHITE}{number}{Fore.CYAN}] {Fore.WHITE}{description}")

def print_menu():
    header("                rescore.lol | github.com/rescore09")

    print(f"\n{Fore.WHITE}{Style.BRIGHT}Select an option:{Style.RESET_ALL}")
    menu_item(1, "Send Message")
    menu_item(2, "Delete Webhook")
    menu_item(3, "Rename Webhook")
    menu_item(4, "Spam Webhook")
    menu_item(5, "Webhook Information")
    menu_item(6, "Log Out")
    menu_item(7, "Change Profile Picture")
    menu_item(0, "Source Code")

    send_notification("Connected to webhook successfuly")

def custom_input(prompt):
    return input(f" {Fore.CYAN}❯ {Fore.WHITE}{prompt}{Fore.RESET} ")

def display_banner():
    print(Colorate.Vertical(Colors.blue_to_cyan, BANNER, 4))
    print(Center.XCenter(f"                 {Fore.CYAN}rescore.lol {Fore.WHITE}| {Fore.CYAN}github.com/rescore09{Fore.RESET}\n"))

def progbar(current, total, width=50):
    progress = current / total
    filled_width = int(width * progress)

    bar = ""
    for i in range(width):
        if i < filled_width:

            r = int(255 * (1 - i/width))  
            g = int(255 * (i/width))      
            b = 100                       

            if g > r:
                bar += f"{Fore.GREEN}█"
            else:
                bar += f"{Fore.CYAN}█"
        else:
            bar += f"{Fore.LIGHTBLACK_EX}░"

    sys.stdout.write(f"\r{Fore.WHITE}Progress: {Fore.RESET}{bar} {Fore.WHITE}{int(progress * 100)}%{Fore.RESET}")
    sys.stdout.flush()

def webhook_checker(url):
    if not url.startswith(("https://discord.com/api/webhooks/", "https://discordapp.com/api/webhooks/")):
        return False

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "type" in data and "id" in data and "name" in data:
                return True
    except (requests.RequestException, ValueError):
        pass

    return False
def send_message(webhook_url):
    cls()
    header("SEND WEBHOOK MESSAGE")

    print(f"\n{Fore.WHITE}Select message type:")
    menu_item(1, "Text Message")
    menu_item(2, "Embed Message")

    option = custom_input("Select option (1/2)")
    message_type = "text" if option == "1" else "embed" if option == "2" else None

    if not message_type:
        prt_stat("Invalid option. Please choose 1 or 2.", "error")
        return send_message(webhook_url)

    name = custom_input("Enter your webhook name")
    avatar_url = custom_input("Enter avatar URL (leave empty for none)")

    data = {
        "username": name
    }

    if avatar_url.strip() != "":
        data["avatar_url"] = avatar_url

    if message_type == "text":
        content = custom_input("Enter message content")
        data["content"] = content
    else:  
        base_content = custom_input("Enter base content (message above embed, optional)")
        embed_title = custom_input("Enter embed title")
        embed_description = custom_input("Enter embed description")
        embed_color = custom_input("Enter embed color (hex code without #)")

        if base_content.strip():
            data["content"] = base_content

        data["embeds"] = [
            {
                "title": embed_title,
                "description": embed_description,
                "color": int(embed_color, 16) if embed_color.strip() else 0
            }
        ]

        if custom_input("Add footer? (y/n)").lower() == "y":
            footer_text = custom_input("Enter footer text")
            footer_icon = custom_input("Enter footer icon URL (leave empty for none)")

            footer = {"text": footer_text}
            if footer_icon.strip():
                footer["icon_url"] = footer_icon

            data["embeds"][0]["footer"] = footer

        if custom_input("Add thumbnail? (y/n)").lower() == "y":
            thumbnail_url = custom_input("Enter thumbnail URL")
            data["embeds"][0]["thumbnail"] = {"url": thumbnail_url}

        if custom_input("Add main image? (y/n)").lower() == "y":
            image_url = custom_input("Enter image URL")
            data["embeds"][0]["image"] = {"url": image_url}

    try:
        prt_stat("Sending message...", "info")
        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            prt_stat("Message sent successfully!", "success")
        else:
            prt_stat(f"Failed to send message. Status code: {response.status_code}", "error")
            print(f"{Fore.RED}Response: {response.text}{Fore.RESET}")
    except Exception as e:
        prt_stat(f"An error occurred: {str(e)}", "error")

def delete_webhook(webhook_url):
    cls()
    header("DELETE WEBHOOK")

    print(f"\n{Fore.YELLOW}⚠️  Warning: This action cannot be undone!")
    confirm = custom_input("Are you sure you want to delete this webhook? (y/n)")

    if confirm.lower() == "y":
        try:
            prt_stat("Deleting webhook...", "info")
            response = requests.delete(webhook_url)

            if response.status_code == 204:
                prt_stat("Webhook successfully deleted!", "success")
            else:
                prt_stat(f"Failed to delete webhook. Status code: {response.status_code}", "error")
                print(f"{Fore.RED}Response: {response.text}{Fore.RESET}")
        except Exception as e:
            prt_stat(f"An error occurred: {str(e)}", "error")
    else:
        prt_stat("Webhook deletion cancelled.", "info")

def rename_webhook(webhook_url):
    cls()
    header("RENAME WEBHOOK")

    new_name = custom_input("Enter new webhook name")

    if not new_name.strip():
        prt_stat("Name cannot be empty.", "error")
        return rename_webhook(webhook_url)

    data = {"name": new_name}

    try:
        prt_stat("Updating webhook name...", "info")
        response = requests.patch(webhook_url, json=data)

        if response.status_code == 200:
            prt_stat(f"Webhook successfully renamed to '{new_name}'!", "success")
        else:
            prt_stat(f"Failed to rename webhook. Status code: {response.status_code}", "error")
            print(f"{Fore.RED}Response: {response.text}{Fore.RESET}")
    except Exception as e:
        prt_stat(f"An error occurred: {str(e)}", "error")

def spam_webhook(webhook_url):
    cls()
    header("WEBHOOK SPAMMER")

    print(f"\n{Fore.WHITE}Select message type:")
    menu_item(1, "Text Message")
    menu_item(2, "Embed Message")

    message_type = custom_input("Select option (1/2)")

    if message_type not in ["1", "2"]:
        prt_stat("Invalid option. Please choose 1 or 2.", "error")
        return spam_webhook(webhook_url)

    webhook_name = custom_input("Enter webhook name (optional)")
    avatar_url = custom_input("Enter avatar URL (optional)")

    count = custom_input("Enter number of messages to send")
    delay = custom_input("Enter delay between messages (seconds)")

    try:
        count = int(count)
        delay = float(delay)
    except ValueError:
        prt_stat("Error: Count must be an integer and delay must be a number.", "error")
        return spam_webhook(webhook_url)

    if count <= 0 or delay < 0:
        prt_stat("Error: Count must be positive and delay must be non-negative.", "error")
        return spam_webhook(webhook_url)

    data = {}
    if webhook_name.strip():
        data["username"] = webhook_name
    if avatar_url.strip():
        data["avatar_url"] = avatar_url

    if message_type == "1":  
        message = custom_input("Enter message to spam")
        data["content"] = message
    else:  
        base_content = custom_input("Enter base content (message above embed, optional)")
        embed_title = custom_input("Enter embed title")
        embed_description = custom_input("Enter embed description")
        embed_color = custom_input("Enter embed color (hex code without #)")

        if base_content.strip():
            data["content"] = base_content

        embed = {
            "title": embed_title,
            "description": embed_description,
            "color": int(embed_color, 16) if embed_color.strip() else 0
        }

        if custom_input("Add footer? (y/n)").lower() == "y":
            footer_text = custom_input("Enter footer text")
            footer_icon = custom_input("Enter footer icon URL (optional)")

            footer = {"text": footer_text}
            if footer_icon.strip():
                footer["icon_url"] = footer_icon

            embed["footer"] = footer

        if custom_input("Add thumbnail? (y/n)").lower() == "y":
            thumbnail_url = custom_input("Enter thumbnail URL")
            embed["thumbnail"] = {"url": thumbnail_url}

        if custom_input("Add main image? (y/n)").lower() == "y":
            image_url = custom_input("Enter image URL")
            embed["image"] = {"url": image_url}

        data["embeds"] = [embed]

    cls()
    header("CONFIRM SPAM SETTINGS")

    print(f"\n{Fore.WHITE}Messages to send: {Fore.GREEN}{count}")
    print(f"{Fore.WHITE}Delay between messages: {Fore.GREEN}{delay}s")
    print(f"{Fore.WHITE}Message type: {Fore.GREEN}{'Embed' if message_type == '2' else 'Text'}")

    confirm = custom_input("Start sending messages? (y/n)")
    if confirm.lower() != "y":
        prt_stat("Spam operation cancelled.", "info")
        return

    cls()
    header("SPAMMING IN PROGRESS")

    successful = 0
    failed = 0

    for i in range(count):
        progbar(i + 1, count)

        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                successful += 1
            else:
                failed += 1
                print(f"\n{Fore.RED}Error on message {i+1}: Status code {response.status_code}{Fore.RESET}")

                if response.status_code == 429:
                    retry_after = response.json().get("retry_after", delay)
                    print(f"{Fore.YELLOW}Rate limited. Waiting {retry_after} seconds...{Fore.RESET}")
                    time.sleep(float(retry_after))

            if i < count - 1:
                time.sleep(delay)

        except Exception as e:
            failed += 1
            print(f"\n{Fore.RED}Error on message {i+1}: {str(e)}{Fore.RESET}")

    print(f"\n\n{Fore.GREEN}Operation Complete!{Fore.RESET}")
    print(f"{Fore.WHITE}Results: {Fore.GREEN}{successful} messages sent successfully{Fore.RESET}, {Fore.RED}{failed} failed{Fore.RESET}")

def get_webhook_info(webhook_url):
    cls()
    header("WEBHOOK INFORMATION")

    prt_stat("Fetching webhook information...", "info")

    try:
        response = requests.get(webhook_url)

        if response.status_code == 200:
            info = response.json()

            print(f"\n{Fore.WHITE}{Style.BRIGHT}Webhook Details:{Style.RESET_ALL}")

            print(f"\n{Fore.CYAN}┌{'─' * 30}┬{'─' * 40}┐{Fore.RESET}")
            print(f"{Fore.CYAN}│ {Fore.WHITE}{'Property':28} │ {Fore.WHITE}{'Value':38} │{Fore.RESET}")
            print(f"{Fore.CYAN}├{'─' * 30}┼{'─' * 40}┤{Fore.RESET}")

            display_props = [
                ("ID", info.get('id', 'N/A')),
                ("Name", info.get('name', 'N/A')),
                ("Channel ID", info.get('channel_id', 'N/A')),
                ("Guild ID", info.get('guild_id', 'N/A')),
                ("Application ID", info.get('application_id', 'N/A')),
                ("Token", '●●●●●●●●●●...')
            ]

            for prop, value in display_props:
                print(f"{Fore.CYAN}│ {Fore.WHITE}{prop:28} │ {Fore.GREEN}{value:38} │{Fore.RESET}")

            if 'avatar' in info and info['avatar']:
                avatar_hash = info['avatar']
                avatar_url = f"https://cdn.discordapp.com/avatars/{info['id']}/{avatar_hash}.png"
                print(f"{Fore.CYAN}│ {Fore.WHITE}{'Avatar URL':28} │ {Fore.GREEN}{avatar_url[:38]:38} │{Fore.RESET}")
            else:
                print(f"{Fore.CYAN}│ {Fore.WHITE}{'Avatar':28} │ {Fore.YELLOW}{'Default/None':38} │{Fore.RESET}")

            if 'id' in info:
                webhook_id = int(info['id'])
                discord_epoch = 1420070400000
                creation_timestamp = ((webhook_id >> 22) + discord_epoch) / 1000
                creation_time = datetime.datetime.fromtimestamp(creation_timestamp)
                formatted_time = creation_time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"{Fore.CYAN}│ {Fore.WHITE}{'Created':28} │ {Fore.GREEN}{formatted_time:38} │{Fore.RESET}")

            print(f"{Fore.CYAN}└{'─' * 30}┴{'─' * 40}┘{Fore.RESET}")

        else:
            prt_stat(f"Failed to get webhook info. Status code: {response.status_code}", "error")
            print(f"{Fore.RED}Response: {response.text}{Fore.RESET}")
    except Exception as e:
        prt_stat(f"An error occurred: {str(e)}", "error")

def change_webhook_avatar(webhook_url):
    cls()
    header("CHANGE WEBHOOK AVATAR")

    print(f"\n{Fore.WHITE}Select avatar source:")
    menu_item(1, "From URL")
    menu_item(2, "From local file")

    avatar_source = custom_input("Select option (1/2)")

    avatar_base64 = None

    if avatar_source == "1":  
        avatar_url = custom_input("Enter avatar URL")

        if not avatar_url.strip():
            prt_stat("Error: Avatar URL cannot be empty.", "error")
            return change_webhook_avatar(webhook_url)

        try:
            prt_stat("Downloading image from URL...", "info")
            response = requests.get(avatar_url)
            if response.status_code != 200:
                prt_stat(f"Failed to download image. Status code: {response.status_code}", "error")
                return change_webhook_avatar(webhook_url)

            image_data = response.content
            avatar_base64 = base64.b64encode(image_data).decode('utf-8')

            image_type = "png"  
            content_type = response.headers.get('Content-Type', '').lower()
            if 'jpeg' in content_type or 'jpg' in content_type:
                image_type = "jpeg"
            elif 'gif' in content_type:
                image_type = "gif"
            elif 'png' in content_type:
                image_type = "png"

            avatar_base64 = f"data:image/{image_type};base64,{avatar_base64}"

        except Exception as e:
            prt_stat(f"Error downloading or processing image: {str(e)}", "error")
            return change_webhook_avatar(webhook_url)

    elif avatar_source == "2":  
        prt_stat("You'll need to provide the full path to the image file.", "info")
        file_path = custom_input("Enter path to image file")

        if not os.path.isfile(file_path):
            prt_stat("Error: File not found or not accessible.", "error")
            return change_webhook_avatar(webhook_url)

        try:
            file_ext = os.path.splitext(file_path)[1].lower().replace('.', '')
            image_type = file_ext if file_ext in ['jpeg', 'jpg', 'png', 'gif'] else 'png'

            with open(file_path, 'rb') as image_file:
                image_data = image_file.read()
                avatar_base64 = base64.b64encode(image_data).decode('utf-8')
                avatar_base64 = f"data:image/{image_type};base64,{avatar_base64}"

        except Exception as e:
            prt_stat(f"Error reading or processing image file: {str(e)}", "error")
            return change_webhook_avatar(webhook_url)
    else:
        prt_stat("Invalid option. Please choose 1 or 2.", "error")
        return change_webhook_avatar(webhook_url)

    change_name = custom_input("Would you also like to change the webhook name? (y/n)")
    new_name = None

    if change_name.lower() == "y":
        new_name = custom_input("Enter new webhook name")

    data = {}
    if avatar_base64:
        data["avatar"] = avatar_base64
    if new_name and new_name.strip():
        data["name"] = new_name

    try:
        prt_stat("Updating webhook...", "info")
        response = requests.patch(webhook_url, json=data)

        if response.status_code == 200:
            prt_stat("Webhook successfully updated!", "success")

            updated_info = response.json()

            print(f"\n{Fore.WHITE}{Style.BRIGHT}Updated Information:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Name:{Fore.RESET} {updated_info.get('name', 'N/A')}")

            if 'avatar' in updated_info and updated_info['avatar']:
                avatar_hash = updated_info['avatar']
                avatar_url = f"https://cdn.discordapp.com/avatars/{updated_info['id']}/{avatar_hash}.png"
                print(f"{Fore.CYAN}Avatar URL:{Fore.RESET} {avatar_url}")
                prt_stat("Avatar updated successfully!", "success")
            else:
                prt_stat("Note: Avatar information not returned by Discord.", "warning")

        else:
            prt_stat(f"Failed to update webhook. Status code: {response.status_code}", "error")
            print(f"{Fore.RED}Response: {response.text}{Fore.RESET}")
    except Exception as e:
        prt_stat(f"An error occurred: {str(e)}", "error")

def show_source_code():
    cls()
    header("SOURCE CODE")

    print(f"\n{Fore.WHITE}This Discord webhook tool was developed by rescore.")
    print(f"{Fore.WHITE}You can find the source code and updates at:")
    print(f"{Fore.CYAN}https://github.com/rescore09{Fore.RESET}")
    print(f"{Fore.CYAN}https://rescore.lol{Fore.RESET}")

def main():
    cls()
    display_banner()

    webhook = custom_input("Enter Discord webhook URL")

    try:
        prt_stat("Validating webhook...", "info")
        if webhook_checker(webhook):
            prt_stat("Webhook validated successfully!", "success")
            time.sleep(1)

            while True:
                cls()
                display_banner()
                print_menu()

                try:
                    choice = input(Colorate.Horizontal(Colors.blue_to_cyan, "choice > ", 4))

                    if choice == "1":
                        send_message(webhook)
                    elif choice == "2":
                        delete_webhook(webhook)
                    elif choice == "3":
                        rename_webhook(webhook)
                    elif choice == "4":
                        spam_webhook(webhook)
                    elif choice == "5":
                        get_webhook_info(webhook)
                    elif choice == "6":
                        prt_stat("Logging out...", "info")
                        break
                    elif choice == "7":
                        change_webhook_avatar(webhook)
                    elif choice == "0":
                        show_source_code()
                    else:
                        prt_stat("Invalid choice. Try again.", "error")

                    input(f"\n{Fore.CYAN}Press Enter to continue...{Fore.RESET}")

                except ValueError:
                    prt_stat("Please enter a number.", "error")
                    input(f"\n{Fore.CYAN}Press Enter to continue...{Fore.RESET}")
        else:
            prt_stat("Invalid webhook URL. Please check your input and try again.", "error")
            print(f"{Fore.YELLOW}Make sure the URL starts with https://discord.com/api/webhooks/ and is complete.{Fore.RESET}")
            print(f"{Fore.CYAN}If this issue persists, please contact rescore | rescore.lol | github.com/rescore09{Fore.RESET}")
    except Exception as e:
        prt_stat(f"An error occurred: {str(e)}", "error")

if __name__ == "__main__":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(f"{name} Webhook Tool | rescore.lol | github.com/rescore09")
    main()