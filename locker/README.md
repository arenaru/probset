# Locker
# Basic analysis of pcap files and malware with Virus Total

1. What is the total number of packets captured in the network traffic?
Answer: 11961
Description: The total packet count was obtained by opening the PCAP in Wireshark and checking Statistics → Summary, where the total number of captured packets (11961) is displayed

2. Identify the IP address of the infected host.
Answer: 192.168.198.128
Description: The infected host IP (192.168.198.128) was identified by analyzing outbound traffic and observing which host initiated HTTP requests to the server.

3. What is the destination IP address and port number accessed by the victim? (ip:port)
Answer: 192.168.198.129:8000
Description: The destination IP and port (192.168.198.129:8000) were taken from the first HTTP GET request sent by the victim, visible in the packet details.

4. What is the hostname of the victim's machine?
Answer: DESKTOP-P15ADMF
Description: The hostname DESKTOP-P15ADMF was found inside LLMNR, NBNS, or SMB packets that reveal the system name during network discovery or file operations.

5. Identify the filename of the first file downloaded by the victim. (file_name.ext)
Answer: belajar_calculus.pdf
Description: The first downloaded file, belajar_calculus.pdf, was identified by filtering early HTTP GET requests within the capture.

6. What is the filename of the malicious binary? (filename.ext)
Answer: chuongdoung.exe
Description: The malicious binary chuongdoung.exe was found by searching for any HTTP requests containing “.exe” or by exporting files from File → Export Objects → HTTP.
 
7. Provide the absolute path where the malicious file was located.
Answer: /Work/secret/chuongdoung.exe
Description: The absolute path /Work/secret/chuongdoung.exe was recovered from SMB2 file operation packets referencing the file’s full directory location.
 
8. At what exact timestamp was the malicious file executed? (Format: dd/mm/yyyy:hh:mm:ss)
Answer: 20/11/2025:03:21:31
Description: The execution timestamp (20/11/2025:03:21:31) was determined by pinpointing the exact packet representing the start of malicious activity, which is when the key and victim's ID sent.
 
9. What is the SHA256 hash of the malicious file?
Answer: a153d59a98200b035fcc4fbee153e4b3f75358221fb006358f704e574af02993
Description: The SHA256 hash was calculated by extracting the .exe from the PCAP and running sha256sum on it, which produced the given hash value.
 
10. According to the analysis report, how many security vendors flagged this file as malicious?
Answer: 4
Description: The number of antivirus detections (4) was obtained by submitting the extracted hash to VirusTotal and checking how many vendors flagged it.
 
11. Based on the behavioral analysis, what is the MITRE ATT&CK Technique ID associated with "Process Injection"?
Answer: T1055
Description: The MITRE ATT&CK technique ID T1055 was taken from the behavioral analysis report, which mapped the malware’s process injection activity to this specific ATT&CK technique.
 
12. What specific technique did the malware utilize for Command and Control (C2)?
Answer: Application Layer Protocol
Description: The malware’s C2 technique, “Application Layer Protocol,” was determined based on its use of HTTP for command-and-control communication.
 
13. What is the unique Victim ID found in the ransom note?
Answer: 14A929E9
Description: The victim ID 14A929E9 was extracted from the ransom note recovered during the investigation. Or at the packet on Q8.
 
14. Identify the encryption key used by the ransomware.
Answer: 3871445A1BCFC5417780344C650551084BDEEE5C459FAF63014A07C25080097A
Description: The encryption key was located inside the network traffic, typically within HTTP headers or POST body data where the malware transmits its key.
 
15. What is the deadline (in hours) before the ransom demand increases?
Answer: 72
Description: The ransom deadline (72 hours) was identified by reading the ransom note, which explicitly states the time limit before the ransom increases.
