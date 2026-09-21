import time
import signal
import threading
import sys

FLAG = "NCW{y4ng_b1s4_r3v3rs3_m4lw4r3ny4_d4p3t_100k}"

correct_answers = {
    "Q1": "11961",
    "Q2": "192.168.198.128",
    "Q3": "192.168.198.129:8000",
    "Q4": "DESKTOP-P15ADMF",
    "Q5": "belajar_calculus.pdf",  # kept for reference, but we’ll use an explicit list below
    "Q6": "chuongdoung.exe",
    "Q7": "/Work/secret/chuongdoung.exe",
    "Q8": "20/11/2025:03:21:31",
    "Q9": "a153d59a98200b035fcc4fbee153e4b3f75358221fb006358f704e574af02993",
    "Q10": "4",
    "Q11": "T1055",
    "Q12": "Application Layer Protocol",
    "Q13": "14A929E9",
    "Q14": "3871445A1BCFC5417780344C650551084BDEEE5C459FAF63014A07C25080097A",
    "Q15": "72",
}

# explicit valid answers for Q5
valid_q5_answers = [
    "belajar calculus.pdf",
    "belajar_calculus.pdf",
]

valid_q10_answers = [
    "4",
    "6",
    "17",
]

player_answers = {
    "Q1": "",
    "Q2": "",
    "Q3": "",
    "Q4": "",
    "Q5": "",
    "Q6": "",
    "Q7": "",
    "Q8": "",
    "Q9": "",
    "Q10": "",
    "Q11": "",
    "Q12": "",
    "Q13": "",
    "Q14": "",
    "Q15": "",
}

class TimeoutException(Exception):
    pass

def input_with_timeout(prompt, timeout=45):
    def input_thread(prompt, result):
        # Force flush to ensure prompt appears immediately in netcat
        print(f"{prompt}\nAnswer: ", end='', flush=True) 
        result.append(sys.stdin.readline().strip())

    result = []
    thread = threading.Thread(target=input_thread, args=(prompt, result))
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if not result:
        print("\nTime's up!", flush=True)
        sys.exit(0)
    return result[0]

def check_all_correct():
    return all(player_answers.values()) 

print("==================================================", flush=True)
print("\033[91m" + r"""
  _      ____   _____ _  _______ ____  
 | |    / __ \ / ____| |/ / ____|  _ \ 
 | |   | |  | | |    | ' /|  _| | |_) |
 | |___| |__| | |____| . \| |___|  _ < 
 |______\____/ \_____|_|\_\_____|_| \_\
                                       """ + "\033[0m", flush=True)

print("\033[96m[+] DIFFICULTY : EASY", flush=True)
print("[+] AUTHOR     : ARREN", flush=True)
print("[+] MISSION    : ANALYZE THE INCIDENT\033[0m\n", flush=True)
print("==================================================", flush=True)

while not check_all_correct():
    
    if player_answers["Q1"] == "":
        q1_answer = input_with_timeout("1. What is the total number of packets captured in the network traffic? ")
        if q1_answer.lower() == correct_answers["Q1"].lower():
            print("Correct!", flush=True)
            player_answers["Q1"] = q1_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q2"] == "":
        q2_answer = input_with_timeout("2. Identify the IP address of the infected host. ")
        if q2_answer.lower() == correct_answers["Q2"].lower():
            print("Correct!", flush=True)
            player_answers["Q2"] = q2_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q3"] == "":
        q3_answer = input_with_timeout("3. What is the destination IP address and port number accessed by the victim? (ip:port) ")
        if q3_answer.lower() == correct_answers["Q3"].lower():
            print("Correct!", flush=True)
            player_answers["Q3"] = q3_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q4"] == "":
        q4_answer = input_with_timeout("4. What is the hostname of the victim's machine? ")
        if q4_answer.lower() == correct_answers["Q4"].lower():
            print("Correct!", flush=True)
            player_answers["Q4"] = q4_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q5"] == "":
        q5_answer = input_with_timeout("5. Identify the filename of the first file downloaded by the victim. (filename.ext) ")
        # explicit list matching for Q5
        if q5_answer.strip().lower() in [a.lower() for a in valid_q5_answers]:
            print("Correct!", flush=True)
            player_answers["Q5"] = q5_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)
    
    if player_answers["Q6"] == "":
        q6_answer = input_with_timeout("6. What is the filename of the malicious binary? (filename.ext) ")
        if q6_answer.lower() == correct_answers["Q6"].lower():
            print("Correct!", flush=True)
            player_answers["Q6"] = q6_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q7"] == "":
        q7_answer = input_with_timeout("7. Provide the absolute path where the malicious file was located. ")
        if q7_answer.lower() == correct_answers["Q7"].lower():
            print("Correct!", flush=True)
            player_answers["Q7"] = q7_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)
    
    if player_answers["Q8"] == "":
        q8_answer = input_with_timeout("8. At what exact timestamp was the malicious file executed? (Format: dd/mm/yyyy:hh:mm:ss) ")
        if q8_answer.lower() == correct_answers["Q8"].lower():
            print("Correct!", flush=True)
            player_answers["Q8"] = q8_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)
    
    if player_answers["Q9"] == "":
        q9_answer = input_with_timeout("9. What is the SHA256 hash of the malicious file? ")
        if q9_answer.lower() == correct_answers["Q9"].lower():
            print("Correct!", flush=True)
            player_answers["Q9"] = q9_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q10"] == "":
        q10_answer = input_with_timeout("10. According to the analysis report, how many security vendors flagged this file as malicious? ")
        if q10_answer.strip().lower() in [a.lower() for a in valid_q10_answers]:
            print("Correct!", flush=True)
            player_answers["Q10"] = q10_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q11"] == "":
        q11_answer = input_with_timeout("11. Based on the behavioral analysis, what is the MITRE ATT&CK Technique ID associated with \"Process Injection\"? ")
        if q11_answer.lower() == correct_answers["Q11"].lower():
            print("Correct!", flush=True)
            player_answers["Q11"] = q11_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q12"] == "":
        q12_answer = input_with_timeout("12. What specific technique did the malware utilize for Command and Control (C2)? ")
        if q12_answer.lower() == correct_answers["Q12"].lower():
            print("Correct!", flush=True)
            player_answers["Q12"] = q12_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q13"] == "":
        q13_answer = input_with_timeout("13. What is the unique Victim ID found in the ransom note? ")
        if q13_answer.lower() == correct_answers["Q13"].lower():
            print("Correct!", flush=True)
            player_answers["Q13"] = q13_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q14"] == "":
        q14_answer = input_with_timeout("14. Identify the encryption key used by the ransomware. ")
        if q14_answer.lower() == correct_answers["Q14"].lower():
            print("Correct!", flush=True)
            player_answers["Q14"] = q14_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)

    if player_answers["Q15"] == "":
        q15_answer = input_with_timeout("15. What is the deadline (in hours) before the ransom demand increases? ")
        if q15_answer.lower() == correct_answers["Q15"].lower():
            print("Correct!", flush=True)
            player_answers["Q15"] = q15_answer
        else:
            print("Incorrect. Try again.", flush=True)
            sys.exit(0)


print(f"\nCongrats!! Here's ur flag: {FLAG}", flush=True)
