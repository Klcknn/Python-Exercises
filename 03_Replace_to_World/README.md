# Bazı Python Karakter Dizilerinin Metotları
## İçindekiler

- [Bazı Python Karakter Dizilerinin Metotları](#bazı-python-karakter-dizilerinin-metotları)
  - [İçindekiler](#i̇çindekiler)
  - [1. isalpha():](#1-isalpha)
  - [2. isnumeric():](#2-isnumeric)
  - [3. isalnum():](#3-isalnum)
  - [4. isdecimal():](#4-isdecimal)
  - [5. isdigit():](#5-isdigit)
  - [6. islower():](#6-islower)
  - [7. isupper():](#7-isupper)
  - [8. istitle():](#8-istitle)
  - [9. isspace():](#9-isspace)
  - [10. endswith():](#10-endswith)
  - [11. strip():](#11-strip)
  - [12. lstrip():](#12-lstrip)
  - [13. rstrip():](#13-rstrip)

## 1. isalpha():
 *  Karakter dizisinin yanlızca harflerden oluşup oluşmadığını sorgular.
 *  Kullanımı:
    ```bash
      'python'.isalpha()  #  >>> True
    ```

 
## 2. isnumeric(): 
 *  Karakter dizisinin sadece sayılardan oluşup oluşmadığını sorgular.
 *  Kullanımı:
    ```bash
      '2023'.isnumeric()  #  >>> True
    ```


## 3. isalnum(): 
 *  Karakter dizisinin, sadece harflerden ve/veya sayılardan oluşup oluşmadığını sorgular.
 *  Kullanımı:
    ```bash
      '2023Python'.isalnum()  #  >>> True
    ```
    ```bash
      '2023 Python'.isalnum()  #  >>> False ( Aralarındaki boşluk karakterine dikkat edelim.) 
    ```

## 4. isdecimal(): 
 *  Karakter dizisi içindeki sayının ondalık sayı cinsinden olup olmadığını sorgular.
 *  Kullanımı:
    ```bash
      '2023'.isdecimal()  #  >>> True
    ```
    ```bash
      '2023.30'.isdecimal()  #  >>> False
    ```

## 5. isdigit(): 
 *  Karakter dizisinin sadece sayılarda oluşup oluşmadığını sorgular. True dönderebilmesi için, sayı değerli karakter dizilersinin bir tam sayıdan oluşması gerekiyor.
 **Kullanımı:**
    ```bash
      '2023'.isdigit()  #  >>> True
    ```
    ```bash
      '2023.30'.isdigit()  #  >>> False
    ```

## 6. islower(): 
 *  Karakter dizisinin tamamen küçük harflerden oluşup oluşmadığını sorgular.
 **Kullanımı:**
    ```bash
      'python'.islower()  #  >>> True
    ```
    ```bash
      'Python'.islower()  #  >>> False
    ```

## 7. isupper(): 
 * Karakter dizisindeki bütün harflerin büyük harf olup olmadığını sorgular.
 **Kullanımı:**
    ```bash
      'PYTHON'.isupper()  #  >>> True
    ```
    ```bash
      'Python'.isupper()  #  >>> False
    ```

## 8. istitle(): 
 *  Karakter dizisindeki kelimelerin baş harflerinin büyük harf olup olmadığını sorgular. True dönderebilmesi için sorguladığı kelimelerdeki baş haflerinin büyük, geriye kalan diğer harflerin küçük olması gerekiyor.
 **Kullanımı:**
    ```bash
      'Python Language'.istitle()  #  >>> True
    ```
    ```bash
      'python language'.istitle()  #  >>> False
    ```
    ```bash
      'Python language'.istitle()  #  >>> False
    ```
    ```bash
      'python Language'.istitle()  #  >>> False
    ```

## 9. isspace(): 
 *  Karakter dizisinin sadece boşluk karakterinden oluşup oluşmadığını sorgular.
 **Kullanımı:**
    ```bash
      ' '.isspace()  #  >>> True
    ```
    ```bash
      '2023'.isspace()  #  >>> False
    ```

## 10. endswith(): 
 *  Karakter dizisinin parametre olarak verilen karakter ile bitip, bitmediğini sorgular.
 **Kullanımı:**
    ```bash
      'Python'.endswith("n")  #  >>> True
    ```
    ```bash
      'Python'.endswith("o")  #  >>> False
    ```

## 11. strip(): 
 *  Parametresiz olarak kullanıldığında, karakter dizisinin sağında ve solunda bulunan boşluk karakteri ile kaçış dizilerini siler. Parametre olarak bir karakter dizisi alır, girilen parametre karakter dizisinin sağında veya solunda var ise siler.
 **Kullanımı:**
    ```bash
      '  Python  '.strip()  # sağdaki ve soldaki boşlukları siler. >>> 'Python'
    ```
    ```bash
      'Python'.strip("P")  #  >>> 'ython'
    ```
## 12. lstrip(): 
 *  Paremetre olarak girilen karakteri, karakter dizisinin sol tarafından kaldırır. Eğer parametresiz olarak kullanılırsa, kaçış dizilerini (\n, \t) ve boşluk karakterini, karakter dizisinin sol tarafından kaldırır.
 **Kullanımı:**
    ```bash
      'Python'.lstrip("Pyt")  #  >>> 'hon'
    ```

    ```bash
      ' \n  \t     Python'.lstrip()  #  >>> 'Python'
    ```

    ```bash
      '        Python'.lstrip()  #  >>> 'Python'
    ```
## 13. rstrip(): 
 *  Paremetre olarak girilen karakteri, karakter dizisinin sağ tarafından kaldırır. Eğer parametresiz olarak kullanılırsa, kaçış dizilerini (\n, \t) ve boşluk karakterini, karakter dizisinin sağ tarafından kaldırır.
 **Kullanımı:**
    ```bash
      '  Python  '.rstrip("hon")  # >>> 'Pyt'
    ```
    ```bash
      'Python       '.rstrip()  #  >>> 'Python' Sağdan bulunan boşluk karakterlerini ortaan kaldırır.
    ```
