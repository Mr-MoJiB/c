o
    c��b�	  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeeed e
 ��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed � d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ d dlZd dlmZ d dlZdZd dlZd dlZd dlZd dlmZ d dlmZmZmZmZ ed  ZeD ]Z ej!�"e � ej!�#�  e�d!� �qe� Z$d"e$d#< d$e$d%< ee$d&< z	ejee$d'�Z%W n
   eed( � Y e%�� d) d*k�rJeed+ � nee	d, e e%�� d- d.  d � eee	d/ e
 d0 e	 d1 ��Z&e �d� dS )2�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZpudinaZword� r   �
apitonb.py�	logoprint   s
   
�r   z[>] Enter Api Key: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz 
)r
   )�init�Fore�Back�StylezXhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getNickname&msisdn=8801860852031u&   

[♦] Circle ID From This Api Key: 
g�������?�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz	x-api-key)�headersz

	[!] Use VpnZrdesczUnauthorized accessz
[!] Enter Vaild IDz
[>] CIRCLE ID	:	�dataZnicknamez 
	Pressz Enterz To Exit)'�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�input�a�getZresponser
   ZjsonZrequests.structuresr   Zcoloramar   r   r   r   ZurlZwords�charr   r   r   r   ZrespZxnr   r   r   r   �<module>   sz    




	
$ 