ó
N($_c           @   sĖ  d  d l  Z  d  d l Z d  d l m Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m	 Z	 d   Z
 e j	 d  e
 d  e
 d  e
 d  e	 d	  e j d
  e j	 d  e  j d  j Z e j d e  Z d GHd GHd GHd GHd GHe j d  e d  Z d j e e e d d d d  Z d e d Z e j e e  Z e j d  d j e  GHd j e j d  e j d  e j d
  e j d   GHe
 d  e j d  d S(   i’’’’N(   t   get_close_matches(   t   systemc         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   st   c(    (    s   /sdcard/Scan-Covid19.pyt   m   s    t   clears@   [1;91mHello gan kembali lagi dengan saya [1;92mMr.Reyhan [00ms>   [1;91mKali ini saya akan mengasih tools scan corona live[00ms6   [1;91mSebelum lanjut kalian harus subscribe dulu[00msA   xdg-open https://www.youtube.com/channel/UCRcfrQRoRUW75jOuw74PVbwi   s   https://api.kawalcorona.com/s   "Country_Region":"(.*?)"sG   [1;91m+|[1;93m==============================================[1;91m|+s6       [1;93m* [1;92mAuthor[1;91m   :[1;93m Mr.Reyhans9       [1;93m* [1;92mWhatsapp[1;91m :[1;96m 08822158****s7       [1;93m* [1;92mYoutube[1;91m  : [1;96mMas Reyhani   s$   [1;93mInput lokasi [1;91m:[1;92m t    t   ni   t   cutoffi    s"   {"OBJECTID":.*?,"Country_Region":"sm   ","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}s(   

[0;35m       [1;31m{} [0;35m       s   [1;93mTerjangkit [1;91m:[1;92m {}
[1;93mMeninggal [1;91m :[1;92m {}
[1;93mPulih [1;91m     :[1;92m {}
[1;93mAktif [1;91m     :[1;92m {}
i   s(   [1;91mOkh semoga bermanfaat ya ^_^[00m(   t   requestst   ret   difflibR    t   carisR   R   t   ost   getpassR   R
   R   t   gett   textt   at   findallt
   namanegarat	   raw_inputt   askt   joint   carit   patt   searcht   bt   formatt   group(    (    (    s   /sdcard/Scan-Covid19.pyt   <module>   s8   0	



$;
