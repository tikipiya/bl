import os
import time
from colorama import Fore, Style
import string
import threading
import random

# Thread lock for file writing
file_lock = threading.Lock()
def Menu():
    global threads
    threads = 0
    time.sleep(0.5)
    
    def GetOptions():
        while True:
            time.sleep(0.5)
            os.system("cls")
            
            # Near-future styled menu
            print(f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║  {Fore.LIGHTMAGENTA_EX}██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     {Fore.CYAN}║
{Fore.CYAN}║  {Fore.LIGHTMAGENTA_EX}██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    {Fore.CYAN}║
{Fore.CYAN}║  {Fore.LIGHTMAGENTA_EX}██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    {Fore.CYAN}║
{Fore.CYAN}║  {Fore.LIGHTMAGENTA_EX}██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    {Fore.CYAN}║
{Fore.CYAN}║  {Fore.LIGHTMAGENTA_EX}██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    {Fore.CYAN}║
{Fore.CYAN}║  {Fore.LIGHTMAGENTA_EX}╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     {Fore.CYAN}║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║     {Fore.LIGHTCYAN_EX}▓▓▓▓▓▓▓▓▓▓▓▓▓ INVITE GENERATOR ▓▓▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTGREEN_EX}🚀 SELECT GENERATION MODE:{Fore.CYAN}                                        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.YELLOW}┌─────────────────────────────────────────────────────────────────┐{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│{Fore.LIGHTRED_EX} [1] {Fore.LIGHTCYAN_EX}◆ TEMPORARY INVITE    {Fore.WHITE}[8 CHAR LENGTH]   {Fore.LIGHTBLUE_EX}▶ {Fore.YELLOW}│{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│{Fore.LIGHTRED_EX} [2] {Fore.LIGHTCYAN_EX}◆ PERMANENT INVITE    {Fore.WHITE}[10 CHAR LENGTH]  {Fore.LIGHTBLUE_EX}▶ {Fore.YELLOW}│{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│{Fore.LIGHTRED_EX} [3] {Fore.LIGHTCYAN_EX}◆ MIXED MODE          {Fore.WHITE}[RANDOM LENGTH]   {Fore.LIGHTBLUE_EX}▶ {Fore.YELLOW}│{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}└─────────────────────────────────────────────────────────────────┘{Fore.CYAN}  ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTBLACK_EX}◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆{Fore.CYAN}  ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.MAGENTA}⚡ Developed by: {Fore.LIGHTMAGENTA_EX}tikisan{Fore.MAGENTA} ⚡                           {Fore.CYAN}║
{Fore.CYAN}║  {Fore.LIGHTBLACK_EX}Version: 2.0.0-CYBERPUNK | Status: {Fore.LIGHTGREEN_EX}OPERATIONAL{Fore.CYAN}           ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}┌─ INPUT ────────────────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}│ {Fore.YELLOW}> {Style.RESET_ALL}""", end="")
            
            try:
                uc = int(input())
                if uc in {1, 2, 3}: 
                    print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
                    time.sleep(0.3)  # Small delay for effect
                    return uc
                else:
                    print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘")
                    print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Invalid option. Please select 1, 2, or 3.{Style.RESET_ALL}")
                    time.sleep(1.5)
            except ValueError:
                print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘")
                print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Please enter a valid number.{Style.RESET_ALL}")
                time.sleep(1.5)
    
    def ValidInput():
        while True:
            time.sleep(0.5)
            os.system("cls")
            print(f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║     {Fore.LIGHTCYAN_EX}▓▓▓▓▓▓▓▓▓▓▓ THREAD ALLOCATION ▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTGREEN_EX}🔧 THREAD COUNT SPECIFICATION:{Fore.CYAN}                                   ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.YELLOW}┌─────────────────────────────────────────────────────────────────┐{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTCYAN_EX}Enter the number of threads to utilize:{Fore.YELLOW}                 │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│                                                         │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTBLUE_EX}• Recommended: 4-8 threads{Fore.YELLOW}                           │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTBLUE_EX}• Maximum: 50 threads{Fore.YELLOW}                                │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}└─────────────────────────────────────────────────────────────────┘{Fore.CYAN}  ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}┌─ INPUT ────────────────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}│ {Fore.YELLOW}> {Style.RESET_ALL}""", end="")
            
            try:
                threads = int(input())
                print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
                
                if 1 <= threads <= 50:
                    time.sleep(0.3)
                    return threads
                else:
                    print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Thread count must be between 1 and 50.{Style.RESET_ALL}")
                    time.sleep(1.5)
            except ValueError:
                print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
                print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Please enter a valid number.{Style.RESET_ALL}")
                time.sleep(1.5)  
    
    def GetThreadOption():
        while True:
            time.sleep(0.5)
            os.system("cls")
            print(f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║     {Fore.LIGHTCYAN_EX}▓▓▓▓▓▓▓▓▓▓▓ CONFIGURATION MATRIX ▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTGREEN_EX}⚡ THREADING SYSTEM ACTIVATION:{Fore.CYAN}                                 ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.YELLOW}┌─────────────────────────────────────────────────────────────────┐{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTCYAN_EX}Enable multi-threading for faster generation?{Fore.YELLOW}           │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│                                                         │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTGREEN_EX}[YES] {Fore.WHITE}━ Activate parallel processing{Fore.YELLOW}            │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTRED_EX}[NO]  {Fore.WHITE}━ Use single-thread mode{Fore.YELLOW}                   │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}└─────────────────────────────────────────────────────────────────┘{Fore.CYAN}  ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}┌─ INPUT ────────────────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}│ {Fore.YELLOW}> {Style.RESET_ALL}""", end="")
            
            uc = input().strip().lower()
            print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
            
            if uc == "yes" or uc == "no":
                time.sleep(0.3)
                return uc
            else:
                print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Please enter 'yes' or 'no'.{Style.RESET_ALL}")
                time.sleep(1.5)
    
    def GetGenerationCount():
        while True:
            time.sleep(0.5)
            os.system("cls")
            print(f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║     {Fore.LIGHTCYAN_EX}▓▓▓▓▓▓▓▓▓▓▓ GENERATION TARGET ▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTGREEN_EX}📊 INVITE QUANTITY SPECIFICATION:{Fore.CYAN}                                ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.YELLOW}┌─────────────────────────────────────────────────────────────────┐{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTCYAN_EX}How many invite codes do you want to generate?{Fore.YELLOW}          │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│                                                         │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTBLUE_EX}• Small batch: 100-1,000{Fore.YELLOW}                             │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTBLUE_EX}• Medium batch: 10,000-50,000{Fore.YELLOW}                       │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}│ {Fore.LIGHTBLUE_EX}• Large batch: 100,000+{Fore.YELLOW}                             │{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.YELLOW}└─────────────────────────────────────────────────────────────────┘{Fore.CYAN}  ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.LIGHTCYAN_EX}┌─ INPUT ────────────────────────────────────────────────────────────────┐
{Fore.LIGHTCYAN_EX}│ {Fore.YELLOW}> {Style.RESET_ALL}""", end="")
            
            try:
                count = int(input())
                print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
                
                if count > 0:
                    time.sleep(0.3)
                    return count
                else:
                    print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Count must be greater than 0.{Style.RESET_ALL}")
                    time.sleep(1.5)
            except ValueError:
                print(f"{Fore.LIGHTCYAN_EX}└────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
                print(f"{Fore.LIGHTRED_EX}⚠️  ERROR: Please enter a valid number.{Style.RESET_ALL}")
                time.sleep(1.5)
    
    # Show startup animation
    os.system("cls")
    print(f"""
{Fore.LIGHTMAGENTA_EX}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.LIGHTMAGENTA_EX}║                                                                           ║
{Fore.LIGHTMAGENTA_EX}║                    {Fore.LIGHTCYAN_EX}CYBER-GENESIS PROTOCOL v2.0{Fore.LIGHTMAGENTA_EX}                     ║
{Fore.LIGHTMAGENTA_EX}║                                                                           ║
{Fore.LIGHTMAGENTA_EX}║           {Fore.WHITE}Initializing quantum invite generation matrix...{Fore.LIGHTMAGENTA_EX}           ║
{Fore.LIGHTMAGENTA_EX}║                                                                           ║
{Fore.LIGHTMAGENTA_EX}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")
    
    time.sleep(2)
    print(f"{Fore.LIGHTGREEN_EX}⚡ System initialization complete ⚡{Style.RESET_ALL}")
    time.sleep(1)
    
    while True:
        choice = GetOptions()
        use_threads = GetThreadOption()
        threads = ValidInput() if use_threads == "yes" else 1
        count = GetGenerationCount()
        
        match choice:
            case 1: StartThread(8, threads, count)
            case 2: StartThread(10, threads, count)
            case 3: StartThread(0, threads, count)
def StartThread(length, threads_amount, count):
    """
        Starts all the threads based on the amount defined by the user
    """
    # Clear the output file before starting
    with open("generated_invites.txt", "w", encoding="utf-8") as file:
        file.write("")
    
    threads = []    
    print(f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║     {Fore.LIGHTCYAN_EX}▓▓▓▓▓▓▓▓▓▓▓▓ GENERATION ACTIVE ▓▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTGREEN_EX}🚀 INITIALIZING GENERATION MATRIX{Fore.CYAN}                               ║
{Fore.CYAN}║  {Fore.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.LIGHTBLUE_EX}Target Count: {Fore.WHITE}{count:,} codes{Fore.CYAN}                                      ║
{Fore.CYAN}║  {Fore.LIGHTBLUE_EX}Thread Count: {Fore.WHITE}{threads_amount} workers{Fore.CYAN}                                    ║
{Fore.CYAN}║  {Fore.LIGHTBLUE_EX}Output File:  {Fore.WHITE}generated_invites.txt{Fore.CYAN}                           ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")
    
    time.sleep(1)  # Dramatic pause
    print(f"{Fore.LIGHTMAGENTA_EX}⚡ Deploying worker threads...{Style.RESET_ALL}")
    time.sleep(0.5)
    
    invites_per_thread = count // threads_amount
    remaining_invites = count % threads_amount
    
    for i in range(threads_amount):
        thread_count = invites_per_thread + (1 if i < remaining_invites else 0)
        thread = threading.Thread(target=GenerateInvites, args=(length, thread_count, i + 1))
        thread.start()
        threads.append(thread)
        print(f"{Fore.LIGHTBLUE_EX}⚡ Worker-{i+1:02d} deployed: {thread_count:,} codes assigned{Style.RESET_ALL}")
        time.sleep(0.1)  # Stagger thread creation for visual effect
    
    print(f"{Fore.LIGHTGREEN_EX}\n🔥 ALL WORKERS DEPLOYED - GENERATION IN PROGRESS 🔥{Style.RESET_ALL}\n")
    
    for thread in threads:
        thread.join()
    
    print(f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║     {Fore.LIGHTGREEN_EX}▓▓▓▓▓▓▓▓▓▓▓ MISSION COMPLETE ▓▓▓▓▓▓▓▓▓▓▓{Fore.CYAN}        ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.LIGHTGREEN_EX}✅ GENERATION MATRIX: SUCCESSFUL{Fore.CYAN}                                ║
{Fore.CYAN}║  {Fore.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.CYAN}  ║
{Fore.CYAN}║  {Fore.LIGHTBLUE_EX}Generated: {Fore.WHITE}{count:,} invite codes{Fore.CYAN}                                  ║
{Fore.CYAN}║  {Fore.LIGHTBLUE_EX}Output:    {Fore.WHITE}generated_invites.txt{Fore.CYAN}                              ║
{Fore.CYAN}║  {Fore.LIGHTBLUE_EX}Status:    {Fore.LIGHTGREEN_EX}READY FOR DEPLOYMENT{Fore.CYAN}                            ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}║  {Fore.MAGENTA}⚡ System ready for next operation ⚡{Fore.CYAN}                            ║
{Fore.CYAN}║                                                                           ║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")
    
    print(f"{Fore.LIGHTCYAN_EX}\n🎉 Press ENTER to continue...{Style.RESET_ALL}", end="")
    input()  # Wait for user input before continuing
def GenerateInvites(length, count, thread_id):
    """
    Generate random Discord invite codes
    """
    generated_codes = []
    
    for i in range(count):
        # Choose length for mixed mode
        actual_length = random.choice([8, 10]) if length == 0 else length
        
        # Generate random invite code
        invite_code = ''.join(random.choices(
            string.ascii_letters + string.digits, 
            k=actual_length
        ))
        
        invite_url = f"https://discord.com/invite/{invite_code}"
        generated_codes.append(invite_url)
        
        # Progress display
        if (i + 1) % 100 == 0 or i + 1 == count:
            percentage = ((i + 1) / count) * 100
            progress_bar = "█" * int(percentage // 5) + "░" * (20 - int(percentage // 5))
            print(f"{Fore.LIGHTCYAN_EX}⚡ Worker-{thread_id:02d} {Fore.WHITE}[{progress_bar}] {Fore.LIGHTGREEN_EX}{percentage:5.1f}% {Fore.WHITE}({i + 1:,}/{count:,}){Style.RESET_ALL}")
    
    # Save to file with thread safety
    with file_lock:
        with open("generated_invites.txt", "a", encoding="utf-8") as file:
            for code in generated_codes:
                file.write(f"{code}\n")
    
    print(f"{Fore.LIGHTGREEN_EX}🎯 Worker-{thread_id:02d}: {Fore.WHITE}MISSION ACCOMPLISHED {Fore.LIGHTGREEN_EX}[{count:,} codes generated]{Style.RESET_ALL}")
if __name__ == "__main__":
    Menu()